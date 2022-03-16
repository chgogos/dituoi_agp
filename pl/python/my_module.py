def print_boxed_text(t):
    """Εκτυπώνει ένα κείμενο περικυκλωμένο από αστεράκια"""
    l = len(t)
    print("*" * (l + 2))
    print(f"*{t}*")
    print("*" * (l + 2))


def triangle(n):
    k = n - 1
    for i in range(0, n):
        for _ in range(0, k):
            print(end=" ")
        k = k - 1
        for _ in range(0, i + 1):
            print("* ", end="")
        print("\r")


if __name__ == "__main__":
    print_boxed_text("Hello")
    triangle(10)
