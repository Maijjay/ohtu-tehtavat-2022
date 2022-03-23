import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self.maito = Tuote("Maito", 3)
        self.kala = Tuote("Kala", 10)


    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuoteen_lisaamisen_jalkeen_korin_hinta_on_sama_kuin_tuotteen(self):
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.hinta(), 3)

    def test_kahden_eri_tuotteen_lisaaminen_jalkeen_korin_hinta_on_tuotteuden_summa(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.kala)
        self.assertEqual(self.kori.hinta(), 13)
    
    def test_kahden_tuotteen_lisaamisen_jalkeen_korissa_on_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.kala)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)