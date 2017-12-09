
class Expr:
    def accept(self):
        pass

class Binary(Expr):
    def __init__(self,left,op,right):
        self.left = left
        self.operator = op
        self.right = right
    def __str__(self):
        return "BINARY EXP \n LEFT: %s \n OP: %s \n RIGHT: %s " % (self.left, self.operator, self.right)

    def accept(self,visitor):
        return visitor.visitBinaryExpr(self)



class Grouping(Expr):
    def __init__(self,ex):
        self.expression = ex
    def __str__(self):
        return "GROUPING EXP \n EXP: %s" % self.expression

    def accept(self,visitor):
        return visitor.visitGroupingExpr(self)

class Literal(Expr):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return "LITERAL: %s" % self.value

    def accept(self,visitor):
        return visitor.visitLiteralExpr(self)

class Unary(Expr):
    def __init__(self, token, expr):
        self.token = token
        self.expression = expr
    def __str__(self):
        return "UNARY EXP \n TOKEN: %s \n EXP: %s " % (self.token, self.expression)

    def accept(self,visitor):
        return visitor.visitUnaryExpr(self)

class Visitor:
    def visitBinaryExpr(self,expr):
        pass
    def visitGroupingyExpr(self,expr):
        pass
    def visitLiteralExpr(self,expr):
        pass
    def visitUnaryExpr(self,expr):
        pass
