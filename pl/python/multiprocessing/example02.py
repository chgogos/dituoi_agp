import multiprocessing
import time

def func():
    print('Ύπνος')
    time.sleep(1)
    print('Αφύπνιση')

def run():
    start = time.perf_counter()
    p1 = multiprocessing.Process(target=func)
    p2 = multiprocessing.Process(target=func)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    finish = time.perf_counter()
    print(f'Τερματισμός μετά από {round(finish-start, 2)} δευτερόλεπτα')

if __name__ == '__main__':
    run()