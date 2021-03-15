def outer_func():
    message = "Hi"

    def inner_function():
        print(message)  # free variable

    return inner_function


my_func = outer_func()
my_func()

# Hi