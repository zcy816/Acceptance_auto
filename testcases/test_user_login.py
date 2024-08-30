# !/usr/bin/env python3.8
# encoding: utf-8
# Time:2023/8/16 17:48
# Author:xiaobin
# File:test_user_login.py
# Software:PyCharm

import pytest
import settings
from common.base_case import BaseCase
from page_objects.login_page import LoginPage
from page_objects.My_page import MyPage
from common.excel_handler import ExcelHandle
from page_objects.settings_page import SettingsPage

F1_cases = ExcelHandle().read_data(settings.TEST_DATA_FILE, 'user_fail_cases1')
F2_cases = ExcelHandle().read_data(settings.TEST_DATA_FILE, 'user_fail_cases2')
T1_cases = ExcelHandle().read_data(settings.TEST_DATA_FILE, 'user_success_cases1')
T2_cases = ExcelHandle().read_data(settings.TEST_DATA_FILE, 'user_success_cases2')


class TestUserLogin(BaseCase):
    name = '账号密码登录'

    @pytest.mark.run(order=1)
    @pytest.mark.fail
    @pytest.mark.login
    @pytest.mark.parametrize('case', F1_cases)
    def test_user_f1(self, case, to_login_page):
        self.logger.info('================ {} 开始测试================'.format(self.name))
        # 1、登录
        lg = LoginPage(to_login_page)
        lg.login(**eval(case['request_data']))
        # 2、断言
        try:
            assert case['error_msg'] in lg.get_toast_msg()
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            self.logger.info('================ {} 测试结束================'.format(self.name))

    @pytest.mark.run(order=2)
    @pytest.mark.success
    @pytest.mark.login
    @pytest.mark.parametrize('case', T1_cases)
    def test_user_p1(self, case, to_login_page):
        self.logger.info('================ {} 开始测试================'.format(self.name))
        # 1、登录
        lg = LoginPage(to_login_page)
        lg.login(**eval(case['request_data']))
        mp = MyPage(to_login_page)
        # 2、断言昵称是否一致
        try:
            assert case['nick_name'] == mp.get_nick_name()
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            # 退出登录，重新回到账号密码输入页面
            mp.enter_settings_page()
            sp = SettingsPage(to_login_page)
            sp.logout()
            mp.enter_login_page()
            self.logger.info('================ {} 测试结束================'.format(self.name))

    @pytest.mark.run(order=3)
    @pytest.mark.fail
    @pytest.mark.login
    @pytest.mark.parametrize('case', F2_cases)
    def test_user_f2(self, case, to_login_page):
        self.logger.info('================ {} 开始测试================'.format(self.name))
        # 1、登录
        lg = LoginPage(to_login_page)
        lg.login(**eval(case['request_data']))
        # 2、断言
        try:
            assert case['error_msg'] in lg.get_toast_msg()
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            self.logger.info('================ {} 测试结束================'.format(self.name))

    @pytest.mark.run(order=4)
    @pytest.mark.success
    @pytest.mark.login
    @pytest.mark.parametrize('case', T2_cases)
    def test_user_p2(self, case, to_login_page):
        self.logger.info('================ {} 开始测试================'.format(self.name))
        # 1、登录
        lg = LoginPage(to_login_page)
        lg.login(**eval(case['request_data']))
        mp = MyPage(to_login_page)
        # 2、断言昵称是否一致
        try:
            assert case['nick_name'] == mp.get_nick_name()
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            self.logger.info('================ {} 测试结束================'.format(self.name))
