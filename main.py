# !/usr/bin/env python3.8
# encoding: utf-8
# Time:2023/8/24 18:47
# Author:xiaobin
# File:main.py
# Software:PyCharm

import os
import time


if __name__ == '__main__':
    # 时间戳为文件夹命名
    name = time.strftime('%Y%m%d')
    reportName = time.strftime('%H%M%S')
    # 生成allure的json文件
    os.system('pytest -vs -q --alluredir ./result/allure/{}/{}'.format(name, reportName))
    # 生成测试报告
    os.system('allure generate ./result/allure/{}/{} -o ./result/report/{}/{}'.format(
        name, reportName, name, reportName
    ))
    # pytest.main([
    #         '--report=_reports',
    #         '--title=小7手游测试报告',
    #         '--tester=测试人',
    #         '--desc=报告描述信息',
    #         '--template=1'])
