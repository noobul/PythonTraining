import unittest
import city_class as cc

class CitiesTestCase(unittest.TestCase):
    """Tests for ciity_class.py function."""

    def test_city_formatert(self):
        """Do countries like Satiago, Chile work?"""
        sc = cc.City('santiago', 'chile')
        sc_formated = sc.city_formater()
        self.assertEqual(sc_formated, "Santiago, Chile")

    def test_city_formatert_pop(self):
        """can I add population for cities?"""
        sc = cc.City('santiago', 'chile', 6_269_384)
        sc_formated = sc.city_formater()
        self.assertEqual(sc_formated, "Santiago, Chile has a population of 6269384")

if __name__ == '__main__':
    unittest.main()