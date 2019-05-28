#!/usr/bin/python
#-*- coding: utf-8 -*-
import os
from convert2csv import author_ids_from_file
from base import APISpiderTask, SpiderFetcher

class AuthorItemInfoFetcher(SpiderFetcher):

    def output_dir(self):
        return os.path.join(self.dir_path, "items")

    def task_generator(self):
        for page in range(self.page_start, self.page_end + 1):
            ids = author_ids_from_file(str(page), self.dir_path)
            for author_id in ids:
                outputfn = os.path.join(self.output_dir(), '{}.json'.format(author_id))
                yield APISpiderTask(self.headers, outputfn, url_pattern=self.url_pattern, params=[author_id])

url_pattern = "https://star.toutiao.com/v/api/demand/author_item_info/?author_id={}&platform_source=1"
item_fetcher = AuthorItemInfoFetcher(url_pattern)

class AuthorItemDetailFetcher(SpiderFetcher):

    def output_dir(self):
        return os.path.join(self.dir_path, "items_detail")

    def task_generator(self):
        for page in range(self.page_start, self.page_end + 1):
            ids = author_ids_from_file(str(page), self.dir_path)
            for author_id in ids:
                outputfn = os.path.join(self.output_dir(), '{}.json'.format(author_id))
                yield APISpiderTask(self.headers, outputfn, url_pattern=self.url_pattern, params=[author_id, 50])

detail_url_pattern = "https://star.toutiao.com/v/api/demand/author_item_data/?author_id={}&platform_source=1&item_cnt={}"
item_detail_fetcher = AuthorItemDetailFetcher(detail_url_pattern)