# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 19:52:54 2018

@author: LS
"""
#读取网页中的表格数据
import pandas as pd
data =pd.read_html("http://www.ukcrimestats.com/National_Picture/")[0] #填写url
print(data)
data.to_csv('1.csv') #填写文件名