# !/usr/bin/env python3.8
# encoding: utf-8
# Time:2023/8/17 10:52
# Author:xiaobin
# File:login_page.py
# Software:PyCharm

from common.base_case import BaseCase
from appium.webdriver.common.mobileby import MobileBy
from page_objects.base_page import AppBasePage


class LoginPage(AppBasePage, BaseCase):
    name = '登录页面'

    # 密码登录按钮
    password_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/password_login_tv')

    # 用户名输入框
    username_input_loc = (MobileBy.ID, 'com.smwl.x7market:id/account_et')

    # 密码输入框
    password_input_loc = (MobileBy.ID, 'com.smwl.x7market:id/login_password_et')

    # 登录按钮
    submit_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/login_ensure_tv')

    # 同意按钮
    agree_btn = (MobileBy.ID, 'com.smwl.x7market:id/login_protocol_know_tv')

    def app_policy(self):
        """
        隐私政策
        :return:
        """
        if self.wait(MobileBy.ID, 'com.smwl.x7market:id/privacy_policy_top_content_tv'):
            self.logger.info('弹出隐私政策弹窗')
            self.wait_element_is_visible(self.agree_policy_loc, '同意').click()
        while True:
            if self.long_wait(MobileBy.XPATH, '//android.widget.TextView[@text="推荐"]'):
                break
            else:
                continue

    def login(self, username, password):
        """
        账号密码登录
        :param username:
        :param password:
        :return:
        """
        try:
            # 判断是否在验证码登录页面
            if self.wait(MobileBy.ID, 'com.smwl.x7market:id/password_login_tv'):
                self.wait_element_is_visible(self.password_btn_loc, '密码登录按钮').click()
            else:
                self.logger.info('当前处于账号密码登录页面')
        except Exception as e:
            self.logger.error('目前不在登录页面')
            self.get_page_screenshot()
            raise e
        self.delay(1)
        # 进入账号密码登录页面
        self.wait_element_is_visible(self.username_input_loc, '输入账号').send_keys(username)
        self.wait_element_is_visible(self.password_input_loc, '输入密码').send_keys(password)
        self.wait_element_is_visible(self.submit_btn_loc, '点击登录').click()
        try:
            # 判断是否存在toast提示，如果有toast，则认为已经勾选用户协议
            if self.wait(MobileBy.XPATH, '//*[@class="android.widget.Toast"]'):
                self.logger.info('已勾选用户协议')
            # 判断是否出现登录弹窗
            elif self.wait(MobileBy.ID, 'com.smwl.x7market:id/login_protocol_know_tv'):
                self.wait_element_is_visible(self.agree_btn).click()
                self.logger.info('勾选用户协议并登录成功')
            else:
                self.logger.error('没有捕获到页面上的元素')
        except Exception as e:
            self.get_page_screenshot()
            raise e
