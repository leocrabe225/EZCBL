import re
from enum import Enum

class TokenEnum(Enum):
    IF =          0
    ELSE =        1
    LBRACE =      2
    RBRACE =      3
    LPAREN =      4
    RPAREN =      5
    COMMA =       6
    EQUALS =      7
    STRING =      8
    IDENTIFIER =  9
    WHITESPACE =  10 
    NEWLINE =     11

class Token:
    def __init__(self, type:TokenEnum, value:str, line:int=0, col:int=0):
        self.type = type
        self.value = value
        self.line = line
        self.col = col

    def __repr__(self):
        return f"Token({self.type}, {self.value})"

TOKEN_PATTERNS = [
    (TokenEnum.IF,          r'\bif\b'),
    (TokenEnum.ELSE,        r'\bif\b'),
    (TokenEnum.LBRACE,      r'\{'),
    (TokenEnum.RBRACE,      r'\}'),
    (TokenEnum.LPAREN,      r'\('),
    (TokenEnum.RPAREN,      r'\)'),
    (TokenEnum.COMMA,       r','),
    (TokenEnum.EQUALS,      r'=='),
    (TokenEnum.STRING,      r'"[^"]*"'),
    (TokenEnum.IDENTIFIER,  r'[A-Z][A-Z0-9_-]*'),
    (TokenEnum.WHITESPACE,  r'[ \t]+'),
    (TokenEnum.NEWLINE,     r'\n'),
    ]

def tokenize(code:str) -> list[Token]:
    tokens:list[Token] = []
    pos = 0
    line = 1
    line_start = 0

    while pos < len(code):
        match_found = False

        for token_type, pattern in TOKEN_PATTERNS:
            regex = re.compile(pattern)
            match = regex.match(code, pos)

            if match:
                value = match.group()

                if token_type not in (TokenEnum.WHITESPACE, TokenEnum.NEWLINE):
                    col = pos - line_start
                    tokens.append(Token(token_type, value, line, col))
                
                if token_type == TokenEnum.WHITESPACE:
                    line += 1
                    line_start = match.end()
                
                pos = match.end()
                match_found = True
                break
        
        if not match_found:
            raise SyntaxError(f"Unexpected character at line {line}: {code[pos]}")

    return tokens

if __name__ == '__main__':
    test = '''if STATUS == "OK" {
    CUSTOMER_VALIDATE(A, B, C)
}'''
    
    tokens = tokenize(test)
    for token in tokens:
        print(token)