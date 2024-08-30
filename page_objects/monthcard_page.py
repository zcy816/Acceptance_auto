# !/usr/bin/env python3.8
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: monthcard_page.py
# @Author:hejunrong
# @Time : 2023/9/25

from common.base_case import BaseCase
from appium.webdriver.common.mobileby import MobileBy
from page_objects.base_page import AppBasePage


class MonthCardPage(AppBasePage, BaseCase):
    name = '月卡页面'

    # 我知道了
    know_btn_loc = (MobileBy.XPATH, '//android.widget.TextView[@text="我知道了"]')

    # 联系客服按钮
    service_btn_loc = (MobileBy.XPATH, '//android.view.View[@text="联系客服"]')

    # 规则
    rule_btn_loc = (MobileBy.XPATH, '//android.widget.TextView[@text="规则"]')

    # 返回
    back_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/imageview_title_left')

    # 查看不适用游戏
    unsuited_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/unavailable_game_cl')

    # 0.1折专属券
    arrow_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/arrow_icon_iv')

    def monthcard_rule(self):
        """
        月卡规则页面
        :return:
        """
        self.wait_element_is_visible(self.rule_btn_loc, '月卡规则').click()
        self.delay(1)
        self.swipe_by_direction('up', action='向上滑动', duration=1000, distance=1500)
        text = self.wait_element_is_visible(self.service_btn_loc, '获取控件文本').get_text()
        self.wait_element_is_visible(self.back_btn_loc, '返回').click()
        self.logger.info('月卡规则页面正常')
        return text

    def unsuited(self):
        """
        不适用游戏(普通用户)
        :return:
        """
        self.wait_element_is_visible(self.unsuited_btn_loc, '不适用游戏').click()
        if self.wait(MobileBy.XPATH, "//android.widget.TextView[@text='以下游戏不可用']"):
            text = self.wait_element_is_visible(self.know_btn_loc, '我知道了').get_text()
            self.wait_element_is_visible(self.know_btn_loc, '我知道了').click()
            self.logger.info('存在游戏不可用弹窗')
            return text
        else:
            self.get_page_screenshot()
            self.logger.error('没有游戏不可用弹窗')

    def exclusive(self):
        """
        兑换规则(月卡用户)
        :return:
        """
        try:
            self.delay(2)
            self.wait_element_is_visible(self.arrow_btn_loc, '0.1折游戏专属券').click()
            if self.wait(MobileBy.ID, 'com.smwl.x7market:id/view_details_title_tv'):
                text = self.wait_element_is_visible(self.know_btn_loc, '我知道了').get_text()
                self.wait_element_is_visible(self.know_btn_loc, '我知道了').click()
                self.logger.info('0.1折游戏兑换规则弹窗正常展示')
                return text
            else:
                self.get_page_screenshot()
                self.logger.error('0.1折游戏兑换规则弹窗异常')
        except Exception as e:
            raise e
