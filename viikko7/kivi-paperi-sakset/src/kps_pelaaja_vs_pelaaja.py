from peli import KiviPaperiSakset


class KPSPelaajaVsPelaaja(KiviPaperiSakset):

    def _toka_siirto(self, eka_siirto):
        return input("Toisen pelaajan siirto: ")

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
