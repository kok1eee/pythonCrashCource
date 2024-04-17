import unittest
from city_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """city_function.pyをテストする"""

    def test_city_country_name(self):
        """'Santiego,Chile'のような名前で動作するか？"""
        formatted_name = get_formatted_name('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago,Chile')

    def test_city_country_population_name(self):
        """'Santiego,Chile - 人口 5000000のような名前で動作するか？"""
        formatted_name = get_formatted_name('santiago', 'chile', 5000000)
        self.assertEqual(formatted_name, 'Santiago,Chile - 人口 5000000')
        
if __name__ == '__main__':
    unittest.main()