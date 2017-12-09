from assignment.token import tokenClasses,Token
from assignment.writer import Expr, Binary, Unary, Grouping, Literal
from assignment.errors import report

types = tokenClasses.TokenTypes

def error(token, message):
    report(token.line, "at '%s' "  % token.lexeme, " %s " % message )


class Parser:

    def __init__(self, tokens, scanner):
        self.tokens = tokens
        self.current = 0
        self.scanner = scanner

    def parse(self):
        try:
            return self.expression()
        except ParseError:
            return None

    # Rules
    def expression(self):
        return self.equality();

    # equality → comparison ( ( "!=" | "==" ) comparison )* ;
    def equality(self):
        expr = self.comparison()
        while(self.match(types.BANG_EQUAL,types.EQUAL_EQUAL)):
            operator = self.previous();
            right = self.comparison();
            expr = Binary(expr, operator, right)

        return expr

    # comparison → addition ( ( ">" | ">=" | "<" | "<=" ) addition )* ;
    def comparison(self):
        expr = self.addition()
        while (self.match(types.GREATER, types.GREATER_EQUAL, types.LESS, types.LESS_EQUAL)):
            operator = self.previous();
            right = self.addition();
            expr = Binary(expr, operator, right)
        return expr

    def addition(self):
        expr = self.multiplication()
        while (self.match(types.MINUS, types.PLUS)):
            operator = self.previous();
            right = self.multiplication();
            expr = Binary(expr, operator, right)
        return expr

    def multiplication(self):
        expr = self.unary()
        while (self.match(types.SLASH, types.STAR)):
            operator = self.previous();
            right = self.unary();
            expr = Binary(expr, operator, right)
        return expr

    # unary → ( "!" | "-" ) unary| primary ;
    def unary(self):
        if self.match(types.BANG, types.MINUS):
            operator = self.previous();
            right = self.unary();
            return Unary(operator, right)
        return self.primary()

    def primary(self):
        if self.match(types.FALSE): return Literal(False)
        if self.match(types.TRUE): return Literal(True)
        if self.match(types.NULL): return Literal(None)

        if( self.match(types.NUMBER, types.STRING)):
            return Literal(self.previous().literal)

        if(self.match(types.LEFT_PAREN)):
            expr = self.expression()
            self.consume(types.RIGHT_PAREN, "Expected ')' after expression")
            return Grouping(expr)

        raise self.error(self.peek(), "Expected expression")

    # Helpers
    def match(self,*types):
        for type in types:
            if self.check(type):
                self.advance()
                return True

        return False

    def check(self,type):
        if self.isAtEnd(): return False
        return self.peek().tokenType == type

    def advance(self):
        if not self.isAtEnd(): self.current += 1
        return self.previous()

    def isAtEnd(self):
        return self.peek().tokenType == types.EOF

    def peek(self):
        return self.tokens[self.current]

    def previous(self):
        return self.tokens[self.current - 1]

    def consume(self, expected, message):
        if self.check(expected): return self.advance()
        raise self.error(self.peek(), message)

    def error(self, token, message):
        error(token, message)
        return ParseError()

    def synch(self):
        self.advance()
        while not self.isAtEnd():
            if self.previous().tokenType == types.SEMICOLON: return

            self.advance()

class ParseError(Exception):
    pass