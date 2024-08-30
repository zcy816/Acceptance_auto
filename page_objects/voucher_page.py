# !/usr/bin/env python3.8
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: voucher_page.py
# @Author:hejunrong
# @Time : 2023/11/2 15:44

from common.base_case import BaseCase
from appium.webdriver.common.mobileby import MobileBy
from page_objects.base_page import AppBasePage


class VoucherPage(AppBasePage, BaseCase):
    name = '代金券页面'

    # 代金券
    voucher_title_loc = (MobileBy.ID, "com.smwl.x7market:id/center_title")

    # 代金券规则
    voucherrule_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/imageview_title_right')

    # 我知道了
    know_btn_loc = (MobileBy.XPATH, '//android.widget.TextView[@text="我知道了"]')

    # 待使用
    not_used_loc = (MobileBy.XPATH,'//android.widget.TextView[@text="待使用"]')

    # 已使用
    used_btn_loc = (MobileBy.XPATH, '//android.widget.TextView[@text="已使用"]')

    # 已过期
    expired_btn_loc = (MobileBy.XPATH, '//android.widget.TextView[@text="已过期"]')

    def voucher_rule(self):
        """
        代金券规则
        :return:
        """
        self.wait_element_is_visible(self.voucherrule_btn_loc, '代金券规则').click()
        if self.wait(MobileBy.XPATH, '//android.widget.TextView[@text="小7温馨提示"]'):
            text = self.wait_element_is_visible(self.know_btn_loc, '获取控件文本').get_text()
            self.logger.info('代金券规则弹窗正常')
            return text
        else:
            self.get_page_screenshot()
            self.logger.info('代金券规则弹窗异常')

    def not_used(self):
        """
        待使用的代金券
        :return:
        """
        self.wait_element_is_visible(self.not_used_loc,'待使用').click()

    def had_used(self):
        """
        已使用的代金券
        :return:
        """
        self.wait_element_is_visible(self.used_btn_loc,'已使用').click()

    def had_expired(self):
        """
        已使用的代金券
        :return:
        """
        self.wait_element_is_visible(self.expired_btn_loc,'已使用').click()

    def check_vourchar(self):
        """
        检查代金券内容是否展示
        :return:
        """
        if self.wait(MobileBy.ID,'com.smwl.x7market:id/voucher_empty_iv') or self.wait(MobileBy.ID,'com.smwl.x7market:id/item_moneyticket_all_ll'):
            return True
        else:
            return False
