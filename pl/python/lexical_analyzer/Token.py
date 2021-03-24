class Token:
    def __init__(self, tok, value):
        self._t = tok
        self._c = value

    def __str__(self):
        if self._t.value == TokenTypes.IDENT.value:
            return f"<{self._t}:{self._c}>"
        elif self._t.value == TokenTypes.INT.value:
            return f"<INT:{self._c}>"
        else:
            return self._t

    def get_token(self):
        return self._t

    def get_value(self):
        return self._c