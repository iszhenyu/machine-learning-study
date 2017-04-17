# -*- coding: utf-8 -*-
"""
@author: xiaoz
@time: 2017/4/17 下午10:52
"""
from __future__ import unicode_literals

from algorithms import trees


def create_data_set():
    data_set = [
        [1, 1, 'yes'],
        [1, 1, 'yes'],
        [1, 0, 'no'],
        [0, 1, 'no'],
        [0, 1, 'no']
    ]
    return data_set, ['no surfacing', 'flippers']


if __name__ == '__main__':
    data, labels = create_data_set()
    print trees.create_tree(data, labels)