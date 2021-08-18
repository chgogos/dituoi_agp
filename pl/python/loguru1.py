# https://towardsdatascience.com/3-tools-to-track-and-visualize-the-execution-of-your-python-code-666a153e435e

# exception occurs but for what inputs?

from itertools import combinations


def division(num1: int, num2: int):
    return num1 / num2


def divide_numbers(num_list: list):
    """Division of 2 numbers in the number list """

    for comb in combinations(num_list, 2):
        num1, num2 = comb
        res = division(num1, num2)
        print(f"{num1} divided by {num2} is equal to {res}.")


if __name__ == "__main__":
    num_list = [2, 1, 0]
    divide_numbers(num_list)
