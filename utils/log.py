# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :log
# @Time      :2022/8/11 11:14
# @Author    :user
import datetime
import os
import sys

from loguru import logger

from common.parse_yaml import parse_yaml
from config.config import base_path


class MyLogger:
    # 文件名称，按天创建
    DATE = datetime.datetime.now().strftime('%Y-%m-%d')

    # 项目路径下创建log目录保存日志文件
    log_path = base_path + parse_yaml("wms.path.logs", 'config/data.yaml')
    filename_info = log_path + "wms_info" + DATE + '.log'
    filename_error = log_path + "wms_error" + DATE + '.log'
    # 判断目录是否存在，不存在则创建新的目录
    logpath = os.path.join(os.path.dirname(os.getcwd()), "logs")
    if not os.path.isdir(logpath):
        os.makedirs(logpath)

    def __init__(self):
        self.logger = logger
        # 清空所有设置
        self.logger.remove()
        # 添加控制台输出的格式,sys.stdout为输出到屏幕;关于这些配置还需要自定义请移步官网查看相关参数说明
        self.logger.add(sys.stdout,
                        format="<green>{time:YYYYMMDD HH:mm:ss}</green> | "  # 颜色>时间
                               "{process.name} | "  # 进程名
                               "{thread.name} | "  # 进程名
                               "<cyan>{module}</cyan>.<cyan>{function}</cyan>"  # 模块名.方法名
                               ":<cyan>{line}</cyan> | "  # 行号
                               "<level>{level}</level>: "  # 等级
                               "<level>{message}</level>",  # 日志内容
                        )
        # 输出到文件的格式,注释下面的add',则关闭日志写入
        self.logger.add(self.filename_info, level='INFO',
                        format='{time:YYYYMMDD HH:mm:ss} - '  # 时间
                               "{process.name} | "  # 进程名
                               "{thread.name} | "  # 进程名
                               '{module}.{function}:{line} - {level} -{message}',  # 模块名.方法名:行号
                        rotation="10 MB")
        self.logger.add(self.filename_error, level='ERROR',
                        format='{time:YYYYMMDD HH:mm:ss} - '  # 时间
                               "{process.name} | "  # 进程名
                               "{thread.name} | "  # 进程名
                               '{module}.{function}:{line} - {level} -{message}',  # 模块名.方法名:行号
                        rotation="10 MB")

    def get_logger(self):
        return self.logger


logger = MyLogger().get_logger()

# if __name__ == '__main__':
#     logger.info('woshi info')
#     logger.error('woshi error')
