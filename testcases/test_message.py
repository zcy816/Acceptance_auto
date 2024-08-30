# !/usr/bin/env python3.8
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: test_message.py
# @Author:hejunrong
# @Time : 2023/11/6 20:14

import pytest
import settings
from common.base_case import BaseCase
from page_objects.message_page import MessagePage
from common.excel_handler import ExcelHandle

M_data = ExcelHandle().read_data(settings.TEST_DATA_FILE, 'select_message_data')


class TestMessage(BaseCase):
    name = "私信消息"

    # 执行需要后台发送1条私信
    @pytest.mark.run(order=13)
    @pytest.mark.msg
    def test_view_message(self, to_message_page):
        self.logger.info('================ {} 开始测试================')
        # 1、进入消息列表
        mp = MessagePage(to_message_page)
        # 2、查看消息
        text = mp.view_message('自动化测试')
        # 3、断言
        try:
            assert text != ''
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            self.logger.info('================ {} 测试结束================')

    @pytest.mark.run(order=14)
    @pytest.mark.msg
    @pytest.mark.parametrize('data', M_data)
    def test_delete_message(self, data, to_message_page):
        self.logger.info('================ {} 开始测试================')
        # 1、进入消息列表
        mp = MessagePage(to_message_page)
        # 2、删除消息
        mp.delete_one_message(**eval(data['request_data']))
        # 3、断言
        try:
            assert data['error_msg'] in mp.get_toast_msg()
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            self.logger.info('================ {} 测试结束================')
