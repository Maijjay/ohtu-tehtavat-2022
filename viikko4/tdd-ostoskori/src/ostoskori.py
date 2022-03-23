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
        uusiOstos = Ostos(lisattava)

        self.tuotteidenMaaraKorissa += 1
        self.kokonaishinta = self.kokonaishinta + lisattava.hinta()

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
                
                self.tuotteidenMaaraKorissa -= 1
                self.kokonaishinta -= ostos.hinta()


    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.kaikkiOstokset