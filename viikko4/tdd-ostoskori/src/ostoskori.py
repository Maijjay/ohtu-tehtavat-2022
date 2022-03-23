from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.kaikkiOstokset = [] 

    def tavaroita_korissa(self):
        summa = 0
        for ostos in self.kaikkiOstokset:
            summa += ostos.lukumaara()
        return summa
    
    def hinta(self):
        summa = 0
        for ostos in self.kaikkiOstokset:
            summa += ostos.hinta()
        return summa

    def lisaa_tuote(self, lisattava: Tuote):
        uusiOstos = Ostos(lisattava)

        if len(self.kaikkiOstokset) == 0:
            self.kaikkiOstokset.append(uusiOstos)
        else:
            for i in range (len(self.kaikkiOstokset)):
                ostos: Ostos = self.kaikkiOstokset[i]
                if ostos.tuotteen_nimi() == uusiOstos.tuotteen_nimi():
                    ostos.muuta_lukumaaraa(1)
                    return
            self.kaikkiOstokset.append(uusiOstos)
    

    def poista_tuote(self, poistettava: Tuote):
        for i in range (len(self.kaikkiOstokset)):
            ostos: Ostos = self.kaikkiOstokset[i]
            if ostos.tuotteen_nimi() == poistettava.nimi():
                if (ostos.lukumaara == 1):
                    self.kaikkiOstokset.remove[i]
                else:
                    ostos.muuta_lukumaaraa(-1)
                

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.kaikkiOstokset