# !/usr/bin/env python3.8
# encoding: utf-8
# Time:2023/8/15 16:27
# Author:xiaobin
# File:navigation_page.py
# Software:PyCharm

from appium.webdriver.common.mobileby import MobileBy
from page_objects.base_page import AppBasePage


class NavigationPage(AppBasePage):
    name = '导航栏'

    # 游戏按钮
    game_loc = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="com.smwl.x7market:id/tab_name_tv" and @text="游戏"]')

    # 群聊按钮
    group_loc = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="com.smwl.x7market:id/tab_name_tv" and @text="群聊"]')

    # 回收按钮
    recovery_loc = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="com.smwl.x7market:id/tab_name_tv" and @text="回收"]')

    # 我的按钮
    my_loc = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="com.smwl.x7market:id/tab_name_tv" and @text="我的"]')

    # 我知道了
    know_btn_loc = (MobileBy.XPATH, '//android.widget.TextView[@text="我知道了"]')

    def switch_navigation(self, nav_name):
        """
        切换到名字为nav_name的页面
        :param nav_name:
        :return:
        """
        if nav_name == '游戏':
            self.wait_element_is_visible(self.game_loc, '导航到游戏').click()
        elif nav_name == '群聊':
            self.wait_element_is_visible(self.group_loc, '导航到群聊').click()
        elif nav_name == '回收':
            self.wait_element_is_visible(self.recovery_loc, '导航到回收').click()
            if self.wait(MobileBy.XPATH, '//android.widget.TextView[@text="小7温馨提示"]'):
                self.wait_element_is_visible(self.know_btn_loc, '我知道了').click()
                self.logger.info('首次回收提醒弹窗正常')
        elif nav_name == '我的':
            self.wait_element_is_visible(self.my_loc, '导航到我的').click()
        else:
            raise ValueError('没有这个菜单')
