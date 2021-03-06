import unittest
from apis.weather import weather, creates_formatted_string
import requests
import json

with open('../keys/weather_api_key') as archive:
    for token in archive:
        weather_token = token


class WeatherTestCase(unittest.TestCase):

    def test_invalid_api_key_returns_error_401(self):
        token = 'invalid_token'
        self.assertEqual(weather('guarapuava', token), 'Algo não está certo, tente novamente mais tarde.')

    def test_no_param_returns_TypeError(self):
        with self.assertRaises(TypeError):
            weather()

    def test_empty_strings_returns_empty_search_error(self):
        cities = ['', '    ']
        for city in cities:
            with self.subTest():
                self.assertEqual(weather(city, weather_token), 'A cidade não pode ser vazia.')

    def test_a_city_returns_expected_data(self):
        cities = ['guarapuava', 'new york', 'amsterdam']
        for city in cities:
            with self.subTest():
                self.assertIn(city.upper(), weather(city, weather_token))

    def test_unexisting_city_returns_KeyError(self):
        cities = ['sla', 'not a city', 'something']
        for city in cities:
            with self.subTest():
                with self.subTest():
                    self.assertEqual(weather(city, weather_token), 'Cidade não encontrada.')

    def test_numbers_returns_TypeError(self):
        cities = [1, 0.5, -17, 0, 3 / 10]
        for city in cities:
            with self.subTest():
                self.assertEqual(weather(city, weather_token), 'A cidade não pode ser um número.')

    def test_empty_arrays_return_KeyError(self):
        cities = [[], {}, ()]
        for city in cities:
            with self.subTest():
                self.assertEqual(weather(city, weather_token), 'Cidade não encontrada.')

    def test_arrays_with_values_return_KeyError(self):
        cities = [{'amsterdam': 'guarapuava'}, ['new york'], (1, True)]
        for city in cities:
            with self.subTest():
                self.assertEqual(weather(city, weather_token), 'Cidade não encontrada.')


class CreatesFormatedStringTestCase(unittest.TestCase):

    def test_no_param_returns_TypeError(self):
        with self.assertRaises(TypeError):
            creates_formatted_string()

    def test_empty_strings_returns_TypeError(self):
        cases = ['', '    ']
        for case in cases:
            with self.subTest():
                with self.assertRaises(TypeError):
                    creates_formatted_string(case)

    def test_numbers_returns_TypeError(self):
        cases = [-5, 0, 17, 3 / 10]
        for case in cases:
            with self.subTest():
                with self.assertRaises(TypeError):
                    creates_formatted_string(case)

    def test_empty_list_returns_TypeError(self):
        case = []
        with self.assertRaises(TypeError):
            creates_formatted_string(case)

    def test_empty_tuple_returns_TypeError(self):
        case = ()
        with self.assertRaises(TypeError):
            creates_formatted_string(case)

    def test_empty_dict_returns_TypeError(self):
        case = {}
        with self.assertRaises(KeyError):
            creates_formatted_string(case)

    def test_dict_with_values_returns_KeyError(self):
        cases = [{'guarapuava': 'amsterdam'}, {1: 'new york'}, {'sao paulo': 4}]
        for case in cases:
            with self.subTest():
                with self.assertRaises(KeyError):
                    creates_formatted_string(case)

    def test_tuple_with_values_returns_TypeError(self):
        cases = [('guarapuava', 'amsterdam', 'sao paulo'), (1, 'new york'), ('sao paulo', 4), (True, False)]
        for case in cases:
            with self.subTest():
                with self.assertRaises(TypeError):
                    creates_formatted_string(case)

    def test_list_with_values_returns_TypeError(self):
        cases = [['guarapuava', 'amsterdam'], ['guarapuava', 'amsterdam', 'sao paulo'], [True, False], ['sao paulo', 4]]
        for case in cases:
            with self.subTest():
                with self.assertRaises(TypeError):
                    creates_formatted_string(case)

    def test_cities_returns_expected_values(self):

        cities = ['guarapuava', 'new york', 'amsterdam']

        for city in cities:
            with self.subTest():

                url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_token}'
                json_response = requests.request('GET', url).text
                response_obj = json.loads(json_response)

                self.assertIn(city.upper(), creates_formatted_string(response_obj))

    def test_unexisting_cities_returns_error_200(self):

        cities = ['not a city', 'something']

        for city in cities:
            with self.subTest():
                url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_token}'
                json_response = requests.request('GET', url).text
                response_obj = json.loads(json_response)

                self.assertEqual(creates_formatted_string(response_obj), 'Cidade não encontrada.')


if __name__ == '__main__':
    unittest.main()
