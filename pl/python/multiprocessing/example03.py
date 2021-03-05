import multiprocessing
import time

def func(pid):
    print(f'Η διεργασία {pid} θα κοιμηθεί για 1 δευτερόλεπτο')
    time.sleep(1)
    print(f'Αφύπνιση διεργασίας {pid}')
def run():
    start = time.perf_counter()
    processes = []
    for i in range(10):
        p = multiprocessing.Process(target=func, args=[i])
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    finish = time.perf_counter()
    print(f'Τερματισμός μετά από {round(finish-start, 2)} δευτερόλεπτα')

if __name__ == '__main__':
    run()