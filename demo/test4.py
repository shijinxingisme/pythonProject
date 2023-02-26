# JSON
import json
a_dict={'a':1,"b":2,"c":3,100:200}
# with open("my.json","w") as f:
#     json.dump(a_dict,f)     #存放
#
with open("my.json","r") as f:
    j = json.load(f)          #加载
    print(j)
