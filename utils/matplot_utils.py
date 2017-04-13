# -*- coding: utf-8 -*-
"""
@author: xiaoz
@time: 2017/4/13 下午7:41
"""
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as plt


def figure(x, y, labels=None):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    if not labels:
        ax.scatter(x, y)
    else:
        print labels
        l = 15 * np.array(labels)
        print l
        ax.scatter(x, y, l, l)
    plt.show()


if __name__ == '__main__':
    pass