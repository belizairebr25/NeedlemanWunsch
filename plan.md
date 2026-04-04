#Deliverable 1
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

Deliverable 3 Plans:
    Fix file input handling bug
    Streamline code and add more comments for readability
    Identify and implement optimization opportunities
    Implement tie breaking motion order selection or deliver every possible optimal alignment rather than deterministic, hardcoded current priority
    Continue searching for potential edge cases and bugs
    Final Reflection

            

