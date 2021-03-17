from WAELexer import lexer


data = '{with {{x 5} {y 2}} {+ x y}};'

print("Tokenizing: ", data)
lexer.input(data)

# tokenize
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)


# OUTPUT

# Tokenizing:
# {with {{x 5} {y 2}} {+ x y}};

# LexToken(LBRACE,'{',1,1)
# LexToken(WITH,'with',1,2)
# LexToken(LBRACE,'{',1,7)
# LexToken(LBRACE,'{',1,8) --> 1 είναι ο αριθμός γραμμής και 8 είναι η θέση στη γραμμή
# LexToken(ID,'x',1,9)
# LexToken(NUMBER,5.0,1,11)
# LexToken(RBRACE,'}',1,12)
# LexToken(LBRACE,'{',1,14)
# LexToken(ID,'y',1,15)
# LexToken(NUMBER,2.0,1,17)
# LexToken(RBRACE,'}',1,18)
# LexToken(RBRACE,'}',1,19)
# LexToken(LBRACE,'{',1,21)
# LexToken(PLUS,'+',1,22)
# LexToken(ID,'x',1,24)
# LexToken(ID,'y',1,26)
# LexToken(RBRACE,'}',1,27)
# LexToken(RBRACE,'}',1,28)
# LexToken(SEMI,';',1,29)