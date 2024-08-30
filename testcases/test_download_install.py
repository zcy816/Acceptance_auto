# !/usr/bin/env python3.8
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: test_download_install.py
# @Author:hejunrong
# @Time : 2023/10/18 9:28

import pytest
import settings
from common.base_case import BaseCase
from page_objects.base_page import AppBasePage
from page_objects.download_install import DownloadInstall
from page_objects.navigation_page import NavigationPage
from page_objects.My_page import MyPage
from page_objects.settings_page import SettingsPage
from page_objects.login_page import LoginPage


class TestDownloadInstall(BaseCase):
    name = "下载安装"

    # 执行可能会遇到小米检测频繁安装拦截，需要手动验证
    @pytest.mark.run(order=62)
    @pytest.mark.down
    def test_details_download(self, to_game_details_page):
        self.logger.info('================ {} 开始测试================')
        # 1、进入游戏详情页
        di = DownloadInstall(to_game_details_page)
        # 2、下载游戏
        di.details_download()
        # 3、安装
        di.game_install()
        # 4、查看安装结果
        text = di.install_result()
        # 5、断言
        try:
            assert text == '完成'
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            # 1、卸载游戏
            di.uninstall_game('com.cwlr.x7sy')
            # 3、切换账号
            ab = AppBasePage(to_game_details_page)
            ab.return_home()
            ab.delay(1)
            np = NavigationPage(to_game_details_page)
            np.switch_navigation('我的')
            mp = MyPage(to_game_details_page)
            mp.enter_settings_page()
            sp = SettingsPage(to_game_details_page)
            sp.logout()
            mp.delay(1)
            mp.enter_login_page()
            lp = LoginPage(to_game_details_page)
            lp.login(**settings.TEST_USER)
            self.logger.info('================ {} 测试结束================')

    @pytest.mark.run(order=63)
    @pytest.mark.down
    def test_center_download(self, to_played_page):
        self.logger.info('================ {} 开始测试================')
        # 1、进入我玩过的
        di = DownloadInstall(to_played_page)
        # 2、点击下载
        di.center_download()
        # 3、安装
        di.game_install()
        # 4、查看安装结果
        text = di.install_result()
        # 5、断言
        try:
            assert text == '完成'
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            # 1、卸载游戏
            di.uninstall_game('com.moling.x7sy')
            # 2、切换账号
            ab = AppBasePage(to_played_page)
            ab.return_home()
            ab.delay(1)
            np = NavigationPage(to_played_page)
            np.switch_navigation('我的')
            mp = MyPage(to_played_page)
            mp.enter_settings_page()
            sp = SettingsPage(to_played_page)
            sp.logout()
            mp.delay(1)
            mp.enter_login_page()
            lp = LoginPage(to_played_page)
            lp.login(**settings.TEST_USER2)
            self.logger.info('================ {} 测试结束================')

    @pytest.mark.run(order=64)
    @pytest.mark.down
    def test_cloud_download(self, to_cloudgame_page):
        self.logger.info('================ {} 开始测试================')
        # 1、进入云试玩内
        di = DownloadInstall(to_cloudgame_page)
        # 2、下载游戏
        toast = di.cloud_download()
        # 3、安装
        di.game_install()
        # 4、查看安装结果
        text = di.install_result()
        # 5、断言
        try:
            assert toast == '已添加到下载管理中' and text == '完成'
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            # 1、卸载游戏
            di.uninstall_game('com.shunjie.ycqstly.x7sy')
            # 2、返回APP
            ab = AppBasePage(to_cloudgame_page)
            ab.return_home()
            ab.delay(1)
            self.logger.info('================ {} 测试结束================')

    @pytest.mark.run(order=65)
    @pytest.mark.down
    def test_role_download(self, to_role_details_page):
        self.logger.info('================ {} 开始测试================')
        # 1、进入角色详情页
        di = DownloadInstall(to_role_details_page)
        # 2、点击下载
        di.role_download()
        # 3、安装
        di.game_install()
        # 4、查看安装结果
        text = di.install_result()
        # 5、断言
        try:
            assert text == '完成'
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            # 1、卸载游戏
            di.uninstall_game('com.tlpxzf.x7sy')
            # 2、清除APP缓存
            ab = AppBasePage(to_role_details_page)
            ab.return_home()
            np = NavigationPage(to_role_details_page)
            np.switch_navigation('我的')
            mp = MyPage(to_role_details_page)
            mp.enter_settings_page()
            sp = SettingsPage(to_role_details_page)
            sp.clear_cache()
            self.logger.info('================ {} 测试结束================')
