#!/usr/bin/python
#-*- coding: utf-8 -*-
import json
import os


class Entity(object):
    def __init__(self, d):
        self.__dict__ = d

class Author(Entity):
    pass
    
class AuthorInfo(object):
    pass


def write2csv(lines, filename):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line.strip()+"\n")


def cvs_title(fields):
    return ",".join(fields)


def get_authors_from_page(pfilename):
    objects = []
    with open(pfilename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            data = json.loads(line)
            for author_dict in data.get('data', {}).get('authors'):
                author = json.loads(json.dumps(author_dict), object_hook=Entity)
                objects.append(author)
    return objects

def get_authorid_list(pfilename):
    return [getattr(author,"id") for author in get_authors_from_page(pfilename)]


class Convertor(object):

    def __init__(self, dir_path, out_path, fields):
        self.dir_path = dir_path
        self.out_path = out_path
        self.fields = fields

    def convert(obj):
        pass

    def write(filename):
        pass