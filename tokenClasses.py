
class TokenTypes:
    # Single chars
    LEFT_PAREN = 0
    RIGHT_PAREN = 1
    LEFT_BRACE = 2
    RIGHT_BRACE = 3
    COMMA = 4
    DOT = 5
    MINUS = 6
    PLUS = 7
    SEMICOLON = 8
    SLASH = 9
    STAR = 10

    # One or two character tokens
    BANG = 11
    BANG_EQUAL = 12
    EQUAL = 13
    EQUAL_EQUAL = 14
    GREATER = 15
    GREATER_EQUAL = 16
    LESS = 17
    LESS_EQUAL = 18
    COLON = 27
    COLON_EQUAL = 28

    # Literals
    IDENTIFIER = 19
    STRING = 20
    NUMBER = 21

    # TODO: llenar con las de modula
    # KEYWORDS
    BEGIN = 22
    END = 23
    VAR = 24
    TRUE = 25
    FALSE = 26
    IF = 29
    ELSE = 30

    #EOF , la verdad no la necesitamos
    EOF = 40

    keywords = {
        'begin': BEGIN,
        "var": VAR,
        "end": END,
        "true":TRUE,
        "false": FALSE
    }