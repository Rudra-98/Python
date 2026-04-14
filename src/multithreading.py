#Multithreading in Python allows you to run multiple threads (smaller units of a process) concurrently.
# It’s useful for tasks like I/O operations (network calls, file reading) where waiting time can be utilized efficiently.

import threading
import time


def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(i)


def print_alphabets():
    for i in 'xyz':
        time.sleep(2)
        print(i)

#
#create thread for each function
thread_1 = threading.Thread(target=print_numbers)

thread_2 = threading.Thread(target=print_alphabets)


t1 = time.time()
thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()
print(time.time() - t1)
