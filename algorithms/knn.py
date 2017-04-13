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
        [1.0, 1.2],
        [1.0, 1.0],
        [0.1, 0],
        [0.2, 0.1]
    ])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def auto_norm(data_set):
    """
    归一化特征值
    :param data_set:
    :return:
    """
    min_vals = data_set.min(0)
    max_vals = data_set.max(0)
    ranges = max_vals - min_vals
    data_size = data_set.shape[0]
    norm_data_set = data_set - np.tile(min_vals, (data_size, 1))
    norm_data_set = norm_data_set / np.tile(ranges, (data_size, 1))
    return norm_data_set


def classify(in_data, data_set, data_labels, k):
    norm_data_set = auto_norm(data_set)
    # 获取样本数据的数量
    data_set_size = norm_data_set.shape[0]
    # 对输入数据在列上复制data_set_size份
    in_data_matrix = np.tile(in_data, (data_set_size, 1))
    # 计算输入数据与样本数据的差值
    diff_mat = in_data_matrix - norm_data_set
    # 对矩阵的每个元素进行平方处理
    sq_diff_mat = diff_mat ** 2
    # 对矩阵的每行求和, 结果是一个数组
    sq_distances = sq_diff_mat.sum(axis=1)
    # 对数组每个元素开方处理
    distances = sq_distances ** 0.5
    # distances排序后每个元素在原数组中所处的位置下标
    sorted_distance_indexes = distances.argsort()

    # 统计排名前k
    classify_count = {}
    for i in range(k):
        vote_label = data_labels[sorted_distance_indexes[i]]
        classify_count[vote_label] = classify_count.get(vote_label, 0) + 1

    # 将分类按匹配次数从大到小排列
    sorted_class_count = sorted(classify_count.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sorted_class_count[0][0]


if __name__ == '__main__':
    group, labels = create_data_set()
    print classify([1.0, 0.2], group, labels, 3)