# -*- coding: utf-8 -*-
"""
@author: xiaoz
@time: 2017/4/13 下午5:52
"""
from __future__ import unicode_literals
import numpy as np
import os

from utils import matplot_utils


def file2matrix(filename):
    with open(filename) as f:
        lines = f.readlines()
        number_of_lines = len(lines)
        result_mat = np.zeros((number_of_lines, 3))
        classify_labels = []

        index = 0
        for line in lines:
            line = line.strip()
            line_items = line.split(' ')
            result_mat[index, :] = line_items[:3]
            classify_labels.append(int(line_items[-1]))
            index += 1

    return result_mat, classify_labels


if __name__ == '__main__':
    resources_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources')
    knn_file = os.path.join(resources_dir, 'knn.txt')
    data_set, data_labels = file2matrix(knn_file)
    matplot_utils.figure(data_set[:, 1], data_set[:, 2], data_labels)