import time
CURSOR_UP = "\033[1A"
CLEAR = "\x1b[2K"

for i in range(10):
    print(i)
    time.sleep(1)
    print((CURSOR_UP + CLEAR)*2, end="")
print("finished")