# Better developers newsletter

import multiprocessing

mylist = [10, 20, 30]


def add_one(x):
    mylist.append(x)
    print("In add_one({0}), mylist is {1}".format(x, mylist))


processes = []
for i in range(5):
    p = multiprocessing.Process(target=add_one, args=(i,))
    processes.append(p)
    p.start()

for one_process in processes:
    p.join()

print(mylist)