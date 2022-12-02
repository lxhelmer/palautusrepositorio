class Summa:
    def __init__(self, logiikka,arvo):
        self.logiikka = logiikka
        self.arvo = arvo
        self.vanha = 0
    
    def suorita(self):
        self.vanha = self.logiikka.tulos
        value = 0
        try:
            value = int(self.arvo())
        except Exception:
            pass
        self.logiikka.plus(value)
    def kumoa(self):
        self.logiikka.aseta_arvo(self.vanha)


class Erotus:
    def __init__(self, logiikka,arvo):
        self.logiikka = logiikka
        self.arvo = arvo
        self.vanha = 0

    def suorita(self):
        self.vanha = self.logiikka.tulos
        value = 0
        try:
            value = int(self.arvo())
        except Exception:
            pass

        self.logiikka.miinus(value)

    def kumoa(self):
        self.logiikka.aseta_arvo(self.vanha)

class Nollaus:
    def __init__(self, logiikka,arvo):
        self.arvo = arvo()
        self.logiikka = logiikka
        self.vanha = 0
    def suorita(self):
        self.vanha = self.logiikka.tulos
        self.logiikka.nollaa()

    def kumoa(self):
        self.logiikka.aseta_arvo(self.vanha)



class Kumoa:
    def __init__(self,logiikka, arvo):
        self.arvo = arvo() 
        self.logiikka = logiikka
    def suorita(self):
        self.logiikka.vika.kumoa()
        
