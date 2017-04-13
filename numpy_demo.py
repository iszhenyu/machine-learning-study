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
    print a.dtype


def triangle_wave(x, c, c0, hc):
    x = x - int(x)  # 三角波的周期为1，因此只取x坐标的小数部分进行计算
    if x >= c:
        r = 0.0
    elif x < c0:
        r = x / c0 * hc
    else:
        r = (c - x) / (c - c0) * hc
    return r


def triangle_func(c, c0, hc):
    def trifunc(x):
        x = x - int(x) # 三角波的周期为1，因此只取x坐标的小数部分进行计算
        if x >= c: r = 0.0
        elif x < c0: r = x / c0 * hc
        else: r = (c-x) / (c-c0) * hc
        return r

    # 用trifunc函数创建一个ufunc函数，可以直接对数组进行计算, 不过通过此函数
    # 计算得到的是一个Object数组，需要进行类型转换
    return np.frompyfunc(trifunc, 1, 1)


def ufunc_demo():
    # x = np.linspace(0, 2*np.pi, 10)
    # print x
    # y = np.sin(x)
    # print y
    #
    # a = np.arange(0, 4)
    # b = np.arange(1, 5)
    # print np.add(a, b)
    # print a + b

    x = np.linspace(0, 2, 1000)
    # print x
    # y = np.array([triangle_wave(t, 0.6, 0.4, 1.0) for t in x])
    # print y

    # triangle_ufunc = np.frompyfunc(lambda v: triangle_wave(v, 0.6, 0.4, 1.0), 1, 1)
    # y2 = triangle_ufunc(x)
    # print y2

    y2 = triangle_func(0.6, 0.4, 1.0)(x)
    print y2


def matrix_demo():
    a = np.matrix([[1, 2, 3], [5, 5, 6], [7, 9, 9]])
    print a
    a = a * a ** -1
    print a


if __name__ == '__main__':
    matrix_demo()