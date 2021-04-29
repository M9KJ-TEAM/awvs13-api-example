# -*- coding:UTF-8 -*-
import time
import requests
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


def profile(url):
    #函数功能：规则查询
    req = requests.get(url = url + '/api/v1/scanning_profiles',headers = headers ,verify=False)
    profilelist = req.json()
    # print(profilelist)
    num = 1
    for profile_name,profile_content in profilelist.items():
        # print('%s : %s' % (profile_name,profile_name))
        for profile_content in profile_content:
            # print(profile_content)
            print('《规则' + str(num) + '》' + '--------------------------------------------------------------------------------')
            num += 1
            str_profile_content = str(profile_content).replace('custom','定制')
            str_profile_content = str_profile_content.replace('profile_id','规则ID')
            str_profile_content = str_profile_content.replace('name','规则名称')
            str_profile_content = str_profile_content.replace('checks','检查核实')
            str_profile_content = str_profile_content.replace('sort_order','规则等级')
            try:
                global profile_content_second
                profile_content_second = eval(str_profile_content)
                # print(profile_content_second)
            except:
                pass
            for profile_content_name,profile_content_content in profile_content_second.items():
                print('%s:%s' % (profile_content_name,profile_content_content))