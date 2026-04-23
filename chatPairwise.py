#FIXME: implement read from file option
import sys
class Pairwise():
    def __init__(self, seq1 = None, seq2 = None):
        """initialize object variables
        set up alignment matrix and compute optimal path"""
        #object vars
        if type(seq1) != str or type(seq2) != str :
            raise ValueError("Bad input")
        self._seq1 = [char for char in seq1] #list stores sequence 1
        self._seq2 = [char for char in seq2] #list stores sequence 2
        self._final_seq1 = None
        self._final_seq2 = None
        self._score = None
        #set of all acceptable values:
        _acceptable = {'A', 'G', 'C', 'T', 'U'}
        _all = self._seq1 + self._seq2
        #check all values for acceptability O(n)
        if all(char in _acceptable for char in _all):
            pass
        else:
            raise ValueError("Invalid Sequence")
        #call methods
        self._alignment = self._fill_matrix(self._seq1, self._seq2)
        self._alignments = self._alignment[0]
        self._score = self._alignment[1]
        

    def _matrix_init(self, a, b):
        """create alignment matrix"""
        a.insert(0, 'X')
        b.insert(0, 'X')
        nested = [['N' for _ in range(len(a))] for _ in range(len(b))]
        traceback = [['N' for _ in range(len(a))] for _ in range(len(b))]
        a_loc = 0
        b_loc = 0
        if a[a_loc] == 'X' and b[b_loc] == 'X':
            nested[0] = [-1 * i for i in range(len(a))]
            for i in range(len(b)):       
                nested[i][0] = i * -1
            nested[a_loc][b_loc] = 0  
        else:
            raise ValueError("Bad input")
        a_loc = 0
        b_loc = 0
        if a[a_loc] == 'X' and b[b_loc] == 'X':
            traceback[0] = ['horizontal' for i in range(len(a))]
            for i in range(len(b)):
                traceback[i][0] = 'vertical'
            traceback[a_loc][b_loc] = 0
        return [traceback, nested]
    
    def _cell_score(self, a, b, i, j, nested, traceback):
        """return alignment matrix cell score"""
        if a[j] == b[i]:
            score = 1
        else:
            score = -1    
        vertical = nested[i - 1][j] - 1
        horizontal = nested[i][j - 1] -1
        diagonal = nested[i - 1][j - 1] + score
        motions = {
            'diagonal': diagonal,
            'vertical': vertical,
            'horizontal': horizontal
        }
        maximum = max(motions.values())
        traceback[i][j] = [move for move, val in motions.items() if val == maximum]

        return [maximum, traceback]
    
    def _print_matrix(self, a, b, nested):
        """troubleshooting method prints matrix; not used nominally"""
        print("X", a)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        for i in range(0, len(nested)):
            print(b[i], nested[i])

    def _traceback_all(self, a, b, traceback, i, j, a_acc, b_acc, results):
        if i == 0 and j == 0:
            results.append((a_acc[::-1], b_acc[::-1]))
            return

        for move in traceback[i][j]:
            if move == 'diagonal':
                self._traceback_all(
                    a, b, traceback,
                    i-1, j-1,
                    a_acc + [a[j]],
                    b_acc + [b[i]],
                    results
                )
            elif move == 'vertical':
                self._traceback_all(
                    a, b, traceback,
                    i-1, j,
                    a_acc + ['-'],
                    b_acc + [b[i]],
                    results
                )
            elif move == 'horizontal':
                self._traceback_all(
                    a, b, traceback,
                    i, j-1,
                    a_acc + [a[j]],
                    b_acc + ['-'],
                    results
                )
    
    def _fill_matrix(self, a, b):
        """fill the alignment matrix with values"""
        values = self._matrix_init(a, b)
        traceback = values[0]
        nested = values[1]
        for i in range(1, len(b)):
            for j in range(1, len(a)):
                values = self._cell_score(a, b, i, j, nested, traceback)
                nested[i][j] = values[0]
                traceback = values[1]
        score = nested[-1][-1]
        results = []
        self._traceback_all(a, b, traceback, len(b)-1, len(a)-1, [], [], results)
        return [results, score]
    ##### ~Interface~ #####
    def score(self):
        """getter for _score"""
        return self._score
    
    def __str__(self):
        """getter for the alignment on two different lines"""
        output = []
        for a_seq, b_seq in self._alignments:
            output.append("".join(a_seq))
            output.append("".join(b_seq))
            output.append("")  # blank line between alignments
        return "\n".join(output)

if __name__ == "__main__":
    P1 = Pairwise("CAGATA", "GATTACA")
    print(P1)
    print(f"Alignment score: {P1.score()}")