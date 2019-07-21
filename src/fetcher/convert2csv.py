#!/usr/bin/python
#-*- coding: utf-8 -*-
import os
import json
from parse_argv import parse_start, parse_end

Author_Used_Fields =[
            "long_video_price",
            "is_star",
            "rank",
            "follower",
            "create_time",
            "total_favour_cnt",
            "avg_play",
            "abandon_sign_result",
            "id",
            "appeal_id",
            "city",
            "short_id",
            "tags",
            "platform_source",
            "cut_rate",
            "recommend",
            "lowest_price",
            "next_month_price",
            "author_type",
            "province",
            "online_status",
            "next_month_long_video_price",
            "price",
            "is_online",
            "has_phone",
            "core_user_id",
            "category_id",
            "protocol_id",
            "nick_name",
            "gender",
            # "aweme_tags",
            "order_cnt",
            "rate",
            "modify_time",
            "avatar_uri",
            "price_info",
            "task_status",
            "unique_id"
            ]

class Author(object):
    def __init__(self, d):
        self.__dict__ = d
    
def author_ids_from_file(page, dir_path):
    return [getattr(author,"id") for author in convert2objects(page, dir_path)]

def convert2objects(page, dir_path):
    authors = []
    with open(os.path.join(dir_path, '{}.json'.format(page)), 'r') as f:
        lines = f.readlines()
        for line in lines:
            data = json.loads(line)
            # print(json.dumps(data, ensure_ascii=False))
            for author_dict in data.get('data', {}).get('authors'):
                author = json.loads(json.dumps(author_dict), object_hook=Author)
                authors.append(author)
    return authors

def convert2csvstr(author):
    if not isinstance(author, Author):
        raise
    csv = []
    for field in Author_Used_Fields:
        data = getattr(author, field, 'null')
        if field == 'tags':
            value = ";".join(json.loads(data))
        elif field == 'price_info':
            value =";".join([":".join([getattr(info,"desc"),str(getattr(info,'price'))]) for info in data])
        else:
            value = str(data)
        # print(value)
        csv.append(value)
    return ",".join(csv)

def convert2csvlist(authors):
    result = []
    for author in authors:
        result.append(convert2csvstr(author))
    return result

def cvs_title(fields):
    return ",".join(fields)

def write2csv(lines, filename):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line.strip()+"\n")

if __name__ == '__main__':
    # TODO
    output_path = os.path.join(os.getcwd(), 'output','2019-05-23')
    file_start, file_end = int(parse_start()), int(parse_end())
    lines =[cvs_title()]
    for i in range(file_start, file_end):
        authors = convert2objects(i, output_path)
        lines.extend(convert2csvlist(authors))
    output = os.path.join(output_path,"data.csv")
    write2csv(lines, output)