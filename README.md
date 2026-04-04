This program is an object oriented python implementation of the Needleman Wunsch pairwise alignment algorithm.
This algorithm is used in bioinformatics to find the optimal alignment of two sequences and quantify how related they are.
This has applications in evolutionary relationship identification as well as mutation and function identification from nucleotide and amino acid sequences.

To use this program for sequences input as cmdl arguments navigate to the directory where it is stored and run:
python3 pairwise.py "<sequence1>" "<sequence2>"

To use this program for files input as cmdl arguments navigate to the directory where it is stored and run:
python3 pairwise.py "<filename1.txt>" "<filename2.txt>"

The program currently works for txt files and nucleotide sequences(ACTGU)

plan.md describes milestone plans and next steps

test.py contains unit tests for functionality and edge cases of pairwise.py

data1 and data2.txt are sample data

To use this program as a module:
  from pairwise import Pairwise as Pairwise
  result = Pairwise(sequence1, sequence2)

the result contains optimal alignment and alignment score

Thank You
-Brician Belizaire
