import unittest 

import numpy as np 
import numpy.testing as nptest
from lib import * 

class TestMakeMatrix(unittest.TestCase):
    
    def test_ones(self):
        expected = np.array([[1, -1, 0, 0, 0, 0], [0, 1, -1, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, -1, 0, 0], [0, 0, 0, 0, -1, 0], [0, 0, 0, 0, 0, -1]])
        nptest.assert_equal(make_matrix([0, 0, 0], [1, 1, 1], 1), expected)


class TestMakeBVector(unittest.TestCase):
    
    def test_basic(self):
        nptest.assert_equal(make_b_vector([0, 0, 0], 0, [0, 0, 0]), np.array([0, 0, 0, 0, 0, 0]))

if __name__ == '__main__':
    unittest.main()
