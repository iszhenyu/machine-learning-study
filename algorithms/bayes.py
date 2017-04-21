# -*- coding: utf-8 -*-
"""
@author: xiaoz
@time: 2017/4/18 下午6:19
"""
from __future__ import unicode_literals
import numpy as np
import math


def create_vocab_list(data_set):
    """
    创建不重复词的词汇表
    :param data_set:
    :return:
    """
    vocab_set = set([])
    for item in data_set:
        vocab_set = vocab_set | set(item)
    return list(vocab_set)


def a_set_of_words_2_vec(vocab_list, input_data):
    """
    词集模型
    :param vocab_list:
    :param input_data:
    :return:
    """
    vec = [0] * len(vocab_list)
    for word in input_data:
        if word in vocab_list:
            vec[vocab_list.index(word)] = 1
        else:
            print 'the word: %s is not in Vocabulary' % word
    return vec


def a_big_of_words_2_vec(vocab_list, input_set):
    """
    词袋模型
    :param vocab_list:
    :param input_set:
    :return:
    """
    vec = [0] * len(vocab_list)
    for word in input_set:
        if word in vocab_list:
            vec[vocab_list.index(word)] += 1
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

    # 这里不用np.zeros 是因为p(w|c)可能为0, 相乘后分子会为0
    p1_num = np.ones(num_words_per_doc)
    p0_num = np.ones(num_words_per_doc)
    p1_demon = 2.0
    p0_demon = 2.0
    for i in range(num_train_docs):
        if train_category[i] == 1:
            p1_num += train_matrix[i]
            p1_demon += sum(train_matrix[i])
        else:
            p0_num += train_matrix[i]
            p0_demon += sum(train_matrix[i])
    # 通过求对数, 避免下溢或浮点数舍入导致的错误
    p1_vec = math.log(p1_num / p1_demon)
    p0_vec = math.log(p0_num / p0_demon)
    return p0_vec, p1_vec, prob_abusive


def classify(vec_2_classify, p0_vec, p1_vec, p_class_1):
    p1 = sum(vec_2_classify * p1_vec) + math.log(p_class_1)
    p0 = sum(vec_2_classify * p0_vec) + math.log(1.0 - p_class_1)
    return 1 if p1 > p0 else 0


if __name__ == '__main__':
    a = np.zeros(5)
    a += [1, 1, 1, 1, 0]
    print a