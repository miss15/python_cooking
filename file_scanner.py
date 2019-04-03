import os
import sys
import time
from datetime import  datetime

path = 'c:\\'
all_items=set()

for root,dirs,files in os.walk(path):
    file_path = [os.path.join(root,file) for file in files]
    #print(file_path)
    for item in file_path:
        all_items.add(item)
        print(item)

def timestamp_to_datetime(timestamp):
    #local_dt_time = datetime.utcfromtimestamp(timestamp / 1000.0).strftime('%Y-%m-%d %H:%M:%S.%f')
    local_dt_time = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
    return local_dt_time

def isModify_today(path):
    current_day = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d')
    item_modify_time = timestamp_to_datetime(os.path.getmtime(path))
    if current_day == item_modify_time:
        print("請注意，這個文件:",path,"今天已經被修改!!!")
    return True


print("Finaly total items: ", len(all_items))
print("開始掃描被修改的文件.....")
for i in all_items:
    try:
        result = isModify_today(i)
    except:
        print("警告：",i," 文件路徑有異常！")

print("掃描完畢!!!")
