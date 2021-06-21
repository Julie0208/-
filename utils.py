# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 22:12:46 2021

@author: 陈存
"""

import random

#将情感匹配问答库内的回答分别分类到非常消极、消极、中性、积极、非常积极这五类中，输入字典。
def Get_emtions():
    emotions = {'非常消极：': [], "消极：": [], "中性：": [], "积极：": [], "非常积极：": []}
    now_key = '非常积极：'
    with open('.\情感匹配问答库.txt', encoding='utf-8', errors='ignore') as f:
        while True:
            line = f.readline().rstrip('\n')
            if line:
                if line != now_key and line in emotions.keys():
                    now_key = line
                else:
                    emotions[now_key].append(line)
            else:
                break
    return emotions

#获取情感分类对应的回答。
#将情感按积极情感系数分为5类，0-0.2为非常消极，0.2-0.4为消极，0.4-0.6为中性，0.6-0.8为积极，0.8-1为非常积极。
def Get_EM_AN(emtion,emotions):
    if(emtion<0.2):
        key='非常消极：'
    elif (emtion<0.4):
        key='消极：'
    elif (emtion<0.6):
        key='中性：'
    elif (emtion<0.8):
        key='积极：'
    else:
        key='非常积极：'
#随机抽取对应回答中的一个。
    return emotions[key][random.randint(0,len(emotions[key])-1)]

#逐行读入对应语料库，形成问答字典，问题与答案之间用英文逗号隔开。
def Get_Q_A():
    Q_A = {}
    with open('.\前置语料库.txt',encoding='utf-8',errors='ignore') as f:
        f.readline()
        while True:
            line=f.readline()
            if line:
                Qstr,Astr=line.split(',',1)
                Q_A[Qstr]=Astr
            else:
                break
    return Q_A
