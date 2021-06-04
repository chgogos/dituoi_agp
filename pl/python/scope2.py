# Sebesta page 223

g = 3

def sub1():
    a = 5
    b = 7
    print(f"checkpoint1:  g={g}, a={a}, b={b}")
    def sub2():
        global g
        c = 9
        print(f"checkpoint2:  g={g}, c={c}")
        def sub3():
            nonlocal c
            g = 11
            print(f"checkpoint3:  g={g}, c={c}")
        sub3()
    sub2()

sub1()

# checkpoint1:  g=3, a=5, b=7
# checkpoint2:  g=3, c=9
# checkpoint3:  g=11, c=9