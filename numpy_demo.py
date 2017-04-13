# -*- coding: utf-8 -*-
"""
@author: xiaoz
@time: 2017/4/13 上午11:15
"""
from __future__ import unicode_literals
import numpy as np


def create_array():
    a = np.array([1, 2, 3, 4])
    b = np.array([5, 6, 7, 8])
    c = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]])
    print c
    print c.dtype

    print 'a.shape', a.shape
    print 'c.shape', c.shape

    print '------------------------------'

    # 改变每个轴的大小, 并不改变原数组元素位置
    c.shape = 4, 3
    print c

    print '------------------------------'

    c.shape = 2, -1
    print c

    print '------------------------------'

    # 创建一个改变了尺寸的新数组, 原数组shape不变, 但新旧两个数组共享数据存储内存区域, 改变其中任意一个数组元素都会同时修改另一个
    d = a.reshape((2, 2))
    print d
    print a

    a[1] = 100
    print d

    print '------------------------------'

    print np.array([1, 2, 3, 4], dtype=np.float)
    print np.array([1, 2, 3, 4], dtype=np.complex)

    print '------------------------------'

    print np.arange(0, 1, 0.1)

    print np.linspace(0, 1, 12)

    print np.logspace(0, 2, 20)


def set_get_element_from_array():
    a = np.arange(10)
    print a
    print a[5]
    print a[3:5]
    print a[:5]
    print a[:-1]
    print a[1:-1:2]
    print a[::-1]
    print a[5:1:-2]

    # Python的列表序列不同，通过下标范围获取的新的数组是原始数组的一个视图。它与原始数组共享同一块数据空间：
    b = a[3:7]
    print b
    b[0] = 100
    print a

    c = a[[3, 3, 1, 8]]  # 获取a中的下标为3, 3, 1, 8的4个元素，组成一个新的数组, 不共享内存
    print c
    c[0] = -10
    print c
    print a


def multi_dimension_array():
    a = np.arange(0, 60, 10)
    print a
    a = a.reshape(-1, 1)
    print a
    a = a + np.arange(0, 6)
    print a

    print a[(0, 1, 2, 3, 4), (1, 2, 3, 4, 5)]
    print a[3:, [0, 2, 5]]


def struct_array():
    persontype = np.dtype({
        'names': ['name', 'age', 'weight'],
        'formats': ['S32', 'i', 'f']})
    a = np.array([("Zhang", 32, 75.5), ("Wang", 24, 65.2)],
                 dtype=persontype)
    print a


if __name__ == '__main__':
    struct_array()