#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/4/11 
# @Author  : Mik


import zmail
import yaml
import os
import time


# def open_yaml():
#     file_dir = os.path.dirname(__file__)
#     path_file = file_dir.replace('libs/utils', 'config/cfg.yaml')
#     print(path_file)
#     with open(path_file, mode='r', encoding='utf-8') as file:
#         msg = yaml.load(file, Loader=yaml.FullLoader)
#         sender = tuple(msg['mail']['sender'])
#         receiver = msg['mail']['receiver']
#         print(receiver,type(receiver))
#
#     return sender,receiver
#         #print(tuple(msg1), type(msg1))  # ['sender'],type(msg['mail']['user']))
#         # print(msg['mail']['password'])
#
#
# data=open_yaml()
# print(data[0],data[1],type(data[0]),type(data[1]))


# import zmail
# # 发件人：发件人账号，密码(授权码) dzpqnpfrbgnndjeg
# sender=('1457139077@qq.com','jmhzkervwxedbafb')
# # 收件人
# receiver=['751212216@qq.com','e751212216@163.com']  #元组只有一个值,一定要加上逗号
# # 邮件内容：主题/正文
# msg={
#     'subject':'邮件主题：测试zmail发送邮件是否成功',
#     'content_text':'邮件正文：zmail发送邮件比smtp发送邮件简单'
# }
# # 发送邮件
# # 1：创建zmail发送邮件的服务
# # email_server=zmail.server(sender[0],sender[1])  #username: str, password: str
# email_server=zmail.server(*sender) # * 解包
# # 2:发送邮件
# email_server.send_mail(receiver,msg)
# import datetime
# import time
#
# now_time = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M')
# print(now_time)

# from selenium import webdriver
#
# driver=webdriver.Chrome()
# driver.get('http://www.baidu.com')

# print(type(time.time()),time.time())
#
# try:
#     print(1221)
#
# except Exception as e:
#     raise e
# else:
#     print(2323)
# from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from libs.utils import log_module
# driver = webdriver.Chrome()
# driver.get('http://www.baidu.com')
#
# l = log_module.Logger()
# log = l.get_log(file='web')
# try:
#     log.info('开始等待页面元素<{}>是否可见！'.format("loc"))
#     start_time = time.time()
#     ele = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'kw')))
#
# except Exception as e:
#     #
#     raise e
#
# else:
#     end_time = time.time()
#     log.info('页面元素<{}>等待可见，等待时间：{}秒'.format('loc', round(end_time - start_time, 1)))
#     print('执行时间',round(end_time - start_time, 1))
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# #
# driver = webdriver.Chrome()
# driver.get('http://127.0.0.1')
# driver.find_element(By.LINK_TEXT, '注册').click()
#
# ww=driver.window_handles
# print(ww)

# driver.find_element(By.NAME, 'username').send_keys("123")
# driver.find_element(By.NAME, 'password').send_keys("123")
# driver.find_element(By.NAME, 'userpassword2').send_keys("123")
# driver.find_element(By.NAME, 'mobile_phone').send_keys("123")
# driver.find_element(By.NAME, 'email').send_keys("123")


# a= 1
#
# print(f'我是{a}')


# a = {'a': 123}
# b = {'a': 123}
#
# print(id(a), id(b))

# import pytest
#
# from libs.utils.log_module import log
# class TestZc():
#     # def setup_class(self):
#     #     log.info(f'开始执行{self.__class__.__name__}测试')
#     #
#     # def teardown_class(self):
#     #     log.info(f'{self.__class__.__name__}测试完成')
#
#     def test(self):
#         print(f'开始执行{self.__class__.__name__}测试')
#
#
# a=TestZc()
# a.test()

# for line in range(5):
#
#     for row in range(line+1):
#
#         print('*',end=' ')
#
#     print()

# assert '欢迎' in '1234_迎'
# import os
# from libs.utils.base_path import root_dir
# dir = root_dir + r'\imgs\.'
# os.remove(dir)

# try:
#     assert 1==2
#
# except Exception as e:
#     raise e

#
# assert 1==2


# print(os.path.basename(__file__))


# import platform
# cur_sysinfo=platform.uname()
# print(cur_sysinfo)
# print(cur_sysinfo.system,cur_sysinfo.machine)


# try:
#     print(123+'asd')
#
# except:
#     raise


class A:
    loc = {}

    def __init__(self):
        pass

    def __getattr__(self, loc):
        if loc not in self.loc.keys():
            raise Exception

        by, val = self.loc[loc]
        return by, val


class B(A):
    loc = {
        'username': ('id', 'account')
    }

    def text(self):
        a = self.username
        print(a)


cl = B()
cl.text()