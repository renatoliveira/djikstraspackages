import unittest, tempfile
import os
from main import Grafo

class TestFindShortestPath(unittest.TestCase):

    def setUp(self):
        paths_file = open('paths.testing', 'w')
        lines = ['LS SF 1\n', 'SF LS 2\n', 'LS LV 1\n', 'LV LS 1\n', 'SF LV 2\n', 'LV SF 2\n', 'LS RC 1\n', 'RC LS 2\n', 'SF WS 1\n', 'WS SF 2\n', 'LV BC 1\n', 'BC LV 1\n']
        paths_file.writelines(lines)
        paths_file.close()

        track_file = open('tracks.testing', 'w')
        t_lines = ['SF WS\n', 'LS BC\n', 'WS BC\n']
        track_file.writelines(t_lines)
        track_file.close()
        
    def test_geral(self):
        grafo = Grafo('paths.testing', 'tracks.testing', 'routes.testing')

    def test_add_node(self):
        grafo = Grafo('paths_input', 'tracks_input', 'routes.testing')
        grafo.add_node('XX')
        self.assertTrue('XX' in grafo.nodes)

    def test_add_path(self):
        grafo = Grafo('paths_input', 'tracks_input', 'routes.testing')
        grafo.add_path('a', 'b', 5)
        grafo.add_path('b', 'c', 6)

        self.assertTrue('a' in grafo.adjacents)
        self.assertTrue('b' in grafo.adjacents)
        self.assertTrue('c' in grafo.adjacents)

        self.assertTrue(len(grafo.adjacents['a']) == 1)
        self.assertTrue(len(grafo.adjacents['b']) == 2)
        self.assertTrue(len(grafo.adjacents['c']) == 1)

    def test_write_result(self):
        grafo = Grafo('paths_input', 'tracks_input', 'routes.testing')
        grafo.write_result({'a':0, 'b':1}, {'a':'b'}, 'a', 'b')

        self.assertTrue(os.path.exists('routes.testing'))

    def test_format_route(self):
        grafo = Grafo('paths_input', 'tracks_input', 'routes.testing')
        result = grafo.format_route({'B':'A', 'C':'B'}, 'C')
        self.assertTrue(result == 'A B')

    def tearDown(self):
        os.remove('paths.testing')
        os.remove('tracks.testing')

        # nem todos os testes criam o output...
        if os.path.exists('routes.testing'):
            os.remove('routes.testing')

if __name__ == '__main__':
    unittest.main()
