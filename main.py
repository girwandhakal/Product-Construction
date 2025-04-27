import argparse
import json
import os


class Node:
    """
    A Node class.

    Attributes:
        name (str): State name.
        acceptState (bool): True if yes, False if no.
        rules (dict): Key-value pairs of input symbol and next state.

    """

    def __init__(self, name:str, acceptState:bool, rules:dict):
        """
        Initializes the Node class.

        Args:
            name (str): Name of the state.
            acceptState (bool): Specifies whether it is an accepting state or not.
            rules (dict): Inputs and transitions for the current state.

        """
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
        """
        Returns the name of the next state.
        Args:
            c (str) : Input symbol.
        """
        return self.rules[c]
    

class DFA:
    """
    A DFA Class.

    Attributes:
        alphabets (list): List of input symbols accepted by the language.
        start (Node): Start state of the DFA.
        stateList (dict): key-value pairs of state name and Node object.
    """

    def __init__(self, alphabets:list, startState:Node, stateList:dict):
        """
        Initializes the DFA class.

        Args:
            alphabets (list): Alphabet symbols of the language.
            startState (Node): Start state of the DFA.
            stateList (dict): key-value pairs of name of the state and the respective Node object. 

        Returns:
            DFA: A DFA object.

        """
                
        if not isinstance(stateList, dict):
            raise TypeError("Expected a dict")
        if not isinstance(startState, Node):
            raise TypeError("Expected a Node object")
        if not isinstance(alphabets, list):
            raise TypeError("Expected a list") 
               
        self.alphabets = alphabets
        self.stateList = stateList
        self.start = startState

    def inAlphabet(self, anInput):
        """
        Checks whether input symbols is part of accepted input symbols.

        Args:
            anInput(str) : input. 

        Returns:
            bool: True if the input symbol is part of the language and False if it is not.

        """
        for ch in anInput:
            if ch not in self.alphabets:
                return False
    
    def getNode(self, name):
        """
        Returns the object for the state of the given name.

        Args:
            name(str) : name of symbol. 

        Returns:
            Node: Returns a Node object.

        """

        return self.stateList[name]
    
    def isAccepted(self, anInput):
        """
        Returns whether the input is accepted by the DFA.

        Args:
            anInput (str): Input string.

        Returns:
            bool: True if accepted and False if rejected.

        """
        if self.inAlphabet(anInput) == False:
            return False        
        currentNode = self.start
        for ch in anInput:
            nextNodeName = currentNode.getNextNode(ch)
            nextNode = self.getNode(nextNodeName)
            currentNode = nextNode

        if currentNode.acceptState == True:
            return True
        return False

    def createJson(self, operation):
        os.makedirs("dfa", exist_ok=True)

        # Data to write
        dfa = {
            "alphabet": self.alphabets,
            "states": list(self.stateList.keys()),
            "startState": self.start.name,
            "acceptStates": [name for name, node in self.stateList.items() if node.acceptState],
            "transitions":  {
                name: node.rules for name, node in self.stateList.items()
            }
        }

        # File path
        file_path = os.path.join("dfa", "dfa_" + operation + ".json")

        # Write to the JSON file
        with open(file_path, "w") as f:
            json.dump(dfa, f, indent=4)

        print(f"JSON file created at {file_path}")
        
def ProductConstruction(l1, l2, operation):
        """
        Returns the DFA object after product construction has been applied.

        Args:
            l1 (DFA) : A DFA for a language.
            l2 (DFA) : A DFA for a language.
            operation (str) : 'union' or 'intersection'
        
        Returns:
            DFA: A DFA object.

        """
        if operation not in ['union', 'intersection']:
            raise ValueError("operation must be 'union' or 'intersection'")
        if not isinstance(l1, DFA) or not isinstance(l2, DFA):
            raise TypeError("Both l1 and l2 must be instances of the DFA class.")
        
        def getNewNodeName(node1,node2):
            """
            Returns the concatenation of the two node names.

            Args:
                node1 (Node) : A node.
                node2 (Node) : A node.
            
            Returns:
                str: New Node name .

            """
            return (node1.name + node2.name)
        
        def getNewAcceptState(node1, node2, op):
            """
            Returns whether the new node is an accepting state or not.

            Args:
                node1 (Node) : A node.
                node2 (Node) : A node.
                op (str) : 'union'(default) or 'intersection'
            
            Returns:
                List: A list of symbols.

            """
            if(op == 'union'):
                if(node1.acceptState or node2.acceptState):
                    return True
                return False
            elif(op == 'intersection'):
                if(node1.acceptState and node2.acceptState):
                    return True
                return False
            else:
                raise ValueError("Accepted operations are 'union'(default) or 'intersection'. ")
            
        def getNewRules(node1, node2):
            """
            Returns the new rules dictionary after product construction.

            Args:
                node1 (Node) : A node.
                node2 (Node) : A node.
            
            Returns:
                dict: A dictionary mapping each input symbol to the name of the next state.
            """

            alphabet = l1.alphabets
            res = {}
            for ch in alphabet:
                res[ch] = node1.rules[ch] + node2.rules[ch] #appends the name of the new node to the dictionary  
            # print(res)
            return res              

        def getNewstateList(l1, l2):
            """
            Returns the a dictionary of new Node objects after product construction.

            Args:
                l1 (DFA) : A DFA.
                l2 (DFA) : A DFA.
            
            Returns:
                dict: A dictionary mapping each name of state to the Node object.
            """
            
            newstateList = {}
            for node1 in l1.stateList.values():
                for node2 in l2.stateList.values():
                    newNodeName = getNewNodeName(node1, node2)
                    newNodeAcceptState = getNewAcceptState(node1, node2, operation)
                    # print("For node: ", newNodeName, "The rule list is: ")
                    newRules = getNewRules(node1, node2)
                    newstateList[newNodeName] = Node(newNodeName, newNodeAcceptState, newRules)
            
            return newstateList
        
        newAlphabet = l1.alphabets #does not matter since it has to be equal anyways
        newstateList = getNewstateList(l1, l2)
        newStartNodeName = getNewNodeName(l1.start, l2.start)
        newStartNode = newstateList[newStartNodeName]

        newDFA = DFA(newAlphabet, newStartNode, newstateList)
        return newDFA



#Example
#q0 = Node('q0', False, {'0':'q0', '1':'q1'})
#q1 = Node('q1', True, {'0':'q1', '1': 'q1'})

#r0 = Node('r0', False, {'0':'r1', '1':'r2'})
#r1 = Node('r1', True, {'0':'r1', '1':'r1'})
#r2 = Node('r2', False, {'0':'r2', '1':'r2'})

#l1 = DFA(['0','1'], r0, {'r0':r0, 'r1':r1, 'r2':r2})
#l2 = DFA(['0','1'], q0, {'q0':q0, 'q1':q1})

#l3 = ProductConstruction(l1,l2, "union")
#print(l3.isAccepted('00000002'))

#l3 = ProductConstruction(l1,l2)
#print(l3.isAccepted('1000000'))

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
    
    stateList = {}
    for state in states:
        if state not in transitions:
            raise ValueError(f"No transitions defined for state {state}")
        rules = transitions[state]
        if not isinstance(rules, dict):
            raise ValueError(f"Transitions for state {state} must be a dictionary")
        for symbol in alphabet:
            if symbol not in rules:
                raise ValueError(f"No transition for symbol '{symbol}' in state {state}")
            nextState = rules[symbol]
            if nextState not in states:
                raise ValueError(f"Transition for {state} on '{symbol}' points to invalid state {nextState}")
        
        isAccept = state in acceptStates
        stateList[state] = Node(state, isAccept, rules)

    startNode = stateList[startState]
    return DFA(alphabet, startNode, stateList)



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

        if l1.alphabets != l2.alphabets:
            print("\nError: For product construction, the alphabets of the two DFA's have to be the same.\n")
            return
        
        resultDFA = ProductConstruction(l1, l2, args.operation)
        resultDFA.createJson(args.operation)
        
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
        
        