# threading.Timer

import threading


def func(tid):
    print("ΜΠΟΥΜ!")

t = threading.Timer(5.0, function=func, args=(1,))
t.start()
x = input("Πατήστε το πλήκτρο 1 για να αποτρέψετε την εκκίνηση του νήματος: ")
if x == "1":
    t.cancel()
