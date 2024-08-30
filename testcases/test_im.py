# !/usr/bin/env python3.8
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: test_im.py
# @Author:hejunrong
# @Time : 2023/11/6 20:14

import pytest
from common.base_case import BaseCase
from page_objects.IM_page import IMPage


class TestIM(BaseCase):
    name = "群聊页面"

    @pytest.mark.run(order=37)
    @pytest.mark.success
    @pytest.mark.IM
    def test_send_message(self, to_im_page):
        self.logger.info('================ {} 开始测试================')
        # 1、进入群聊
        im = IMPage(to_im_page)
        # 2、发送消息
        im.send_messages('test')
        # 3、断言
        try:
            assert im.verify_message('test') == True
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            self.logger.info('================ {} 测试结束================')

    @pytest.mark.run(order=38)
    @pytest.mark.IM
    def test_withdraw_message(self, to_im_page):
        self.logger.info('================ {} 开始测试================')
        # 1、进入群聊
        im = IMPage(to_im_page)
        # 2、撤回消息
        toast = im.withdraw_messages('test')
        # 3、断言
        try:
            assert toast == '撤回成功'
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            self.logger.info('================ {} 测试结束================')

    @pytest.mark.run(order=39)
    @pytest.mark.fail
    @pytest.mark.IM
    def test_violation_message(self, to_im_page):
        self.logger.info('================ {} 开始测试================')
        # 1、进入群聊
        im = IMPage(to_im_page)
        # 2、发送违规消息
        im.send_messages('共产党')
        # 3、断言
        try:
            assert im.verify_alert_message() == True
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            self.logger.info('================ {} 测试结束================')

    @pytest.mark.run(order=40)
    @pytest.mark.IM
    def test_delete_message(self, to_im_page):
        self.logger.info('================ {} 开始测试================')
        # 1、进入群聊
        im = IMPage(to_im_page)
        # 2、删除消息
        im.delete_message('共产党')
        # 3、断言
        try:
            assert im.verify_alert_message() == False
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            self.logger.info('================ {} 测试结束================')

    @pytest.mark.run(order=41)
    @pytest.mark.IM
    def test_send_emoji(self, to_im_page):
        self.logger.info('================ {} 开始测试================')
        # 1、进入群聊
        im = IMPage(to_im_page)
        # 2、发送通用表情
        im.send_messages('[可爱]')
        # 3、断言
        try:
            assert im.verify_message('[可爱]') == True
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            self.logger.info('================ {} 测试结束================')

    @pytest.mark.run(order=42)
    @pytest.mark.IM
    def test_withdraw_emoji(self, to_im_page):
        self.logger.info('================ {} 开始测试================')
        # 1、进入群聊
        im = IMPage(to_im_page)
        # 2、撤回通用表情
        toast = im.withdraw_messages('[可爱]')
        # 3、断言
        try:
            assert toast == '撤回成功'
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            self.logger.info('================ {} 测试结束================')

    @pytest.mark.run(order=43)
    @pytest.mark.IM
    def test_add_emoji(self, to_im_page):
        self.logger.info('================ {} 开始测试================')
        # 1、进入群聊
        im = IMPage(to_im_page)
        # 2、添加自定义表情
        toast = im.add_emoji()
        # 3、断言
        try:
            assert toast == '成功添加1张图片到我的收藏'
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            self.logger.info('================ {} 测试结束================')

    @pytest.mark.run(order=44)
    @pytest.mark.IM
    def test_delete_emoji(self, to_im_page):
        self.logger.info('================ {} 开始测试================')
        # 1、进入群聊
        im = IMPage(to_im_page)
        # 2、删除自定义表情
        toast = im.delete_emoji()
        # 3、断言
        try:
            assert toast == '成功删除1个表情'
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            self.logger.info('================ {} 测试结束================')

    @pytest.mark.run(order=45)
    @pytest.mark.IM
    def test_send_picture(self, to_im_page):
        self.logger.info('================ {} 开始测试================')
        # 1、进入群聊
        im = IMPage(to_im_page)
        # 2、发送图片
        im.send_picture()
        # 3、断言
        try:
            assert im.verify_picture() == True
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            self.logger.info('================ {} 测试结束================')

    @pytest.mark.run(order=46)
    @pytest.mark.IM
    def test_withdraw_picture(self, to_im_page):
        self.logger.info('================ {} 开始测试================')
        # 1、进入群聊
        im = IMPage(to_im_page)
        # 2、撤回图片
        toast = im.withdraw_picture()
        # 3、断言
        try:
            assert toast == '撤回成功'
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            self.logger.info('================ {} 测试结束================')
