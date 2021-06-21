import math
import random
import utils
from fuzzywuzzy import fuzz
from html import unescape
import requests
import re
import jieba
import paddlehub as hub


class Robot:
    def __init__(self):
        self.Q_A = utils.Get_Q_A()
        self.emotions = utils.Get_emtions()
        self.URL = 'https://www.duanwenxue.com/duanwen/xiaohua/'
        self.item = 0
        self.send = [self.start,self.chat,self.weather,self.joke,self.idiom]
        self.senta = hub.Module(name="senta_bilstm")
        with open('.\stop_words.txt', encoding='utf-8') as f:
            self.stop_words = f.readlines()
            self.stopword = set(word.strip('\n') for word in self.stop_words)
        with open('chengyu.txt', 'r', encoding='utf-8') as f:
            self.idioms = f.readlines()
        self.last = None
    def start(self,reply):
        if reply != '':
            self.item = int(reply)
        return ''

    def chat(self,reply):
        if reply != None:
            input_questions = ""
            for x in reply:
                if x not in self.stop_words:
                    input_questions += x
            dict = {}
            for key, value in self.Q_A.items():
                similarity = fuzz.ratio(input_questions, key)
                if similarity > 60:
                    dict[key] = similarity
            if not dict:
                print('糊弄')
                emotion = self.Get_em(reply)
                return utils.Get_EM_AN(emotion,self.emotions)
            target = max(dict,key=dict.get)
            return self.Q_A[target]

    def joke(self,reply):
        i = random.randint(1, 140)
        url = self.URL + 'list_' + str(i) + 'html'
        try:
            html = requests.get(url, timeout=30)
            content = html.text
        except:
            print("fail!")
        jokes = re.search("<a target=\"_blank\" href=\"/article/\d\d\d\d\d\d\d.html\">(.*?)</a>", content)
        return unescape(jokes.group(1))

    def weather(self,reply):
        print(reply)
        rep = requests.get(f'http://www.tianqiapi.com/api?version=v6&appid=78643371&appsecret=Cyw6AfRx&city={reply.rsplit()}')
        rep.encoding = 'utf-8'
        print(rep.url)
        print('城市：%s' % rep.json()['city'])
        print('天气：%s' % rep.json()['wea'])
        print('风向：%s' % rep.json()['win'])
        print('温度：%s' % rep.json()['tem'] + '°C')
        print('风力：%s' % rep.json()['win_speed'])
        print('湿度：%s' % rep.json()['humidity'])
        print('空气质量：%s' % rep.json()['air_level'])
        return '城市: '+rep.json()['city']+'\n'+'天气: '+rep.json()['wea']+'\n'+'风向: '+rep.json()['win']+'温度: '+rep.json()['tem']+'°C'+'\n'+'风力: '+rep.json()['win_speed']+'\n'+'湿度: '+rep.json()['humidity']+'\n'+'空气质量：'+rep.json()['air_level']

    def idiom(self,reply):
        #reply=reply.split()
        if self.last == None:
            self.last = self.find(reply[4])
            return self.last
        else:
            key = self.last[3]
            this = reply
            if this[1] == key:
                self.last = self.find(this[4])
                if self.last != None:
                    return self.last
                else :
                    return '呜呜呜，我输了'
            return '请重新输入'

    def find(self,key):
        for i in self.idioms:
            if i[0] == key:
                return i.strip()

    def Get_em(self,text):
        word_list = jieba.lcut(text, use_paddle=True)
        filtered_word = [word for word in word_list if word not in self.stopword]
        results = self.senta.sentiment_classify(texts=filtered_word, use_gpu=False, batch_size=1)
        scores = 0.0
        count = 0
        for result in results:
            score = result['positive_probs']
            scores += score
            count += 1
        s = scores / count
        return s



