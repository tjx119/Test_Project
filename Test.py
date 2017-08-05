# -*- coding: UTF-8 -*-
import pandas as pd
from pandas import DataFrame, Series

csv_path = 'e:/Test_Data/2017_08_05-10_40_13.csv'

sales = pd.read_csv(csv_path, encoding='GBK', skiprows=9)
print sales.head()
print '的骄傲ID静安寺'
