def foo(x):
    x += 1


a = 5
# μεταβίβαση κατά τιμή
foo(a)
print(a)

print("#" * 40)


def fun(x):
    x[0] = 99


a_list = [1, 2, 3, 4, 5]
fun(a_list)
print(a_list)

print("#" * 40)


class MyClass:
    def __init__(self, a):
        self.a = a


def bar(x):
    x.a += 1


obj = MyClass(5)
# μεταβίβαση κατά αναφορά
bar(obj)
print(obj.a)
