# !/usr/bin/env python3.8
# encoding: utf-8
# Time:2023/8/6 17:29
# Author:xiaobin
# File:base_case.py
# Software:PyCharm

import settings
from common import logger


class BaseCase:
    """
    测试用例基类
    """
    name = None
    logger = logger
    settings = settings

    @classmethod
    def setup_class(cls):
        cls.logger.info('=========================={}测试开始========================='.format(cls.name))

    @classmethod
    def teardown_class(cls):

        cls.logger.info('=========================={}测试结束========================='.format(cls.name))
