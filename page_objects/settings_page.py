# !/usr/bin/env python3.8
# encoding: utf-8
# Time:2023/9/14 16:01
# Author:xiaobin
# File:settings_page.py
# Software:PyCharm

from appium.webdriver.common.mobileby import MobileBy
from page_objects.base_page import AppBasePage


class SettingsPage(AppBasePage):
    name = '设置页面'

    # 退出按钮
    loginout_btn_loc = (MobileBy.XPATH, '//android.widget.TextView[@text="退出登录"]')

    # 确认退出登录
    confirm_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/dialog_user_realname_ensure_btn')

    # 安全与绑定
    security_btn_loc = (MobileBy.XPATH, '//android.widget.TextView[@text="安全与绑定"]')

    # 实名认证
    authentication_btn_loc = (MobileBy.XPATH, '//android.widget.TextView[@text="实名认证"]')

    # 关于小7
    about_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/x7_setting_center_item_center_tv')

    # 通用设置
    general_setting_loc = (MobileBy.XPATH, '//android.widget.TextView[@text="通用设置"]')

    # 清除缓存
    clear_cache_loc = (MobileBy.XPATH, '//android.widget.TextView[@text="清除缓存"]')

    def logout(self):
        """
        退出登录
        :return:
        """
        try:
            if self.wait(MobileBy.XPATH, '//android.widget.TextView[@text="退出登录"]'):
                self.wait_element_is_visible(self.loginout_btn_loc, '退出登录').click()
                self.wait_element_is_visible(self.confirm_btn_loc, '确认退出按钮').click()
                self.logger.info('退出登录成功')
            else:
                self.logger.info('当前处于未登录状态')
        except Exception as e:
            self.get_page_screenshot()
            raise e

    def security(self):
        """
        进入实名认证
        :return:
        """
        try:
            self.wait_element_is_visible(self.security_btn_loc, '安全与绑定').click()
            if self.wait(MobileBy.XPATH, '//android.widget.TextView[@text="去认证"]'):
                self.wait_element_is_visible(self.authentication_btn_loc, '实名认证').click()
            else:
                self.logger.info('当前处于已实名状态')
        except Exception as e:
            self.get_page_screenshot()
            raise e

    def about_version(self):
        """
        进入关于小7
        :return:
        """
        self.wait_element_is_visible(self.about_btn_loc, '关于小7').click()

    def clear_cache(self):
        """
        APP内清除缓存
        :return:
        """
        self.wait_element_is_visible(self.general_setting_loc,'通用设置').click()
        self.wait_element_is_visible(self.clear_cache_loc,'清除缓存').click()
        try:
            if self.wait(MobileBy.ID,'com.smwl.x7market:id/dialog_user_realname_title_tv'):
                self.wait_element_is_visible(self.confirm_btn_loc,'确认').click()
            else:
                self.get_page_screenshot()
                self.logger.error('清除缓存失败')
        except Exception as e:
            raise e
