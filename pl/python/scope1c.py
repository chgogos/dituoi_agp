day = "Monday"


def tester():
    global day
    print(f"The day is {day}")  # πρόσβαση στην global μεταβλητή day
    day = "Tuesday"
    print(f"The day is {day}")  # πρόσβαση στην global μεταβλητή day


tester()