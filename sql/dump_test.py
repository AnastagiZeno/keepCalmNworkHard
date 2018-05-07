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

print res['workYear']

sql = """
INSERT INTO jobs (
  id,
  businessZones,
  city,
  companyFullName,
  companyId,
  companyLabelList,
  companyShortName,
  companySize,
  createTime,
  district,
  education,
  explains,
  financeStage,
  firstType,
  secondType,
  formatCreateTime,
  gradeDescription,
  industryField,
  industryLables,
  jobNature,
  lastLogin,
  latitude,
  longitude,
  linestaion,
  stationname,
  subwayline,
  positionAdvantage,
  positionId,
  positionLables,
  positionName,
  publisherId,
  resumeProcessDay,
  resumeProcessRate,
  salary,
  score,
  workYear
)VALUES(
{1},{2},{3},{4},{5},{6},{7},STR_TO_DATE({8}, '%Y-%m-%d'),{9},{10},{11},{12},{13},{14},'{15}',{16},{17},{18},{19},{20},{21},{22},{23},{24},{25},{26},{27},{28},{29},{30},{31},{32},{33},{34},{35}
)
""".format(
    "".join(res['businessZones']) if res['businessZones'] else None,
    res['city'],
    res['companyFullName'],
    int(res['companyId']),
    "".join(res['companyLabelList']) if res['companyLabelList'] else None,
    res['companyShortName'],
    res['companySize'],
    escape_string(res['createTime'].strip().split(' ')[0]),
    res['district'],
    res['education'],
    res['explain'],
    res['financeStage'],
    res['firstType'],
    res['secondType'],
    escape_string(res['formatCreateTime']),
    res['gradeDescription'],
    res['industryField'],
    "".join(res['industryLables']) if res['industryLables'] else None,
    res['jobNature'],
    res['lastLogin'],
    res['latitude'],
    res['longitude'],
    "-".join(res['linestaion'].split(';')) if res['linestaion'] else None,
    res['stationname'],
    res['subwayline'],
    res['positionAdvantage'],
    int(res['positionId']),
    "".join(res['positionLables']) if res['positionLables'] else None,
    res['positionName'],
    int(res['publisherId']),
    int(res['resumeProcessDay']),
    int(res['resumeProcessRate']),
    res['salary'],
    int(res['score']),
    res['workYear']
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




