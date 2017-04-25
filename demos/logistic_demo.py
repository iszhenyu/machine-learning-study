# -*- coding: utf-8 -*-
"""
@author: xiaoz
@time: 2017/4/24 下午5:47
"""
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as plt



def load_data_set(filename):
    data_mat = []
    label_mat = []
    with open(filename) as f:
        for line in f.readlines():
            line_arr = line.strip().split()
            data_mat.append([1.0, float(line_arr[0]), float(line_arr[1])])
            label_mat.append(int(line_arr[2]))
    return data_mat, label_mat


def plot_best_fit(wei, filename):
    weights = wei.get_weights()
    data_mat, label_mat = load_data_set(filename)
    data_arr = np.array(data_mat)
    doc_size = np.shape(data_arr)[0]
    x1_records = []
    y1_records = []
    x2_records = []
    y2_records = []
    for i in range(doc_size):
        if int(label_mat[i]) == 1:
            x1_records.append(data_arr[i, 1])
            y1_records.append(data_arr[i, 2])
        else:
            x2_records.append(data_arr[i, 1])
            y2_records.append(data_arr[i, 2])

    figure = plt.figure()
    ax = figure.add_subplot(111)
    ax.scatter(x1_records, y1_records, s=30, c='red', marker='s')
    ax.scatter(x2_records, y2_records, s=30, c='green')
    x = np.arange(-3.0, 3.0, 0.1)
    y = (-weights[0]-weights[1] * x) / weights[2]
    ax.plot(x, y)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()


if __name__ == '__main__':
    pass