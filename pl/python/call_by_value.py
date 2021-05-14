def foo(x):
    x += 1


a = 5
# κλήση με τιμή
foo(a)
print(a)


class MyClass:
    def __init__(self, a):
        self.a = a


def bar(x):
    x.a += 1


obj = MyClass(5)
# προσομοίωση κλήσης με αναφορά
bar(obj)
print(obj.a)
