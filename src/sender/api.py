#-*- coding: utf-8 -*-
from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation
import sys
from schema import schema
import json
from datetime import datetime
import requests

url = 'http://www.catatech.cn:3003/query'

class BaseClient:
    def query_operation(self):
        op = Operation(schema.Query)
        return op

    def mutation_operation(self):
        op = Operation(schema.Mutation)
        return op

    def do_request(self, operation):
        endpoint = HTTPEndpoint(url)
        data = endpoint(operation)
        return data

    def update_userinfo(self, data):
        op = self.mutation_operation()
        update_result = op.update_user_info(inputs=data)
        update_result.message()
        print(op)
        data = self.do_request(op)
        print(data)
        # self.update_userinfo_v2(data)

    def update_statsinfo(self, data):
        op = self.mutation_operation()
        update_result = op.update_stats(inputs=data)
        update_result.message()
        print(op)
        data = self.do_request(op)
        print(data)

    def update_itemsinfo(self, data):
        op = self.mutation_operation()
        update_result = op.update_item(inputs=data)
        update_result.message()
        print(op)
        data = self.do_request(op)
        print(data)

    def update_userinfo_v2(self, data):
        query = '''
        mutation post_data($datas:[UserInfoInput!]!){
            UpdateUserInfo(inputs:$datas){
                message
            }
        }
        '''
        variables = {'datas': data}
        endpoint = HTTPEndpoint(url)
        resp = endpoint(query, variables)
        print(resp)

class Transformer(object):

    transform_map = None

    def __init__(self, element):
        self.element = element
        self.result = {}

    def get_transform_map(self):
        return self.transform_map

    def addon(self, key, value):
        return False

    def transform(self):
        tm = self.get_transform_map()
        if tm is None:
            return
        for k, v in tm.items():
            if self.addon(k, v):
                continue
            field_val = getattr(self.element, k, None)
            if field_val is None:
                continue
            if isinstance(v, str): 
                self.result[v] = field_val
                continue
            if isinstance(v, tuple):
                type_m = v[1]
                new_k = v[0]
                new_v = None
                if type_m == "String":
                    new_v = str(field_val)
                elif type_m == "Int":
                    new_v = int(field_val)
                elif type_m == "Date":
                    new_v = datetime.utcfromtimestamp(field_val).strftime('%Y-%m-%d %H:%M:%S')
                else:
                    raise Exception("unsupport type transform")
                self.result[new_k] = new_v

    def to_dict(self):
        print(self.result)
        return self.result
    
class CommentInputTransformer(Transformer):
    transformer_map = {
        "source",
        "item",
        "content",
        "author",
        "like",
        "time_created",
        "time_updated",
    }

class ItemInputTransformer(Transformer):
    transform_map = {
        "source" : "source",
        "item_id": "id",
        "author": "author",
        "item_title" :"title",
        "type": "type",
        "url":"url",
        "play":"view",
        "like":"like",
        "brands": "brands",
        "comments":"comments",
        "comment":"comment",
        "share":"share",
        "create_time": ("time_created","Date"),
        "Null":"is_business",
        "Null":"is_accepted",
        "Null":"is_completed",
        "Null":"cover",
        "Null":"cover_animated",
        "Null":"content",
        "Null":"exposure",
        "Null":"favorite",
        "Null":"time_updated",
    }

    def addon(self, key, value):
        if value == "source":
            self.result[value] = "toutiao"
            return True
        if value == "type":
            self.result[value] = "VIDEO"
            return True
        if value == "brands":
            self.result[value] = ["Null"]
            return True
        if value == "comments":
            self.result[value] = [{"content":"null"}]
        if key == "Null":
            return True
        return False


# class StatsInputTransformer(Transformer):
#     transform_map = {
#     "domain",
#     "user",
#     "item",
#     "source",
#     "data",
#     }


class UserInfoInputTransformer(Transformer):
    transform_map = {
        "source": "source",
        "id": ("id", "String"),
        "nick_name": "nickname",
        "Null":"type",
        "Null":"is_primary",
        "phone":"phone",
        "Null": "wechat",
        "avatar_uri": "avatar",
        "Null": "signature",
        "gender": "gender",
        "Null": "birthdate",
        "province": "province",
        "city":"city",
        "Null": "constellation",
        "mcn_name": "mcn",
        "Null": "mcn_id",
        "tags": "tags",
        "price":("price_video", "Int"),
        "long_video_price": ("price_long_video", "Int"),
        "Null": "price_article",
        "create_time": ("time_created","Date"),
        "modify_time": ("time_updated", "Date"),
    }

    def addon(self, key, value):
        if value == "source":
            self.result[value] = "toutiao"
            return True
        if value == 'tags':
            self.result[value] = json.loads(getattr(self.element, key))
            return True
        if value == "gender":
            self.result[value] = "MALE" if getattr(self.element, key) == 1 else "FEMALE"
            return True
        if key == "Null":
            return True
        return False