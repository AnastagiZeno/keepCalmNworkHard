# -*- coding: utf-8 -*-
import requests
import json

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Connection':'Keep-Alive',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept':'*/*',
    'Cache-Control':'no-cache',
    'Host': 'www.lagou.com',
    'Origin': 'https://www.lagou.com',
    'Pragma':'no-cache',
    'Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'X-Anit-Forge-Code':'0',
    'X-Anit-Forge-Token':'None',
    'X-Requested-With':'XMLHttpRequest'
}


cookies_raw = '_ga=GA1.2.1702941217.1525426089; index_location_city=%E5%8C%97%E4%BA%AC; user_trace_token=20180504172842-88fbfd55-4f7d-11e8-806c-525400f775ce; LGUID=20180504172842-88fc0018-4f7d-11e8-806c-525400f775ce; _gid=GA1.2.1960632061.1525672171; PRE_UTM=; JSESSIONID=ABAAABAAAGFABEF59CEB0588E5C0E4DBF1C9C099F2175A0; LGSID=20180507140810-04ae239e-51bd-11e8-8ff4-525400f775ce; PRE_HOST=www.google.com.ph; PRE_SITE=https%3A%2F%2Fwww.google.com.ph%2F; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1525429597,1525672171,1525672339,1525673291; TG-TRACK-CODE=search_code; LGRID=20180507142454-5b290868-51bf-11e8-818f-5254005c3644; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1525674294; SEARCH_ID=a14a8d29fcf04343a3a212a9286a389b'

items = cookies_raw.split(';')
cookies = {}

for item in items:
    k, v = item.strip().split('=')
    cookies[k] = v


def execute():
    try:
        formdata = {
            'first': 'true',
            'pn': 1,
            'kd': u'python工程师'
        }
        url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city={0}&needAddtionalResult=false'.format('北京')
        page = requests.post(url=url, headers=headers, cookies=cookies, data=formdata)
        return page.content
    except Exception as e:
        print e


def jsformat(raw):
    if not isinstance(raw, dict):
        raw = json.loads(raw)
    return json.dumps(raw, sort_keys=True, indent=4, separators=(',', ':'))


if __name__ == '__main__':
    print jsformat(execute())