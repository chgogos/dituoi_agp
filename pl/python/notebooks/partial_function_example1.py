import functools
from operator import add

add5 = functools.partial(add, 5)

print(add5(15))


# 20
