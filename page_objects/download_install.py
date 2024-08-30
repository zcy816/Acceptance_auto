# !/usr/bin/env python3.8
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: download_install.py
# @Author:hejunrong
# @Time : 2023/10/17 9:52

from common.base_case import BaseCase
from appium.webdriver.common.mobileby import MobileBy
from page_objects.base_page import AppBasePage
import subprocess


class DownloadInstall(AppBasePage, BaseCase):
    name = '下载安装'

    # 详情页下载按钮
    details_download_loc = (MobileBy.ID, 'com.smwl.x7market:id/game_detail_download_tv')

    # 角色详情页下载按钮
    role_download_loc = (MobileBy.ID, 'com.smwl.x7market:id/game_download_state_tv')

    # 个人中心下载按钮
    center_download_loc = (MobileBy.ID, 'com.smwl.x7market:id/mine_download_tv')

    # 云试玩清晰度按钮
    definition_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/cloud_game_floating_definition_fl')

    # 云试玩下载按钮
    cloud_download_loc = (MobileBy.ID,'com.smwl.x7market:id/cloud_game_floating_download_fl')

    # 前往安装按钮
    go_to_install = (MobileBy.ID,'com.smwl.x7market:id/go_to_install_tv')

    # 安装按钮（雷电9）
    install_btn_loc = (MobileBy.ID,'com.android.packageinstaller:id/ok_button')

    # 完成按钮（雷电9）
    finish_btn_loc = (MobileBy.ID, 'com.android.packageinstaller:id/done_button')

    def details_download(self):
        """
        游戏详情页下载功能
        :return:
        """
        self.wait_element_is_visible(self.details_download_loc, '点击下载').click()

    def role_download(self):
        """
        角色详情页下载功能
        :return:
        """
        self.wait_element_is_visible(self.role_download_loc, '点击下载').click()

    def center_download(self):
        """
        个人中心下载功能
        :return:
        """
        self.wait_element_is_visible(self.center_download_loc, '点击下载').click()

    def cloud_download(self):
        """
        云试玩下载功能
        :return:
        """
        self.wait_element_is_visible(self.definition_btn_loc, '查看清晰度').click()
        self.wait_element_is_visible(self.cloud_download_loc, '点击下载').click()
        try:
            toast = self.get_toast_msg()
            if self.long_wait(MobileBy.ID,'com.smwl.x7market:id/title_tv'):
                self.wait_element_is_visible(self.go_to_install, '前往安装').click()
                return toast
            else:
                self.get_page_screenshot()
                self.logger.error('云试玩安装弹窗异常')
        except Exception as e:
            self.get_page_screenshot()
            self.logger.error('toast定位异常')
            raise e

    def game_install(self):
        """
        游戏安装（雷电9）
        :return:
        """
        try:
            if self.long_wait(MobileBy.ID, 'com.android.packageinstaller:id/install_confirm_question'):
                self.wait_element_is_visible(self.install_btn_loc, '安装').click()
            else:
                self.get_page_screenshot()
                self.logger.error('安装弹窗异常')
        except Exception as e:
            self.get_page_screenshot()
            self.logger.error('安装失败')
            raise e

    def install_result(self):
        """
        安装结果（雷电9）
        :return:
        """
        try:
            if self.long_wait(MobileBy.XPATH, '//android.widget.TextView[contains(@text,"应用安装完成")]'):
                self.logger.info('安装成功')
                text = self.wait_element_is_visible(self.finish_btn_loc, '获取控件文本').get_text()
                self.delay(1)
                self.wait_element_is_visible(self.finish_btn_loc, '完成').click()
                return text
            else:
                self.get_page_screenshot()
                self.logger.error('安装失败')
        except Exception as e:
            self.get_page_screenshot()
            raise e

    def uninstall_game(self, package_name):
        """
        卸载游戏
        :param package_name
        :return:
        """
        command = ["adb", "uninstall", package_name]
        process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout = process.stdout
        stderr = process.stderr

        if process.returncode == 0:
            self.logger.info(f"===============成功卸载游戏：{package_name}===============")
        else:
            self.get_page_screenshot()
            self.logger.error(f"===============卸载游戏失败：{package_name}===============")
            self.logger.error(stderr)
        return stdout, stderr
