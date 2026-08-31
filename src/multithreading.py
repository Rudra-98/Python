#Multithreading in Python allows you to run multiple threads (smaller units of a process) concurrently.
# It’s useful for tasks like I/O operations (network calls, file reading) where waiting time can be utilized efficiently.

import threading
import time


def print_numbers():
    # This function will run on a SEPARATE thread
    for i in range(5):
        time.sleep(2)   # simulate work/delay (I/O-bound style wait)
        print(i)        # prints 0,1,2,3,4 (each after a 2s gap)


def print_alphabets():
    # This function will also run on its OWN separate thread,
    # concurrently with print_numbers()
    for i in 'xyz':
        time.sleep(2)   # simulate work/delay
        print(i)        # prints x, y, z (each after a 2s gap)


# Create Thread objects.
# 'target' = the function this thread will execute when started.
# NOTE: creating a Thread object does NOT start it yet — just prepares it.
thread_1 = threading.Thread(target=print_numbers)
thread_2 = threading.Thread(target=print_alphabets)

t1 = time.time()  # record start time, to measure total elapsed time later

# .start() actually begins execution of the thread's target function
# in the background. Execution moves to the NEXT line immediately —
# it does NOT wait for thread_1 to finish before starting thread_2.
thread_1.start()
thread_2.start()

# At this point, BOTH threads are running concurrently:
# thread_1 printing numbers, thread_2 printing letters,
# interleaved roughly every 2 seconds since both sleep(2) at the same pace.

# .join() blocks the MAIN thread until the given thread finishes.
# We join thread_1 first, then thread_2 — but since both were already
# running in parallel, this doesn't serialize their execution,
# it just makes the main thread WAIT for both to complete
# before moving past this point.
thread_1.join()
thread_2.join()

# Because both threads ran concurrently (not sequentially),
# total time is ~10 seconds (5 iterations x 2s each) —
# NOT ~20 seconds (which is what you'd get running them one after another).
print(time.time() - t1)