# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 17:33:02 2021

@author: 季雅琪
"""

#【查天气】
#调用API查询某城市实时天气

import requests
city = input('输入城市名称查询实时天气：')
rep = requests.get(f'http://www.tianqiapi.com/api?version=v6&appid=78643371&appsecret=Cyw6AfRx&city={city}')
rep.encoding = 'utf-8'
print('城市：%s' % rep.json()['city'])
print('天气：%s' % rep.json()['wea'])
print('风向：%s' % rep.json()['win'])
print('温度：%s' % rep.json()['tem'] + '°C')
print('风力：%s' % rep.json()['win_speed'])
print('湿度：%s' % rep.json()['humidity'])
print('空气质量：%s' % rep.json()['air_level'])