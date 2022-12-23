from tekoaly_parannettu import TekoalyParannettu
from peli import KiviPaperiSakset

class KPSParempiTekoaly(KiviPaperiSakset):
    def __init__(self):
        self.tekoaly = TekoalyParannettu(10)

    def _toka_siirto(self, eka_siirto):
        self.tekoaly.aseta_siirto(eka_siirto)
        siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {siirto}")
        return siirto
        
    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
