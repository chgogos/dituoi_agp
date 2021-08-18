# https://towardsdatascience.com/3-tools-to-track-and-visualize-the-execution-of-your-python-code-666a153e435e

import heartrate

heartrate.trace(browser=True)


def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


if __name__ == "__main__":
    num = 5
    print(f"The factorial of {num} is {factorial(num)}")
