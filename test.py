import unittest
from pairwise import *

class testPairwise(unittest.TestCase):
    def setUp(self):
        """define data for tests and make objects"""
        #data
        self.test_seq1 = "GCATGCG"
        self.test_seq2 = "GATTACA"
        self.test_seq3 = "CAGCTA"
        self.test_seq4 = "CACATA"
        self.test_seq_op1 = "GCA-TGCG"
        self.test_seq_op2 = "G-ATTACA"
        self.test_seq_op3 = "CAGC-TA"
        self.test_seq_op4 = "CA-CATA"
        self.test_seq_op13 = "GCATGC-G"
        self.test_seq_op31 = "-CA-GCTA"
        self.test_seq_op24 = "CA-CATA"
        self.test_seq_op42 = "GATTACA"

        self.optimal_score12 = 0
        self.optimal_score34 = 3
        self.optimal_score13 = 0
        self.optimal_score42 = -1

        #objects
        self.P1 = Pairwise(self.test_seq1, self.test_seq2)
        self.P2 = Pairwise(self.test_seq3, self.test_seq4)

    def test_score_case1(self):
        """test normal behavior returns correct score"""
        self.assertEqual(self.P1.score(), self.optimal_score12)
        self.assertEqual(self.P2.score(), self.optimal_score34)

    def test_alignment_case1(self):
        """test normal behavior returns correct alignment"""
        self.assertEqual(str(self.P1), f"{self.test_seq_op1}\n{self.test_seq_op2}")
        self.assertEqual(str(self.P2), f"{self.test_seq_op3}\n{self.test_seq_op4}")

    ##### ~Test Edge Cases~ #####

    def test_asymetric_input1(self):
        """test for case where string 1 is longer than string 2"""
        self.P3 = Pairwise(self.test_seq1, self.test_seq3)
        self.assertEqual(self.P3.score(), self.optimal_score13)
        self.assertEqual(str(self.P3), f"{self.test_seq_op13}\n{self.test_seq_op31}")

    def test_asymetric_input2(self):
        """test for case where string 2 is longer than string 1"""
        self.P4 = Pairwise(self.test_seq4, self.test_seq2)
        self.assertEqual(self.P4.score(), self.optimal_score42)
        self.assertEqual(str(self.P4), f"{self.test_seq_op24}\n{self.test_seq_op42}")

    def test_improper_input(self):
        """Assert bad inputs(nonstring) raise value errors"""
        with self.assertRaises(ValueError): Pairwise(5, 6)
        with self.assertRaises(ValueError): Pairwise(True, False)
        with self.assertRaises(ValueError): Pairwise('LAUGHABLE', 'SEQUENCE')


if __name__ == "__main__":
    unittest.main()
