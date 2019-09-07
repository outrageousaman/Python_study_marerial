import unittest
from Assignment_2.country import Country


class TestCountry(unittest.TestCase):
    def setUp(self):
        self.country_1 = Country('India')
        self.country_2 = Country('USA')

    def test_country_name(self):
        self.assertEqual(self.country_1.country, 'India')
        self.assertEqual(self.country_2.country, 'USA')


if __name__ == '__main__':
    unittest.main()