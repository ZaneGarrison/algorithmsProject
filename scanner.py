import logging

from tokens import *

logging.basicConfig(filename='ADAdebug')


class Scanner:

    # constructor
    def __init__(self, testfile):
        try:
            import os
            assumedFile = os.path.realpath(__file__)
            assumedFile = assumedFile[:assumedFile.rfind('/') + 1]
            self.outputFileName = assumedFile + "output.txt"
            self.inputFileName = assumedFile + testfile
            # set up the input and output files as well as the buffered writer for writing to an output file
            # input file mut be in the same directory as the package

            self.inputFile = open(self.inputFileName, 'r')
            try:
                self.outputFile = open(self.outputFileName, 'w')
            except:
                self.outputFile = open(self.outputFileName, 'x')
                self.outputFile.close()
                self.outputFile = open(self.outputFileName, 'w')
            self.bw = open(self.outputFileName, 'w')
            self.variables = None
            self.code = ''


        except Exception as ex:
            logging.log('error', ex)

    def getTokens(self, returnTokens=None):

        tokenList = []
        try:
            # initialize Arraylist to hold tokens
            data = self.readInputFile()

            # iterate through every string
            for s in data:
                # call the lookup function which will determine the token type and return the appropriate output message
                if returnTokens is None:
                    tokenList.append(self.search(s))
                else:
                    tokenList.append(self.searchToken(s))
                # System.out.println(s);

            for t in tokenList:
                pass
                # System.out.println(t.toString());

            # close the output file
            self.bw.close()


        except Exception as ex:
            logging.log('error', ex)
        # print(data)

        return tokenList

    def readInputFile(self):
        # set up string for holding file contents as well as the buffered reader
        data = ""
        br = self.inputFile
        ## //used to read file line by line

        # //read file line by line

        for line in br.readlines():
            self.code = self.code + line
            if line != None:
                data += line + " "
        # //splits the String by white space except where it is between quotation marks, also splits string by brackets to seperate the brackets out, and commas

        stringArray = data.split(" (?=([^\\\"]*\\\"[^\\\"]*\\\")*[^\\\"]*$)|"
                                 + "\\[(?=([^\\\"]*\\\"[^\\\"]*\\\")*[^\\\"]*$)|"
                                 + "\\](?=([^\\\"]*\\\"[^\\\"]*\\\")*[^\\\"]*$)|"
                                 + ",(?=([^\\\"]*\\\"[^\\\"]*\\\")*[^\\\"]*$)")

        # //convert string array into an arraylist
        list1 = str(stringArray[0]).split('\n')
        list1 = [broken for data in list1 for broken in data.split(' ')]
        # //remove all excess whitespace that may be left over from the split
        list1 = [temp for temp in list1 if len(temp.strip()) > 0]
        return list1

    # checks whether a string is an integer number or not
    def isIntNumber(self, s):
        return s.matches("-?\\d+?")

    # checks whether a string is a float number or not
    def isfloat(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def isFloatNumber(self, s):
        return s.matches("-?\\d+(\\.\\d+)")

    # checks whether a string is a string literal or not
    def isStringLiteral(self, s):
        return (s.startsWith("\"") and s.endsWith("\""))

    # checks whether a string is an identifier or not
    def isIdentifier(self, s):
        return (not s.contains("(") or not s.contains(")")) and (not s.startsWith("\"") or not s.endsWith("\""))

    def search(self, tokens):
        currentCode = -1
        keyword = ""
        currentToken = tokens


        if str(EQUAL_OPERATOR.returnvalue()).lower() in str(tokens).lower():
            currentCode = EQUAL_OPERATOR.returnid()
            keyword = EQUAL_OPERATOR.returnkeyword()
        elif str(ADD_OPERATOR.returnvalue()).lower() in str(tokens).lower():
            currentCode = ADD_OPERATOR.returnid()
            keyword = ADD_OPERATOR.returnkeyword()
        elif str(SUB_OPERATOR.returnvalue()).lower() in str(tokens).lower():
            currentCode = SUB_OPERATOR.returnid()
            keyword = SUB_OPERATOR.returnkeyword()
        elif str(MUL_OPERATOR.returnvalue()).lower() in str(tokens).lower():
            currentCode = MUL_OPERATOR.returnid()
            keyword = MUL_OPERATOR.returnkeyword()
        elif str(DIV_OPERATOR.returnvalue()).lower() in str(tokens).lower():
            currentCode = DIV_OPERATOR.returnid()
            keyword = DIV_OPERATOR.returnkeyword()
        elif str(MOD_OPERATOR.returnvalue()).lower() in str(tokens).lower():
            currentCode = MOD_OPERATOR.returnid()
            keyword = MOD_OPERATOR.returnkeyword()
        elif str(EXP_OPERATOR.returnvalue()).lower() in str(tokens).lower():
            currentCode = EXP_OPERATOR.returnid()
            keyword = EXP_OPERATOR.returnkeyword()
        elif str(LEFT_PARENTHESIS.returnvalue()).lower() in str(tokens).lower():
            currentCode = LEFT_PARENTHESIS.returnid()
            keyword = LEFT_PARENTHESIS.returnkeyword()
        elif str(RIGHT_PARENTHESIS.returnvalue()).lower() in str(tokens).lower():
            currentCode = RIGHT_PARENTHESIS.returnid()
            keyword = RIGHT_PARENTHESIS.returnkeyword()
        elif str(tokens).lower().isidentifier():
            currentCode = VARIABLE.returnid()
            keyword = VARIABLE.returnkeyword()
        elif str(tokens).lower().isdigit():
            currentCode = INT.returnid()
            keyword = INT.returnkeyword()
        elif self.isfloat(str(tokens).lower()):
            currentCode = FLOAT_LITERAL.returnid()
            keyword = FLOAT_LITERAL.returnkeyword()
        else:
            logging.error('The lookup function was unable to process. \n' + str(
                tokens).lower() + "\nPlease find the missing element.")

        return [currentToken, currentCode, keyword]

    def searchToken(self, tokens):
        currentCode = -1


        if str(EQUAL_OPERATOR.returnvalue()).lower() in str(tokens).lower():
            currentCode = EQUAL_OPERATOR
        elif str(ADD_OPERATOR.returnvalue()).lower() in str(tokens).lower():
            currentCode = ADD_OPERATOR
        elif str(SUB_OPERATOR.returnvalue()).lower() in str(tokens).lower():
            currentCode = SUB_OPERATOR
        elif str(MUL_OPERATOR.returnvalue()).lower() in str(tokens).lower():
            currentCode = MUL_OPERATOR
        elif str(DIV_OPERATOR.returnvalue()).lower() in str(tokens).lower():
            currentCode = DIV_OPERATOR
        elif str(MOD_OPERATOR.returnvalue()).lower() in str(tokens).lower():
            currentCode = MOD_OPERATOR
        elif str(EXP_OPERATOR.returnvalue()).lower() in str(tokens).lower():
            currentCode = EXP_OPERATOR
        elif str(LEFT_PARENTHESIS.returnvalue()).lower() in str(tokens).lower():
            currentCode = LEFT_PARENTHESIS
        elif str(RIGHT_PARENTHESIS.returnvalue()).lower() in str(tokens).lower():
            currentCode = RIGHT_PARENTHESIS
        elif str(tokens).lower().isidentifier():
            currentCode = VARIABLE
            currentCode = Tokens(str(tokens).lower(), currentCode.getTypeID(), currentCode.getKeyword())
        elif str(tokens).lower().isdigit():
            currentCode = INT
            currentCode = Tokens(str(tokens).lower(), currentCode.getTypeID(), currentCode.getKeyword())
        elif self.isfloat(str(tokens).lower()):
            currentCode = FLOAT_LITERAL
            currentCode = Tokens(str(tokens).lower(), currentCode.getTypeID(), currentCode.getKeyword())
        else:
            logging.error('The lookup function was unable to process. \n' + str(
                tokens).lower() + "\nPlease find the missing element.")

        return currentCode


#s = Scanner("test5.jl")
#print(s.getTokens())
# s = Scanner("test2.jl")
# print(s.getTokens())
# s = Scanner("test3.jl")
# print(s.getTokens())
# s = Scanner("test4.jl")
# print(s.getTokens())
