# συνάρτηση ως παράμετρος συνάρτησης


def square(x):
    return x * x


# custom map function
def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result


squares = my_map(square, [1, 2, 3, 4, 5])
print(squares)

# [1, 4, 9, 16, 25]