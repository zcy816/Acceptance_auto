# !/usr/bin/env python3.8
# encoding: utf-8
# Time:2023/9/12 19:19
# Author:xiaobin
# File:sign_page.py
# Software:PyCharm

import random
from common.base_case import BaseCase
from appium.webdriver.common.mobileby import MobileBy
from page_objects.base_page import AppBasePage


class SignPage(AppBasePage, BaseCase):
    name = '签到功能'

    # 签到按钮
    sign_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/sign_in_tv')

    def click_sign(self):
        """
        点击签到
        :return:
        """
        self.wait_element_is_visible(self.sign_btn_loc, '签到按钮').click()
        try:
            toast = self.get_toast_msg()
            return toast
        except Exception as e:
            self.get_page_screenshot()
            self.logger.error(e)
            raise e
