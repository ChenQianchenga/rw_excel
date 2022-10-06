# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :parse_yaml
# @Time      :2022/8/10 15:07
# @Author    :user
import yaml

from config.config import base_path


# 根据对应的key读取对应的value
def parse_yaml(key, filepath='config/data.yaml'):
    filename = base_path + filepath
    with open(filename, "r", encoding="utf-8") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        keys = key.split('.')
        for k in keys:
            data = data[k]
        return data


if __name__ == '__main__':
    value = parse_yaml("wms.url.dept.delete", 'config/data.yaml')
    print(value)
