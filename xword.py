#coding:utf-8
import io
import sys
import random
import os
from wordcloud import WordCloud,ImageColorGenerator
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

import numpy as np
from PIL import Image

path = os.path.dirname(__file__)
images = np.array(Image.open(path.join("5.png")))

arr = [u'温柔',u'知性',u'大猪蹄子',u'傻大袍子',u'地主家的傻儿子',u'钢铁直男',
u'智商250',u'乐天派',u'纯情',u'集美貌与才华于一身',u'人见人爱',u'花见花开',
u'沉鱼落雁',u'闭月羞花',u'纯洁的白纸',u'有很强的狗屎运',u'团队活宝',u'花痴',
u'小妖精',u'蒜你狠',u'猥琐大叔',u'小萝莉',u'御姐范',u'犀利哥',
u'蜘蛛侠',u'老铁，没毛病',u'老司机',u'尴聊1号',u'搞笑达人',u'圈粉范儿',
u'为你打call',u'嘻哈达人',u'歌唱家',u'演说家',u'土豪',u'穷到吃土',
u'温柔',u'知性',u'大猪蹄子',u'诶呀呀呀',u'下一届微信群群主',u'下一个宋小宝',
u'哈哈哈哈',u'嘻嘻嘻',u'555',u'333',u'22',u'11',u'打不死的小强']
# arr = ['a','b','ac','ad','ae','ar','ag','ad','a',]
fre = {}
for i in range(len(arr)):

	key = random.randint(0,len(arr)-1)
	data = arr[key]
	fre[data] = random.uniform(1,7)
	#fre.update('1'=random.randint(1,8))

wordcloud = WordCloud(background_color='#E1FFFF',font_path = "simhei.ttf",mask=images).generate_from_frequencies(fre)
from scipy.misc import imread
import matplotlib.pyplot as plt
bimg=imread('5.png')
bimgColors=ImageColorGenerator(bimg)
wordcloud.recolor(color_func=bimgColors)
fig2 = plt.figure(num='fig2',figsize=(3,6),dpi=75,facecolor='#FFFFFF',edgecolor='#FF0000')
plt.imshow(wordcloud.recolor(color_func=bimgColors))
plt.axis("off")
plt.savefig("word.jpg")
plt.show()




#词汇放入库中








