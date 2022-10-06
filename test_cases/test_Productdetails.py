# -*- coding: utf-8 -*-#
# Name:test_Product-details.py
# Description:
# Author:ChenQiancheng
# Date:2022/10/4  21:16
import jsonpath
import pytest
import requests

from utils.log import logger
from utils.rw_xlsx import ReadExcel, WriteExcel

rd_excel = ReadExcel('Sheet1')
datas = rd_excel.get_sheet_data()

write_excel = WriteExcel()
write_excel.write_call('A1', 'name')


class TestProductDetails:
    def setup(self):
        print('在每个用例之前执行')

    def teardown(self):
        print("在每个用例执行之后执行")

    def setup_class(self):
        print('在每个测试类之前执行')

    def teardown_class(self):
        print('在每个测试类之后执行')

    @pytest.mark.parametrize("goods_id", datas)
    def test_goods_01(self, goods_id):
        print(goods_id)
        params = {
            'id': goods_id['id']
        }
        url = "http://127.0.0.1:6688/api/goods/getGoodsDetail"
        headers = {
            'token': 'false'
        }
        rep = requests.get(url=url, headers=headers, params=params)
        check_name = '$.data.name'
        print(jsonpath.jsonpath(rep.json(), check_name))
        name_list = jsonpath.jsonpath(rep.json(), check_name)
        try:
            write_excel.write_row(name_list)
        except:
            logger.info('写入{}失败'.format(name_list))
        finally:
            write_excel.save_book()
            logger.info('表格保存成功！')
