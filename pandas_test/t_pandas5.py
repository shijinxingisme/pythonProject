'''pandas读取及写入文件'''

import pandas as pd

#读取csv
file = pd.read_csv('testpython.csv', encoding='gbk')
print(file)

file.iloc[2,0] = '深圳'
print(file)

file.to_csv('test_.csv')
file.to_json('test_.json')
