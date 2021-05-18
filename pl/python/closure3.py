def outer_func(msg):
    message = msg

    def inner_function():
        print(message)  # free variable

    return inner_function


hi_func = outer_func("Hi")
hello_func = outer_func("hello")

hi_func()
hello_func()

# Hi
# hello
