#!/usr/bin/python
#-*- coding: utf-8 -*-
import os
import requests
import json
import time
import random
from parse_argv import parse_cookie, parse_start, parse_end, parse_max_time, parse_min_time

def print_f(msg):
    print(msg)

def rate_control(min_time=1, max_time=10):
    def decorator(func):
        def func_wrapper(*args, **kwargs):
            sleeptime=random.randint(min_time, max_time)
            print_f("next run at {}s later".format(sleeptime))
            time.sleep(sleeptime)
            ret = func(*args, **kwargs)
            return ret
        return func_wrapper
    return decorator

class APIFetchException(Exception):
    def __init__(self, msg):
        self.msg = msg
    
class SpiderTaskHelper(object):
    @staticmethod
    def write2jsonfile(filename, data):
        with open(filename, 'w') as f:
            if isinstance(data, str):
                f.write(data)
            else:
                f.write(json.dumps(data, ensure_ascii=False))
    @staticmethod
    def new_headers(cookie): 
        headers = {
            "X-csrftoken": "jwrMgOAg8BEuC9n0WG4Z2Orj1c0gIK2f",
            "Referer": "https://star.toutiao.com/ad",
            "Cookie": cookie,
            "User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36"
        }
        return headers


class SpiderManager(object):

    def __init__(self, fetchers, output_root):
        self.fetchers = fetchers
        self.output_root = output_root

    def make_env(self):
        self.cookie = parse_cookie()
        self.headers = SpiderTaskHelper.new_headers(self.cookie)
        self.start = parse_start()
        self.end = parse_end()
        max_time = parse_max_time() 
        min_time = parse_min_time()
        if max_time is None:
            max_time = 10
        if min_time is None:
            min_time = 0
        for fetcher in self.fetchers:
            fetcher.prepare(self.headers, int(self.start), int(self.end), int(max_time), int(min_time), self.output_root)

    # need to extend run
    def run(self):
        print_f("start runing on fetchers: {}".format(self.fetchers))
        for fetcher in self.fetchers:
            try:
                fetcher.start()
            except Exception as e:
                self.handle_exception(e)
        print_f("finish run!")

    def handle_exception(self, exception):
        exception_msg = ""
        if isinstance(exception, APIFetchException):
            exception_msg = exception.msg
        else:
            exception_msg = str(exception)
        print_f("[Exception] env: {}, msg:{}".format(",".join([self.start, self.end]), exception_msg))

class APISpiderTask(object):

    def __init__(self, headers, outputfn, url_pattern, params):
        self.headers = headers
        self.url_pattern = url_pattern
        self.outputfn = outputfn
        self.params = params
    
    def execute(self):
        # fetch
        url = self.url_pattern.format(*self.params)
        print_f("Start fetch: {} ,args: {}".format(url, self.params))
        resp = requests.get(url=url, headers=self.headers)
        if resp.status_code != 200:
            raise APIFetchException("Fail at url: {}, status_code:{}".format(url, resp.status_code))
        data = resp.json()
        if not data.get("data"):
            msg = []
            msg.append(url)
            msg.append(self.params)
            msg.append(json.dumps(data, ensure_ascii=False))
            raise APIFetchException("Fail at url: {}, params:{}, resp:{}".format(*msg))
        # store
        SpiderTaskHelper.write2jsonfile(self.outputfn, data=data)

    def __str__(self):
        return "url_pattern: {} params:{}".format(self.url_pattern, params)

class SpiderFetcher(object):

    def __init__(self, url_pattern):
        self.url_pattern = url_pattern
        self.prepared = False

    def __str__(self):
        return "{}, dir_path:{} url_pattern:{}".format(self, self.dir_path, self.url_pattern)

    def prepare(self, headers, startp, endp, max_time, min_time, output_root):
        self.prepared = True
        self.output_root = output_root
        self.headers = headers
        self.page_start = startp
        self.page_end = endp
        self.max_time = max_time
        self.min_time = min_time
        self.make_dirs()

    def make_dirs(self):
        if not os.path.isdir(self.output_dir()):
            os.makedirs(self.output_dir())

    def output_dir(self):
        return self.output_root

    def update_headers(self, headers):
        self.headers = headers

    def start(self):
        if not self.prepared:
            raise APIFetchException("Error: started before called perpare")
        
        for task in self.task_generator():
            @rate_control(max_time=self.max_time, min_time=self.min_time)
            def execute(task):
                task.execute()
            execute(task)

    def task_generator(self):
        pass
