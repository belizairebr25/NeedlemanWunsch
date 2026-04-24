#import file handling modules 
import sys
import os

class Pairwise():
    """Compute Global Sequence Alignment using the Needleman Wunsch Algorithm. 
    The scoring scheme used is +1 for a match, -1 for a mismatch or an indel.
    To use this tool, create an object MyAlignment = Pairwise(<"sequence1">, <"sequence2">)
    To veiw alignment print the Pairwise object: print(MyAlignment). 
    To veiw the alignment score print the output of the .score() method."""

    def __init__(self, seq1 = None, seq2 = None, match_score = 1, mismatch_score = -1):
        """initialize object variables
        set up alignment matrix and call methods to compute all optimal paths
        Optional parameters: match_score and mismatch_score set the penalties/rewards.
        They are initialized to 1 and -1 respectively by default"""
        #set up scores
        self.match_score = match_score
        self.mismatch_score = mismatch_score
        #validate input type
        if type(seq1) != str or type(seq2) != str :
            raise ValueError("Bad input")
        self._seq1 = [char for char in seq1] #list stores sequence 1
        self._seq2 = [char for char in seq2] #list stores sequence 2
        self._score = None
        #set of all acceptable values:
        _acceptable = {'A', 'G', 'C', 'T', 'U'}
        _all = self._seq1 + self._seq2
        #check all values for acceptability O(n)
        if all(char in _acceptable for char in _all):
            pass
        else:
            raise ValueError("Invalid Sequence")
        
        #call methods to preform alignment
        self._alignment = self._fill_matrix(self._seq1, self._seq2)
        self._score = self._alignment[1]
        self._final_seq1 = self._alignment[0]

    ##### ~Alignment~ #####
    def _matrix_init(self, a, b):
        """create score table and traceback table.
        Score cells store the optimal score up to that cell
        In this version each traceback cell stores ALL optimal next moves, 
        whereas in the last version it only stored one determined by the tiebreaking scheme"""
        #insert a space at the beginning of each sequence so cell scoring always starts at zero
        a = ['X'] + a
        b = ['X'] + b
        #nested is the score table, traceback is the traceback table
        nested = [['N' for _ in range(len(a))] for _ in range(len(b))]
        traceback = [['N' for _ in range(len(a))] for _ in range(len(b))]
        #score position indicators
        a_loc = 0
        b_loc = 0
        #initialize first column and row of score matrix
        if a[a_loc] == 'X' and b[b_loc] == 'X':
            nested[0] = [-1 * i for i in range(len(a))]
            for i in range(len(b)):       
                nested[i][0] = i * -1
            nested[a_loc][b_loc] = 0  
        else:
            raise ValueError("Bad input")
        #traceback position indicators
        a_loc = 0
        b_loc = 0
        #initialize first column and row of traceback matrix
        if a[a_loc] == 'X' and b[b_loc] == 'X':
            traceback[0] = ['horizontal' for i in range(len(a))]
            for i in range(len(b)):
                traceback[i][0] = 'vertical'
            traceback[a_loc][b_loc] = 0
        #return the two tables
        return [traceback, nested]
    
    def _cell_score(self, a, b, i, j, nested, traceback):
        """calculate individual cell score and possible traceback motions"""
        #if there is a match set a positive score
        if a[j] == b[i]:
            score = self.match_score
        #if there is a mismatch set a negative score
        else:
            score = self.mismatch_score
        #calculate the score for a vertical or horizontal motion (gap in one sequence)    
        vertical = nested[i - 1][j] + self.mismatch_score
        horizontal = nested[i][j - 1] + self.mismatch_score
        #calculate the score for a diagonal motion(progression in both sequences)
        diagonal = nested[i - 1][j - 1] + score
        #find the motion that returns the maximum possible score
        motions = [diagonal, vertical, horizontal]
        maximum = max(motions)
        #add ALL optimal motions to that cell in the traceback matrix
        traceback[i][j] = []
        if diagonal == maximum:
            traceback[i][j].append('diagonal')
        if vertical == maximum:
            traceback[i][j].append('vertical')
        if horizontal == maximum:
            traceback[i][j].append('horizontal')
        #return the calculated cell score
        return maximum
    
    def _print_matrix(self, a, b, nested):
        """troubleshooting method prints matrix; not used nominally"""
        print("X", a)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        for i in range(0, len(nested)):
            print(b[i], nested[i])

    def _traceback_func(self, a, b, traceback, i, j, a_acc = None, b_acc = None, results = None):
        """finds every optimal route through traceback matrix"""
        #setup case
        if a_acc == None and b_acc == None and results == None:
            a_acc = []
            b_acc = []
            results = []
        #base case: at (0,0)
        if i == 0 and j == 0:
            results.append(("".join(a_acc[::-1]), "".join(b_acc[::-1])))
            return results
        #recursive case
        #branches for each optimal traceback move
        if 'diagonal' in traceback[i][j]:
            self._traceback_func(a, b, traceback, i-1, j-1, a_acc + [a[j]] , b_acc + [b[i]], results)
        if 'vertical' in traceback[i][j]:
            self._traceback_func(a, b, traceback, i-1, j, a_acc + ['-'], b_acc + [b[i]], results)
        if 'horizontal' in traceback[i][j]:
            self._traceback_func(a, b, traceback, i, j-1, a_acc + [a[j]], b_acc + ['-'], results)
    
        return results

    def _fill_matrix(self, a, b):
        """This method handles the program flow by:
        initializing the score and traceback matricies,
        calling _cell_score to score each cell in the score matrix and getting the final score
        running the traceback function to calculate all optimal sequence alignments"""
        #initialize score and traceback matricies
        values = self._matrix_init(a, b)
        traceback = values[0]
        nested = values[1]
        #match the insertion at 0,0 from the matrix setup
        a = ['X'] + a
        b = ['X'] + b
        #fill the score and traceback matricies
        for i in range(1, len(b)):
            for j in range(1, len(a)):
                nested[i][j] = self._cell_score(a, b, i, j, nested, traceback)
        #the score is the last cell in the score matrix
        score = nested[-1][-1]
        #calculate all optimal alignments
        result = self._traceback_func(a, b, traceback, len(b)-1, len(a)-1)
        #return [list of all optimal alignments, alignment score]
        return [result, score] 

    ##### ~User Interface~ #####
    def score(self):
        """getter for _score"""
        return self._score
    
    def __str__(self):
        """prints the calculated alignments (result in _fill_matrix)"""
        output = []
        for a_seq, b_seq in self._final_seq1:
            output.append(a_seq)
            output.append(b_seq)
            output.append("")
        return "\n".join(output)

def get_inputs(file1 = None, file2 = None):
    """handle CMDL input or called inputs for files or string sequences"""
    #CMDL input
    if file1 is None and file2 is None:
        if len(sys.argv) != 3:
            raise ValueError("Invalid sequence inputs, must be files or sequences in format: 'sequence1' 'sequence2' or file1 file2")
        arguments = sys.argv[1:3]
    #called input
    else:
        arguments = [0, 0]
        try:
            arguments[0], arguments[1] = file1, file2
        except:
            raise ValueError("invalid sequence input")
    #output list
    results = []
    for i in arguments:
        #handle file inputs
        if os.path.isfile(i):
            with open(i, 'r') as f:
                results.append(f.read().strip())
        else:
            #handle string inputs
            results.append(i)
    
    return results[0], results[1]

if __name__ == "__main__":
    """run demo"""
    #get inputs from CMDL
    seq1, seq2 = get_inputs()
    #make object and find optimal alignments
    P1 = Pairwise(seq1, seq2)
    #print optimal alignments
    print(P1)
    #print Alignment score
    print(f"Alignment score: {P1.score()}")
