# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from wordcloud import WordCloud
from redistest import RedisHelper

from dirty_words_filter import scan as dirty_scan

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

NAMESPACE = 'lagou-python::' #14
PARTITION = 'jobdetail-des::' #15
FONT_PATH = '../fonts/chinese.msyh.ttf'
IMAGE_PATH = '../image/wordcloud.png'

r = RedisHelper(name_space=NAMESPACE, partition=PARTITION)
key_words_items = r.scan()

# words = map(lambda s: s[29:], key_words.keys())
dirty_words = map(lambda d: d.split("::")[2].strip().decode('utf-8'), dirty_scan().keys())
cut_prefix = lambda s: s.split("::")[2].strip().decode('utf-8')
words_with_frequency = {cut_prefix(k): float(v) for k, v in key_words_items.iteritems() if cut_prefix(k) not in dirty_words}
wordcloud = WordCloud(width=1600, height=1000, relative_scaling=.8, font_path='cn_font.ttf', max_font_size=240).generate_from_frequencies(words_with_frequency)
wordcloud.to_file(IMAGE_PATH)

import matplotlib.pyplot as plt

plt.imshow(wordcloud)
plt.axis("off")
plt.show()