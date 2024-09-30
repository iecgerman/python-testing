import unittest, requests
from src.api_client import get_location
from unittest.mock import patch

class ApiClientTest(unittest.TestCase):

    @patch("src.api_client.requests.get")
    def test_get_location_returns_expected_data(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'countryName': 'USA',
            'regionName': 'FLORIDA',
            'cityName': 'MIAMI',
        }
        result = get_location("8.8.8.8")
        self.assertEqual(result.get("country"), "USA")
        self.assertEqual(result.get("region"), "FLORIDA")
        self.assertEqual(result.get("city"), "MIAMI")

        mock_get.assert_called_once_with("https://freeipapi.com/api/json/8.8.8.8")

    @patch('src.api_client.requests.get')
    def test_get_location_returns_side_effect(self, mock_get):
        mock_get.side_effect = [
            requests.exceptions.RequestException("Service Unavailable"),
            unittest.mock.Mock(
                status_code=200,
                json=lambda: {
                    'countryName': 'USA',
                    'regionName': 'FLORIDA',
                    'cityName': 'MIAMI',
                }
            )
        ]
        # mock_get.return_value.status_code = 200
        # mock_get.return_value.json.return_value = {
        # 'countryName': 'USA',
        # 'regionName': 'FLORIDA',
        # 'cityName': 'MIAMI',
        # }

        with self.assertRaises(requests.exceptions.RequestException):    
            get_location("8.8.8.8")

        result = get_location("8.8.8.8")
        self.assertEqual(result.get("country"), "USA")
        self.assertEqual(result.get("region"), "FLORIDA")
        self.assertEqual(result.get("city"), "MIAMI")
        

# ejecutamos la prueba (recuerden dar ctrl + s)

# Resultado:

# (venv) PS C:\Users\info\github\python-testing> python -m unittest tests.test_api_client
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.248s

# OK
# (venv) PS C:\Users\info\github\python-testing> 

# Clase 12 - Side Effect
#  python -m unittest tests.test_api_client.ApiClientTest.test_get_location_returns_side_effect
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.002s

# OK

# python -m unittest tests.test_api_client.ApiClientTest.test_get_location_returns_side_effect

# AssertionError: 'MIAMI' != 'mty'
# - MIAMI
# + mty

# ----------------------------------------------------------------------
# Ran 1 test in 0.005s

# FAILED (failures=1)