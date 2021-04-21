# https://www.guru99.com/python-check-if-file-exists.html

import os.path
from os import path


def main():

    print("File exists:" + str(path.exists("./README.md")))
    print("File exists:" + str(path.isfile("./README.md")))
    print("Directory exists:" + str(path.isdir("./pl")))


if __name__ == "__main__":
    main()
