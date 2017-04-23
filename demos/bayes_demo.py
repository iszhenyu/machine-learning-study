# -*- coding: utf-8 -*-
"""
@author: xiaoz
@time: 2017/4/18 下午7:31
"""
from __future__ import unicode_literals

from algorithms import bayes
import numpy as np
import math


def create_data():
    posting_list = [
        ['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
        ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
        ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
        ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
        ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
        ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']
    ]
    class_vec = [0, 1, 0, 1, 0, 1]
    return posting_list, class_vec


if __name__ == '__main__':
    post_list, class_list = create_data()
    vocab_list = bayes.create_vocab_list(post_list)
    train_mat = []
    for post in post_list:
        train_mat.append(bayes.a_set_of_words_2_vec(vocab_list, post))
    p0_v, p1_v, p_ab = bayes.train_nbo(np.array(train_mat), np.array(class_list))

    test_entry = ['love', 'my', 'dalmation']
    test_doc = np.array(bayes.a_set_of_words_2_vec(vocab_list, test_entry))
    print bayes.classify(test_doc, p0_v, p1_v, p_ab)

    test_entry = ['stupid', 'my', 'garbage']
    test_doc = np.array(bayes.a_set_of_words_2_vec(vocab_list, test_entry))
    print bayes.classify(test_doc, p0_v, p1_v, p_ab)

