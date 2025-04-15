import json
import argparse
import os

def load_dfa(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)
    
def compute_xor_dfa(union_dfa, intersection_dfa):
    union_accepts = set(union_dfa['acceptStates'])
    intersection_accepts = set(intersection_dfa['acceptStates'])
    xor_accepts = list(union_accepts - intersection_accepts)
    
    xor_dfa = union_dfa.copy()
    xor_dfa['acceptStates'] = xor_accepts
    
    return xor_dfa

def save_dfa(dfa):
    os.makedirs("dfa", exist_ok=True)
    output_path = os.path.join("dfa", "dfa_xor.json")
    with open(output_path, 'w') as f:
        json.dump(dfa, f, indent=4)
    print(f"XOR DFA saved!")
    
def main():
    parser = argparse.ArgumentParser(description='Construct XOR DFA from union and intersection DFAs.')
    parser.add_argument('--union', required=True, help='Path to union DFA JSON file.')
    parser.add_argument('--intersection', required=True, help='Path to intersection DFA JSON file.')
    args = parser.parse_args()
    
    union_dfa = load_dfa(args.union)
    intersection_dfa = load_dfa(args.intersection)
    xor_dfa = compute_xor_dfa(union_dfa, intersection_dfa)
    save_dfa(xor_dfa)
    
if __name__ == '__main__':
    main()