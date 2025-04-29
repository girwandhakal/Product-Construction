# Product-Construction
 
Python 3 is needed to run this program, as well as the python library Graphviz.

Usage:
    main.py:
        python main.py --dfa1 <path_to_dfa1.json> --dfa2 <path_to_dfa2.json> --operation <union || intersection> --testString <string>
    xor.py:
        python xor.py --union <pathToUnion.json> --intersection <pathToIntersection> 

Example usage, using dfa1.json and dfa2.json:
    python main.py --dfa1 dfa/dfa1.json --dfa2 dfa/dfa2.json --operation union --testString 1010
        
For help, use:
    python main.py --help

DFAs are defined with this JSON structure (also found in dfa folder):
    {
        "alphabet": ["0", "1"],
        "states": ["q0", "q1"],
        "startState": "q0",
        "acceptStates": ["q1"],
        "transitions": {
            "q0": {"0": "q0", "1": "q1"},
            "q1": {"0": "q1", "1": "q1"}
        }
    }

All fields are required in JSON files:
    alphabet: possible input symbols, 
    states: state names, 
    startState: start state name (must also be defined in states field), 
    acceptStates: all accepting states (must also be defined in states field), 
    transitions: maps states and its transitions to other states 

Notes:
    - The dfa folder contains several example DFAs that can be used in testing. They   include a comment that explains what strings the DFA accepts

    - The dfa folder also contains a file called "dfa_format.json", which can be copied + pasted to a new JSON file for testing. You can modify any values, but DO NOT modify the field names. These exact field names are used in main.py and it will throw errors if the correct field names are missing.

    - Using --union to find the union of two DFAs will save the resulting DFA to a file called "dfa_union.json", located in the dfa folder. Any subsequent executions using --union will overwrite the data currently stored in the file.

    - Using --intersection to find the intersection of two DFAs will save the resulting DFA to a file called "dfa_intersection.json", located in the dfa folder. Any subsequent executions using --intersection will overwrite the data currently stored in the file.

    - The data currently stored in dfa_intersection.json and dfa_union.json were created using dfa1.json and dfa2.json as inputs, as an example. 

    - A PNG file containing an image of the resulting DFA will be saved to a file called "min_graph.png". This file will also be overwritten after any subsequent executions of the program. 

    - The file "test_minimization.py" was used to conduct an experiment for our report. The actual implementation of minimization is within main.py.