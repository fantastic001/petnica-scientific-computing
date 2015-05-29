import unittest 

import numpy as np 

from lib import * 

class TestMakeMatrix(unittest.TestCase):
    
    def test_ones(self):
        expected = np.array([[1, -1, 0, 0, 0, 0], [0, 1, -1, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, -1, 0, 0], [0, 0, 0, 0, -1, 0], [0, 0, 0, 0, 0, -1]])
        self.assertTrue(make_matrix([0, 0, 0], [1, 1, 1], 1).all(expected))


class TestMakeBVector(unittest.TestCase):
    
    def test_basic(self):
        self.assertEqual(make_b_vector([0, 0, 0], 0, [0, 0, 0]), np.array([0, 0, 0, 0, 0, 0]))

if __name__ == '__main__':
    unittest.main()
