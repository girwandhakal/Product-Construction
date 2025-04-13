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
        nodeList (dict): key-value pairs of state name and Node object.
    """

    def __init__(self, alphabets:list, startState:Node, nodelist:dict):
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
            raise TypeError("Expected a dict")
        if not isinstance(startState, Node):
            raise TypeError("Expected a Node object")
        if not isinstance(alphabets, list):
            raise TypeError("Expected a list") 
               
        self.alphabets = alphabets
        self.nodeList = nodelist
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

        return self.nodeList[name]
    
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
            if nextNode.acceptState == True:
                return True
            currentNode = nextNode

        return False



def ProductConstruction(l1, l2, operation="union"):
        """
        Returns the DFA object after product construction has been applied.

        Args:
            d1 (DFA) : A DFA for a language.
            d2 (DFA) : A DFA for a language.
            operation (str) : 'union' or 'intersection'. default is 'union'.
        
        Returns:
            DFA: A DFA object.

        """

        def getNewAlphabet(l1, l2):
            """
            Returns the new alphabet given two DFA objects which is the intersection of the two languages.

            Args:
                l1 (DFA) : A DFA for a language.
                l2 (DFA) : A DFA for a language.
            
            Returns:
                List: A list of symbols.

            """
            res = []
            for ch in l1.alphabets:
                if ch in l2.alphabets:
                    res.append(ch)
            return res
        
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
            Returns the new alphabet given two DFA objects which is the intersection of the two languages.

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

            alphabet = getNewAlphabet(l1, l2)
            res = {}
            for ch in alphabet:
                res[ch] = node1.rules[ch] + node2.rules[ch] #appends the name of the new node to the dictionary  
            # print(res)
            return res              

        def getNewNodeList(l1, l2):
            """
            Returns the a dictionary of new Node objects after product construction.

            Args:
                l1 (DFA) : A DFA.
                l2 (DFA) : A DFA.
            
            Returns:
                dict: A dictionary mapping each name of state to the Node object.
            """
            
            newNodeList = {}
            for node1 in l1.nodeList.values():
                for node2 in l2.nodeList.values():
                    newNodeName = getNewNodeName(node1, node2)
                    newNodeAcceptState = getNewAcceptState(node1, node2, operation)
                    # print("For node: ", newNodeName, "The rule list is: ")
                    newRules = getNewRules(node1, node2)
                    newNodeList[newNodeName] = Node(newNodeName, newNodeAcceptState, newRules)
            
            return newNodeList
        
        newAlphabet = getNewAlphabet(l1,l2)
        newNodeList = getNewNodeList(l1, l2)
        newStartNodeName = getNewNodeName(l1.start, l2.start)
        newStartNode = newNodeList[newStartNodeName]

        newDFA = DFA(newAlphabet, newStartNode, newNodeList)
        return newDFA



#Example
q0 = Node('q0', False, {'0':'q0', '1':'q1'})
q1 = Node('q1', True, {'0':'q1', '1': 'q1'})

r0 = Node('r0', False, {'0':'r1', '1':'r2'})
r1 = Node('r1', True, {'0':'r1', '1':'r1'})
r2 = Node('r2', False, {'0':'r2', '1':'r2'})

l1 = DFA(['0','1'], r0, {'r0':r0, 'r1':r1, 'r2':r2})
l2 = DFA(['0','1'], q0, {'q0':q0, 'q1':q1})

l3 = ProductConstruction(l1,l2)
print(l3.isAccepted('1000000'))


        
        