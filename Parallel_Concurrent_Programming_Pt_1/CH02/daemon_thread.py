#!/usr/bin/env python3
""" Barron finishes cooking while Olivia cleans """

import threading
import time


def kitchen_cleaner():
    while True:
        print('Olivia cleaned the kitchen.')
        time.sleep(1)

# Threads that are performing background tasks, like garbage collection, can be detached from the main program by
# making them what's called a demon thread. A demon thread, which you may also hear pronounced as daemon, is a thread
# that will not prevent the program from exiting if it's still running. By default, new threads are usually spawned
# as non-demon or normal threads and you have to explicitly turn a thread into a demon or background thread.


if __name__ == '__main__':
    olivia = threading.Thread(target=kitchen_cleaner)
    # if below line is False, Olivia will be running forever
    # it is false by default. So non-daemon thread will prevent the program from ending
    olivia.daemon = True
    olivia.start()

    print('Barron is cooking...')
    time.sleep(0.6)
    print('Barron is cooking...')
    time.sleep(0.6)
    print('Barron is cooking...')
    time.sleep(0.6)
    print('Barron is done!')
