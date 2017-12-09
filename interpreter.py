from assignment.writer import Visitor
from assignment.tokenClasses import TokenTypes

types = TokenTypes

class Interpreter(Visitor):
    def visitLiteralExpr(self,expr):
        return expr.value

    def visitGroupingExpr(self,expr):
        return self.evaluate(expr.expression)

    def visitUnaryExpr(self,expr):
        right = self.evaluate(expr.expression)

        if expr.token.tokenType == types.MINUS:
            return - float(right)
        elif expr.token.tokenType == types.BANG:
            return not isTruthy(right)
        return None

    def visitBinaryExpr(self,expr):
        left = self.evaluate(expr.left)
        right = self.evaluate(expr.right)

        if expr.operator.tokenType == types.MINUS:
            return float(left) - float(right)
        elif expr.operator.tokenType == types.SLASH:
            return float(left) / float(right)
        elif expr.operator.tokenType == types.STAR:
            return float(left) * float(right)
        elif expr.operator.tokenType == types.PLUS:
            return float(left) + float(right)
        elif expr.operator.tokenType == types.GREATER_EQUAL:
            return float(left) >= float(right)
        elif expr.operator.tokenType == types.GREATER:
            return float(left) > float(right)
        elif expr.operator.tokenType == types.LESS_EQUAL:
            return float(left) <= float(right)
        elif expr.operator.tokenType == types.LESS:
            return float(left) < float(right)
        elif expr.operator.tokenType == types.EQUAL_EQUAL:
            return isEqual(left,right)
        elif expr.operator.tokenType == types.BANG_EQUAL:
            return not isEqual(left,right)
        return None

    def evaluate(self,expr):
        return expr.accept(self)

    def interpret(self,expr):
        value = self.evaluate(expr)
        # print("%s" % value)
        return value

def isTruthy(obj):
    if obj is None or obj is False:
        return False
    if obj is True:
        return True
    return True

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
