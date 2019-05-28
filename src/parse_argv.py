#!/usr/bin/python
#-*- coding: utf-8 -*-
import sys
import os
import getopt

def parse_argv(key):
    options, args = parse()
    for value in options:
        if value[0] == '--'+key:
            return value[1]
    return None
    
def parse():
    options, args = getopt.getopt(sys.argv[1:], "h:", ['output_dir=','min_time=','max_time=','cookie=',"start_page=","end_page="])
    return options, args

def parse_cookie():
    return parse_argv("cookie")

def parse_start():
    return parse_argv("start_page")

def parse_end():
    return parse_argv("end_page")

def parse_min_time():
    return parse_argv("min_time")

def parse_max_time():
    return parse_argv("max_time")

def parse_output():
    return parse_argv("output_dir")