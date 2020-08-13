#!/usr/bin/env python3
""" Chopping vegetables with a ThreadPool """

import threading
# running task asynchronously using this module for IO bound tasks
from concurrent.futures import ThreadPoolExecutor
# for cpu-bound tasks use ProcessPoolExecutor
from concurrent.futures import ProcessPoolExecutor


def vegetable_chopper(vegetable_id):
    name = threading.current_thread().getName()
    print(name, 'chopped vegetable', vegetable_id)


if __name__ == '__main__':
    # pool = ThreadPoolExecutor(max_workers=5)
    # for vegetable in range(100):
    #     pool.submit(vegetable_chopper, vegetable)
    # pool.shutdown()

    # using process pool, each process will have its own MainThread
    with ProcessPoolExecutor(max_workers=5) as pool2:
        for vege in range(100):
            pool2.submit(vegetable_chopper, vege)
