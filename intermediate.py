from assignment.writer import Visitor
from assignment.tokenClasses import TokenTypes
from assignment.errors import RuntimeError
types = TokenTypes

class ASToken:
    value = 0;
    name = ""

    def __init__(self,value,name):
        self.value = value
        self.name = name

class Generator(Visitor):
    current = 1
    previous = 0
    stack = []
    name = 'R'
    order = []
    identifier = ""
    assignment = False;


    def __init__(self, assignment = False, identifier = ""):
        self.previous = 0
        self.current = 1
        self.assignment = assignment
        self.identifier = identifier


    def visitLiteralExpr(self,expr):
        # self.passed(types.NUMBER, expr.value, None)
        return expr.value

    def visitGroupingExpr(self,expr):
        return self.evaluate(expr.expression)

    def visitUnaryExpr(self,expr):
        self.isGrouping = True
        right = self.evaluate(expr.expression)

        if expr.token.tokenType == types.MINUS:
            checkNumberOperand(expr.token, right)
            return - float(right)
        elif expr.token.tokenType == types.PLUS:
            checkNumberOperand(expr.token, right)
            return + float(right)
        elif expr.token.tokenType == types.BANG:
            return not isTruthy(right)

        return None

    def visitBinaryExpr(self,expr):
        left = self.evaluate(expr.left)
        right = self.evaluate(expr.right)

        if expr.operator.tokenType == types.MINUS:
            # checkNumberOperands(expr.operator, left,right)
            self.passed(expr.operator.tokenType, left, right)
            n = "%s%s" % (self.name, self.current)
            if(isinstance(left, ASToken)):
                left = left.value
            if(isinstance(right,ASToken)):
                right = right.value
            token = ASToken(float(left) - float(right), n)
            self.current += 1
            return token
        elif expr.operator.tokenType == types.SLASH:
            # checkNumberOperands(expr.operator, left, right)
            # if float(right) == 0:
            #     raise RuntimeError(expr.operator, "You can't divide by 0.")
            self.passed(expr.operator.tokenType, left, right)
            n = "%s%s" % (self.name, self.current)
            if (isinstance(left, ASToken)):
                left = left.value
            if (isinstance(right, ASToken)):
                right = right.value
            token = ASToken(float(left) / float(right), n)
            self.current+=1
            return token
        elif expr.operator.tokenType == types.STAR:
            # checkNumberOperands(expr.operator, left, right)
            self.passed(expr.operator.tokenType, left, right)
            n = "%s%s" % (self.name, self.current)
            if (isinstance(left, ASToken)):
                left = left.value
            if (isinstance(right, ASToken)):
                right = right.value
            token = ASToken(float(left) * float(right), n)
            self.current += 1
            return token
        elif expr.operator.tokenType == types.PLUS:
                self.passed(expr.operator.tokenType, left, right)
                n = "%s%s" % (self.name, self.current)
                if (isinstance(left, ASToken)):
                    left = left.value
                if (isinstance(right, ASToken)):
                    right = right.value
                token = ASToken(float(left) + float(right), n)
                self.current += 1
                return token
        elif expr.operator.tokenType == types.GREATER_EQUAL:
            checkNumberOperands(expr.operator, left, right)
            return float(left) >= float(right)
        elif expr.operator.tokenType == types.GREATER:
            checkNumberOperands(expr.operator, left, right)
            return float(left) > float(right)
        elif expr.operator.tokenType == types.LESS_EQUAL:
            checkNumberOperands(expr.operator, left, right)
            return float(left) <= float(right)
        elif expr.operator.tokenType == types.LESS:
            checkNumberOperands(expr.operator, left, right)
            return float(left) < float(right)
        elif expr.operator.tokenType == types.EQUAL_EQUAL:
            return isEqual(left,right)
        elif expr.operator.tokenType == types.BANG_EQUAL:
            return not isEqual(left,right)
        return None

    def evaluate(self,expr):
        return expr.accept(self)

    def generate(self,expr):
        try:
            value = self.evaluate(expr)
            if (self.assignment):
                self.passed(types.COLON_EQUAL, value, "", self.identifier)
            return value
        except RuntimeError as err:
            print("ERROR: ", err.expression, " ", err.message)

    def passed(self,type, left, right, identifier = None):
        pL = ""
        pR = ""
        if (isinstance(left, ASToken)):
            pL = left.name
        else:
            pL = left
        if (isinstance(right, ASToken)):
            pR = right.name
        else:
            pR = right
        if(type == types.PLUS):
            print("ADD %s %s %s%s" % (pL, pR, self.name, self.current))
        elif(type == types.MINUS):
            print("SUB %s %s %s%s" % (pL, pR, self.name, self.current))
        elif (type == types.STAR):
            print("MUL %s %s %s%s" % (pL, pR, self.name, self.current))
        elif (type == types.SLASH):
            print("DIV %s %s %s%s" % (pL, pR, self.name, self.current))
        elif (type == types.COLON_EQUAL):
            print("STO %s %s" % (pL, identifier))
        elif (type == types.NUMBER):
            print("STO %s  %s%s" % (pL,self.name, self.current))
        # print(self.stack)
        # print(self.order)

def isTruthy(obj):
    if obj is None or obj is False:
        return False
    if obj is True:
        return True
    return True

def checkNumberOperand(operator, operand):
    if (isNumberByException(operand)): return
    raise RuntimeError(operator, "Operand must be a number.");

def checkNumberOperands(operator, left, right):
    if ( isNumberByException(left) and isNumberByException(right)): return
    raise RuntimeError(operator, "Operands must be numbers.");

def isDigit(c):
    return c >= '0' and c <= '9'

def isNumber(string):
    for digit in string:
        if not isDigit(digit):
            return False
    return True

def isNumberByException(c):
    try:
        float(c)
        return True
    except ValueError:
        return False

def isEqual(a, b):
    if (a == None and b == None): return True
    if (a == None): return False;

    return a == b;


