# -*- coding: utf-8 -*-
"""
@author: xiaoz
@time: 2017/4/18 下午6:19
"""
from __future__ import unicode_literals
import numpy as np


def create_vocab_list(data_set):
    vocab_set = set([])
    for item in data_set:
        vocab_set = vocab_set | set(item)
    return list(vocab_set)


def words_2_vec(vocab_list, input_data):
    vec = [0] * len(vocab_list)
    for word in input_data:
        if word in vocab_list:
            vec[vocab_list.index(word)] = 1
        else:
            print 'the word: %s is not in Vocabulary' % word
    return vec


 def train_nbo(train_matrix, train_category):
     pass