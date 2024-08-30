# !/usr/bin/env python3.8
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: test_fastplay.py
# @Author:hejunrong
# @Time : 2023/11/9 13:57

import pytest
from common.base_case import BaseCase
from page_objects.fastplay_page import FastPlayPage


class TestFastPlay(BaseCase):
    name = "快玩功能"

    # 模拟器不支持快玩
    @pytest.mark.run(order=61)
    @pytest.mark.fail
    @pytest.mark.play
    def test_simulator_fastgame(self,to_fastplay_page):
        self.logger.info('================ {} 开始测试================')
        # 1、进入快玩卡片页
        fp = FastPlayPage(to_fastplay_page)
        # 2、选择游戏
        fp.simulator_fastgame()
        # 3、断言
        try:
            assert fp.get_toast_msg() == '该设备暂不适配双开功能'
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            self.logger.info('================ {} 测试结束================')
