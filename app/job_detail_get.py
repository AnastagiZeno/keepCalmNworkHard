# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import MySQLdb as mdb
import requests
from MySQLdb import escape_string

CONFIG = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': 'youneverguess',
    'db': 'lagou',
    'charset': 'utf8mb4'
}


def get_job_details(**condition):
    if condition:
        raise NotImplementedError
    sql = 'select description from JobDetail where hasAnalyzeDone=False;'
    return _get(sql)


def _get(sql):
    try:
        con = mdb.Connect(**CONFIG)
        cursor = con.cursor()
        cursor.execute(sql)
        result = [item[0] for item in cursor.fetchall()]
        con.commit()
    except Exception as e:
        con.rollback()
        result = False
    finally:
        cursor.close()
        con.close()
    return result