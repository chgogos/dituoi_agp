import ply.lex as lex

reserved = {"with": "WITH", "if": "IF"}

tokens = [
    "NUMBER",
    "ID",
    "LBRACE",
    "RBRACE",
    "SEMI",
    "PLUS",
    "MINUS",
    "TIMES",
    "DIV",
] + list(reserved.values())

# τα αναγνωριστικά πρέπει να έχουν τη μορφή t_ΧΧΧΧΧ
t_LBRACE = r"\{"  # το value είναι { και το type είναι t_LBRACE
t_RBRACE = r"\}"
t_SEMI = r";"
t_WITH = r"[wW][iI][tT][hH]"
t_IF = r"[iI][fF]"
t_PLUS = r"\+"
t_MINUS = r"-"
t_TIMES = r"\*"
t_DIV = r"/"


def t_NUMBER(t):
    r"[-+]?[0-9]+(\.([0-9]+)?)?"
    t.value = float(t.value)
    t.type = "NUMBER"
    return t


def t_ID(t):
    r"[a-zA-Z][_a-zA-Z0-9]*"
    t.type = reserved.get(t.value.lower(), "ID")  # αν δεν το βρει, επιστρέφει ID
    return t


# Ignored characters
t_ignore = " \r\n\t"  # δεν είναι raw string
t_ignore_COMMENT = r"\#.*"


def t_error(t):
    print(f"Illegal character {t.value[0]}")
    t.lexer.skip(l)


lexer = lex.lex()
