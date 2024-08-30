# !/usr/bin/env python3.8
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: home_page.py
# @Author:hejunrong
# @Time : 2023/11/2 15:35

from common.base_case import BaseCase
from appium.webdriver.common.mobileby import MobileBy
from page_objects.base_page import AppBasePage


class HomePage(AppBasePage, BaseCase):
    name = '个人主页'

    # 玩过的
    played_columns_loc = (MobileBy.XPATH, '//android.widget.TextView[@text="玩过的"]')

    # 发布的
    release_columns_loc = (MobileBy.XPATH, '//android.widget.TextView[@text="发布的"]')

    # 点赞的
    like_columns_loc = (MobileBy.XPATH, '//android.widget.TextView[@text="点赞的"]')

    # 回复的
    reply_columns_loc = (MobileBy.XPATH, '//android.widget.TextView[@text="回复的"]')

    # 时长切换
    duration_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/user_center_duration_range_tv')

    # 个人主页
    personal_homepage = (MobileBy.ID, 'com.smwl.x7market:id/user_login_arrow_iv')

    # 社区
    community_loc = (MobileBy.XPATH, '//android.widget.TextView[@text="社区999+"]')

    def personal_played(self):
        """
        玩过的
        :return:
        """
        self.wait_element_is_visible(self.played_columns_loc,'玩过的').click()
        self.wait_element_is_visible(self.duration_btn_loc,'切换总时长').click()
        self.delay(1)

    def personal_release(self):
        """
        发布的
        :return:
        """
        self.wait_element_is_visible(self.release_columns_loc,'发布的').click()
        self.delay(1)

    def personal_like(self):
        """
        点赞的
        :return:
        """
        self.wait_element_is_visible(self.like_columns_loc,'点赞的').click()
        self.delay(1)

    def personal_reply(self):
        """
        回复的
        :return:
        """
        self.wait_element_is_visible(self.reply_columns_loc,'回复的').click()
        self.delay(1)

    def enter_community_page(self, gamename):
        """
        进入社区页
        @param gamename:
        :return:
        """
        self.wait_element_is_visible(self.personal_homepage, '个人主页').click()
        self.wait_element_is_visible(self.release_columns_loc, '发布的').click()
        self.delay(1)
        action = '进入[{}]游戏详情页'.format(gamename)
        loc = (MobileBy.XPATH, '//android.widget.TextView[@text="{}"]'.format(gamename))
        self.scroll_to_capture_element(gamename)
        self.wait_element_is_visible(loc, action).click()
        self.wait_element_is_visible(self.community_loc, '进入社区').click()

    def check_content(self):
        """
        检查第一条内容是否展示
        :return:
        """
        if self.wait(MobileBy.XPATH,'//android.widget.RelativeLayout[@resource-id="com.smwl.x7market:id/root_layout"]') or self.wait(MobileBy.ID, 'com.smwl.x7market:id/common_no_data_bg_iv'):
            return True
        else:
            return False

    def check_palyed(self):
        """
        检查玩过的是否展示
        :return:
        """
        if self.wait(MobileBy.XPATH,'//android.view.ViewGroup[@resource-id="com.smwl.x7market:id/mine_bottom_item_cl"]') or self.wait(MobileBy.ID, 'com.smwl.x7market:id/common_no_data_bg_iv'):
            return True
        else:
            return False
