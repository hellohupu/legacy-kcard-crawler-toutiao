import json
import os
import sys 
sys.path.append('/Users/GYB/code/puppeteer-spider')
from api import BaseClient, ItemInputTransformer

Fields = [
"comment",
"status",
"play",
"like",
"url",
"original_status",
"video_id",
"share",
"item_title",
"create_time",
"head_image_uri",
"item_id",
"core_user_id",
]

class ItemInfo(object):
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
            r_data = json.load(f)
            data = json.loads(json.dumps(r_data.get('data'),ensure_ascii=False))
            author = os.path.splitext(filename)[0].split('/')[-1]
            results = []
            for item in data.get('ltm_item_statics'):
                info = json.loads(json.dumps(item,ensure_ascii=False), object_hook=ItemInfo)
                info.author = author
                results.append(info)
            return results

class Convertor2ItemInput(Convertor):

    def convert(self, filenames, dirpath, output):
        self.results = []
        for items in self.iter_objects(filenames, dirpath, output):
            for item in items:
                self.results.append(self.convert2Dict(item))
                if len(self.results) >= 5:
                    BaseClient().update_itemsinfo(self.results)
                    self.results.clear()
                
            
    def convert2Dict(self, item_info):
        ts = ItemInputTransformer(item_info)
        ts.transform()
        return ts.to_dict()


if __name__ == '__main__':
    dir_path = os.path.abspath(os.path.join("/Users/GYB/code/puppeteer-spider","output","2019-05-23", "items_detail"))
    output = os.path.join(dir_path,"item_data.csv")
    print("Start convert author info in {}".format(dir_path))
    for dirpath, dirnames, filenames in os.walk(dir_path):
        Convertor2ItemInput().convert(filenames, dir_path, output)    
    print("Finish convert author info in {}".format(output))
