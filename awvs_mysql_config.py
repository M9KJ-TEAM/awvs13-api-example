# -*- coding:UTF-8 -*-

import pymysql



def create_tasklist():
    # 打开数据库连接
    db = pymysql.connect(host="10.20.6.237", user="admin", password="PPL789789.z", database="auto_awvs")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute() 方法执行 SQL，如果表存在则删除
    cursor.execute("DROP TABLE IF EXISTS TASKLIST")
    # 使用预处理语句创建表
    sql = """CREATE TABLE IF NOT EXISTS `TASKLIST` ( 
          `id` int(22) NOT NULL AUTO_INCREMENT, 
          `featuresid` varchar(255) NOT NULL, 
          `targeturl` varchar(255) NOT NULL, 
          `taskid` varchar(255) NOT NULL, 
          `descript` varchar(255) NOT NULL, 
          `ctime` varchar(255) NOT NULL, 
          PRIMARY KEY (`id`) 
        ) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=0"""
    cursor.execute(sql)
    # 关闭数据库连接
    sql2 = "ALTER TABLE `TASKLIST` ADD unique(`featuresid`);"
    cursor.execute(sql2)
    db.close()

def create_vulinfo():
    # 打开数据库连接
    db = pymysql.connect(host="10.20.6.237", user="admin", password="PPL789789.z", database="auto_awvs")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute() 方法执行 SQL，如果表存在则删除
    cursor.execute("DROP TABLE IF EXISTS VULINFO")
    # 使用预处理语句创建表
    sql = """CREATE TABLE IF NOT EXISTS `VULINFO` ( 
          `id` int(22) NOT NULL AUTO_INCREMENT, 
          `featuresid` varchar(255) NOT NULL DEFAULT 'abc', 
          `vulname` varchar(255) NOT NULL DEFAULT 'abc', 
          `vulurl` varchar(255) NOT NULL DEFAULT 'abc', 
          `opt` varchar(255) NOT NULL DEFAULT 'abc', 
          PRIMARY KEY (`id`) 
        ) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=0"""

    cursor.execute(sql)
    sql2 = "ALTER TABLE `VULINFO` ADD unique(`featuresid`);"
    cursor.execute(sql2)
    # 关闭数据库连接
    db.close()

def create_lastid():
    # 打开数据库连接
    db = pymysql.connect(host="10.20.6.237", user="admin", password="PPL789789.z", database="auto_awvs")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute() 方法执行 SQL，如果表存在则删除
    cursor.execute("DROP TABLE IF EXISTS LSTID")
    # 使用预处理语句创建表
    sql = """CREATE TABLE IF NOT EXISTS `LSTID` ( 
          `id` int(22) NOT NULL AUTO_INCREMENT, 
          `featuresid` varchar(255) NOT NULL DEFAULT 'abc', 
          `targeturl` varchar(255) NOT NULL DEFAULT 'abc', 
          `lastid` varchar(255) NOT NULL DEFAULT 'abc', 
          PRIMARY KEY (`id`) 
        ) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=0"""
    cursor.execute(sql)
    sql2 = "ALTER TABLE `LSTID` ADD unique(`featuresid`);"
    cursor.execute(sql2)
    # 关闭数据库连接
    db.close()
##
if __name__ == '__main__':
    # create_tasklist()
    create_vulinfo()
    # create_lastid()