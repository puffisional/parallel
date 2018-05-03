# -*- coding: utf-8 -*-
from __future__ import print_function
import numpy as np
from random import randint

if __name__ == "__main__":
    resultMatrix = np.zeros((1024, 1024), dtype=np.float64)

    def calc():
        x, y, v = randint(0, 1024), randint(0, 1024), randint(0, 1024)
        return x,y,v

    print(calc())

