'''
αμυντικός προγραμματισμός για επιτρεπτή είσοδο μόνο 0 ή 1 ή 2 ή 3
'''

while True:
    x = input("Δώσε τιμή ένα από τα 0,1,2,3: ")
    if x.isdigit():
        if 0 <= int(x) <= 3:
            break
    print("Λάθος τιμή")
