# Λεκτικός αναλυτής για απλές αριθμητικές εκφράσεις

Αναγνωρίζει:
* Αναγνωριστικά IDENT
* Ακέραια κυριολεκτικά INT_LIT
* Παρενθέσεις
* Αριθμητικοί τελεστές


## Κώδικας

* [TokenTypes.py](./TokenTypes.py)
* [Token.py](./Token.py)
* [Lexer.py](./Lexer.py)
* [LexerTest1.py](./LexerTest1.py)
* [LexerTest2.py](./LexerTest2.py)


```
$ python LexerTest1.py
Tokenizing (sum + 47) / total
Next token: TokenTypes.LPAREN Next lexeme: (
Next token: TokenTypes.INT_LIT Next lexeme: sum
Next token: TokenTypes.ADD Next lexeme: +
Next token: TokenTypes.IDENT Next lexeme: 47
Next token: TokenTypes.RPAREN Next lexeme: )
Next token: TokenTypes.DIV Next lexeme: /
Next token: TokenTypes.INT_LIT Next lexeme: total
Next token: TokenTypes.EOF Next lexeme: EOF
```

```
$ python LexerTest2.py '2 * (x1 + 1) / (x2 - 17)'
Tokenizing 2 * (x1 + 1) / (x2 - 17)
Next token: TokenTypes.IDENT Next lexeme: 2
Next token: TokenTypes.MUL Next lexeme: *
Next token: TokenTypes.LPAREN Next lexeme: (
Next token: TokenTypes.INT_LIT Next lexeme: x1
Next token: TokenTypes.ADD Next lexeme: +
Next token: TokenTypes.IDENT Next lexeme: 1
Next token: TokenTypes.RPAREN Next lexeme: )
Next token: TokenTypes.DIV Next lexeme: /
Next token: TokenTypes.LPAREN Next lexeme: (
Next token: TokenTypes.INT_LIT Next lexeme: x2
Next token: TokenTypes.SUB Next lexeme: -
Next token: TokenTypes.IDENT Next lexeme: 17
Next token: TokenTypes.RPAREN Next lexeme: )
Next token: TokenTypes.EOF Next lexeme: EOF
```

