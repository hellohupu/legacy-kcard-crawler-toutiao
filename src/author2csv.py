import os
import json
from convert2csv import write2csv, cvs_title

Fields = [
        "is_visible",
        "long_video_price",
        "platform_source",
        "follower",
        "create_time",
        "total_favour_cnt",
        "avg_play",
        "abandon_sign_result",
        "id",
        "appeal_id",
        # "city",
        "short_id",
        "platform",
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

def convert2object(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
        info = json.loads(json.dumps(data.get('data')), object_hook=AuthorInfo)
    return info
    
def convert2csvstr(author_info):
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


def convert(filenames, dirpath, output):
    data = [cvs_title(Fields)]
    for filename in filenames:
        target = os.path.join(dirpath, filename)
        author = convert2object(target)
        line = convert2csvstr(author)
        data.append(line)
    write2csv(data, output)


if __name__ == '__main__':
    dir_path = os.path.join(os.getcwd(), 'output','2019-05-23', 'authors')
    print("Start convert author info in {}".format(dir_path))
    output = os.path.join(dir_path,"author_data.csv")
    for dirpath, dirnames, filenames in os.walk(dir_path):
        convert(filenames, dir_path, output)
    print("Finish convert author info in {}".format(output))