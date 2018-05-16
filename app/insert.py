# -*- coding: utf-8 -*-

import MySQLdb as mdb
from MySQLdb import escape_string
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

CONFIG = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': 'youneverguess',
    'db': 'lagou',
    'charset': 'utf8mb4'
}


def execute(raw):
    try:
        items = raw['positionResult']['result']
        batch_sql = sql_batch(items)
        insert(batch_sql)
    except Exception as e:
        print e

    try:
        items = raw['positionResult']['result']
        single_sql = sql_single(items[0])
        insert(single_sql)
    except Exception as e:
        print e


def sql_batch(items):
    pre = 'INSERT INTO Jobs(' + \
          'businessZones,' + \
          'city,' + \
          'companyFullName,' + \
          'companyId,' + \
          'companyLabelList,' + \
          'companyShortName,' + \
          'companySize,' + \
          'createTime,' + \
          'district,' + \
          'education,' + \
          'explains,' + \
          'financeStage,' + \
          'firstType,' + \
          'secondType,' + \
          'formatCreateTime,' + \
          'gradeDescription,' + \
          'industryField,' + \
          'industryLables,' + \
          'jobNature,' + \
          'lastLogin,' + \
          'latitude,' + \
          'longitude,' + \
          'linestaion,' + \
          'stationname,' + \
          'subwayline,' + \
          'positionAdvantage,' + \
          'positionId,' + \
          'positionLables,' + \
          'positionName,' + \
          'publisherId,' + \
          'resumeProcessDay,' + \
          'resumeProcessRate,' + \
          'salary,' + \
          'score,' + \
          'workYear' + \
          ')VALUES'

    pos = ';'
    content = ''
    for data in items:
        content += '({0},{1},{2},{3},{4},{5},{6},STR_TO_DATE({7}, "%Y-%m-%d"),{8},{9},{10},{11},{12},{13},{14},{15},{16},{17},{18},' \
                   '{19},{20},{21},{22},{23},{24},{25},{26},{27},{28},{29},{30},{31},{32},{33},{34}),'.format(
            '\"' + escape_string("".join(data['businessZones'])) + '\"' if data['businessZones'] else "Null",
            '\"' + escape_string(data['city']) + '\"' if data['city'] else "Null",
            '\"' + escape_string(data['companyFullName']) + '\"' if data['companyFullName'] else "Null",
            int(data['companyId']),
            '\"' + escape_string("".join(data['companyLabelList'])) + '\"' if data['companyLabelList'] else "Null",
            '\"' + escape_string(data['companyShortName']) + '\"' if data['companyShortName'] else "Null",
            '\"' + escape_string(data['companySize']) + '\"' if data['companySize'] else "Null",
            '\"' + escape_string(data['createTime'].strip().split()[0]) + '\"' if data['createTime'] else "1900-01-01",
            '\"' + escape_string(data['district']) + '\"' if data['district'] else "Null",
            '\"' + escape_string(data['education']) + '\"' if data['education'] else "Null",
            '\"' + escape_string(data['explain']) + '\"' if data['explain'] else "Null",
            '\"' + escape_string(data['financeStage']) + '\"' if data['financeStage'] else "Null",
            '\"' + escape_string(data['firstType']) + '\"' if data['firstType'] else "Null",
            '\"' + escape_string(data['secondType']) + '\"' if data['secondType'] else "Null",
            '\"' + escape_string(data['formatCreateTime']) + '\"' if data['formatCreateTime'] else "Null",
            '\"' + escape_string(data['gradeDescription']) + '\"' if data['gradeDescription'] else "Null",
            '\"' + escape_string(data['industryField']) + '\"' if data['industryField'] else "Null",
            '\"' + escape_string("".join(data['industryLables'])) + '\"' if data['industryLables'] else "Null",
            '\"' + escape_string(data['jobNature']) + '\"' if data['jobNature'] else "Null",
            int(data['lastLogin']),
            '\"' + escape_string(data['latitude']) + '\"' if data['latitude'] else "Null",
            '\"' + escape_string(data['longitude']) + '\"' if data['longitude'] else "Null",
            '\"' + escape_string("-".join(data['linestaion'].split(';'))[:100]) + '\"' if data['linestaion'] else "Null",
            '\"' + escape_string(data['stationname']) + '\"' if data['stationname'] else "Null",
            '\"' + escape_string(data['subwayline']) + '\"' if data['subwayline'] else "Null",
            '\"' + escape_string(data['positionAdvantage']) + '\"' if data['positionAdvantage'] else "Null",
            int(data['positionId']),
            '\"' + escape_string("".join(data['positionLables'])) + '\"' if data['positionLables'] else "Null",
            '\"' + escape_string(data['positionName']) + '\"' if data['positionName'] else "Null",
            int(data['publisherId']),
            int(data['resumeProcessDay']),
            int(data['resumeProcessRate']),
            '\"' + escape_string(data['salary']) + '\"' if data['salary'] else "Null",
            int(data['score']),
            '\"' + escape_string(data['workYear']) + '\"' if data['workYear'] else "Null"
        )
    content_formalized = content[:len(content) - 1]

    return pre + content_formalized + pos


def sql_single(data):
    sql = 'INSERT INTO Jobs(' + \
          'businessZones,' + \
          'city,' + \
          'companyFullName,' + \
          'companyId,' + \
          'companyLabelList,' + \
          'companyShortName,' + \
          'companySize,' + \
          'createTime,' + \
          'district,' + \
          'education,' + \
          'explains,' + \
          'financeStage,' + \
          'firstType,' + \
          'secondType,' + \
          'formatCreateTime,' + \
          'gradeDescription,' + \
          'industryField,' + \
          'industryLables,' + \
          'jobNature,' + \
          'lastLogin,' + \
          'latitude,' + \
          'longitude,' + \
          'linestaion,' + \
          'stationname,' + \
          'subwayline,' + \
          'positionAdvantage,' + \
          'positionId,' + \
          'positionLables,' + \
          'positionName,' + \
          'publisherId,' + \
          'resumeProcessDay,' + \
          'resumeProcessRate,' + \
          'salary,' + \
          'score,' + \
          'workYear' + \
          ')VALUES(' + \
          '{0},{1},{2},{3},{4},{5},{6},STR_TO_DATE({7}, "%Y-%m-%d"),{8},{9},{10},{11},{12},{13},{14},{15},{16},{17},{18},' \
          '{19},{20},{21},{22},{23},{24},{25},{26},{27},{28},{29},{30},{31},{32},{33},{34});'.format(
              '\"' + escape_string("".join(data['businessZones'])) + '\"' if data['businessZones'] else "Null",
              '\"' + escape_string(data['city']) + '\"' if data['city'] else "Null",
              '\"' + escape_string(data['companyFullName']) + '\"' if data['companyFullName'] else "Null",
              int(data['companyId']),
              '\"' + escape_string("".join(data['companyLabelList'])) + '\"' if data['companyLabelList'] else "Null",
              '\"' + escape_string(data['companyShortName']) + '\"' if data['companyShortName'] else "Null",
              '\"' + escape_string(data['companySize']) + '\"' if data['companySize'] else "Null",
              '\"' + escape_string(data['createTime'].strip().split()[0]) + '\"' if data['createTime'] else "1900-01-01",
              '\"' + escape_string(data['district']) + '\"' if data['district'] else "Null",
              '\"' + escape_string(data['education']) + '\"' if data['education'] else "Null",
              '\"' + escape_string(data['explain']) + '\"' if data['explain'] else "Null",
              '\"' + escape_string(data['financeStage']) + '\"' if data['financeStage'] else "Null",
              '\"' + escape_string(data['firstType']) + '\"' if data['firstType'] else "Null",
              '\"' + escape_string(data['secondType']) + '\"' if data['secondType'] else "Null",
              '\"' + escape_string(data['formatCreateTime']) + '\"' if data['formatCreateTime'] else "Null",
              '\"' + escape_string(data['gradeDescription']) + '\"' if data['gradeDescription'] else "Null",
              '\"' + escape_string(data['industryField']) + '\"' if data['industryField'] else "Null",
              '\"' + escape_string("".join(data['industryLables'])) + '\"' if data['industryLables'] else "Null",
              '\"' + escape_string(data['jobNature']) + '\"' if data['jobNature'] else "Null",
              int(data['lastLogin']),
              '\"' + escape_string(data['latitude']) + '\"' if data['latitude'] else "Null",
              '\"' + escape_string(data['longitude']) + '\"' if data['longitude'] else "Null",
              '\"' + escape_string("-".join(data['linestaion'].split(';'))) + '\"' if data['linestaion'] else "Null",
              '\"' + escape_string(data['stationname']) + '\"' if data['stationname'] else "Null",
              '\"' + escape_string(data['subwayline']) + '\"' if data['subwayline'] else "Null",
              '\"' + escape_string(data['positionAdvantage']) + '\"' if data['positionAdvantage'] else "Null",
              int(data['positionId']),
              '\"' + escape_string("".join(data['positionLables'])) + '\"' if data['positionLables'] else "Null",
              '\"' + escape_string(data['positionName']) + '\"' if data['positionName'] else "Null",
              int(data['publisherId']),
              int(data['resumeProcessDay']),
              int(data['resumeProcessRate']),
              '\"' + escape_string(data['salary']) + '\"' if data['salary'] else "Null",
              int(data['score']),
              '\"' + escape_string(data['workYear']) + '\"' if data['workYear'] else "Null"
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