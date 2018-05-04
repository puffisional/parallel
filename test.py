# -*- coding: utf-8 -*-
from __future__ import print_function
import numpy as np
from random import randint
from multiprocessing.pool import Pool
from multiprocessing.sharedctypes import Value, Array
from multiprocessing import Lock
from time import sleep
import ctypes as c


def init(vv):
    global v
    v = vv

def calc(input):
    global v
    x, y, e = randint(0, 1), randint(0, 1), randint(0, 2)
    # lock.acquire()
    v.get_lock().acquire()
    # with v.get_lock():
    v.value += 1
    v.get_lock().release()
    #resultMatrix[(2 * x + y)] += 1
    # lock.release()

if __name__ == "__main__":
    resultMatrix = Array(c.c_double, 2*2)
    v = Value('d', 0)
    lock = Lock()

    pool = Pool(initializer=init, initargs=(v,))
    pool.map(calc, range(1024*1024))

    arr = np.frombuffer(resultMatrix.get_obj())
    resultArr = np.frombuffer(resultMatrix.get_obj())
    print(v.value)

