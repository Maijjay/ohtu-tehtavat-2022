import unittest
from ..statistics import Statistics
from ..player import Player
from ..statistics import sort_by_points


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )
    
    def test_loytyyko_oikea_pelaaja(self):
        pelaaja = "Kurri"
        etsitty = self.statistics.search(pelaaja)
        self.assertTrue(etsitty.name is pelaaja)

    def test_palautetaanko_none_jos_pelaajaa_ei_loydy(self):
        pelaaja = Player("Matti", "EDM", 37, 53)
        etsitty = self.statistics.search(pelaaja.name)
        self.assertEqual(etsitty, None)

    def test_palauttaako_oikean_pistemaaran(self):
        pelaaja = self.statistics.search("Gretzky")
        pisteet = sort_by_points(pelaaja)
        self.assertAlmostEqual(pisteet, 124)

    def test_toimiiko_joukkueen_filtterointi(self):
        etsittyJoukkue = self.statistics.team("EDM")
        oikein = True
        for pelaaja in etsittyJoukkue:
            if pelaaja.team != "EDM":
                oikein = False
        self.assertEqual(oikein, True)

    def test_loytyyko_parhaat_pelaajat_oikein(self):
        top3 = [Player("Gretzky", "EDM", 35, 89), 
                Player("Lemieux", "PIT", 45, 54),
                Player("Yzerman", "DET", 42, 56)]
        etsittyTop3 = self.statistics.top_scorers(2)
        for pelaaja in etsittyTop3:
            samat = False
            for p in top3:
                if pelaaja.name == p.name:
                    samat = True

        
        self.assertEqual(samat, True)


