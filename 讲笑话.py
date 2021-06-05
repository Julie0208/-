#! -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 18:22:13 2021

@author: 季雅琪
"""

#【讲笑话】
#随机爬取网页不断更新的笑话

import random
import requests
import re
#为处理网页抓取内容的解码问题，使用unescape函数
from html import unescape

#据网页规律，生成随机某页笑话对应的url
u = 'https://www.duanwenxue.com/duanwen/xiaohua/'
i = random.randint(1,140)
url = u+'list_'+str(i)+'html'

#爬取网页笑话内容
try:
    html = requests.get(url, timeout=30)
    content = html.text
except:
    print("fail!")
joke = re.search("<a target=\"_blank\" href=\"/article/\d\d\d\d\d\d\d.html\">(.*?)</a>", content)

print(unescape(joke.group(1)))