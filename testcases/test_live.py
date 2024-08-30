# !/usr/bin/env python3.8
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: test_live.py
# @Author:hejunrong
# @Time : 2023/11/6 20:14

import pytest
from common.base_case import BaseCase
from page_objects.base_page import AppBasePage
from page_objects.live_page import LivePage


class TestLive(BaseCase):
    name = "直播页面"

    # 执行需要在excel表格修改直播列表游戏
    @pytest.mark.run(order=47)
    @pytest.mark.live
    def test_live_speak(self, to_live_page):
        self.logger.info('================ {} 开始测试================')
        # 1、进入直播内页
        lp = LivePage(to_live_page)
        # 2、违规发言
        lp.live_speak("共产党")
        # 3、断言
        try:
            assert lp.alert_message() == True
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            # 关闭礼物特效
            lp.close_gift_effect()
            # 收起列表
            ab = AppBasePage(to_live_page)
            ab.click_coordinates(360, 100)
            ab.delay(1)
            self.logger.info('================ {} 测试结束================')

    @pytest.mark.run(order=48)
    @pytest.mark.success
    @pytest.mark.live
    def test_live_gift(self, to_live_page):
        self.logger.info('================ {} 开始测试================')
        # 1、进入直播内页
        lp = LivePage(to_live_page)
        # 2、直播送礼
        toast = lp.live_gift('123123')
        # 3、断言
        try:
            assert '赠送成功' in toast
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            # 收起列表
            ab = AppBasePage(to_live_page)
            ab.click_coordinates(360, 100)
            ab.delay(1)
            self.logger.info('================ {} 测试结束================')

    @pytest.mark.run(order=49)
    @pytest.mark.live
    def test_live_group(self, to_live_page):
        self.logger.info('================ {} 开始测试================')
        # 1、进入直播内页
        lp = LivePage(to_live_page)
        # 2、直播入聊
        text = lp.live_group()
        # 3、断言
        try:
            assert text == "和大家说点什么吧"
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            self.logger.info('================ {} 测试结束================')

    @pytest.mark.run(order=50)
    @pytest.mark.live
    def test_exit_group(self, to_live_page):
        self.logger.info('================ {} 开始测试================')
        # 1、进入直播内页
        lp = LivePage(to_live_page)
        # 2、退出群聊
        toast = lp.exit_group()
        # 3、断言
        try:
            assert toast == "您已退群"
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            self.logger.info('================ {} 测试结束================')

    @pytest.mark.run(order=51)
    @pytest.mark.fail
    @pytest.mark.live
    def test_feedback_f(self, to_live_page):
        self.logger.info('================ {} 开始测试================')
        # 1、进入直播内页
        lp = LivePage(to_live_page)
        # 2、直播反馈
        lp.enter_live_feedback()
        # 3、反馈失败
        toast = lp.live_feedback("")
        # 4、断言
        try:
            assert '请输入六个字以上' in toast
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            lp.delay(2)
            self.logger.info('================ {} 测试结束================')

    @pytest.mark.run(order=52)
    @pytest.mark.success
    @pytest.mark.live
    def test_feedback_s(self, to_live_page):
        self.logger.info('================ {} 开始测试================')
        # 1、直播反馈
        lp = LivePage(to_live_page)
        # 2、反馈成功
        toast = lp.live_feedback("测试测试测试")
        # 3、断言
        try:
            assert toast == "感谢您的反馈"
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            self.logger.info('================ {} 测试结束================')

    @pytest.mark.run(order=53)
    @pytest.mark.live
    def test_live_share(self, to_live_page):
        self.logger.info('================ {} 开始测试================')
        # 1、进入直播内页
        lp = LivePage(to_live_page)
        # 2、直播分享链接
        toast = lp.share_link()
        # 3、断言
        try:
            assert toast == "链接已复制到手机剪切板~"
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            self.logger.info('================ {} 测试结束================')
