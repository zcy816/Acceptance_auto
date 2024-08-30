# !/usr/bin/env python3.8
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: test_home.py
# @Author:hejunrong
# @Time : 2023/11/6 20:14

import pytest
from common.base_case import BaseCase
from page_objects.home_page import HomePage


class TestHome(BaseCase):
    name = "个人主页"

    @pytest.mark.run(order=9)
    @pytest.mark.success
    @pytest.mark.home
    def test_personal_release(self, to_home_page):
        self.logger.info('================ {} 开始测试================')
        # 1、进入个人主页
        hp = HomePage(to_home_page)
        # 2、发布的
        hp.personal_release()
        # 3、断言
        try:
            assert hp.check_content() == True
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            self.logger.info('================ {} 测试结束================')

    @pytest.mark.run(order=10)
    @pytest.mark.success
    @pytest.mark.home
    def test_personal_like(self, to_home_page):
        self.logger.info('================ {} 开始测试================')
        # 1、进入个人主页
        hp = HomePage(to_home_page)
        # 2、点赞的
        hp.personal_like()
        # 3、断言
        try:
            assert hp.check_content() == True
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            self.logger.info('================ {} 测试结束================')

    @pytest.mark.run(order=11)
    @pytest.mark.success
    @pytest.mark.home
    def test_personal_reply(self, to_home_page):
        self.logger.info('================ {} 开始测试================')
        # 1、进入个人主页
        hp = HomePage(to_home_page)
        # 2、回复的
        hp.personal_reply()
        # 3、断言
        try:
            assert hp.check_content() == True
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            self.logger.info('================ {} 测试结束================')

    @pytest.mark.run(order=12)
    @pytest.mark.success
    @pytest.mark.home
    def test_personal_played(self, to_home_page):
        self.logger.info('================ {} 开始测试================')
        # 1、进入个人主页
        hp = HomePage(to_home_page)
        # 2、玩过的
        hp.personal_played()
        # 3、断言
        try:
            assert hp.check_palyed() == True
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            self.logger.info('================ {} 测试结束================')
