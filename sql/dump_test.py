# -*- coding: utf-8 -*-

import MySQLdb as mdb
from MySQLdb import escape_string
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


with open('jobs.json') as j:
    jobs = json.load(j)


results = jobs['content']['positionResult']['result']
res = results[0]

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
          '\"' + escape_string("".join(res['businessZones'])) + '\"' if res['businessZones'] else "Null",
          '\"' + escape_string(res['city']) + '\"' if res['city'] else "Null" ,
          '\"' + escape_string(res['companyFullName']) + '\"' if res['companyFullName'] else "Null",
          int(res['companyId']),
          '\"' + escape_string("".join(res['companyLabelList'])) + '\"' if res['companyLabelList'] else "Null",
          '\"' + escape_string(res['companyShortName']) + '\"' if res['companyShortName'] else "Null",
          '\"' + escape_string(res['companySize']) + '\"' if res['companySize'] else "Null",
          '\"' + escape_string(res['createTime'].strip().split()[0])+ '\"' if res['createTime'] else "1900-01-01",
          '\"' + escape_string(res['district']) + '\"' if res['district'] else "Null",
          '\"' + escape_string(res['education']) + '\"' if res['education'] else "Null",
          '\"' + escape_string(res['explain']) + '\"' if res['explain'] else "Null",
          '\"' + escape_string(res['financeStage']) + '\"' if res['financeStage'] else "Null",
          '\"' + escape_string(res['firstType']) + '\"' if res['firstType'] else "Null",
          '\"' + escape_string(res['secondType']) + '\"' if res['secondType'] else "Null",
          '\"' + escape_string(res['formatCreateTime']) + '\"' if res['formatCreateTime'] else "Null",
          '\"' + escape_string(res['gradeDescription']) + '\"' if res['gradeDescription'] else "Null",
          '\"' + escape_string(res['industryField']) + '\"' if res['industryField'] else "Null",
          '\"' + escape_string("".join(res['industryLables'])) + '\"' if res['industryLables'] else "Null",
          '\"' + escape_string(res['jobNature']) + '\"' if res['jobNature'] else "Null",
          int(res['lastLogin']),
          '\"' + escape_string(res['latitude']) + '\"' if res['latitude'] else "Null",
          '\"' + escape_string(res['longitude']) + '\"' if res['longitude'] else "Null",
          '\"' + escape_string("-".join(res['linestaion'].split(';'))) + '\"' if res['linestaion'] else "Null",
          '\"' + escape_string(res['stationname']) + '\"' if res['stationname'] else "Null",
          '\"' + escape_string(res['subwayline']) + '\"' if res['subwayline'] else "Null",
          '\"' + escape_string(res['positionAdvantage']) + '\"' if res['positionAdvantage'] else "Null",
          int(res['positionId']),
          '\"' + escape_string("".join(res['positionLables'])) + '\"' if res['positionLables'] else "Null",
          '\"' + escape_string(res['positionName']) + '\"' if res['positionName'] else "Null",
          int(res['publisherId']),
          int(res['resumeProcessDay']),
          int(res['resumeProcessRate']),
          '\"' + escape_string(res['salary']) + '\"' if res['salary'] else "Null",
          int(res['score']),
          '\"' + escape_string(res['workYear']) + '\"' if res['workYear'] else "Null"
      )

print sql

CONFIG = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': 'youneverguess',
    'db': 'lagou',
    'charset': 'utf8mb4'
}

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




