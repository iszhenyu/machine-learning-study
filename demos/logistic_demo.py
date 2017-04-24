# -*- coding: utf-8 -*-
"""
@author: xiaoz
@time: 2017/4/24 下午5:47
"""
from __future__ import unicode_literals


def load_data_set(filename):
    data_mat = []
    label_mat = []
    with open(filename) as f:
        for line in f.readlines():
            line_arr = line.strip().split()
            data_mat.append([1.0, float(line_arr[0]), float(line_arr[1])])
            label_mat.append(int(line_arr[2]))
    return data_mat, label_mat


if __name__ == '__main__':
    pass