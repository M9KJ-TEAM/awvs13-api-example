# -*- coding:UTF-8 -*-
import re
import time
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
#-------------------------------------------功能函数---------------------------
def scanstatus(url,targeturl,fatchid):
    try:
        for scanlist in scan_info(url,targeturl):
            Classtasklist = awvs_mysql_exec.tasklist(fatchid, '0', '0', '0', '0')
            r_t = Classtasklist.mysql_query()[1]
            if r_t == scanlist['任务ID号']:
                finalscanid = scanlist['最后扫描ID']
                finalsessionid = scanlist['最后扫描状态ID']
                s_f = [finalscanid,finalsessionid]
            else:
                s_f = None
            return s_f
    except KeyError as e:
        print('程序抛错',e)
        return 'False'

def scan_info(url,targeturl):
    #函数功能：获取扫描列表
    req = requests.get(url = url + '/api/v1/targets?q=text_search:*{}'.format(targeturl),headers = headers ,verify=False)
    try:
        res = req.json()['targets']
    except Exception as e:
        print('awega2@'+str(e))
        res = []
    num_check = 1
    Scan_list = []
    for tasklist in res:
        pattern = '{.+}'
        tskstr = str(tasklist).replace('target_id', '任务ID号')
        tskstr = tskstr.replace('last_scan_session_status', '最后扫描状态')
        tskstr = tskstr.replace('criticality', '风险等级')
        tskstr = tskstr.replace('last_scan_date', '最后扫描时间')
        tskstr = tskstr.replace('threat', '线程')
        tskstr = tskstr.replace('description', '描述')
        tskstr = tskstr.replace('last_scan_session_id', '最后扫描状态ID')
        tskstr = tskstr.replace('last_scan_id', '最后扫描ID')
        tskstr = tskstr.replace('address', '扫描目标')
        tskstr = tskstr.replace('manual_intervention', '人工干预')
        tskstr = tskstr.replace('severity_counts', '严重性计数')
        tskstr = tskstr.replace('continuous_mode', '连续操作模式')
        try:
            takdic = eval(tskstr)
        except Exception as e:
            print('eval 转化失败 {}'.format(e))
            takdic = {}
        match = re.findall(pattern, str(tasklist))
        if match:
            num_check += 1
            Scan_key = {}
            empty = {}
            for tasktitle, taskcontent in takdic.items():
                Scan_key[tasktitle] = taskcontent
            if Scan_key != empty:
                Scan_list.append(Scan_key)
            else:
                pass
    print(Scan_list)
    return Scan_list

def vulresult(url,targeturl,fatchid):
    stu = scanstatus(url,targeturl,fatchid)
    if stu != 'False' and stu != None:
        Classtasklist = awvs_mysql_exec.lstidist(fatchid,targeturl, stu[0])
        Classtasklist.mysql_insert()
        req = requests.get(url=url + '/api/v1/scans/' + str(stu[0]) + '/results/' + str(stu[1]) + '/vulnerabilities', headers=headers, verify=False)
        Result_req = req.json()
        for detail in Result_req['vulnerabilities']:
            vulnerabilities = detail['vt_name']
            affectsurl = detail['affects_url']
            affectsdetail = detail['affects_detail']
            vul = '漏洞是:' + str(vulnerabilities) + '<<<---|--->>>' + '漏洞URL是：' + str(affectsurl)
            vul2 = '漏洞是:' + str(vulnerabilities) + '<<<---|--->>>' + '漏洞URL是：' + str(affectsurl) + '<<<---|--->>>' + '漏洞细节是：' + str(affectsdetail)
            print(vul)
            print(vul2)
            vulname = str(vulnerabilities).replace(',','_')
            vulname = vulname.replace('\'','')
            Classtasklist = awvs_mysql_exec.vulinfo(targeturl, vulname, str(affectsurl),'否')
            if Classtasklist.mysql_query == '' or Classtasklist.mysql_query == None:
                print('漏洞细节存在问题，无法录入！')
            else:
                if Classtasklist.mysql_query() == str(affectsurl):
                    print('漏洞信息已存在，无法录入！')
                else:
                    Classtasklist.mysql_insert()
        else:
            pass
    else:
        print('>> 漏洞未扫描完成！')



# scanstatus(url,targeturl)  --->  查询最后扫描状态，插入最后扫描ID
# print(scan_info(url))  --->  查询扫描结果参数
# vulresult(url,targeturl)  --->  根据扫描结果参数返回漏洞情况并入库
# print(scan_info(url))
# scanstatus(url,targeturl)
# vulresult(url,targeturl)
#--------------------------------------------------------------
# scan_info(url='https://192.168.18.197:3443',targeturl='s9o0.com')
# scanstatus(url='https://192.168.18.197:3443',targeturl='s9o0.com',fatchid='a4ce536c185eb7dc5877da0e99538653')
# vulresult(url='https://192.168.18.197:3443',targeturl='s9o0.com',fatchid='a4ce536c185eb7dc5877da0e99538653')