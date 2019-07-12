import json
import os
import sys 
sys.path.append('/Users/GYB/code/puppeteer-spider')
from convert2csv import cvs_title, write2csv
from src.graphql.api import UserInfoInputTransformer, BaseClient

Fields = [
        # "is_visible",
        "long_video_price",
        # "platform_source",
        "follower",
        "create_time",
        "total_favour_cnt",
        "avg_play",
        "abandon_sign_result",
        "id",
        "appeal_id",
        # "city",
        "short_id",
        # "platform",
        "mcn_logo",
        # "tags",
        "is_star",
        "star_video_count",
        "lowest_price",
        "next_month_price",
        "author_type",
        "province",
        "mcn_id",
        "online_status",
        "next_month_long_video_price",
        "price",
        "phone",
        "is_online",
        "order_done_count",
        "has_phone",
        "core_user_id",
        "category_id",
        "protocol_id",
        "nick_name",
        "gender",
        "aweme_tags",
        "rate",
        "modify_time",
        "avatar_uri",
        # "price_info",
        "task_status",
        "mcn_name",
        "unique_id",
        ]

class AuthorInfo(object):
      def __init__(self, d):
        self.__dict__ = d

class Convertor:

    def iter_objects(self, filenames, dirpath, output):
        for filename in filenames:
            if os.path.splitext(filename)[-1][1:] != "json":
                continue
            print(filename)
            target = os.path.join(dirpath, filename)
            yield self.convert2object(target)
            

    def convert2object(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            info = json.loads(json.dumps(data.get('data')), object_hook=AuthorInfo)
        return info

class Convertor2Csv(Convertor):
    def convert(self, filenames, dirpath, output):
        data = [cvs_title(Fields)]
        for author in self.iter_objects(filenames,dirpath,output):
            line = self.convert2csvstr(author)
            data.append(line)
        write2csv(data, output)

    def convert2csvstr(self, author_info):
        csv = []
        for field in Fields:
            data = getattr(author_info, field, 'null')
            if field == 'tags':
                value = ";".join(json.loads(data))
            elif field == 'price_info':
                value =";".join([":".join([getattr(info,"desc"),str(getattr(info,'price'))]) for info in data])
            else:
                value = str(data)
            csv.append(value)
        return ",".join(csv)

class Convertor2UserInput(Convertor):

    def convert(self, filenames, dirpath, output):
        result = []
        for author in self.iter_objects(filenames,dirpath,output):
            result.append(self.convert2Dict(author))
            if len(result) == 10:
                BaseClient().update_userinfo(result)
                result.clear()

    def convert2Dict(self, author_info):
        ts = UserInfoInputTransformer(author_info)
        ts.transform()
        return ts.to_dict()
            


if __name__ == '__main__':
    dir_path = os.path.abspath(os.path.join("/Users/GYB/code/puppeteer-spider","output","2019-05-23", "authors"))
    output = os.path.join(dir_path,"author_data.csv")
    print("Start convert author info in {}".format(dir_path))
    for dirpath, dirnames, filenames in os.walk(dir_path):
        Convertor2UserInput().convert(filenames, dir_path, output)    
    print("Finish convert author info in {}".format(output))
