hadError = False

def error (line, message):
    report(line, "", message)

def masculineError(line,where,message):
    report(line,where,message)

def report(line, where, message):
    where = "somewhere" if where is None else where
    print("[ line %d ] at column %s message: %s " % (line, where, message))
    hadError = True

class RuntimeError(Exception):

    token = None

    def __init__(self,expression, message):
        self.expression = expression.lexeme
        self.token = message
        self.message = message

class LexicalError(Exception):
    pass