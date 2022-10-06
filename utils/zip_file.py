#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/7/1 
# @Author  : Mik
import zipfile
import os


def zip_file(file_path: str, out_path: str):
    """
    压缩指定文件夹
    :param file_path: 目标文件夹路径
    :param out_path: 压缩文件保存路径+xxxx.zip
    :return: 无
    """
    # file_path = f"{file_path}/html"
    zip = zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED)
    for path, dirnames, filenames in os.walk(file_path):
        # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
        fpath = path.replace(file_path, '')

        for filename in filenames:
            zip.write(
                os.path.join(
                    path, filename), os.path.join(
                    fpath, filename))
    zip.close()
