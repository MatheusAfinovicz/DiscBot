import unittest
from search import search


class SearchTestCase(unittest.TestCase):
    def test_void_returns_error(self):
        self.assertEqual(search(''), 'A busca não pode ser vazia.')

    def test_multiple_spaces_returns_error(self):
        self.assertEqual(search('   '), 'A busca não pode ser vazia.')

    def test_multiple_results_returns_wikipedia_exceptions_disambiguation_error(self):
        query = 'gremio'
        self.assertEqual(search(query), 'Encontrei muitos resultados para tal busca, por favor, '
                                           'seja mais específico.')

    def test_unexisting_query_returns_wikipedia_exceptions_page_error(self):
        query = 'dhsaudhas'
        self.assertEqual(search(query), 'Não encontrei nenhuma página relacionada a essa busca.')

    def test_animals_returns_a_string(self):
        query = 'animals'
        self.assertIsInstance(search(query), str)


if __name__ == '__main__':
    unittest.main()
