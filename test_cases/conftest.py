# -*- coding: utf-8 -*-#
# Name:contest.py
# Description:
# Author:ChenQiancheng
# Date:2022/10/4  21:38
import pytest as pytest

from utils.rw_xlsx import ReadExcel


@pytest.fixture(scope="class")
def db_connect():
    print("连接数据库")
    yield
    print("断开数据库")


@pytest.fixture(scope='function')
def getData():
    rw_excel = ReadExcel('Sheet1')
    return rw_excel.get_sheet_data()
