# !/usr/bin/env python3.8
# encoding: utf-8
# Time:2023/8/6 17:03
# Author:xiaobin
# File:settings.py
# Software:PyCharm
import os
import datetime

# 项目根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 测试数据路径
TEST_DATA_FILE = os.path.join(BASE_DIR, 'test_data', 'cases.xlsx')
# 测试用例路径
TESTCASE_DIR = os.path.join(BASE_DIR, 'testcases')

# 日志配置
LOG_CONFIG = {
    'name': 'UI 自动化',
    'filename': os.path.join(BASE_DIR, 'logs', '{}.log'.format(datetime.datetime.now().strftime("%Y-%m-%d"))),
    'encoding': 'utf-8',
    'debug': True
}

# 全局默认等待时间
DEFAULT_TIMEOUT = 3

# 错误截图目录
ERROR_SCREENSHOT_DIR = os.path.join(BASE_DIR, 'screenshots')

# APP相关配置
APPIUM_SERVER_HOST = 'http://127.0.0.1:4723/wd/hub'

# desired caps
DESIRED_CAPS = {
    "platformName": "Android",
    # 夜神模拟器
    # "platformVersion": "7.12",
    # "deviceName": "127.0.0.1:62001",
    "platformVersion": "9",
    # 雷电模拟器
    "deviceName": "emulator-5554",
    # 逍遥模拟器
    # "deviceName": "127.0.0.1:21503",
    # 蓝叠模拟器
    # "deviceName": "127.0.0.1:5555",
    # MuMu模拟器
    # "platformVersion": "12",
    # "deviceName": "127.0.0.1:16384",
    "appPackage": "com.smwl.x7market.internation1",
    "appActivity": "com.smwl.x7market.activity.MainActivity",
    "automationName": "Uiautomator2",
    "noReset": True,
    "appium:skipServerInstallation": True,
    "appium:skipDeviceInitialization": True,
    "appium:enableMultiWindows": True
}

# test user
TEST_USER = {
    'username': 'oft326510',
    'password': '123456'
}
TEST_USER2 = {
    'username': 'we123',
    'password': '121212'
}
# test phone
TEST_PHONE = {
    'phone': '15307565939'
}
