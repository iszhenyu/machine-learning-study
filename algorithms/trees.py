# -*- coding: utf-8 -*-
"""
@author: xiaoz
@time: 2017/4/13 下午11:35
"""
from __future__ import unicode_literals

from math import log

import operator


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


def majority_cnt(class_list):
    class_count = {}
    for vote in class_list:
        if vote not in class_count:
            class_count[vote] = 0
        class_count[vote] += 1
    sorted_class_count = sorted(class_count.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sorted_class_count[0][0]


def create_tree(data_set, labels):
    """
    创建树
    :param data_set:
    :param labels:
    :return:
    """
    class_list = [item[-1] for item in data_set]
    # 类别完全相同则停止继续划分
    if class_list.count(class_list[0]) == len(class_list):
        return class_list[0]
    # 遍历完所有特征, 类标签仍然不唯一, 返回出现次数最多的
    if len(data_set[0]) == 1:
        return majority_cnt(class_list)

    # 递归建树
    best_feature = choose_best_feature_to_split(data_set)
    best_label = labels[best_feature]
    tree = {best_label: {}}
    del labels[best_feature]
    feature_values = [item[best_feature] for item in data_set]
    unique_feature_values = set(feature_values)
    for val in unique_feature_values:
        sub_labels = labels[:]
        tree[best_label][val] = create_tree(split_data_set(data_set, best_feature, val), sub_labels)
    return tree


def classify(input_tree, labels, test_vec):
    """
    使用决策树分类
    :param input_tree:
    :param labels:
    :param test_vec:
    :return:
    """
    first_str = input_tree.keys()[0]
    second_dict = input_tree[first_str]
    feature_index = labels.index(first_str)
    for key in second_dict.keys():
        if test_vec[feature_index] == key:
            if type(second_dict[key]).__name__ == 'dict':
                class_label = classify(second_dict[key], labels, test_vec)
            else:
                class_label = second_dict[key]
    return class_label


def store_tree(input_tree, filename):
    import pickle
    fw = open(filename, 'w')
    pickle.dump(input_tree, fw)
    fw.close()


def grab_tree(filename):
    import pickle
    fr = open(filename)
    return pickle.load(fr)

