import argparse
import json
import os


class Node:

    def __init__(self, name:str, acceptState:bool, rules:dict):

        if not isinstance(name, str):
            raise TypeError("Expected a string")
        if not isinstance(acceptState, bool):
            raise TypeError("Expected a boolean")
        if not isinstance(rules, dict):
            raise TypeError("Expected a dictionary")

        self.name = name
        self.acceptState = acceptState 
        self.rules = rules 

    def getNextNode(self, c):

        return self.rules[c]
    

class DFA:

    def __init__(self, alphabets:list, startState:Node, nodelist:dict):
                
        if not isinstance(nodelist, dict):
            raise TypeError("Expected a dict")
        if not isinstance(startState, Node):
            raise TypeError("Expected a Node object")
        if not isinstance(alphabets, list):
            raise TypeError("Expected a list") 
               
        self.alphabets = alphabets
        self.nodeList = nodelist
        self.start = startState

    def inAlphabet(self, anInput):

        for ch in anInput:
            if ch not in self.alphabets:
                return False
    
    def getNode(self, name):

        return self.nodeList[name]
    
    def isAccepted(self, anInput):

        if self.inAlphabet(anInput) == False:
            return False        
        currentNode = self.start
        for ch in anInput:

            nextNodeName = currentNode.getNextNode(ch)
            nextNode = self.getNode(nextNodeName)
            if nextNode.acceptState == True:
                return True
            currentNode = nextNode

        return False

    def createJson(self):
        os.makedirs("dfa", exist_ok=True)

        # Data to write
        dfa = {
            "alphabet": self.alphabets,
            "states": list(self.nodeList.keys()),
            "startState": self.start.name,
            "acceptStates": [name for name, node in self.nodeList.items() if node.acceptState],
            "transitions":  {
                name: node.rules for name, node in self.nodeList.items()
            }
        }

        # File path
        file_path = os.path.join("dfa", "dfa.json")

        # Write to the JSON file
        with open(file_path, "w") as f:
            json.dump(dfa, f, indent=4)

        print(f"JSON file created at {file_path}")
        
def ProductConstruction(l1, l2, operation):

        def getNewAlphabet(l1, l2):

            res = []
            for ch in l1.alphabets:
                if ch in l2.alphabets:
                    res.append(ch)
            return res
        
        def getNewNodeName(node1,node2):

            return (node1.name + node2.name)
        
        def getNewAcceptState(node1, node2, op):

            if(op == 'union'):
                if(node1.acceptState or node2.acceptState):
                    return True
                return False
            elif(op == 'intersection'):
                if(node1.acceptState and node2.acceptState):
                    return True
                return False
            else:
                raise ValueError("Accepted operations are 'union' or 'intersection'. ")
            
        def getNewRules(node1, node2):

            alphabet = getNewAlphabet(l1, l2)
            res = {}
            for ch in alphabet:
                res[ch] = node1.rules[ch] + node2.rules[ch] #appends the name of the new node to the dictionary  
            return res              

        def getNewNodeList(l1, l2):
            
            newNodeList = {}
            for node1 in l1.nodeList.values():
                for node2 in l2.nodeList.values():
                    newNodeName = getNewNodeName(node1, node2)
                    newNodeAcceptState = getNewAcceptState(node1, node2, operation)
                    newRules = getNewRules(node1, node2)
                    newNodeList[newNodeName] = Node(newNodeName, newNodeAcceptState, newRules)
            
            return newNodeList
        
        newAlphabet = getNewAlphabet(l1,l2)
        newNodeList = getNewNodeList(l1, l2)
        newStartNodeName = getNewNodeName(l1.start, l2.start)
        newStartNode = newNodeList[newStartNodeName]

        newDFA = DFA(newAlphabet, newStartNode, newNodeList)
        return newDFA

def parseDFA(dfaPath):
    if not os.path.exists(dfaPath):
        raise FileNotFoundError(f"File {dfaPath} does not exist")
    
    with open(dfaPath, 'r') as f:
        try:
            config = json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in {dfaPath}: {e}")
    
    fields = ["alphabet", "states", "startState", "acceptStates", "transitions"]
    for field in fields:
        if field not in config:
            raise ValueError(f"Missing required field '{field}' in {dfaPath}")
    
    #required fields in json
    alphabet = config["alphabet"]
    states = config["states"]
    startState = config["startState"]
    acceptStates = config["acceptStates"]
    transitions = config["transitions"]

    if not isinstance(alphabet, list) or not alphabet:
        raise ValueError("Alphabet must be non-empty")
    if not isinstance(states, list) or not states:
        raise ValueError("States must be non-empty")
    if startState not in states:
        raise ValueError("Start state must be a defined state")
    if not isinstance(acceptStates, list):
        raise ValueError("Accept states must be a list")
    for state in acceptStates:
        if state not in states:
            raise ValueError(f"Accept state {state} mnust be a defined state")
    if not isinstance(transitions, dict):
        raise ValueError("Transitions must be a dictionary")
    
    node_list = {}
    for state in states:
        if state not in transitions:
            raise ValueError(f"No transitions defined for state {state}")
        rules = transitions[state]
        if not isinstance(rules, dict):
            raise ValueError(f"Transitions for state {state} must be a dictionary")
        for symbol in alphabet:
            if symbol not in rules:
                raise ValueError(f"No transition for symbol '{symbol}' in state {state}")
            next_state = rules[symbol]
            if next_state not in states:
                raise ValueError(f"Transition for {state} on '{symbol}' points to invalid state {next_state}")
        
        is_accept = state in acceptStates
        node_list[state] = Node(state, is_accept, rules)

    start_node = node_list[startState]
    return DFA(alphabet, start_node, node_list)



def main():
    parser = argparse.ArgumentParser(description="Product construction on two DFAs")
    parser.add_argument("--dfa1", required = True, help = "Path for DFA 1")
    parser.add_argument("--dfa2", required = True, help = "Path for DFA 2")
    parser.add_argument("--operation", required = True, choices = ["union", "intersection"], help = "Operation: 'union' or 'intersection'")
    parser.add_argument("--testString", required = True, help = "String to test on result DFA")
    args = parser.parse_args()

    try:
        l1 = parseDFA(args.dfa1)
        l2 = parseDFA(args.dfa2)
        resultDFA = ProductConstruction(l1, l2, args.operation)
        resultDFA.createJson()
        
        if args.testString:
            isAccepted = resultDFA.isAccepted(args.testString)
            print(f"\nString '{args.testString}' is "
                  f"{'accepted' if isAccepted else 'rejected'} by the resulting DFA.")
        else:
            print("\nNo test string provided.")
    except Exception as e:
        print(f"Error: {e}")
        return

if __name__ == "__main__":
    main()
        
        