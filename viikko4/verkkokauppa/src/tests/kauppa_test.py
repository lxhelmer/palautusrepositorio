import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.viitegeneraattori_mock.uusi.return_value = 42
        self.varasto_mock = Mock()
        
        def varasto_saldo(tuote_id):
            if tuote_id in [1,2]:
                return 10
            if tuote_id in [3]:
                return 0

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "leipä",10)
            if tuote_id == 3:
                return Tuote(3, "kahvi",3)
            
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)
    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista
    
    def test_tilisiirto_oikeilla_argumenteilla(self):

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka","12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka",ANY,"12345",ANY,5)
    
    def test_tilisiirto_eri_tuotteilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka","12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka",ANY,"12345",ANY,15)


    def test_tilisiirto_samoilla_tuotteilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka","12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka",ANY,"12345",ANY,10)


    def test_tilisiirto_kun_tuotetta_ei_ole(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("pekka","12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka",ANY,"12345",ANY,5)
    
    def test_uusi_kori(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka","12345")
        self.kauppa.aloita_asiointi()

        self.assertEqual(self.kauppa._ostoskori.hinta(), 0)

    def test_uusi_viitenumero(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka","12345")
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 1)
        
    def test_poista_korista(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.poista_korista(1)
        self.assertEqual(self.kauppa._ostoskori._tuotteet,[])

