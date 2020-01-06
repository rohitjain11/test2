import requests
from celery_worker import *



urls = "http://127.0.0.1:8000/range/"
param = {'start':10, 'end':21}

r = requests.get(urls, params=param)
if r.ok:
    print("success")
#this also add data into database you can check there 

a = add.delay(11, 15)
if a.ready() == "False":
    print("task running : case1 pass")


print(a.status())
time.sleep(15)

if a.ready() == "True":
    print("task complete : case2 pass")

