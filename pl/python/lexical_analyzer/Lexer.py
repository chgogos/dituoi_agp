import sys
from TokenTypes import TokenTypes
from Token import Token


class Lexer:
    """
    Λεκτικός αναλυτής για αριθμητικές εκφράσεις με ονόματα μεταβλητών
    και ακέραια θετικά κυριολεκτικά π.χ. (sum + 47) / total
    """

    def __init__(self, s):
        self._index = 0
        self._tokens = self.tokenize(s)

    def tokenize(self, s):
        result = []
        i = 0
        while i < len(s):
            c = s[i]
            if c in " \r\n\t":
                i += 1
                continue
            if c == "(":
                result.append(Token(TokenTypes.LPAREN, "("))
                i += 1
            elif c == ")":
                result.append(Token(TokenTypes.RPAREN, ")"))
                i += 1
            elif c == "+":
                result.append(Token(TokenTypes.ADD, "+"))
                i += 1
            elif c == "-":
                result.append(Token(TokenTypes.SUB, "-"))
                i += 1
            elif c == "*":
                result.append(Token(TokenTypes.MUL, "*"))
                i += 1
            elif c == "/":
                result.append(Token(TokenTypes.DIV, "/"))
                i += 1
            elif c.isdigit():
                j = i
                while j < len(s) and s[j].isdigit():
                    j += 1
                result.append(Token(TokenTypes.IDENT, s[i:j]))
                i = j
            elif c.isalpha():
                j = i
                while j < len(s) and s[j].isalnum():
                    j += 1
                result.append(Token(TokenTypes.INT_LIT, s[i:j]))
                i = j
            else:
                print(f"UNEXPECTED CHARACTER ENCOUNTERED: {c}")
                sys.exit(-1)
        result.append(Token(TokenTypes.EOF, "EOF"))
        return result

    def lex(self):
        t = None
        if self._index < len(self._tokens):
            t = self._tokens[self._index]
            self._index += 1
        print(f"Next token: {str(t.get_token())} Next lexeme: {t.get_value()}")
        return t
