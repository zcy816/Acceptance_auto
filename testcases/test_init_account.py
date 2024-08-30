# !/usr/bin/env python3.8
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: test_init_account.py
# @Author:hejunrong
# @Time : 2023/11/6 20:13

import pytest
from common.base_case import BaseCase
from page_objects.init_account_page import InitAccountPage


class TestInitAccount(BaseCase):
    name = "开局号"

    @pytest.mark.run(order=29)
    @pytest.mark.init
    def test_switch_district(self, to_init_page):
        self.logger.info('================ {} 开始测试================')
        # 1、进入开局号列表
        iap = InitAccountPage(to_init_page)
        # 2、游戏区服筛选
        text1, text2 = iap.switch_district("Q247")
        # 3、断言
        try:
            assert text1 != text2
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            self.logger.info('================ {} 测试结束================')

    @pytest.mark.run(order=30)
    @pytest.mark.init
    def test_switch_role(self, to_init_page):
        self.logger.info('================ {} 开始测试================')
        # 1、进入开局号列表
        iap = InitAccountPage(to_init_page)
        # 2、角色分类筛选
        text1, text2 = iap.switch_role("龙姬")
        # 3、断言
        try:
            assert text1 != text2
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            self.logger.info('================ {} 测试结束================')

    @pytest.mark.run(order=31)
    @pytest.mark.init
    def test_rule_description(self, to_init_page):
        self.logger.info('================ {} 开始测试================')
        # 1、进入开局号列表
        iap = InitAccountPage(to_init_page)
        # 2、查看规则说明
        text = iap.rule_description()
        # 3、断言
        try:
            assert text == "未成年用户无法获取开局号。  "
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            self.logger.info('================ {} 测试结束================')

    @pytest.mark.run(order=32)
    @pytest.mark.init
    def test_list_remind(self, to_init_page):
        self.logger.info('================ {} 开始测试================')
        # 1、进入开局号列表
        iap = InitAccountPage(to_init_page)
        # 2、添加上架提醒
        text = iap.list_remind("Q248", "任意角色")
        # 3、断言
        try:
            assert text == "新服开服时，对老区服设置的提醒将不再生效"
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            self.logger.info('================ {} 测试结束================')

    @pytest.mark.run(order=33)
    @pytest.mark.init
    def test_delete_remind(self, to_init_page):
        self.logger.info('================ {} 开始测试================')
        # 1、进入开局号列表
        iap = InitAccountPage(to_init_page)
        # 2、删除上架提醒
        text = iap.delete_remind()
        # 3、断言
        try:
            assert text == "您还没有添加上架提醒"
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            self.logger.info('================ {} 测试结束================')
