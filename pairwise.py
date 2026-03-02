#FIXME: assymetric input failure
import sys
class Pairwise():
    def __init__(self, seq1 = None, seq2 = None):
        """initialize object variables
        set up alignment matrix and compute optimal path"""
        #object vars
        if type(seq1) != str or type(seq2) != str:
            raise ValueError("Bad input")
        self._seq1 = [char for char in seq1] #list stores sequence 1
        self._seq2 = [char for char in seq2] #list stores sequence 2
        self._final_seq1 = None
        self._final_seq2 = None
        self._score = None
        #check input values:
        
        #call methods
        self._alignment = self._fill_matrix(self._seq1, self._seq2)
        self._score = self._alignment[2]
        self._final_seq1 = self._alignment[0]
        self._final_seq2 = self._alignment[1]

    def _matrix_init(self, a, b):
        """create alignment matrix"""
        a.insert(0, 'X')
        b.insert(0, 'X')
        nested = [['N' for _ in range(len(b))] for _ in range(len(a))]
        traceback = [['N' for _ in range(len(b))] for _ in range(len(a))]
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
        motions = [diagonal, vertical, horizontal]
        maximum = max(motions)
        motion = motions.index(maximum)
        if motion == 0:
            traceback[i][j] = 'diagonal'
        elif motion == 1:
            traceback[i][j] = 'vertical'
        else:
            traceback[i][j] = 'horizontal'
        return [maximum, traceback]
    
    def _print_matrix(self, a, b, nested):
        """troubleshooting method prints matrix"""
        print("X", a)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        for i in range(0, len(nested)):
            print(b[i], nested[i])

    def _traceback_func(self, a, b, traceback):
        """finds route through traceback matrix"""
        a_pos = len(traceback[0]) - 1
        b_pos = len(traceback) - 1
        a_final = []
        b_final = [] 
        while a_pos != 0 or b_pos != 0:
            if traceback[b_pos][a_pos] == 'diagonal':
                a_final.insert(0, a[a_pos])
                b_final.insert(0, b[b_pos])
                a_pos -= 1
                b_pos -= 1
            elif traceback[b_pos][a_pos] == 'vertical':
                a_final.insert(0, '-')
                b_final.insert(0, b[b_pos])
                b_pos -= 1
            elif traceback[b_pos][a_pos] == 'horizontal':
                a_final.insert(0, a[a_pos])
                b_final.insert(0, '-')
                a_pos -= 1
        return [a_final, b_final]
    
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
        result = self._traceback_func(a, b, traceback)
        return [result[0], result[1], score] #returns a_final, b_final, score

    ##### ~Interface~ #####
    def score(self):
        """getter for _score"""
        return self._score
    
    def __str__(self):
        """getter for the alignment on two different lines"""
        final_seq1 = ""
        final_seq2 = ""
        for char in self._final_seq1:
            final_seq1 += char
        for char in self._final_seq2:
            final_seq2 += char
        return f"{final_seq1}\n{str(final_seq2)}"

if __name__ == "__main__":
    seq1 = sys.argv[1]
    seq2 = sys.argv[2]
    #FIX get seq1 and seq2 from cmdl arguments
    P1 = Pairwise(seq1, seq2)
    print(P1)
    print(f"Alignment score: {P1.score()}")

