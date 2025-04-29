# Product-Construction
 
Python 3 is needed to run this program, as well as the python library Graphviz.

Usage:
    main.py:
        python main.py --dfa1 <pathToDFA1.json> --dfa2 <pathToDFA2.json> --operation <union | intersection> --testString <string>
    xor.py:
        python xor.py --union <pathToUnion.json> --intersection <pathToIntersection> 
        
For help, use: python main.py --help

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
    alphabet: possible input symbols
    states: state names
    startState: start state name (must be defined in states field)
    acceptStates: all accepting states (must be defined in states field)
    transitions: maps states and its transitions to other states