# -*- coding:UTF-8 -*-
import time
import json
import hashlib
import requests
import awvs_mysql_exec
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

#-------------------------------------------读取配置---------------------------
readurl = open('headers.ini', 'r' , encoding='UTF-8')
headersconfig = eval(readurl.read())
X_Auth = headersconfig['X-Auth']
content_type = headersconfig['content-type']
headers = {
    'content-type':content_type,
    'X-Auth':X_Auth,
    # 'cookie':'ui_session: 2986ad8c0a5b3df4d7028d5f3c06e936c5d75c0df2decdc9dd6664a2186ccc6989fe455e34a4a7896af3c7ecb2360b935e6b98ce929b540bc2344cf6fc72a7656',
}

nowtime = time.strftime("%Y-%m-%d", time.localtime())


def add(url,targeturl,description,criticality):
    #函数功能：添加任务
    postdata = {
        'address':'%s' % (targeturl),
        'description':'%s' % (description),
        'criticality':'%s' % (criticality),
    }
    data = json.dumps(postdata)
    req = requests.post(url = url + '/api/v1/targets',headers = headers ,data = data,verify=False)
    add_res = req.json()
    for add_name,add_content in add_res.items():
        if add_name == 'target_id':
            time_f = targeturl +  time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            m = hashlib.md5()
            m.update(time_f.encode('utf-8'))  # 传入需要加密的字符串进行MD5加密
            features = m.hexdigest()  # 获取到经过MD5加密的字符串并返回
            Classtasklist = awvs_mysql_exec.tasklist(features,targeturl, add_content, description,time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            Classtasklist.mysql_insert()
            print('添加扫描任务成功！')
        else:
            pass

def startscan(url,fatchid,level):
    #函数功能：进行扫描
    global profile_id
    if level == 1:
        profile_id = '11111111-1111-1111-1111-111111111111'
    elif level == 2:
        profile_id = '11111111-1111-1111-1111-111111111112'
    elif level == 3:
        profile_id = '11111111-1111-1111-1111-111111111116'
    elif level == 4:
        profile_id = '11111111-1111-1111-1111-111111111113'
    elif level == 5:
        profile_id = '11111111-1111-1111-1111-111111111115'
    elif level == 6:
        profile_id = '11111111-1111-1111-1111-111111111117'
    else:
        pass
    Classtasklist = awvs_mysql_exec.tasklist(fatchid,'0', '0', '0','0')
    r = Classtasklist.mysql_query()
    postdata = {
    'target_id':r[1],
    'profile_id':profile_id,
    'schedule': {
        'disable': False,
        'start_date': None,
        'time_sensitive': False,
    }
    }
    data = json.dumps(postdata)
    req = requests.post(url = url + '/api/v1/scans',headers = headers ,data = data,verify=False)
    scan_res = req.json()
    # print(scan_res)
    print('---------------------------------------------------------------------------------------------')
    print('INFO:目标URL：'+ r[0] + '加入扫描成功开始扫描....')
    str_scan_res = str(scan_res).replace('target_id','任务ID')
    str_scan_res = str_scan_res.replace('schedule','计划安排')
    str_scan_res = str_scan_res.replace('profile_id','扫描规则')
    str_scan_res = str_scan_res.replace('ui_session_id','用户cookie')
    try:
        global cn_scan_res
        cn_scan_res = eval(str_scan_res)
    except:
        pass
    for scan_name,scan_content in cn_scan_res.items():
        print('%s:%s' % (scan_name,scan_content))

if __name__ == '__main__':
    add('https://192.168.18.197:3443','http://blog.m9scan.com','test001',30)
    startscan('https://192.168.18.197:3443','http://blog.m9scan.com',1)