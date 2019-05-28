#!/usr/bin/python
#-*- coding: utf-8 -*-
import os
import author
import detail
import item
from base import SpiderManager
from parse_argv import parse, parse_output

def parse_tasks():
    _ , args = parse()
    return args

FETCHERS_REGISTRY = {
    "author": author.fetcher,
    "detail": detail.fetcher,
    "item": item.item_fetcher,
    "item_detail": item.item_detail_fetcher
}

OUTPUT_ROOT = os.path.join(os.getcwd(), 'output')

if __name__ == '__main__':
    fetchers = []
    tasks = parse_tasks()
    output_root = parse_output()
    if output_root is None:
        output_root = OUTPUT_ROOT
    for k, v in FETCHERS_REGISTRY.items():
        if 'all' in tasks or k in tasks:
            print("task {} has added!".format(k))
            fetchers.append(v)
    if len(fetchers) <= 0:
        raise Exception("task name is not specified")
    manager = SpiderManager(fetchers, output_root)
    manager.make_env()
    manager.run()