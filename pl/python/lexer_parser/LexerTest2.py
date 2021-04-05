import sys
from Lexer import *
from TokenTypes import *


if __name__ == "__main__":
    input = sys.argv[1]
    lexer = Lexer(input)
    print("Tokenizing ", end="")
    print(input)
    while True:
        t = lexer.lex()
        if t.get_token().value == TokenTypes.EOF.value:
            break