#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
import pandas as pd
from pandas import DataFrame, Series
import matplotlib
import matplotlib.pyplot as plt


csv_path = 'e:/Test_Data/salesdata(0301-0731).csv'
sales = pd.read_csv(csv_path, encoding='GBK', skiprows=6, skipfooter=0)

del sales[u'行号']
#sales.set_index(u'商品编号', inplace=True)
#sales.dtypes
#sales.head()

sales.columns = ['Date', 'ProdID', 'ProdSKU', 'ProdName', 'WareHouse', 'CustName', 'Staff', 'ReturnedNO', 'SalesNO', 'Price', 'TotalAmount']


cust_sales_jul = sales[(sales.Date >= '2017-7-1')].groupby('CustName').SalesNO.sum()
cust_sales_jul = cust_sales_jul[cust_sales_jul.values > cust_sales_jul.values.mean()]

#plt.plot(cust_sales_jul)
#plt.show()
cust_sales_jul = cust_sales_jul.value_counts(normalize=True)

matplotlib.pyplot.plot(cust_sales_jul)