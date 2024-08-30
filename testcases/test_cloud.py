# !/usr/bin/env python3.8
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: test_cloud_page.py
# @Author:hejunrong
# @Time : 2023/11/9 19:42

import pytest
import settings
from page_objects.base_page import AppBasePage
from common.base_case import BaseCase
from page_objects.cloud_page import CloudPage
from common.excel_handler import ExcelHandle

S_data = ExcelHandle().read_data(settings.TEST_DATA_FILE, 'cloudonhook_success_data')
F_data = ExcelHandle().read_data(settings.TEST_DATA_FILE, 'cloudonhook_fail_data')


class TestCloudPage(BaseCase):
    name = "云挂机"

    # 执行需要后台发放1台云挂机设备
    @pytest.mark.run(order=56)
    @pytest.mark.fail
    @pytest.mark.cloud
    @pytest.mark.parametrize('data', F_data)
    def test_firing_unsupport(self, data, to_onhook_page):
        self.logger.info('================ {} 开始测试================')
        # 1、进入云挂机卡片页
        coh = CloudPage(to_onhook_page)
        # 2、搜索云挂机游戏
        coh.search_onhook(**eval(data['request_data']))
        # 3、闲置中启动不支持云挂机的游戏
        coh.firing_unsupport()
        # 4、断言
        try:
            assert coh.get_toast_msg() == '当前游戏暂时不支持云挂机'
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            self.logger.info('================ {} 测试结束================')

    @pytest.mark.run(order=57)
    @pytest.mark.success
    @pytest.mark.cloud
    @pytest.mark.parametrize('data', S_data)
    def test_firing_support(self, data, to_onhook_page):
        self.logger.info('================ {} 开始测试================')
        # 1、进入云挂机卡片页
        coh = CloudPage(to_onhook_page)
        # 2、搜索云挂机游戏
        coh.search_onhook(**eval(data['request_data']))
        # 3、启动未挂机的游戏
        coh.firing_support()
        # 4、返回云挂机卡片
        text = coh.back_to_onhook()
        # 5、断言
        try:
            assert text == '挂机中'
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            self.logger.info('================ {} 测试结束================')

    @pytest.mark.run(order=58)
    @pytest.mark.cloud
    def test_firing_onhook(self, to_onhook_page):
        self.logger.info('================ {} 开始测试================')
        # 1、进入云挂机卡片页
        coh = CloudPage(to_onhook_page)
        # 2、挂机中启动云挂机游戏
        coh.firing_onhook()
        # 3、返回云挂机卡片
        text = coh.back_to_onhook()
        # 4、断言
        try:
            assert text == '挂机中'
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            self.logger.info('================ {} 测试结束================')

    @pytest.mark.run(order=59)
    @pytest.mark.cloud
    def test_exit_onhook(self, to_onhook_page):
        self.logger.info('================ {} 开始测试================')
        # 1、进入云挂机卡片页
        coh = CloudPage(to_onhook_page)
        # 2、退出云挂机中的游戏
        coh.exit_onhook()
        # 3、断言
        try:
            assert coh.get_toast_msg() == '已成功退出挂机'
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            self.logger.info('================ {} 测试结束================')
