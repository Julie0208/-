# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 10:19:21 2021

@author: ASUS
"""

list_result = []
file = open('成语大全（31648个成语解释）.Txt', encoding="UTF-8")
for line in file.readlines():
    index = line.find('释义')
    if index > 0:
        list_result.append(line[0: index])
    else:
        list_result.append(line.replace("\n", ""))
file2 = open('成语大全（成语+拼音）', 'w', encoding="UTF-8")
for line in list_result:
    file2.write(line + "\n")
file.close()
file2.close()