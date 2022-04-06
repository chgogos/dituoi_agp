# Χρονομέτρηση κώδικα με διαφορετικούς τρόπους

# Leibniz’s formula:
# pi/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - ...
#  https://proofwiki.org/wiki/Leibniz's_Formula_for_Pi


# συνάρτηση υπολογισμού του π
def pi(n):
    pi = 0
    s = 1
    d = 1
    for i in range(n):
        pi += s / d
        s = -s
        d += 2
    return pi * 4


N = 1_000_000

##########################################
# 1ος τρόπος χρονομέτρησης

import time

start = time.time()
x = pi(N)
elapsed_time = time.time() - start
print(f"time: pi={x}, time={elapsed_time}")

##########################################
# 2ος τρόπος χρονομέτρησης

import time

start = time.perf_counter()
# Return the value (in fractional seconds) of a performance counter,
# i.e. a clock with the highest available resolution to measure a
# short duration. It does include time elapsed during sleep and is system-wide.
x = pi(N)
elapsed_time = time.perf_counter() - start
print(f"time.perf_counter: pi={x}, time={elapsed_time}")

##########################################
# 3ος τρόπος χρονομέτρησης

import time

start = time.process_time()
# Return the value (in fractional seconds) of the sum of the system
# and user CPU time of the current process. It does not include
# time elapsed during sleep.
x = pi(N)
elapsed_time = time.process_time() - start
print(f"time.process_time: pi={x}, time={elapsed_time}")

##########################################
# 4ος τρόπος χρονομέτρησης

import datetime

start = datetime.datetime.now()
x = pi(N)
elapsed_time = datetime.datetime.now() - start
print(f"datetime: pi={x}, time={elapsed_time}")


##########################################
# 5ος τρόπος χρονομέτρησης

import timeit

start = timeit.default_timer()
x = pi(N)
elapsed_time = timeit.default_timer() - start
print(f"timeit: pi={x}, time={elapsed_time}")
