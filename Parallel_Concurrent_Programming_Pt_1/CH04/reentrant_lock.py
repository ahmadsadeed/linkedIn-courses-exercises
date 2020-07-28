#!/usr/bin/env python3
""" Two shoppers adding garlic and potatoes to a shared notepad """

import threading

garlic_count = 0
potato_count = 0

# using re-entrant lock to prevent deadlock
lock = threading.RLock()


def add_garlic():
    global garlic_count
    lock.acquire()
    garlic_count += 1
    lock.release()


def add_potato():
    global potato_count
    lock.acquire()
    potato_count += 1
    add_garlic()
    lock.release()


def shopper():
    for i in range(10_000):
        add_garlic()
        add_potato()


if __name__ == '__main__':
    barron = threading.Thread(target=shopper)
    olivia = threading.Thread(target=shopper)
    barron.start()
    olivia.start()
    barron.join()
    olivia.join()
    print('We should buy', garlic_count, 'garlic.')
    print('We should buy', potato_count, 'potatoes.')
