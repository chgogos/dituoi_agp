day = "Monday"


def tester():
    print(f"The day is {day}")  # πρόσβαση στην global μεταβλητή day (UnboundLocalError: local variable 'day' referenced before assignment )
    day = "Tuesday"
    print(f"The day is {day}")  # πρόσβαση στην global μεταβλητή day


tester()