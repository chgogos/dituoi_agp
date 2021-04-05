import sys
from Lexer import *

next_token = None
l = None


def main():
    global next_token
    global l
    l = Lexer(sys.argv[1])
    # l = Lexer("(sum + 20)/30")
    next_token = l.lex()
    expr()
    if next_token.get_token().value == TokenTypes.EOF.value:
        print("PARSE SUCCESS")
    else:
        print("PARSE FAIL")


# <expr> : <term> {(+|-) <term>}
def expr():
    global next_token
    global l
    print("Enter <expr>")
    term()
    while (
        next_token.get_token().value == TokenTypes.ADD.value
        or next_token.get_token().value == TokenTypes.SUB.value
    ):
        next_token = l.lex()
        term()
    print("Exit <expr>")


# <term> : <factor> {(*|/) <factor>}
def term():
    global next_token
    global l
    print("Enter <term>")
    factor()
    while (
        next_token.get_token().value == TokenTypes.MUL.value
        or next_token.get_token().value == TokenTypes.DIV.value
    ):
        next_token = l.lex()
        factor()
    print("Exit <term>")


# <factor> : IDENT | INT_LIT | (<expr>)
def factor():
    global next_token
    global l
    print("Enter <factor>")
    if next_token.get_token().value == TokenTypes.IDENT.value:
        next_token = l.lex()
    elif next_token.get_token().value == TokenTypes.INT_LIT.value:
        next_token = l.lex()
    else:
        if next_token.get_token().value == TokenTypes.LPAREN.value:
            next_token = l.lex()
            expr()
            if next_token.get_token().value == TokenTypes.RPAREN.value:
                next_token = l.lex()
            else:
                error("Expecting RPAREN")
                sys.exit(-1)
        else:
            error("Expecting LPAREN")
            sys.exit(-1)
    print("Exit <factor>")


def error(s):
    print(f"SYNTAX ERROR {s}")


if __name__ == "__main__":
    main()