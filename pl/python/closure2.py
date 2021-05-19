def outer_func():
    message = "Hi"

    def inner_function():
        print(message)  # free variable

    return inner_function # αλλαγή σε σχέση με το closure1.py, επιστρέφει το όνομα της εμφωλευμένης συνάρτησης


my_func = outer_func()
my_func()

# Hi