import time

start = time.perf_counter()

def func():
    print('Sleep')
    time.sleep(1)
    print('Wake up')

func()
func()
finish = time.perf_counter()
print(f'Finished after {round(finish-start, 2)} seconds')