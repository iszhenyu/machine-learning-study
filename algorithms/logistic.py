# -*- coding: utf-8 -*-
"""
@author: xiaoz
@time: 2017/4/24 下午5:29
"""
from __future__ import unicode_literals
import numpy as np


def sigmoid(in_x):
    """
    sigmoid函数
    """
    return 1.0 / (1 + np.exp(-in_x))


def grad_ascent(data_mat_in, class_labels_in):
    """
    梯度上升算法
    """
    data_mat = np.mat(data_mat_in)
    label_mat = np.mat(class_labels_in).transpose()
    m, n = np.shape(data_mat)
    alpha = 0.001
    max_cycle = 500
    weights = np.ones((n, 1))
    for i in range(max_cycle):
        h = sigmoid(data_mat * weights)
        error = label_mat - h
        weights = weights + alpha * data_mat.transpose() * error
    return weights


