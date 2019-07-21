#!/usr/bin/python
#-*- coding: utf-8 -*-
import os
from convert2csv import author_ids_from_file
from base import APISpiderTask, SpiderFetcher, print_f

class AuthorDetailFetcher(SpiderFetcher):

    def output_dir(self):
        return os.path.join(self.output_root, "authors")

    def task_generator(self):
        for page in range(self.page_start, self.page_end + 1):
            ids = author_ids_from_file(str(page), os.path.join(self.output_root, "list"))
            for author_id in ids:
                outputfn = os.path.join(self.output_dir(),'{}.json'.format(author_id))
                print_f("fetch page at: {}".format(page))
                yield APISpiderTask(self.headers, outputfn, url_pattern=self.url_pattern, params=[author_id, False])

url_pattern = "https://star.toutiao.com/v/api/user/author_page/?author_id={}&recommend={}&platform_source=1"
fetcher = AuthorDetailFetcher(url_pattern)