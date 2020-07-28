#!/usr/bin/env python3
""" Several users reading a calendar, but only a few users updating it """

import threading
from readerwriterlock import rwlock

WEEKDAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
today = 0
lock = rwlock.RWLockFair()


def calendar_reader(id_number):
    global today
    # lock for reading
    read_lock = lock.gen_rlock()
    name = 'Reader-' + str(id_number)
    while today < len(WEEKDAYS) - 1:
        read_lock.acquire()
        print(name, 'sees that today is', WEEKDAYS[today], '-read count:', read_lock.c_rw_lock.v_read_count)
        read_lock.release()


def calendar_writer(id_number):
    global today
    # lock for writing
    write_lock = lock.gen_wlock()
    name = 'Writer-' + str(id_number)
    while today < len(WEEKDAYS) - 1:
        write_lock.acquire()
        today = (today + 1) % 7
        print(name, 'updated date to ', WEEKDAYS[today])
        write_lock.release()


if __name__ == '__main__':
    # create ten reader threads
    for i in range(10):
        threading.Thread(target=calendar_reader, args=(i,)).start()
    # ...but only two writer threads
    for i in range(2):
        threading.Thread(target=calendar_writer, args=(i,)).start()
