# -*- coding:UTF-8 -*-

import pymysql

class tasklist:
    """
  `featuresid` varchar(255) NOT NULL,
  `targeturl` varchar(255) NOT NULL,
  `taskid` varchar(255) NOT NULL,
  `descript` varchar(255) NOT NULL,
    """
    def __init__(self,featuresid,url,id,dspt,ctimes):
        self.features = featuresid
        self.url = url
        self.id = id
        self.dspt =dspt
        self.ctime = ctimes
    def mysql_insert(self):
        # 打开数据库连接
        db = pymysql.connect(host="10.20.6.237", user="admin", password="PPL789789.z", database="auto_awvs")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 插入语句
        sql = """INSERT INTO TASKLIST(featuresid,targeturl,taskid, descript, ctime) 
               VALUES ('%s','%s','%s','%s','%s')""" % (self.features,self.url,self.id,self.dspt,self.ctime)
        try:
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            db.rollback()
        # 关闭数据库连接
        db.close()

    def mysql_query(self):
        # 打开数据库连接
        db = pymysql.connect(host="10.20.6.237", user="admin", password="PPL789789.z", database="auto_awvs")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 查询语句
        sql = """SELECT * FROM TASKLIST WHERE featuresid LIKE '%s'""" % (self.features)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchone()
            targeturl = results[2]
            taskid = results[3]
            db.close()
            return [targeturl,taskid]
        except Exception as e:
            print("Error: unable to fetch data",e)
            db.close()
    #
    # def mysql_url_query(self):
    #     # 打开数据库连接
    #     db = pymysql.connect(host="10.20.6.237", user="admin", password="PPL789789.z", database="auto_awvs")
    #     # 使用cursor()方法获取操作游标
    #     cursor = db.cursor()
    #     # SQL 查询语句
    #     # print(self.url)
    #     sql = """SELECT * FROM TASKLIST WHERE targeturl LIKE '%s'""" % (self.url)
    #     try:
    #         # 执行SQL语句
    #         cursor.execute(sql)
    #         # 获取所有记录列表
    #         results = cursor.fetchall()
    #         targeturllist = []
    #         for row in results:
    #             id = row[0]
    #             targeturl = row[1]
    #             taskid = row[2]
    #             descript = row[3]
    #             # 打印结果
    #             # print("序号：%s,目标URL：%s,任务ID：%s,描述：%s," % \
    #             #       (id, targeturl, taskid, descript))
    #             # 关闭数据库连接
    #             db.close()
    #             targeturllist.append(targeturl)
    #         return targeturllist
    #     except Exception as e:
    #         print("Error: unable to fetch data",e)
    #         db.close()
    #
    # def mysql_delete(self):
    #     # 打开数据库连接
    #     db = pymysql.connect(host="10.20.6.237", user="admin", password="PPL789789.z", database="auto_awvs")
    #     # 使用cursor()方法获取操作游标
    #     cursor = db.cursor()
    #     # SQL 删除语句
    #     sql = """DELETE FROM TASKLIST WHERE targeturl LIKE '%s'""" % (self.url)
    #     try:
    #         # 执行SQL语句
    #         cursor.execute(sql)
    #         # 提交修改
    #         db.commit()
    #         db.close()
    #         return '删除成功'
    #     except:
    #         # 发生错误时回滚
    #         db.rollback()
    #         db.close()
    #     # 关闭连接
class vulinfo:
    def __init__(self,targeturl,vulname,vulurl,opt):
        self.targeturl = targeturl + '%'
        self.vulname = vulname
        self.vulurl = vulurl
        self.opt =opt
    def mysql_insert(self):
        # 打开数据库连接
        db = pymysql.connect(host="10.20.6.237", user="admin", password="PPL789789.z", database="auto_awvs")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 插入语句
        sql = """INSERT INTO VULINFO(vulname,vulurl,opt) 
               VALUES ('%s','%s','%s')""" % (self.vulname,self.vulurl,self.opt)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except Exception as e:
            # 如果发生错误则回滚
            db.rollback()
        # 关闭数据库连接
        db.close()

    def mysql_query(self):
        # 打开数据库连接
        db = pymysql.connect(host="10.20.6.237", user="admin", password="PPL789789.z", database="auto_awvs")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 查询语句
        sql = """SELECT * FROM VULINFO WHERE vulurl LIKE '%s'""" % (self.targeturl)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                id = row[0]
                vulname = row[1]
                vulurl = row[2]
                opt = row[3]
                # 打印结果
                # print("序号：%s,漏洞名称：%s,漏洞URL：%s,是否导出：%s," % \
                #       (id, vulname, vulurl, opt))
                # 关闭数据库连接
                db.close()
                return vulurl
        except Exception as e:
            print("Error: unable to fetch data",e)
            db.close()

    def mysql_delete(self):
        # 打开数据库连接
        db = pymysql.connect(host="10.20.6.237", user="admin", password="PPL789789.z", database="auto_awvs")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 删除语句
        sql = """DELETE FROM VULINFO WHERE vulurl LIKE '%s'""" % (self.vulurl)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 提交修改
            db.commit()
            db.close()
            return '删除成功'
        except:
            # 发生错误时回滚
            db.rollback()
            db.close()
        # 关闭连接
class lstidist:
    def __init__(self,featuresid,targeturl,lastid):
        self.url = targeturl
        self.id = lastid
        self.featuresid = featuresid
    def mysql_insert(self):
        # 打开数据库连接
        db = pymysql.connect(host="10.20.6.237", user="admin", password="PPL789789.z", database="auto_awvs")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 插入语句
        sql = """INSERT INTO LSTID(featuresid,targeturl,lastid) 
               VALUES ('%s','%s','%s')""" % (self.featuresid,self.url,self.id)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except Exception as e:
            # 如果发生错误则回滚
            db.rollback()
        # 关闭数据库连接
        db.close()
    def mysql_query(self):
        # 打开数据库连接
        db = pymysql.connect(host="10.20.6.237", user="admin", password="PPL789789.z", database="auto_awvs")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 查询语句
        sql = """SELECT * FROM LSTID WHERE targeturl LIKE '%s'""" % (self.url)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                global lastid
                id = row[0]
                targeturl = row[1]
                lastid = row[2]
                # # 打印结果
                # print('数据库INFO：' + "序号：%s,目标URL：%s,最后扫描ID：%s," % (id, targeturl,lastid ))
                # 关闭数据库连接
                db.close()
                return lastid
        except Exception as e:
            print("Error: unable to fetch data",e)
            db.close()
            return lastid
#测试区域----------------------------------------
# 测试插入数据
# mysql_insert('http://www.baidu.com','NAFJKFNJAKF-AG-AG6-AG5-AG-AG-AG5-GAG25A-GA-G-AG-AG--GA','测试案例')
#测试查询数据
# mysql_query('http://www.baidu.com')
# if mysql_query('http://www.baidu.com') == 'NAFJKFNJAKF-AG-AG6-AG5-AG-AG-AG5-GAG25A-GA-G-AG-AG--GA':
#     print('成功！')
# else:
#     print('失败！')
# if mysql_delete('url') == '删除成功':
#     print('成功')
# else:
#     print('失败')
#-----------------------------------------------
# s = lstidist('http://ljb.gzhaituikeji.cn/sso/login','0')
# s.mysql_query()
#-----------------------------------------------.
# if tasklist('123', '1', '1').mysql_query() == None:
#     print ('yes')
#
# else:
#     pass
# test = tasklist('http://wx.10086.cn/zhejiang', '1', '1')
# ss = test.mysql_url_query()
# print(ss)