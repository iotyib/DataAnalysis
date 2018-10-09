#-*-coding:utf-8-*-
__author__ = 'yib'
__date__ = '18-10-9 下午8:34'

import numpy as np
import sys
from datetime import datetime
'''
def numpySum(n):
    a = np.arange(n)**2
    b = np.arange(n)**3
    c = a+b
    return c

size = 1000

start = datetime.now()
c = numpySum(size)
end = datetime.now() - start
print 'The last 2 elements of the num',c[-2:]
print 'PythonSum elapsed time in microseconds',end.microseconds

'''

'''
输出多维数组
'''
# m = np.array([np.arange(2),np.arange(2)])
# print m
# print np.empty((3, 6))
print np.array([[1,2],[3,4]])