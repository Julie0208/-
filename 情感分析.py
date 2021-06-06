# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 21:35:50 2021

@author: 季雅琪
"""

#四大模块：input、logic、storage、output

print ('你好，开始聊天吧！输入“退出”结束聊天。')
text = input ('真人：')

if text == '退出':
    print('机器人：很高兴和你聊天，下次见！')
else:
    #【分词】
    #考虑到机器分词的出错率，并为尽可能防止全模式下出现的断章取义问题影响情感分析及回答，通过enable_paddle优化
    import jieba
    word_list = jieba.lcut(text,use_paddle=True)
    
    #为更多地关注定义文本含义的词，自定义停用词集进行过滤
    #考虑到中文语境，停用词集改编自中文停用词表、哈工大停用词表、百度停用词表、四川大学机器智能实验室停用词库，链接：https://github.com/elephantnose/characters/blob/master/stop_words
    with open('stop_words.txt','r',encoding='utf-8') as f:
        txt = f.readlines()  
        stopword = set(word.strip('\n') for word in txt) 
        filtered_word = [word for word in word_list if word not in stopword]
    #print(filtered_word)
   
    #【情感分析】
    #调用paddlehub中senta情感分析模型，得出积极情感系数s
    import paddlehub as hub
    
    senta = hub.Module(name="senta_bilstm")
    results = senta.sentiment_classify(texts=filtered_word, use_gpu=False, batch_size=1)
    scores = 0.0
    count = 0
    for result in results:
        score = result['positive_probs']
        scores += score
        count += 1
    s = scores/count
    #print(s)
