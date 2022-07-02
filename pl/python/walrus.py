def without_walrus():
    print("Trying classic")
    while True:
        s = input("Enter a value (enter to stop):")
        if not s:
            break
        print(f"You entered {s}")


def with_walrus():
    print("Trying walrus a.k.a assignment expression operator (>= python3.8)")
    while s := input("Enter a value (enter to stop):"):
        print(f"You entered {s}")


without_walrus()
with_walrus()
