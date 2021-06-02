import functools


def my_func4(a, b, c, d):
    return a + b + c + d


my_func3 = functools.partial(my_func4, 1)
my_func2 = functools.partial(my_func3, 2)
my_func1 = functools.partial(my_func2, 3)

print(my_func4(1, 2, 3, 4))
print(my_func3(2, 3, 4))
print(my_func2(3, 4))
print(my_func1(4))


# 10
# 10
# 10
# 10
