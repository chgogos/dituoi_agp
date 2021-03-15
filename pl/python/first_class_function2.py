# ανάθεση συνάρτησης σε μεταβλητή


def square(x):
    return x * x


f = square  # το f είναι ψευδώνυμο για τη συνάρτηση square
print(square)
print(f(5))  # κλήση της συνάρτησης square με παράμετρο 5


# <function square at 0x0000024357595160>
# 25