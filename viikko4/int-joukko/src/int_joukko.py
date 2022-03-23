
class IntJoukko:
    def __init__(self, kapasiteetti=0, kasvatuskoko=0):
        if kapasiteetti == 0:
            self.kapasiteetti = 5
        elif kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")
        else:
            self.kapasiteetti = kapasiteetti

        if kasvatuskoko == 0:
            self.kasvatuskoko = 5
        elif kasvatuskoko < 0:
            raise Exception("Väärä kasvatuskoko") 
        else:
            self.kasvatuskoko = kasvatuskoko

        self.ljono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, etsittava):
        for i in range(0, self.alkioiden_lkm):
            if etsittava == self.ljono[i]:
                return True
        
        return False

    def lisaa(self, lisattava):
        if self.alkioiden_lkm == 0:
            self.ljono[0] = lisattava
            self.alkioiden_lkm += 1
            return True
        
        if not self.kuuluu(lisattava):
            self.ljono[self.alkioiden_lkm] = lisattava
            self.alkioiden_lkm = self.alkioiden_lkm + 1

            if self.alkioiden_lkm % len(self.ljono) == 0:
                taulukko_old = self.ljono
                self.kopioi_taulukko(self.ljono, taulukko_old)
                self.ljono = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_taulukko(taulukko_old, self.ljono)
            return True

        return False

    def poista(self, poistettava):
        for indeksi in range(0, self.alkioiden_lkm):
            if poistettava == self.ljono[indeksi]:
                self.ljono[indeksi] = 0
                
                for j in range(indeksi, self.alkioiden_lkm - 1):
                    apu = self.ljono[j]
                    self.ljono[j] = self.ljono[j + 1]
                    self.ljono[j + 1] = apu
                self.alkioiden_lkm = self.alkioiden_lkm - 1
                return True

        return False

    def kopioi_taulukko(self, joukkoA, joukkoB):
        for i in range(0, len(joukkoA)):
            joukkoB[i] = joukkoA[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lkm

        for i in range(0, len(taulu)):
            taulu[i] = self.ljono[i]

        return taulu

    @staticmethod
    def yhdiste(joukkoA, joukkoB):
        uusiJoukko = IntJoukko()
        a_taulu = joukkoA.to_int_list()
        b_taulu = joukkoB.to_int_list()

        for i in range(0, len(a_taulu)):
            uusiJoukko.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            uusiJoukko.lisaa(b_taulu[i])

        return uusiJoukko

    @staticmethod
    def leikkaus(joukkoA, joukkoB):
        joukkojen_leikkaus = IntJoukko()
        a_taulu = joukkoA.to_int_list()
        b_taulu = joukkoB.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    joukkojen_leikkaus.lisaa(b_taulu[j])

        return joukkojen_leikkaus

    @staticmethod
    def erotus(joukkoA, joukkoB):
        joukkojen_erotus = IntJoukko()
        a_taulu = joukkoA.to_int_list()
        b_taulu = joukkoB.to_int_list()

        for i in range(0, len(a_taulu)):
            joukkojen_erotus.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            joukkojen_erotus.poista(b_taulu[i])

        return joukkojen_erotus

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.ljono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.ljono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.ljono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
