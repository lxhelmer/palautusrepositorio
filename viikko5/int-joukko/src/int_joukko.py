import copy
KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None:
            self.kapasiteetti = KAPASITEETTI
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")  # heitin vaan jotain :D
        else:
            self.kapasiteetti = kapasiteetti

        if kasvatuskoko is None:
            self.kasvatuskoko = OLETUSKASVATUS
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("kapasiteetti2")  # heitin vaan jotain :D
        else:
            self.kasvatuskoko = kasvatuskoko

        self.luvut = [0] * self.kapasiteetti

        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        
        if n in self.luvut: 
                return True
        return False


    def lisaa(self, n):
        
        if not self.kuuluu(n):
            self.luvut[self.alkioiden_lkm] = n
            self.alkioiden_lkm = self.alkioiden_lkm + 1
        
            if self.alkioiden_lkm == len(self.luvut):
                self.luvut.extend([0] * self.kasvatuskoko)    
            return True

        return False

    def poista(self, n):
        kohta = -1
        apu = 0

        if self.kuuluu(n):
            kohta = self.luvut.index(n)  # siis luku löytyy tuosta kohdasta :D
            self.luvut[kohta] = 0

        if kohta != -1:
            for j in range(kohta, self.alkioiden_lkm - 1):
                apu = self.luvut[j]
                self.luvut[j] = self.luvut[j + 1]
                self.luvut[j + 1] = apu

            self.alkioiden_lkm = self.alkioiden_lkm - 1
            return True

        return False

    def kopioi_taulukko(self, a, b):
        b = copy.deepcopy(a)

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lkm

        for i in range(0, len(taulu)):
            taulu[i] = self.luvut[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        summa = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            summa.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            summa.lisaa(b_taulu[i])

        return summa

    @staticmethod
    def leikkaus(a, b):
        molemmissa = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            if a_taulu[i] in b_taulu:
                    molemmissa.lisaa(a_taulu[i])
        return molemmissa

    @staticmethod
    def erotus(a, b):
        uniikit = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            uniikit.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            uniikit.poista(b_taulu[i])

        return uniikit

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.luvut[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.luvut[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.luvut[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
