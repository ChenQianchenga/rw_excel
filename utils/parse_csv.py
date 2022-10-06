# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :parse_csv
# @Time      :2022/9/15 10:51
# @Author    :user
import csv
import json


class CsvUtil:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_csv_data(self):
        with open(file=self.file_path, mode='r', encoding='utf-8-sig') as f:
            read = list(csv.reader(f))
            dict_list = []
            for i in range(1, len(read)):
                d = {}
                data = read[i]
                keys = read[0]
                for j in range(len(keys)):
                    d[keys[j]] = data[j]
                dict_list.append(d)
            return dict_list


if __name__ == '__main__':
    with open(file='../data/webdata.csv', mode='r', encoding='utf-8-sig') as f:
        read = list(csv.reader(f))
        print(read)