This program is an object oriented python implementation of the Needleman Wunsch pairwise alignment algorithm.

This algorithm is used in bioinformatics to find the optimal alignment of two sequences and quantify how related they are.
This has applications in evolutionary relationship identification as well as mutation and function identification from nucleotide and amino acid sequences.

There are several ways to run this program:
  1: CMDL: python3 main.py "<sequence1>" "<sequence2>"

  2: To use this program for files input as cmdl arguments navigate to the directory where it is stored and run:
  python3 main.py "<filename1.txt>" "<filename2.txt>"

  3: To use the program as a module:
    from main import *
    seq1, seq2 = get_inputs(<sequences or files>)

The program currently works for file(.txt) and string inputs
plan.md describes milestone plans
test.py contains unit tests for functionality and edge cases of main.py
data1 and data2.txt are sample data

As of Milestone 3 deterministic tiebreaking is no longer used.
  Instead at every cell in the traceback, all optimal motions are preformed in a more paralell structure by branching the recursion. This severely harms the time complexity, but calculates and outputs every possible optimal sequence rather than the one given by deterministic tie breaking.

Thank You
-Brician Belizaire
