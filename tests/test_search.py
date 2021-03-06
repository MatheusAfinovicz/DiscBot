import unittest
from apis.search import search


class SearchTestCase(unittest.TestCase):

    def test_no_param_returns_Type_error(self):
        with self.assertRaises(TypeError):
            search()

    def test_empty_string_returns_empty_search_error(self):
        query = ['', '    ']
        for string in query:
            with self.subTest():
                self.assertEqual(search(string), 'A busca não pode ser vazia.')

    def test_multiple_results_returns_wikipedia_exceptions_disambiguation_error(self):
        query = 'gremio'
        self.assertEqual(search(query), 'Encontrei muitos resultados para tal busca, por favor, '
                                        'seja mais específico.')

    def test_unexisting_query_returns_wikipedia_exceptions_page_error(self):
        query = 'dhsaudhas'
        self.assertEqual(search(query), 'Não encontrei nenhuma página relacionada a essa busca.')

    def test_a_string_returns_wiki_summary(self):
        query = 'animals'
        self.assertIsInstance(search(query), str)

    def test_a_empty_dict_returns_no_param(self):
        query = {}
        self.assertEqual(search(query), 'Não encontrei nenhum parâmentro para buscar sobre.')

    def test_a_empty_list_returns_no_param(self):
        query = []
        self.assertEqual(search(query), 'Não encontrei nenhum parâmentro para buscar sobre.')

    def test_a_empty_tuple_returns_no_param(self):
        query = ()
        self.assertEqual(search(query), 'Não encontrei nenhum parâmentro para buscar sobre.')

    def test_ints_returns_Type_Error(self):
        query = [-7, 0, 3]
        for number in query:
            with self.subTest():
                with self.assertRaises(TypeError):
                    search(number)

    def test_floats_returns_Type_Error(self):
        query = [-0.7, 0.21, 1.93]
        for number in query:
            with self.subTest():
                with self.assertRaises(TypeError):
                    search(number)

    def test_tuples_lists_dicts_with_values_returns_wiki_summary(self):
        query = [('testing', 'values'), (-7, 0, 32), [1, 'None'], [-1, 0], {3: True}, {'key': 2}]
        for values in query:
            with self.subTest():
                self.assertIsInstance(search(values), str)


if __name__ == '__main__':
    unittest.main()
