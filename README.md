# Product-Construction

A tool for DFA (Deterministic Finite Automaton) operations - union, intersection, and minimization.

## Requirements

- Python 3
- Graphviz library (download from [https://graphviz.org/download/](https://graphviz.org/download/))

## Usage

### main.py

```bash
python main.py --dfa1 <path_to_dfa1.json> --dfa2 <path_to_dfa2.json> --operation <union | intersection> --testString <string>
```

### xor.py

```bash
python xor.py --union <pathToUnion.json> --intersection <pathToIntersection>
```

### Example

```bash
python main.py --dfa1 dfa/dfa1.json --dfa2 dfa/dfa2.json --operation union --testString 1010
```

### Help

```bash
python main.py --help
```

## DFA JSON Structure

DFAs are defined with the following JSON structure (examples can be found in the `dfa` folder):

```json
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
```

### Required Fields

- **alphabet**: Possible input symbols
- **states**: State names
- **startState**: Start state name (must also be defined in states field)
- **acceptStates**: All accepting states (must also be defined in states field)
- **transitions**: Maps states and their transitions to other states

## Notes

- The `dfa` folder contains several example DFAs for testing, each with a comment explaining what strings it accepts.

- `dfa_format.json` in the `dfa` folder can be copied and modified for testing. Do not modify the field names as they're used by the program.

- Using `--union` creates a `dfa_union.json` file in the `dfa` folder. Subsequent executions overwrite this file.

- Using `--intersection` creates a `dfa_intersection.json` file in the `dfa` folder. Subsequent executions overwrite this file.

- The current `dfa_intersection.json` and `dfa_union.json` files were created using `dfa1.json` and `dfa2.json` as examples.

- An image of the resulting DFA is saved to `min_graph.png`, which is overwritten with each execution.

- `test_minimization.py` was used for experiments in our report. The actual minimization implementation is in `main.py`.

- If you have problems with Graphviz, comment out line 555 in `main.py` by adding a `#` at the beginning of the line.
