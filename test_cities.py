import unittest
from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):
    """Tests for city_functions.py"""
    
    def test_city_country(self):
        """Do city and country like 'Hyderabad, India' work?"""
        formatted_city_country = city_country('hyderabad','india')
        self.assertEqual(formatted_city_country, 'Hyderabad, India')

unittest.main()