def outer_fun():
    a = 1
    print(f"αρχή συνάρτησης outer_fun, a={a}")
    def inner_fun(x):
        print(f"κλήση ένθετης συνάρτησης inner_fun, x={x}, a={a}")

    inner_fun(2)
    inner_fun(4)
    print(f"τέλος συνάρτησης outer_fun, a={a}")

outer_fun()