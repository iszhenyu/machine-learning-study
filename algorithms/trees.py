# -*- coding: utf-8 -*-
"""
@author: xiaoz
@time: 2017/4/13 下午11:35
"""
from __future__ import unicode_literals

from math import log


def cal_shannon_ent(data_set):
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

