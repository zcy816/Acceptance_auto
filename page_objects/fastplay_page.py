# !/usr/bin/env python3.8
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: fastplay_page.py
# @Author:hejunrong
# @Time : 2023/11/6 20:19

from common.base_case import BaseCase
from appium.webdriver.common.mobileby import MobileBy
from page_objects.base_page import AppBasePage


class FastPlayPage(AppBasePage, BaseCase):
    name = '快玩功能'

    # 选择游戏
    select_game_loc = (MobileBy.ID, 'com.smwl.x7market:id/x7_select_game_tv')

    def simulator_fastgame(self):
        """
        模拟器不支持快玩
        :return:
        toast：该设备暂不适配双开功能
        """
        self.wait_element_is_visible(self.select_game_loc, "选择游戏").click()
