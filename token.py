from . import tokenClasses

class Token:

    tokenType = None
    lexeme = ""
    literal = {}
    line = 0
    def __init__(self, tokenType, lex,  literal, line ):
        self.tokenType = tokenType
        self.lexeme = lex
        self.literal = literal
        self.line = line
    def __str__(self):
        return "TOKEN\n\t TYPE: %s \t LEXEME: %s \t LITERAL: %s " % (self.tokenType, self.lexeme, self.literal)

