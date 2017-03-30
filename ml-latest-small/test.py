import unittest
import csv
from movielens import Conversions, nombre_films

class TestConversions(unittest.TestCase):
    def test_renvoyer_index(self):
        conv = Conversions()
        self.assertEqual(conv.renvoyer_index(1), 0)
        for i in range(nombre_films()):
            self.assertEqual(conv.renvoyer_index(conv.renvoyer_id(i)), i)
    def test_renvoyer_nom(self):
        conv = Conversions()
        self.assertEqual("Toy Story (1995)", conv.renvoyer_nom_index(0))
        self.assertEqual("Toy Story (1995)", conv.renvoyer_nom_id(1))
        films = open("movies.csv")
        reader = csv.reader(films)
        for i, row in enumerate(reader):
            if i != 0:
                self.assertEqual(row[1], conv.renvoyer_nom_index(i-1))
                self.assertEqual(row[1], conv.renvoyer_nom_id(int(row[0])))
        films.close()
if __name__ == "__main__":
    unittest.main()