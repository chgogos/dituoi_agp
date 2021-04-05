from Lexer import *
from TokenTypes import *


if __name__ == "__main__":
    input = "(sum + 47) / total"
    lexer = Lexer(input)
    print("Tokenizing ", end="")
    print(input)
    while True:
        t = lexer.lex()
        if t.get_token().value == TokenTypes.EOF.value:
            break