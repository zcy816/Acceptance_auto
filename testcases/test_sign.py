# !/usr/bin/env python3.8
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: test_sign.py
# @Author:hejunrong
# @Time : 2023/10/20 19:55

import pytest
from common.base_case import BaseCase
from page_objects.sign_page import SignPage


class TestSign(BaseCase):
    name = "签到功能"

    # 模拟器不支持签到
    @pytest.mark.run(order=26)
    @pytest.mark.fail
    @pytest.mark.sign
    def test_sign(self,to_sign_page):
        self.logger.info('================ {} 开始测试================')
        # 1、模拟器进入签到页面
        sip = SignPage(to_sign_page)
        # 2、点击签到按钮
        toast = sip.click_sign()
        # 3、断言
        try:
            assert "暂不支持使用模拟器进行签到" in toast
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            self.logger.info('================ {} 测试结束================')
