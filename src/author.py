#!/usr/bin/python
#-*- coding: utf-8 -*-
import os
from base import APISpiderTask, SpiderFetcher, print_f
class AuthorBaseFetcher(SpiderFetcher):

    def output_dir(self):
        return os.path.join(self.output_root, "list")

    def task_generator(self):
        for page in range(self.page_start, self.page_end + 1):
            outputfn = os.path.join(self.output_dir(), '%d.json'%page)
            print_f("fetch page: {}".format(page))
            yield APISpiderTask(self.headers, outputfn, url_pattern=self.url_pattern, params=[page, 20])

list_url_pattern = "https://star.toutiao.com/v/api/demand/author_list/?page={}&limit={}&need_detail=true&platform_source=1&order_by=score"
fetcher = AuthorBaseFetcher(list_url_pattern)
