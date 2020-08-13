#!/usr/bin/env python3
""" Check how many vegetables are in the pantry """
# A Future acts as a placeholder for a result that's initially unknown,
# but will be available at some point in the future. It provides a mechanism
# to access the result of an asynchronous operation.
from concurrent.futures import ThreadPoolExecutor
import time


def how_many_vegetables():
    print('Olivia is counting vegetables...')
    time.sleep(3)
    return 42


if __name__ == '__main__':
    print('Barron asks Olivia how many vegetables are in the pantry.')
    with ThreadPoolExecutor() as pool:
        # the submit method returns a future object that has a result() method
        future = pool.submit(how_many_vegetables)
        print('Barron can do others things while he waits for the result...')
        print('Olivia responded with', future.result())
