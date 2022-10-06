#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/7/5 
# @Author  : Mik
import os
from configparser import ConfigParser
from libs.utils.log import logger
from libs.utils.base_path import root_dir


class MyConfigParser(ConfigParser):
    # 重写 configparser 中的 optionxform 函数，解决 .ini 文件中的 键option 自动转为小写的问题
    def __init__(self, defaults=None):
        ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionstr):
        return optionstr


def load_ini(section, file_path=root_dir + r'\config\appcfg.ini'):
    """
    读取ini文件并返回字典数据
    :param section: 标签名
    :param file_path: 路径
    :return: 字典
    """
    file_path = file_path.replace(r'\/'.replace(os.sep, ''), os.sep)
    logger.info("加载 {} 文件......".format(file_path))
    config = MyConfigParser()
    config.read(file_path, encoding="UTF-8")
    load_data = dict(config.items(section))
    return load_data

# t=load_ini('desired')
