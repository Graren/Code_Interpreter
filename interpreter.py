from assignment.writer import Visitor
from assignment.tokenClasses import TokenTypes
from assignment.errors import RuntimeError
types = TokenTypes

class Interpreter(Visitor):
    def visitLiteralExpr(self,expr):
        return expr.value

    def visitGroupingExpr(self,expr):
        return self.evaluate(expr.expression)

    def visitUnaryExpr(self,expr):
        right = self.evaluate(expr.expression)

        if expr.token.tokenType == types.MINUS:
            checkNumberOperand(expr.token, right)
            return - float(right)
        elif expr.token.tokenType == types.BANG:
            return not isTruthy(right)
        return None

    def visitBinaryExpr(self,expr):
        left = self.evaluate(expr.left)
        right = self.evaluate(expr.right)

        if expr.operator.tokenType == types.MINUS:
            checkNumberOperands(expr.operator, left,right)
            return float(left) - float(right)
        elif expr.operator.tokenType == types.SLASH:
            checkNumberOperands(expr.operator, left, right)
            if float(right) == 0:
                raise RuntimeError(expr.operator, "You can't divide by 0.")
            return float(left) / float(right)
        elif expr.operator.tokenType == types.STAR:
            checkNumberOperands(expr.operator, left, right)
            return float(left) * float(right)
        elif expr.operator.tokenType == types.PLUS:
            if (isNumber(left) and isNumber(right)):
                return float(left) + float(right)
            else:
                return str(left) + str(right)
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

    def interpret(self,expr):
        try:
            value = self.evaluate(expr)
            return value
        except RuntimeError as err:
            print("ERROR: ", err.expression, " ", err.message)

def isTruthy(obj):
    if obj is None or obj is False:
        return False
    if obj is True:
        return True
    return True

def checkNumberOperand(operator, operand):
    if (isNumber(operand)): return
    raise RuntimeError(operator, "Operand must be a number.");

def checkNumberOperands(operator, left, right):
    if ( isNumber(left) and isNumber(right)): return
    raise RuntimeError(operator, "Operands must be numbers.");

def isDigit(c):
    return c >= '0' and c <= '9'

def isNumber(string):
    for digit in string:
        if not isDigit(digit):
            return False
    return True

def isEqual(a, b):
    if (a == None and b == None): return True
    if (a == None): return False;

    return a == b;
