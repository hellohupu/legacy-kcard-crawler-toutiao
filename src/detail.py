#!/usr/bin/python
#-*- coding: utf-8 -*-
import os
from convert2csv import author_ids_from_file
from base import APISpiderTask, SpiderFetcher

class AuthorDetailFetcher(SpiderFetcher):
    def task_generator(self):
        for page in range(self.page_start, self.page_end + 1):
            ids = author_ids_from_file(str(page), self.dir_path)
            for author_id in ids:
                outputfn = os.path.join(self.output_dir(), "authors",'{}.json'.format(author_id))
                yield APISpiderTask(self.headers, outputfn, url_pattern=self.url_pattern, params=[author_id, False])

url_pattern = "https://star.toutiao.com/v/api/user/author_page/?author_id={}&recommend={}&platform_source=1"
fetcher = AuthorDetailFetcher(url_pattern)