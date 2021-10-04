g = 3

def sub1():
    a = 5
    b = 7
    print(f"checkpoint1: g={g}, a={a}, b={b}")
    def sub2():
        global g
        nonlocal a
        g = 9
        a = 9
        b = 9
        print(f"checkpoint2: g={g}, a={a}, b={b}")
    sub2()
    print(f"checkpoint3: g={g}, a={a}, b={b}")

sub1()
print(f"checkpoint4: g={g}")

# checkpoint1: g=3, a=5, b=7
# checkpoint2: g=9, a=9, b=9
# checkpoint3: g=9, a=9, b=7
# checkpoint4: g=9