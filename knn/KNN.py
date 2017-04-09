# -*- coding: utf-8 -*-
"""
@author: xiaoz
@time: 2017/4/8 下午10:49
"""
from __future__ import unicode_literals
import numpy as np
import operator


def create_data_set():
    group = np.array([
        [1.0, 1.1],
        [1.0, 1.0],
        [0, 0],
        [0, 0.1]
    ])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify(in_x, group, labels, k):
    data_set_size = group.shape[0]
    diff_mat = np.tile(in_x, (data_set_size, 1)) - group
    sq_diff_mat = diff_mat ** 2
    sq_distances = sq_diff_mat.sum(axis=1)
    distances = sq_distances ** 0.5
    sorted_distances = distances.argsort()

    class_count = {}
    for i in range(k):
        vote_label = labels[sorted_distances[i]]
        class_count[vote_label] = class_count.get(vote_label, 0) + 1
    sorted_class_count = sorted(class_count.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sorted_class_count[0][0]


def figure(x, y):
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(x, y)
    plt.show()


if __name__ == '__main__':
    group, labels = create_data_set()
    figure(group[:, 0], group[:, 1])
