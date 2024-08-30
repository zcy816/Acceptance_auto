# !/usr/bin/env python3.8
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: test_voucher.py
# @Author:hejunrong
# @Time : 2023/11/6 20:15

import pytest
from common.base_case import BaseCase
from page_objects.base_page import AppBasePage
from page_objects.voucher_page import VoucherPage


class TestVoucher(BaseCase):
    name = "代金券页面"

    @pytest.mark.run(order=16)
    @pytest.mark.vou
    def test_had_used(self, to_vouchers_page):
        self.logger.info('================ {} 开始测试================')
        # 1、进入代金券页面
        vp = VoucherPage(to_vouchers_page)
        # 2、查看已使用代金券
        vp.had_used()
        # 3、断言
        try:
            assert vp.check_vourchar() == True
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            self.logger.info('================ {} 测试结束================')

    @pytest.mark.run(order=17)
    @pytest.mark.vou
    def test_had_expired(self, to_vouchers_page):
        self.logger.info('================ {} 开始测试================')
        # 1、进入代金券页面
        vp = VoucherPage(to_vouchers_page)
        # 2、查看已过期代金券
        vp.had_expired()
        # 3、断言
        try:
            assert vp.check_vourchar() == True
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            self.logger.info('================ {} 测试结束================')

    @pytest.mark.run(order=18)
    @pytest.mark.vou
    def test_not_used(self, to_vouchers_page):
        self.logger.info('================ {} 开始测试================')
        # 1、进入代金券页面
        vp = VoucherPage(to_vouchers_page)
        # 2、查看待使用代金券
        vp.not_used()
        # 3、断言
        try:
            assert vp.check_vourchar() == True
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            # 返回首页
            ab = AppBasePage(to_vouchers_page)
            ab.return_home()
            self.logger.info('================ {} 测试结束================')

    @pytest.mark.run(order=19)
    @pytest.mark.vou
    def test_had_used2(self, to_vouchers_page2):
        self.logger.info('================ {} 开始测试================')
        # 1、进入月卡代金券页面
        vp = VoucherPage(to_vouchers_page2)
        # 2、查看已使用的代金券
        vp.had_used()
        # 3、断言
        try:
            assert vp.check_vourchar() == True
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            self.logger.info('================ {} 测试结束================')

    @pytest.mark.run(order=20)
    @pytest.mark.vou
    def test_had_expired2(self, to_vouchers_page2):
        self.logger.info('================ {} 开始测试================')
        # 1、进入月卡代金券页面
        vp = VoucherPage(to_vouchers_page2)
        # 2、查看已过期的代金券
        vp.had_expired()
        # 3、断言
        try:
            assert vp.check_vourchar() == True
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            self.logger.info('================ {} 测试结束================')

    @pytest.mark.run(order=21)
    @pytest.mark.vou
    def test_not_used2(self, to_vouchers_page2):
        self.logger.info('================ {} 开始测试================')
        # 1、进入月卡代金券页面
        vp = VoucherPage(to_vouchers_page2)
        # 2、查看待使用的代金券
        vp.not_used()
        # 3、断言
        try:
            assert vp.check_vourchar() == True
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            self.logger.info('================ {} 测试结束================')

    @pytest.mark.run(order=22)
    @pytest.mark.vou
    def test_voucher_rule(self, to_vouchers_page):
        self.logger.info('================ {} 开始测试================')
        # 1、进入代金券页面
        vp = VoucherPage(to_vouchers_page)
        # 2、查看代金券规则
        text = vp.voucher_rule()
        # 3、断言
        try:
            assert text == '我知道了'
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            self.logger.info('================ {} 测试结束================')
