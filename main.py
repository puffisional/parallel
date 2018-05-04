# -*- coding: utf-8 -*-
from __future__ import print_function
import numpy as np
from random import randint
from multiprocessing.pool import Pool
from multiprocessing.sharedctypes import Value, Array
from multiprocessing import Lock
from time import sleep
import ctypes as c

def calc(input):
    randNum = randint(0, 1024)
    return randNum

if __name__ == "__main__":
    resultMatrix = Array(c.c_double, 2*2)

    pool = Pool()
    out = pool.map(calc, range(1024*1024*20))
    print(sum(out))
