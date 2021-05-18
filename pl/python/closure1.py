def outer_func():
    message = "Hi"

    def inner_function():
        print(message)  # free variable

    return inner_function()


outer_func()

# Hi
