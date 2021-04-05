# Λεκτικός αναλυτής (lexer) και συντακτικός αναλυτής (parser) για απλές αριθμητικές εκφράσεις

Αναγνωρίζει:
* Αναγνωριστικά IDENT
* Ακέραια κυριολεκτικά INT_LIT
* Παρενθέσεις LPAREN, RPAREN
* Αριθμητικοί τελεστές ADD SUB MUL DIV


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
Next token: TokenTypes.IDENT Next lexeme: sum  
Next token: TokenTypes.ADD Next lexeme: +      
Next token: TokenTypes.INT_LIT Next lexeme: 47 
Next token: TokenTypes.RPAREN Next lexeme: )   
Next token: TokenTypes.DIV Next lexeme: /      
Next token: TokenTypes.IDENT Next lexeme: total
Next token: TokenTypes.EOF Next lexeme: EOF
```

```
$ python LexerTest2.py '2 * (x1 + 1) / (x2 - 17)'
Tokenizing 2 * (x1 + 1) / (x2 - 17)
Next token: TokenTypes.INT_LIT Next lexeme: 2
Next token: TokenTypes.MUL Next lexeme: *
Next token: TokenTypes.LPAREN Next lexeme: (
Next token: TokenTypes.IDENT Next lexeme: x1
Next token: TokenTypes.ADD Next lexeme: +
Next token: TokenTypes.INT_LIT Next lexeme: 1
Next token: TokenTypes.RPAREN Next lexeme: )
Next token: TokenTypes.DIV Next lexeme: /
Next token: TokenTypes.LPAREN Next lexeme: (
Next token: TokenTypes.IDENT Next lexeme: x2
Next token: TokenTypes.SUB Next lexeme: -
Next token: TokenTypes.INT_LIT Next lexeme: 17
Next token: TokenTypes.RPAREN Next lexeme: )
Next token: TokenTypes.EOF Next lexeme: EOF
```

## Parser

* [Parser.py](./Parser.py)

```
$ python Parser.py '2 * (x1 + 1) / (x2 - 17)'
Next token: TokenTypes.INT_LIT Next lexeme: 2
Enter <expr>
Enter <term>
Enter <factor>
Next token: TokenTypes.MUL Next lexeme: *
Exit <factor>
Next token: TokenTypes.LPAREN Next lexeme: (
Enter <factor>
Next token: TokenTypes.IDENT Next lexeme: x1
Enter <expr>
Enter <term>
Enter <factor>
Next token: TokenTypes.ADD Next lexeme: +
Exit <factor>
Exit <term>
Next token: TokenTypes.INT_LIT Next lexeme: 1
Enter <term>
Enter <factor>
Next token: TokenTypes.RPAREN Next lexeme: )
Exit <factor>
Exit <term>
Exit <expr>
Next token: TokenTypes.DIV Next lexeme: /
Exit <factor>
Next token: TokenTypes.LPAREN Next lexeme: (
Enter <factor>
Next token: TokenTypes.IDENT Next lexeme: x2
Enter <expr>
Enter <term>
Enter <factor>
Next token: TokenTypes.SUB Next lexeme: -
Exit <factor>
Exit <term>
Next token: TokenTypes.INT_LIT Next lexeme: 17
Enter <term>
Enter <factor>
Next token: TokenTypes.RPAREN Next lexeme: )
Exit <factor>
Exit <term>
Exit <expr>
Next token: TokenTypes.EOF Next lexeme: EOF
Exit <factor>
Exit <term>
Exit <expr>
PARSE SUCCESS
```