# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import MySQLdb as mdb
import requests
from MySQLdb import escape_string
import json
import time

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


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


cookies_raw = '_ga=GA1.2.1702941217.1525426089; ' \
              'index_location_city=%E5%8C%97%E4%BA%AC; ' \
              'user_trace_token=20180504172842-88fbfd55-4f7d-11e8-806c-525400f775ce; ' \
              'LGUID=20180504172842-88fc0018-4f7d-11e8-806c-525400f775ce; _gid=GA1.2.1960632061.1525672171; PRE_UTM=; ' \
              'JSESSIONID=ABAAABAAAGFABEF59CEB0588E5C0E4DBF1C9C099F2175A0; ' \
              'LGSID=20180507140810-04ae239e-51bd-11e8-8ff4-525400f775ce; PRE_HOST=www.google.com.ph; ' \
              'PRE_SITE=https%3A%2F%2Fwww.google.com.ph%2F; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; ' \
              'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1525429597,1525672171,1525672339,1525673291; ' \
              'TG-TRACK-CODE=search_code; LGRID=20180507142454-5b290868-51bf-11e8-818f-5254005c3644; ' \
              'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1525674294; SEARCH_ID=a14a8d29fcf04343a3a212a9286a389b'

items = cookies_raw.split(';')
cookies = {}

for item in items:
    k, v = item.strip().split('=')
    cookies[k] = v

print cookies


CONFIG = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': 'youneverguess',
    'db': 'lagou',
    'charset': 'utf8mb4'
}


def get_test_html():
    with open('../html/job_detail_template.html', 'r') as ht:
        html = ht.read()
    return html


def get_details_from_page(html):
    soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')

    jb_advantage = soup.find('dd', class_='job-advantage')
    jb_bt = soup.find('dd', class_='job_bt')
    jb_address_set = soup.find('dd', class_='job-address clearfix')
    jb_address = jb_address_set.find_all('input', attrs={'type': 'hidden'})

    if not (jb_advantage and jb_bt and jb_address_set and jb_address):
        return False

    jb_addr_longitude = jb_address[0]['value']
    jb_addr_latitude = jb_address[1]['value']
    jb_addr_text = jb_address[2]['value']
    jb_addr_region = jb_address[3]['value']

    base_info = {
        'jb_advantage': jb_advantage.text.strip()
        , 'jb_bt': jb_bt.text.strip()
        , 'jb_addr_longitude': jb_addr_longitude.strip()
        , 'jb_addr_latitude': jb_addr_latitude.strip()
        , 'jb_addr_text': jb_addr_text.strip()
        , 'jb_addr_region': jb_addr_region.strip()
    }


    jb_name = soup.find('div', class_='job-name')
    jb_request = soup.find('dd', class_='job_request')
    jb_labels = soup.find('ul', class_='position-label clearfix')

    try:
        jb_title_kw = soup.find('meta', attrs={'name': 'keywords'})['content']
        jb_title_des = soup.find('meta', attrs={'name': 'description'})['content']

        jb_department = jb_name.find('div', class_='company').text
        jb_pos = jb_name.find('span', class_='name').text

        jb_request_s = jb_request.p.find_all('span')

        jb_request_salary = jb_request_s[0].text.replace('/', '')
        jb_request_city = jb_request_s[1].text.replace('/', '')
        jb_request_expr = jb_request_s[2].text.replace('/', '')
        jb_request_edu = jb_request_s[3].text.replace('/', '')
        jb_request_fp = jb_request_s[4].text.replace('/', '')

        labels = jb_labels.find_all('li', class_='labels')
        labels_text = ";".join([lb.text for lb in labels])

        extra_info = {
            'jb_department': jb_department.strip()
            , 'jb_pos': jb_pos.strip()
            , 'jb_request_salary': jb_request_salary.strip()
            , 'jb_request_city': jb_request_city.strip()
            , 'jb_request_expr': jb_request_expr.strip()
            , 'jb_request_edu': jb_request_edu.strip()
            , 'jb_request_fp': jb_request_fp.strip()
            , 'labels_text': labels_text.strip()
            , 'jb_title_kw': jb_title_kw.strip()
            , 'jb_title_des': jb_title_des.strip()
        }

        base_info.update(extra_info)

    except Exception:
        pass
    return base_info


def get_position_ids(**condition):
    if condition:
        raise NotImplementedError
    sql = 'select id, positionId from Jobs where city = "北京";'
    return _get(sql)


def _get(sql):
    try:
        con = mdb.Connect(**CONFIG)
        cursor = con.cursor()
        cursor.execute(sql)

        result = [(int(item[0]), str(item[1])) for item in cursor.fetchall()]
        con.commit()
    except Exception as e:
        con.rollback()
        result = False
    finally:
        cursor.close()
        con.close()
    return result


def insert_sql_generate(data):
    sql = 'INSERT INTO JobDetail(' + \
          'job_id,' + \
          'positionName,' + \
          'education,' + \
          'salary,' + \
          'parttime,' + \
          'region,' + \
          'address,' + \
          'experienceYear,' + \
          'advantage,' + \
          'description,' + \
          'labels,' + \
          'title,' + \
          'keyword,' + \
          'latitude,' + \
          'longitude' + \
          ')VALUES(' + \
          '{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14});'.format(
              int(data.get('job_id')) if data.get('job_id') else "Null",
              '\"' + escape_string(data.get('jb_pos', 'Null')) + '\"',
              '\"' + escape_string(data.get('jb_request_edu', 'Null')) + '\"',
              '\"' + escape_string(data.get('jb_request_salary', 'Null')) + '\"',
              '\"' + escape_string(data.get('jb_request_fp', 'Null')) + '\"',
              '\"' + escape_string(data.get('jb_addr_region', 'Null')) + '\"',
              '\"' + escape_string(data.get('jb_addr_text', 'Null')) + '\"',
              '\"' + escape_string(data.get('jb_request_expr', 'Null')) + '\"',
              '\"' + escape_string(data.get('jb_advantage', 'Null')) + '\"',
              '\"' + escape_string(data.get('jb_bt', 'Null')) + '\"',
              '\"' + escape_string(data.get('labels_text', 'Null')) + '\"',
              '\"' + escape_string(data.get('jb_title_kw', 'Null')) + '\"',
              '\"' + escape_string(data.get('jb_title_des', 'Null')) + '\"',
              '\"' + escape_string(data.get('jb_addr_latitude', 'Null')) + '\"',
              '\"' + escape_string(data.get('jb_addr_longitude', 'Null')) + '\"'
          )
    return sql


def insert(sql):
    try:
        con = mdb.Connect(**CONFIG)
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
    except Exception as e:
        print e
        con.rollback()
    finally:
        cursor.close()
        con.close()


def main():
    pending_pages = get_position_ids()[100:]
    for idx, t in enumerate(pending_pages):
        try:
            time.sleep(1.5)
            _id = t[0]
            position_id = t[1]
            resp = requests.get('https://www.lagou.com/jobs/{0}.html'.format(position_id), cookies=cookies, headers=headers)
            base_info = get_details_from_page(resp.content)
            base_info.update({'job_id': _id})
            sql = insert_sql_generate(base_info)
            insert(sql)
            print sql
        except Exception as e:
            print e


if __name__ == '__main__':
    main()
