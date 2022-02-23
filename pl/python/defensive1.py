"""
αμυντικός προγραμματισμός για είσοδο θετικού ακέραιου αριθμού
"""

while True:
    x = input("Δώσε ακέραιο αριθμό: ")
    # isdigit() returns True if the string is a digit string, False otherwise. 
    # A string is a digit string if all characters in the string are digits and 
    # there is at least one character in the string.
    if not x.isdigit():
        print("Λάθος είσοδος")
    else:
        if int(x) <= 0:
            print("Λάθος είσοδος")
        else:
            break

print(x)
