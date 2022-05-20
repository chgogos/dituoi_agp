import random

c = 5


def fun1(x):
    global c
    y = 2 * x + c
    c += 1
    return y


def fun2(x):
    y = 2 * x + random.randint(1, 100)
    return y


x = 5
print("1η κλήση συνάρτησης", fun1(x))
x = 5
print("2η κλήση συνάρτησης", fun1(x))

# ----------

x = 5
print("1η κλήση συνάρτησης", fun2(x))
x = 5
print("2η κλήση συνάρτησης", fun2(x))
