import os
import awvs_mysql_config


print('[info]：开始配置数据库，请设置数据库账号密码为root')
os.system('pause')

print('开始配置任务列表数据库....')
awvs_mysql_config.create_tasklist()
print('任务列表数据库配置完毕...')

print('开始配置漏洞信息数据库....')
awvs_mysql_config.create_vulinfo()
print('漏洞信息数据库配置完毕...')

print('开始配置最后扫描ID数据库....')
awvs_mysql_config.create_lastid()
print('最后扫描ID数据库配置完毕...')

print('[FBI waring：您可以使用awvs调用扫描器了！注意有bug请反馈我的邮箱 ：hack9090@126.com]')
os.system('pause')
