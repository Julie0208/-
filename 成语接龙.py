# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 11:02:53 2021

@author: 季雅琪
"""

#【成语接龙】
import random

s =input('请输入成语：')
#输入成语的最后一个字
ns = s[-1]

list = []
f = open ('chengyu.txt','r',encoding='utf-8')
cy = f.readlines()

try:
    for i in cy:
        #成语库中成语的第一个字
        ni = i[:1]
        if ni == ns:
            list.append(i)
    print (u'接龙:',random.choice(list))
except:
    print (u'接龙:是在下输了')
    
    
