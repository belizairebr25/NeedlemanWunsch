#veiw in code mode for best format

Deliverable 1
Project Plan:
    Steps:
        Deliverable 1:
            Research Needleman Wunsch algorithm
                Helpful youtube videos, wikipedia page
            Perform Needleman Wunsch by hand on paper
                Will be used for later test cases and can be verified if video examples chosen
            Implement tests using video example alignment and score
            Set up alignment matrix
            Set up traceback matrix
            Preform traceback and return score
            Allow for cmdl inputs
        Deliverable 2:
            Fix asymetric alignment bug
            Create other edge case tests and implement fixes
            Identifiy optimization opportunities to reduce time complexity
            Formally document implementation and prepare presentation on algorithm
        Deliverable 3: 
            Write program instructions and verbose documentation
            Write final reflection

#Deliverable 2
Deliverable 2 Progress:
    Implemented handling and tests for several invalid or odd input edge cases. Program works for nucleotide sequences only(GATCU)
    Membership testing for valid inputs implemented with sets for O(n) time complexity. Type checking used for other input handling
    Factored out input conditioning function that allows for direct command line inputs or filename inputs.
    Fixed Asymmetric Sequence alignment bug which stemmed from using the wrong iterator in certain methods. 
    Created Algorithm Slideshow

    Failing test asserts proper input handling for test files as opposed to CMDL input which is working nominally. This is to be resolved in the next milestone.

Deliverable 3:
    Fixed input handling such that the get_inputs method can be used directly, or the pairwise file can be run directly either with file or string arguments.
    Removed deterministic tie breaking and instead branch the recursive traceback every time there is a tie to return every optimal alignment rather than just one.
    Added verbose and descriptive comments/docstrings to main program
    Updated unit tests to handle new output format
    All tests pass

            

