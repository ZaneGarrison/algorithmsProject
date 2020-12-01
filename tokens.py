class Tokens:
    def __init__(self, value, id, keyword):
        self.value = value
        self.ID = id
        self.keyword = keyword

    def setvalue(self, v):
        value = v

    def returnvalue(self):
        return self.value

    def getValue(self):
        return self.value

    def setid(self, id):
        self.ID = id

    def returnid(self):
        return self.ID

    def getTypeID(self):
        return self.ID

    def setkeyword(self, kw):
        self.keyword = kw

    def returnkeyword(self):
        return self.keyword

    def getKeyword(self):
        return self.keyword


EQUAL_OPERATOR = Tokens("=", 100, "EQUAL_OPERATOR")
ADD_OPERATOR = Tokens("+", 101, "add_operator")
SUB_OPERATOR = Tokens("-", 102, "sub_operator")
MUL_OPERATOR = Tokens("*", 103, "mul_operator")
DIV_OPERATOR = Tokens("/", 104, "div_operator")
MOD_OPERATOR = Tokens("%", 105, "mod_operator")
EXP_OPERATOR = Tokens("^", 106, "exp_operator")
LEFT_PARENTHESIS = Tokens("(", 107, "left_parenthesis")
RIGHT_PARENTHESIS = Tokens(")", 108, "right_parenthesis")
VARIABLE = Tokens("", 109, "VARIABLE")
INT = Tokens("", 110, "int")
FLOAT_LITERAL = Tokens("", 111, "float_literal")
