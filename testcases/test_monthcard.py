# !/usr/bin/env python3.8
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: test_monthcard.py
# @Author:hejunrong
# @Time: 2023/9/26

import pytest
import settings
from page_objects.base_page import AppBasePage
from common.base_case import BaseCase
from page_objects.navigation_page import NavigationPage
from page_objects.monthcard_page import MonthCardPage
from page_objects.My_page import MyPage
from page_objects.settings_page import SettingsPage
from page_objects.login_page import LoginPage


class TestMonthcard(BaseCase):
    name = "月卡功能"

    # 执行需要后台发送1张月卡1天
    @pytest.mark.run(order=23)
    @pytest.mark.success
    @pytest.mark.mon
    def test_rule(self, to_monthcard_page):
        self.logger.info('================ {} 开始测试================')
        # 1、打开月卡页面
        mcp = MonthCardPage(to_monthcard_page)
        mcp.delay(1)
        # 2、查看月卡规则页面
        text = mcp.monthcard_rule()
        # 3、断言
        try:
            assert text == '联系客服'
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            self.logger.info('================ {} 测试结束================')

    @pytest.mark.run(order=24)
    @pytest.mark.success
    @pytest.mark.mon
    def test_exclusive(self, to_monthcard_page):
        self.logger.info('================ {} 开始测试================')
        # 1、打开月卡页面
        mcp = MonthCardPage(to_monthcard_page)
        # 2、查看月卡用户兑换规则
        text = mcp.exclusive()
        # 3、断言
        try:
            assert text == '我知道了'
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            # 返回首页
            ab = AppBasePage(to_monthcard_page)
            ab.return_home()
            # 切换账号
            np = NavigationPage(to_monthcard_page)
            np.switch_navigation('我的')
            mp = MyPage(to_monthcard_page)
            mp.enter_settings_page()
            sp = SettingsPage(to_monthcard_page)
            sp.logout()
            mp.delay(1)
            mp.enter_login_page()
            lp = LoginPage(to_monthcard_page)
            lp.login(**settings.TEST_USER)
            mp.enter_monthcard_page()
            self.logger.info('================ {} 测试结束================')

    @pytest.mark.run(order=25)
    @pytest.mark.success
    @pytest.mark.mon
    def test_unsuited(self, to_monthcard_page):
        self.logger.info('================ {} 开始测试================')
        # 1、打开月卡页面
        mcp = MonthCardPage(to_monthcard_page)
        # 2、查看普通用户不适用游戏
        text = mcp.unsuited()
        # 3、断言
        try:
            assert text == '我知道了'
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            # 返回首页
            ab = AppBasePage(to_monthcard_page)
            ab.return_home()
            # 切换账号
            np = NavigationPage(to_monthcard_page)
            np.switch_navigation('我的')
            mp = MyPage(to_monthcard_page)
            mp.enter_settings_page()
            sp = SettingsPage(to_monthcard_page)
            sp.logout()
            mp.delay(1)
            mp.enter_login_page()
            lp = LoginPage(to_monthcard_page)
            lp.login(**settings.TEST_USER2)
            mp.enter_monthcard_page()
            self.logger.info('================ {} 测试结束================')
