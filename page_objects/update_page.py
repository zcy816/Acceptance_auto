# !/usr/bin/env python3  
# -*- coding: utf-8 -*-  
# @Software: PyCharm  
# @File: update_page.py
# @Author: Zhoucaiyun 
# @Time: 2024/12/20 14:06
from common.base_case import BaseCase
from appium.webdriver.common.mobileby import MobileBy
from page_objects.base_page import AppBasePage
import json
import requests
import re


class UpdatePage(AppBasePage, BaseCase):
    # def __init__(self):
    #     pass
    # 我的按钮
    my_loc = (
        MobileBy.XPATH, '(//android.widget.ImageView[@resource-id="com.smwl.x7market.internation1:id/tab_icon_iv"])[4]')
    # 设置按钮
    setting_loc = (MobileBy.ID, 'com.smwl.x7market.internation1:id/set_ll')
    # 当前版本按钮
    version_loc = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="com.smwl.x7market.internation1:id/x7_setting_center_item_title_tv" and @text="当前版本"]')
    # 跳过按钮
    skip_but_loc = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="com.smwl.x7market.internation1:id/cancel"]')
    # 下载按钮
    download_loc = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="com.smwl.x7market.internation1:id/ok"]')
    # 安装时点击了解风险
    understand_risks_loc = (
        MobileBy.XPATH, '//android.widget.CheckBox[@resource-id="com.android.packageinstaller:id/cb_hint"]')
    # 继续安装
    Proceed_installation = (
        MobileBy.XPATH, '//android.widget.TextView[@resource-id="com.android.packageinstaller:id/ok_button"]')
    # 安装完成后点击打开
    open_loc = (MobileBy.XPATH,'//android.widget.TextView[@resource-id="com.android.packageinstaller:id/launch_button"]')
    # 当前版本号,去获取元素的文本，跟接口返回的版本进行对比
    current_version_loc = (MobileBy.XPATH,
                           '//android.widget.LinearLayout[@resource-id="com.smwl.x7market.internation1:id/settingCenter_activity_two_ll"]/android.view.ViewGroup[4]/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[2]')

    # 进入我的页面
    def go_mypage(self):
        self.wait_element_is_visible(self.my_loc, '我的').click()
        self.delay(1)

    # 进入设置页面
    def go_setting(self):
        self.wait_element_is_visible(self.setting_loc, '我的').click()
        self.delay(1)

    # 点击版本
    def click_version_button(self):
        self.wait_element_is_visible(self.current_version_loc, '当前版本').click()
        self.delay(2)

    # 点击下载
    def click_down(self):
        self.wait_element_is_visible(self.download_loc, '下载').click()
        self.delay(2)

    def click_skip(self):
        self.wait_element_is_visible(self.skip_but_loc, '跳过').click()
        self.delay(1)

    def go_down(self):
        now_version = self.wait_element_is_visible(self.current_version_loc, '当前版本').get_text()
        oline_version = self.pub_setting()
        if now_version < oline_version:
            self.logger.info('================ {} 当前版本小于线上版本================')
            self.click_version_button()
            self.click_down()
            self.wait_element_is_visible(self.understand_risks_loc, '了解风险').click()
            self.delay(2)
            self.wait_element_is_visible(self.Proceed_installation, '继续').click()
            self.delay(2)
            self.wait_element_is_visible(self.open_loc, '打开').click()
            self.delay(2)
            self.go_mypage()
            self.go_setting()
            self.current_now_version()

        elif now_version >= oline_version:
            self.logger.info('================ {} 当前版本大于等于线上版本================')
            self.current_now_version()

        return self.current_now_version()

    # 获取当前版本
    def current_now_version(self):
        now_version = self.wait_element_is_visible(self.current_version_loc, '当前版本').get_text()
        return now_version

    # 1、正常更新  2、当前是最新版本

    def pub_setting(self):
        """
        获取pub后台配置地址
        :return:
        """
        headers = {
            "User-Agent": "X7Market/5.80.999.5229/Android/5.1.1/phone/vivo_V1923A/2d1b13aa93f641071a423a7871822598/be93d73f874b76df252de138102d188e"
        }
        url_a = 'https://m.x7sy.com/p/X7Basic/getdownloadurl?sign=467095e250d26dbd3ad8d9c1ad831d436c6e1a3d&timeStamp=1719763200'
        pub_data = requests.get(headers=headers, url=url_a).text
        datas = json.loads(pub_data)
        version_foreigb = datas['download_url']['android_url_foreign']
        # print(version_foreigb)  # 'android_url_foreign': 'https://dl1.x7sy.com/market/android/6-6-0_1510-100/x7market_6-6-0_1510-100_1.apk'}

        url = version_foreigb

        pattern = r"/(\d+-\d+-\d+_\d+-\d+)"  # 匹配数字-数字-数字_数字-数字的模式

        match = re.search(pattern, url)
        if match:
            result = match.group(1)  # 提取匹配到的第一个组
            # print(result)  # 输出 6-6-0_1510-100
        else:
            print("No match found")

        # 分割字符串
        version_part, build_info_with_suffix = result.split("_")
        build_number = build_info_with_suffix.split("-")[0]  # 提取构建信息中的 1510 部分

        # 替换版本号中的 - 为 .
        version_number = version_part.replace("-", ".")
        global formatted_string
        # 构造最终字符串（我们知道版本号后缀是固定的 .100）
        formatted_string = f"{version_number}.100({build_number})"

        # print(formatted_string)  # 输出: 6.6.0.100(1510)
        return formatted_string
