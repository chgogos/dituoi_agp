# Δημιουργία "άπειρης" ακολουθίας Fibonacci με generator
def a_simple_generator():
    a = b = 1
    yield a
    yield b
    while True:
        yield a + b
        b += a
        a = b - a


gen = a_simple_generator()

for _ in range(20):
    print(next(gen))

# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55
# 89
# 144
# 233
# 377
# 610
# 987
# 1597
# 2584
# 4181
# 6765
