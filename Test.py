#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
import pandas as pd
from pandas import DataFrame, Series

csv_path = 'e:/Test_Data/2017_08_05-10_40_13.csv'

sales = pd.read_csv(csv_path, encoding='GBK', skiprows=9, skipfooter=1)
print sales.head()
class func(object):

    def __init__(self):
        pass

    def add(self):
        a = 6
        return a + 3


f = func()
print f.add()
