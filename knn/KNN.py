# -*- coding: utf-8 -*-
"""
@author: xiaoz
@time: 2017/4/8 下午10:49
"""
from numpy import *
import operator


def create_data_set():
    group = array([
        [1.0, 1.1],
        [1.0, 1.0],
        [0, 0],
        [0, 0.1]
    ])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


if __name__ == '__main__':
    group, labels = create_data_set()
    print group
    print labels