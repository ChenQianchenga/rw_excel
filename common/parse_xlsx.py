# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :parse_xlsx
# @Time      :2022/8/10 15:30
# @Author    :user

from openpyxl import load_workbook

# 解析excel表格中的全部数据，返回的数据是一个元组
from config.config import base_path


def parse_xlsx(filename, sheet_name='Sheet1'):
    excel = load_workbook(filename)
    data = []
    # value 是一个元组，从表格第一行开始
    for value in excel[sheet_name].values:
        print(value)
        if value[0] > 1:
            data.append(value[1:])
    excel.close()
    return data


if __name__ == '__main__':
    data = parse_xlsx(base_path + 'data/商品新增测试用例.xlsx')
    print(data)
