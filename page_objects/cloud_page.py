# !/usr/bin/env python3.8
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: cloud_page.py
# @Author:hejunrong
# @Time : 2023/11/6 20:19

from common.base_case import BaseCase
from appium.webdriver.common.mobileby import MobileBy
from page_objects.base_page import AppBasePage


class CloudPage(AppBasePage, BaseCase):
    name = '云挂机功能'

    # 清晰度按钮
    definition_btn_loc = (MobileBy.ID,'com.smwl.x7market:id/cloud_game_floating_definition_fl')

    # 退出按钮
    exit_btn_loc = (MobileBy.ID,'com.smwl.x7market:id/cloud_game_floating_exit_fl')

    # 详情页云玩按钮
    cloud_game_btn_loc = (MobileBy.XPATH, '//android.widget.TextView[@text="云试玩"]')

    # 闲置中
    idle_btn_loc = (MobileBy.XPATH, '//android.widget.TextView[@text="闲置中"]')

    # 挂机中
    onhook_btn_loc = (MobileBy.XPATH, '//android.widget.TextView[@text="挂机中"]')

    # 启动游戏icon
    start_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/item_cloud_on_hook_device_idle_iv')

    # 搜索输入框
    search_input_loc = (MobileBy.ID, 'com.smwl.x7market:id/cloud_on_hook_game_search_content_et')

    # 搜索按钮
    search_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/cloud_on_hook_game_search_tv')

    # 关闭搜索按钮
    close_search_loc = (MobileBy.ID, 'com.smwl.x7market:id/cloud_on_hook_game_search_close_iv')

    # 云挂机按钮
    cloud_btn_loc = (MobileBy.XPATH, '(//android.widget.TextView[@resource-id="com.smwl.x7market:id/search_result_cloud_on_hook_tv"])[1]')

    # 返回
    back_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/cloud_game_floating_exit_fl')

    # 确定
    determine_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/confirm_action')

    # 云挂机截图
    onhook_frame_loc = (MobileBy.XPATH, '(//android.widget.ImageView[@resource-id="com.smwl.x7market:id/item_cloud_on_hook_device_background_iv"])[1]')

    # 退出挂机
    exit_onhook_loc = (MobileBy.ID, 'com.smwl.x7market:id/item_cloud_on_hook_quit_ll')

    # 确认
    confirm_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/dialog_user_realname_ensure_btn')

    def exit_cloudgame(self):
        """
        退出云试玩
        :return:
        """
        self.wait_element_is_visible(self.definition_btn_loc,'查看清晰度').click()
        self.wait_element_is_visible(self.exit_btn_loc,'退出云试玩').click()
        self.delay(3)
        if self.wait(MobileBy.ID,'com.smwl.x7market:id/dialog_user_realname_title_tv'):
            self.wait_element_is_visible(self.confirm_btn_loc,'确认').click()
            text = self.wait_element_is_visible(self.cloud_game_btn_loc,'获取控件文本').get_text()
            return text
        else:
            self.get_page_screenshot()
            self.logger.error('云试玩退出弹窗异常')

    def search_onhook(self, gamename):
        """
        搜索云挂机游戏
        :param:gamename
        :return:
        """
        try:
            if self.wait(MobileBy.XPATH, '//android.widget.TextView[@text="闲置中"]'):
                self.wait_element_is_visible(self.start_btn_loc, "启动游戏").click()
                self.wait_element_is_visible(self.search_input_loc, "输入游戏名").send_keys(gamename)
                self.wait_element_is_visible(self.search_btn_loc, "搜索").click()
            else:
                self.get_page_screenshot()
                self.logger.error('无设备/设备未处于挂机中状态')
        except Exception as e:
            self.get_page_screenshot()
            raise e

    def firing_support(self):
        """
        启动未挂机的游戏
        :return:
        """
        self.wait_element_is_visible(self.cloud_btn_loc, '云挂机按钮').click()
        self.wait_element_is_visible(self.back_btn_loc, '返回按钮').click()
        self.delay(5)

    def firing_unsupport(self):
        """
        启动不支持云挂机的游戏
        :return:
        toast:当前游戏暂时不支持云挂机
        """
        self.wait_element_is_visible(self.cloud_btn_loc, '云挂机按钮').click()
        self.wait_element_is_visible(self.close_search_loc, '关闭搜索').click()

    def firing_onhook(self):
        """
        启动挂机中的游戏
        :return:
        """
        try:
            if self.wait(MobileBy.XPATH, '//android.widget.TextView[@text="挂机中"]'):
                self.wait_element_is_visible(self.onhook_frame_loc, '云挂机截图').click()
                self.wait_element_is_visible(self.back_btn_loc, '返回按钮').click()
            else:
                self.logger.error('无设备/设备未处于挂机中状态')
        except Exception as e:
            self.get_page_screenshot()
            raise e

    def back_to_onhook(self):
        """
        返回云挂机卡片
        :return:
        """
        if self.wait(MobileBy.XPATH, '//android.widget.TextView[@text="返回APP"]'):
            self.wait_element_is_visible(self.determine_btn_loc, '确定').click()
            self.delay(1)
            text = self.wait_element_is_visible(self.onhook_btn_loc, ' 获取控件文本').get_text()
            return text
        elif self.wait(MobileBy.XPATH, '//android.widget.TextView[@text="挂机中"]'):
            self.logger.info('返回APP弹窗已开启不再提醒弹出')
            text = self.wait_element_is_visible(self.onhook_btn_loc, '获取控件文本').get_text()
            return text
        else:
            self.get_page_screenshot()
            self.logger.error('云挂机页面异常')

    def exit_onhook(self):
        """
        退出云挂机中的游戏
        :return:
        toast:已成功退出挂机
        """
        try:
            if self.wait(MobileBy.XPATH, '//android.widget.TextView[@text="挂机中"]'):
                self.wait_element_is_visible(self.exit_onhook_loc, '退出挂机').click()
                self.wait_element_is_visible(self.confirm_btn_loc, '确认').click()
            else:
                self.get_page_screenshot()
                self.logger.error('无设备/设备未处于挂机中状态')
        except Exception as e:
            self.get_page_screenshot()
            raise e
