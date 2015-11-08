# pylint: disable=R0904
# pylint: disable=C0111

import unittest
import Helpers as H
import operator as op

class LetterRangeTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(H.letter_range("a", "c"), ['a', 'b'])

    def test_2(self):
        self.assertEqual(H.letter_range("a", "a"), [])

    def test_3(self):
        self.assertEqual(H.letter_range("a", "f", step=3), ['a', 'd'])


class ScanExlTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(H.scan_exl(op.add, 0, [1, 2, 3, 4]), [0, 1, 3, 6])
    def test_2(self):
        self.assertEqual(H.scan_exl(op.mul, 1, [2, 2, 2]), [1, 2, 4])
    def test_3(self):
        self.assertEqual(H.scan_exl(op.mul, 1, []), [])

class ScanIncTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(H.scan_inc(op.add, 0, [1, 2, 3, 4]), [1, 3, 6, 10])
    def test_2(self):
        self.assertEqual(H.scan_inc(op.mul, 1, [2, 2, 2]), [2, 4, 8])
    def test_3(self):
        self.assertEqual(H.scan_inc(op.mul, 1, []), [])

class QuicksortTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(H.quicksort([]),[])
    def test_2(self):
        self.assertEqual(H.quicksort([1,1,1,1]),[1,1,1,1])
    def test_3(self):
        self.assertEqual(H.quicksort([4,2,7,9,11,1]),[1,2,4,7,9,11])
            
            

if __name__ == '__main__':
    unittest.main()


    