#!/usr/bin/python
#-*- coding: utf-8 -*-
from gevent import monkey; monkey.patch_all()
import gevent
import requests
import json
import sys, os
import time
import random

url_pattern = "https://star.toutiao.com/v/api/demand/author_list/?page={}&limit={}&need_detail=true&platform_source=1&order_by=score"
cookie = 'gr_user_id=a2f90083-76fa-413c-821d-18bfe5141cd4; grwng_uid=56d2004d-5237-4b05-a6ae-00453c7b3be3; csrftoken=jwrMgOAg8BEuC9n0WG4Z2Orj1c0gIK2f; tt_webid=6693481726045767181; toutiao_sso_user=52964076a74a43c4874d3abc0b72cf39; sso_uid_tt=7fc206cc5fb9c9b4ec5bbf3f81949919; login_flag=f4606e2a9e56027f762f483a07b5bbf3; sid_tt=8b8ff7186bf0e3cc404e25b07ec11363; uid_tt=3e4d6a7260928261078a15345ce1f2eb; sessionid=8b8ff7186bf0e3cc404e25b07ec11363; sid_guard="8b8ff7186bf0e3cc404e25b07ec11363|1558455048|15552000|Sun\054 17-Nov-2019 16:10:48 GMT"; 8632e941eb705978_gr_session_id=3e0983aa-e87f-4aa8-909d-0829d2696340; 8632e941eb705978_gr_session_id_3e0983aa-e87f-4aa8-909d-0829d2696340=true; star_sessionid=8b8ff7186bf0e3cc404e25b07ec11363; s_v_web_id=ab6fac3dff8e9125916948b3809d3c0b'
headers = {
    "X-csrftoken": "jwrMgOAg8BEuC9n0WG4Z2Orj1c0gIK2f",
    "Referer": "https://star.toutiao.com/ad",
    "Cookie": cookie,
    "User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36"
}
output_path = os.path.join(os.getcwd(), 'output','2019-05-23')

def get_total_count(headers):
    resp = requests.get(url=url_pattern.format(1,1),headers=headers)
    if resp.status_code == 200:
        data = resp.json()
        if not data.get("data"):
            raise Exception("Exception: {}".format(data))
        return data.get("data").get('pagination').get('total_count')

def write_data_file(filename, data):
    with open(filename, 'w') as f:
        if isinstance(data, str):
            f.write(data)
        else:
            f.write(json.dumps(data))

def fetch_list(total_count, limit, headers):
    total_page = total_count // limit + 1
    for i in range(1, total_page):
        sleeptime=random.random(0, 5)
        time.sleep(sleeptime)
        do_fetch(i, limit, headers)

def concurrent_fetch_list(total_count, limit, headers):
    total_page = total_count // limit + 1
    tasks = []
    for i in range(1, total_page):
        task = gevent.spawn(do_fetch, i, limit, headers)
        tasks.append(task)
    gevent.joinall(tasks)

def do_fetch(page,limit,headers):
    resp = requests.get(url=url_pattern.format(page,limit),headers=headers)
    if resp.status_code == 200:
        data = resp.json()
        if not data.get("data"):
            print ("Fail: {}".format(resp.text))
        filename = os.path.join(output_path,'%d.json'%page)
        data = resp.json()
        write_data_file(filename=filename, data=data) 
    else:
        raise Exception("args: page {}, limit {}, headers {} \n resp: {}".format(page, limit, headers, resp.text))

if __name__ == '__main__':
    print ("Start fetch star.tuotiao.com list")
    total_count = get_total_count(headers)
    print("total_count: %s"%total_count)
    print("output path:%s"%output_path)
    fetch_list(total_count, limit=50, headers=headers)
    # concurrent_fetch_list(total_count=total_count, limit=20, headers=headers)
