# !/usr/bin/env python3.8
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: test_community.py
# @Author:hejunrong
# @Time : 2023/11/6 20:11

import pytest
from common.base_case import BaseCase
from page_objects.community_page import CommunityPage


class TestCommunity(BaseCase):
    name = "玩家圈子"

    @pytest.mark.run(order=34)
    @pytest.mark.post
    def test_create_post(self, to_community_page):
        self.logger.info('================ {} 开始测试================')
        # 1、进入社区页
        cp = CommunityPage(to_community_page)
        # 2、发布帖子
        text = cp.release_post("这个游戏好玩吗")
        # 3、断言
        try:
            assert text == "这个游戏好玩吗"
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            self.logger.info('================ {} 测试结束================')

    @pytest.mark.run(order=35)
    @pytest.mark.post
    def test_comment_post(self, to_community_page):
        self.logger.info('================ {} 开始测试================')
        # 1、进入社区页
        cp = CommunityPage(to_community_page)
        # 2、搜索帖子
        cp.search_post("这个游戏好玩吗")
        # 3、评论帖子
        toast = cp.comment_post("大佬带带我")
        # 4、断言
        try:
            assert toast == "发布成功"
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            self.logger.info('================ {} 测试结束================')

    @pytest.mark.run(order=36)
    @pytest.mark.post
    def test_delete_post(self, to_community_page):
        self.logger.info('================ {} 开始测试================')
        # 1、进入社区页
        cp = CommunityPage(to_community_page)
        # 2、删除
        toast = cp.delete_post()
        # 3、断言
        try:
            assert toast == "删除成功"
        except AssertionError as e:
            self.logger.error('{}测试失败'.format(self.name))
            raise e
        else:
            self.logger.info('{}测试成功'.format(self.name))
        finally:
            self.logger.info('================ {} 测试结束================')
