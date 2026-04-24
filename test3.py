import unittest
from main import *

class testPairwise(unittest.TestCase):
    def setUp(self):
        """define data for tests and make objects"""
        try:
            self.P1 = Pairwise("CAGCTA", "CACATA")
            self.score1 = 3
            #one possible alignment
            self.an_alignment1 = "CAGC-TA\nCA-CATA\n"
        except:
            raise AssertionError("Could not create object P1")
        try:
            self.P2 = Pairwise("GATTACA", "CAGCTA")
            self.score2 = -2
            #one possible alignment
            self.an_alignment2 = "GATTAC-A\nCA--GCTA\n\n"
        except:
            raise AssertionError("Could not create object P2")
        try:
            self.P3 = Pairwise("CAGCTA", "GATTACA")
            self.score3 = -2
            #one possible alignment
            self.an_alignment3 = "CAGCT--A\nGA-TTACA\n\n"
 
        except:
            raise AssertionError("Could not create object P3")

    def test_score_case1(self):
        """test normal behavior returns correct score"""
        self.assertEqual(self.P1.score(), self.score1)

    def test_alignment_case1(self):
        """test normal behavior returns correct alignment"""
        self.assertIn(self.an_alignment1, str(self.P1))

    ##### ~Test Edge Cases~ #####

    def test_asymetric_input1(self):
        """test for case where string 1 is longer than string 2"""
        self.assertIn(self.an_alignment2, str(self.P2))
        self.assertEqual(self.P2.score(), self.score2)

    def test_asymetric_input2(self):
        """test for case where string 2 is longer than string 1"""
        self.assertIn(self.an_alignment3, str(self.P3))
        self.assertEqual(self.P3.score(), self.score3)

    def test_improper_input(self):
        """Assert bad inputs(nonstring) raise value errors"""
        with self.assertRaises(ValueError): Pairwise(5, 6)
        with self.assertRaises(ValueError): Pairwise(True, False)
        with self.assertRaises(ValueError): Pairwise('LAUGHABLE', 'SEQUENCE')

    def test_file_read(self):
        """test file input handling"""
        inputs = get_inputs('data1.txt', 'data2.txt')
        self.assertEqual(inputs, ('GCATGCG', 'GATTACA'))

if __name__ == "__main__":
    unittest.main()
