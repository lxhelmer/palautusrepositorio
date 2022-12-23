from tekoaly import Tekoaly
from peli import KiviPaperiSakset

class KPSTekoaly(KiviPaperiSakset):
    def __init__(self):
        self.tekoaly = Tekoaly()
        
    def _toka_siirto(self, eka_siirto):
        siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {siirto}")
        return siirto

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
