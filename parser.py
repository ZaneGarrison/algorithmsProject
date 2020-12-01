from tokens import *
from scanner import Scanner
from binaryTree import *


class Parser:
    def __init__(self):
        self.parseTreeRoot = None
        self.parseTrees = []
        self.tokens = []
        self.nextToken = None
        self.idIntHolder = None

        self.analyser = Scanner("test5.jl")
        print('Equation: ')
        temp = self.analyser.getTokens(returnTokens=True)
        for data in temp:
            self.tokens.append(data)
        self.nextToken = self.tokens.pop(0)

    def parse(self):
        print(self.analyser.code)
        s = Scanner("test5.jl")
        print(s.getTokens())
        self.block()

    def statement(self):

        if (
                self.nextToken.getTypeID() == VARIABLE.getTypeID() or self.nextToken.getTypeID() == INT.getTypeID()):
            self.idIntHolder = self.nextToken
            self.lex()
        if (self.nextToken.getTypeID() == EQUAL_OPERATOR.getTypeID() or
                self.nextToken.getTypeID() == ADD_OPERATOR.getTypeID() or
                self.nextToken.getTypeID() == SUB_OPERATOR.getTypeID() or
                self.nextToken.getTypeID() == MUL_OPERATOR.getTypeID() or
                self.nextToken.getTypeID() == DIV_OPERATOR.getTypeID() or
                self.nextToken.getTypeID() == MOD_OPERATOR.getTypeID()):
            self.parseTreeRoot = self.addToParseTree(self.parseTreeRoot, self.nextToken)
            self.parseAssignment()

        self.printInOrderValueToKeyword(self.parseTreeRoot)
        self.printPreOrder(self.parseTreeRoot)
        print()
        self.printPostOrder(self.parseTreeRoot)
        self.addToParseTreeList()

    # parses assignment statements into BNF form also works with for loop assignment expressions
    def parseAssignment(self):
        # add it to the parse tree
        self.parseTreeRoot = self.addToParseTree(self.parseTreeRoot, self.idIntHolder)
        # move the next token
        self.lex()
        self.arithmeticExpression()

    # handles parsing simple math expressions
    def arithmeticExpression(self):

        # if the nextToken is an operator
        if (self.nextToken.getTypeID() == ADD_OPERATOR.getTypeID() or
                self.nextToken.getTypeID() == SUB_OPERATOR.getTypeID() or
                self.nextToken.getTypeID() == MUL_OPERATOR.getTypeID() or
                self.nextToken.getTypeID() == DIV_OPERATOR.getTypeID() or
                self.nextToken.getTypeID() == MOD_OPERATOR.getTypeID()):
            # add it to the parse tree
            self.parseTreeRoot = self.addToParseTree(self.parseTreeRoot, self.nextToken)
            # move to the next token
            self.lex()
            # calls itself since  you could have something like 1+1-3
            self.arithmeticExpression()
            # move to the next token
            self.lex()

        # determines if the token is a left parenthesis
        if self.nextToken.getTypeID() == LEFT_PARENTHESIS.getTypeID():
            # calls itself since an arithmetic expression is conrained between two parenthesis
            self.arithmeticExpression()
            # error checks
            if self.nextToken.getTypeID() != RIGHT_PARENTHESIS.getTypeID():
                self.error("Error unclosed parenthesis")

        # determines if the token is an identifier or an int
        if (self.nextToken.getTypeID() == VARIABLE.getTypeID() or
                self.nextToken.getTypeID() == INT.getTypeID()):
            # add the token to the parse tree
            self.parseTreeRoot = self.addToParseTree(self.parseTreeRoot, self.nextToken)

    # removes a token from the tokens linked list effectively incrementing by one
    def lex(self):
        if len(self.tokens) < 1:
            return None
        else:
            self.nextToken = self.tokens.pop(0)

    def block(self):
        # iterate through the tokens
        while len(self.tokens) > 0:
            if self.nextToken.getTypeID() == INT.getTypeID():
                self.statement()
            # move to the next token
            self.lex()

    # outputs error messages to the console
    @staticmethod
    def error(msg):
        print(msg)

    def addToParseTree(self, root, item):
        if root is None:
            root = binaryTree()
            root.setValue(item)
        elif root.getLeftChild() is None:
            root.setLeftChild(self.addToParseTree(root.getLeftChild(), item))
        elif root.getRightChild() is None:
            root.setRightChild(self.addToParseTree(root.getRightChild(), item))
        elif root.getRightChild() is not None:
            root.setRightChild(self.addToParseTree(root.getRightChild(), item))
        return root

    def printInOrderValueToKeyword(self, root):
        if root is None:
            return
        self.printInOrderValueToKeyword(root.getLeftChild())
        self.printInOrderValueToKeyword(root.getRightChild())

    def printPreOrder(self, root):
        if root is None:
            return
        print(root.getValue().getValue() + " ", end=' ')
        self.printPreOrder(root.getLeftChild())
        self.printPreOrder(root.getRightChild())

    def printPostOrder(self, root):
        if root is None:
            return
        print(root.getValue().getValue() + " ", end=' ')
        self.printPostOrder(root.getRightChild())
        self.printPostOrder(root.getLeftChild())

    def addToParseTreeList(self):
        self.parseTrees.append(self.parseTreeRoot)
        self.parseTreeRoot = None


test = Parser()
test.parse()
