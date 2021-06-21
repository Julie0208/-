import random


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
    return emotions[key][random.randint(0,len(emotions[key])-1)]

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
