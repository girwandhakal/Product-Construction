
class DFA:
    def __init__(self, alphabets, startState, nodelist):
        """
        Initializes the DFA class.

        Args:
            alphabets (list): Alphabet symbols of the language.
            startState (Node): Start state of the DFA.
            nodelist (dict): key-value pairs of name of the state and the respective Node object. 

        Returns:
            DFA: A DFA object.

        """
                
        if not isinstance(nodelist, dict):
            raise TypeError("Expected a list")
        
        self.alphabets = alphabets
        self.nodeList = nodelist
        self.start = startState

    def inAlphabet(self, char):
        """
        Checks whether a symbol is part of accepted input symbols.

        Args:
            char(str) : input symbol. 

        Returns:
            bool: True if the input symbol is part of the language and False if it is not.

        """
        return char in self.alphabets
    
    def getNode(self, name):
        """
        Returns the node object for the state of the given name.

        Args:
            name(str) : name of symbol. 

        Returns:
            Node: Returns a Node object.

        """

        return self.nodeList[name]
    
    def isAccepted(self, anInput):
        """
        Returns whether the input is accepted by the DFA.

        Args:
            anInput (str): Input string.

        Returns:
            bool: True if accepted and False if rejected.

        """
        currentNode = self.start
        for ch in anInput:
            if self.inAlphabet(ch) == False:
                return False
            nextNodeName = currentNode.getNextNode(ch)
            nextNode = self.getNode(nextNodeName)
            if nextNode.acceptState == True:
                return True
            currentNode = nextNode

        return False


class Node:
    def __init__(self, name, acceptState, rules:dict):
        """
        Initializes the Node class.

        Args:
            name (str): Name of the state.
            acceptState (bool): Specifies whether it is an accepting state or not.
            rules (dict): Inputs and transitions for the current state.

        """

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
    

#Example
q0 = Node('q0', False, {'0':'q0', '1':'q1'})
q1 = Node('q1', True, {'0':'q1', '1': 'q1'})

d = DFA([0,1], q0, {'q0':q0, 'q1':q1})

print(d.isAccepted('0000000000000000000'))



        
        