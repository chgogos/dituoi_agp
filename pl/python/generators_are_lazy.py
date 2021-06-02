def a_simple_generator():
    for i in [1,1,2,3,5,8,11,17]:
        yield i

gen = a_simple_generator()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))