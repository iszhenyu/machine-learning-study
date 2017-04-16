# -*- coding: utf-8 -*-
"""
@author: xiaoz
@time: 2017/4/13 下午11:35
"""
from __future__ import unicode_literals

from math import log


def cal_shannon_entropy(data_set):
    """
    计算香农熵
    :param data_set:
    :return:
    """
    entity_size = len(data_set)
    label_count_map = {}
    for item in data_set:
        cur_label = item[-1]
        if cur_label not in label_count_map:
            label_count_map[cur_label] = 0
        label_count_map[cur_label] += 1
    result = 0.0
    for key, val in label_count_map.items():
        prob = float(val) / entity_size
        result -= prob * log(prob, 2)
    return result


def split_data_set(data_set, axis, value):
    """
    按照给定特征划分数据集
    :param data_set: 待划分数据集
    :param axis: 划分数据集的特征
    :param value: 需要返回的特征的值
    :return:
    """
    result = []
    for item in data_set:
        if item[axis] == value:
            reduced_vec = item[:axis]
            reduced_vec.extend(item[axis + 1:])
            result.append(reduced_vec)
    return result


def choose_best_feature_to_split(data_set):
    """
    选择最好的数据集划分方式
    :param data_set: 待划分数据集
    :return:
    """
    data_size = len(data_set)
    feature_size = len(data_set[0]) - 1
    base_entropy = cal_shannon_entropy(data_set)

    biggest_entropy_difference = 0.0
    best_feature = -1
    for i in range(feature_size):
        feature_list = [item[i] for item in data_set]
        feature_set = set(feature_list)
        tmp_entropy = 0.0
        for val in feature_set:
            sub_data_set = split_data_set(data_set, i, val)
            prob = len(sub_data_set) / float(data_size)
            tmp_entropy += prob * cal_shannon_entropy(sub_data_set)
        entropy_difference = base_entropy - tmp_entropy
        if entropy_difference > biggest_entropy_difference:
            biggest_entropy_difference = entropy_difference
            best_feature = i
    return best_feature