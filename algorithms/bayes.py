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
    """
    计算训练集中侮辱性文档的概率, 以及每个类别下词汇的概率
    :param train_matrix: 文档矩阵
    :param train_category: 每篇文档类别标签构成的向量, e.g: [0, 0, 1, 0, 1, 1, 0, 1]
    :return:
    """
    num_train_docs = len(train_matrix)
    num_words_per_doc = len(train_matrix[0])
    prob_abusive = sum(train_category) / float(num_train_docs)

    p1_num = np.zeros(num_words_per_doc)
    p0_num = np.zeros(num_words_per_doc)
    p1_demon = 0.0
    p0_demon = 0.0
    for i in range(num_train_docs):
        if train_category[i] == 1:
            p1_num += train_matrix[i]
            p1_demon += sum(train_matrix[i])
        else:
            p0_num += train_matrix[i]
            p0_demon += sum(train_matrix[i])
    p1_vec = p1_num / p1_demon
    p0_vec = p0_num / p0_demon
    return p0_vec, p1_vec, prob_abusive


if __name__ == '__main__':
    a = np.zeros(5)
    a += [1, 1, 1, 1, 0]
    print a