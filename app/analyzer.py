# -*- coding: utf-8 -*-

# import thulac
import jieba
from redistest import RedisHelper
from job_detail_get import get_job_details
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

NAMESPACE = 'lagou-python::'
PARTITION = 'jobdetail-des::'
CJK_UNICODE_ENCODING_INTERVAL = [19968, 40895]
LATIN_UNICODE_ENCODING_INTERVAL = [65, 122]

# def thu():
#     thu1 = thulac.thulac(seg_only=True)
#     text = thu1.cut(des, text=True)
#     return text



# def jb(text):
#     seg_list = jieba.cut_for_search(des)
#     return [s for s in seg_list]


def word_meaningful(word):
    if not isinstance(word, basestring):
        return False
    if CJK_UNICODE_ENCODING_INTERVAL[0] <= ord(word[0]) <= CJK_UNICODE_ENCODING_INTERVAL[1] \
            and CJK_UNICODE_ENCODING_INTERVAL[0] <= ord(word[-1]) <= CJK_UNICODE_ENCODING_INTERVAL[1]:
        return word
    if LATIN_UNICODE_ENCODING_INTERVAL[0] <= ord(word[0]) <= LATIN_UNICODE_ENCODING_INTERVAL[1] \
            and LATIN_UNICODE_ENCODING_INTERVAL[0] <= ord(word[-1]) <= LATIN_UNICODE_ENCODING_INTERVAL[1]:
        return word.lower().capitalize()
    return False



def segments_get(text):
    seg_list = jieba.cut_for_search(text)
    for segment in seg_list:
        word = word_meaningful(segment)
        if word:
            yield word


def vote_to_redis(seg_list):
    r = RedisHelper(name_space=NAMESPACE, partition=PARTITION)
    for segment in seg_list:
        r.vote(segment)


def scan(name_space=NAMESPACE, partition=PARTITION):
    r = RedisHelper(name_space=name_space, partition=partition)
    res = r.scan()
    for k, v in res.iteritems():
        print k, ' -> ', v
    return res


def run(text):
    sgs = segments_get(text)
    vote_to_redis(sgs)
    print time.time()


def main():
    details_list = get_job_details()
    for detail in details_list:
        run(detail)
    scan()


if __name__ == '__main__':
    main()
