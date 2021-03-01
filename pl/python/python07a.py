# Better developers newsletter

import threading

mylist = [10, 20, 30] # shared by all threads


def add_one(x):
    mylist.append(x)

threads = []
for i in range(5):
    t = threading.Thread(target=add_one, args=(i,))
    threads.append(t)
    t.start()

for one_thread in threads:
    t.join()

print(mylist)