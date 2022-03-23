from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.tuotteidenMaaraKorissa = 0
        self.kokonaishinta = 0
        self.kaikkiOstokset = []

    def tavaroita_korissa(self):
        return self.tuotteidenMaaraKorissa
    
    def hinta(self):
        return self.kokonaishinta

    def lisaa_tuote(self, lisattava: Tuote):
        if lisattava in self.kaikkiOstokset:
            lisattava.muuta_lukumaara(1)
        else:
            uusiOstos = Ostos(lisattava)
            self.kaikkiOstokset.append(uusiOstos)
        
        self.tuotteidenMaaraKorissa += 1
        self.kokonaishinta = self.kokonaishinta + lisattava.hinta()

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.kaikkiOstokset