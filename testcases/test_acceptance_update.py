# !/usr/bin/env python3  
# -*- coding: utf-8 -*-  
# @Software: PyCharm  
# @File: test_acceptance_update.py
# @Author: Zhoucaiyun 
# @Time: 2024/12/20 11:58

from page_objects.update_page import UpdatePage
from common.base_case import BaseCase


class TestAcceptanceUpdate(BaseCase):
    def test_update(self, to_settings_page_acctptance):
        self.logger.info('================ {} 开始测试================')
        AC = UpdatePage(to_settings_page_acctptance)
        now_version=AC.go_down()

        oline_version=AC.pub_setting()
        try:
            assert now_version >= oline_version
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功,当前为最新版本'.format(self.name))
        finally:
            self.logger.info('================ {} 测试结束================')
