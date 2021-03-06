import concurrent.futures
import time

def func(pid, seconds):
    print(f"Η διεργασία {pid} θα κοιμηθεί για {seconds} δευτερόλεπτα")
    time.sleep(seconds)
    print(f"Αφύπνιση διεργασίας {pid}")
    return pid

def run():
    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = executor.map(func, range(5), secs)
    
    for result in results:     
        print(f'Αποτέλεσμα={result}')

    finish = time.perf_counter()
    print(f"Τερματισμός μετά από {round(finish-start, 2)} δευτερόλεπτα")

if __name__ == "__main__":
    run()