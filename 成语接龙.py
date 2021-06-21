# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 11:02:53 2021

@author: 季雅琪
"""

#【成语接龙】
#可选择先后手、判断输入是否为成语

import random
a = input ('即将开始成语接龙，想先手请输入1，想后手请输入0。在你的回合输入“走了”退出游戏\n')
with open ('chengyu.txt','r',encoding='utf-8') as f:
    cy = f.readlines()
            
def find(key):
    for i in cy:
        if i[0] == key:
            return i.strip()
    
    
    
def idiom(last = None):
    if last == None:
        this = input('input :')
        last = find(this[-1])
        print(last)
    else:
        key = last[-1]
        while True:
            this = input('input :')
            if this == 'stop':
                return
            if this[0]==key:
                break
            print(this[0])
            print('Sorry u are wrong!')
        last = find(this[-1])
        print(last)
    idiom(last)
                
if a == '1':
    idiom()
elif a == '0':
    b = random.choice(cy)
    idiom(b)
else:
    print ('对不起，我不知道你想先手还是后手，我们下次再玩吧！')