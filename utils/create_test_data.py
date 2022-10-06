#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/31 
# @Author  : Mik

# from faker import Faker
#
# class Testdata():
#     def __init__(self):
#         self.fake_cn = Faker("zh_CN")
#         self.fake_us = Faker('en_US')
#
#     def name(self):
#         name = self.fake_cn.name()
#         name1 = self.fake_us.name()
#         print(name,name1)
#
#
#
#
#
# tmp = Testdata()
# tmp.name()


import random


def createUserPassword():
    """
    自定义生成用户名和密码
    :return: 用户名和密码，元组类型
    """
    usableName_char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"  # 可作为用户名的字符
    usablePassword_char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"  # 可作为密码的字符，根据所需可适当增减
    usableName_char1 = '1234567890'
    e_userName = []
    e2_userName = []  # 定义一个临时List变量,使用list.append添加字符
    e_userPassword = []
    #在数据池随机生成用户名和密码
    for i in range(random.randint(1, 6)):
        e_userName.append(random.choice(usableName_char))
        e2_userName.append(random.choice(usableName_char1))
    for j in range(6):
        e_userPassword.append(random.choice(usablePassword_char))
    e_userName = e_userName + ['_'] + e2_userName
    # print("e_userName = ", e_userName)  # 输出用户名字符list
    # print("e_userPassword = ", e_userPassword)  # 输出密码字符list
    #将数据列表转化为字符串
    userName = ''.join(e_userName)
    userPassword = ''.join(e_userPassword)
    return userName, userPassword
