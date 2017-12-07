
class Expr:
    pass

class Binary(Expr):
    def __init__(self,left,op,right):
        self.left = left
        self.operator = op
        self.right = right

class Grouping(Expr):
    def __init__(self,ex):
        self.expression = ex

class Literal(Expr):
    def __init__(self,value):
        self.value = value

class Unary(Expr):
    def __init__(self, token, expr):
        self.token = token
        self.expression = expr