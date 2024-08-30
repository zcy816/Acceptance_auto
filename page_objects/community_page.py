# !/usr/bin/env python3.8
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: community_page.py
# @Author:hejunrong
# @Time : 2023/11/2 14:47

from common.base_case import BaseCase
from appium.webdriver.common.mobileby import MobileBy
from page_objects.base_page import AppBasePage


class CommunityPage(AppBasePage, BaseCase):
    name = '玩家圈子'

    # 帖子搜索
    search_input_loc = (MobileBy.ID,'com.smwl.x7market:id/community_search_rl')

    # 搜索输入框
    search_input_loc2 = (MobileBy.ID,'com.smwl.x7market:id/community_search_et')

    # 搜索按钮
    search_btn_loc = (MobileBy.ID,'com.smwl.x7market:id/community_search_tv')

    # 搜索第一条帖子
    search_first_post = (MobileBy.XPATH,'//androidx.recyclerview.widget.RecyclerView[@resource-id="com.smwl.x7market:id/search_result_rv"]/android.widget.LinearLayout[1]')

    # 搜索最新
    search_new_loc = (MobileBy.ID,'com.smwl.x7market:id/search_result_newest_tv')

    # 搜索返回
    search_back_loc = (MobileBy.ID,'com.smwl.x7market:id/community_search_back_iv')

    # 新建帖子按钮
    create_btn_loc = (MobileBy.ID,'com.smwl.x7market:id/community_publish_sl')

    # 评论输入框
    comment_input_loc = (MobileBy.ID, 'com.smwl.x7market:id/myview_userReply_gameImpress_tv')

    # 内容编辑
    edit_content_loc = (MobileBy.ID, 'com.smwl.x7market:id/ed_user_comment')

    # 发布按钮
    release_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/video_publish_tv')

    # 发布顺序
    order_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/view_comment_select_order_iv')

    # 最新发布
    new_release_loc = (MobileBy.ID, 'com.smwl.x7market:id/community_newest_comment_order')

    # 更多按钮
    more_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/myView_title_more_operate_tv')

    # 云信输入框
    comment_input_loc2 = (MobileBy.ID, 'com.smwl.x7market:id/yunXin_messageEdit_editTextMessage_et')

    # 云信发送按钮
    send_icon_loc = (MobileBy.ID, 'com.smwl.x7market:id/yunXin_messageEdit_commit_iv')

    # 编辑
    edit_btn_loc = (MobileBy.XPATH, '//android.widget.TextView[@text="编辑"]')

    # 删除
    delete_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/x7_edit_send_comment_delete_iv')

    # 确定
    confirm_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/dialog_user_realname_ensure_btn')

    def release_post(self, content):
        """
        发布帖子
        :param content:
        :return:
        toast:发布成功
        """
        self.wait_element_is_visible(self.create_btn_loc, '新建').click()
        self.wait_element_is_visible(self.edit_content_loc, '输入文本').send_keys(content)
        self.wait_element_is_visible(self.release_btn_loc, '发布').click()
        try:
            loc = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="com.smwl.x7market:id/comment_summary_tv" and @text="{}"]'.format(content))
            text = self.wait_element_is_visible(loc,'获取控件文本').get_text()
            return text
        except Exception as e:
            self.get_page_screenshot()
            raise e

    def search_post(self, content):
        """
        搜索进入帖子内页
        :param content:
        :return:
        """
        try:
            if self.long_wait(MobileBy.ID,"com.smwl.x7market:id/community_search_rl"):
                self.wait_element_is_visible(self.search_input_loc, '搜索输入框').click()
                self.wait_element_is_visible(self.search_input_loc2, '输入文本').send_keys(content)
                self.wait_element_is_visible(self.search_btn_loc, '搜索').click()
                self.wait_element_is_visible(self.search_new_loc, '最新').click()
                self.wait_element_is_visible(self.search_first_post, '进入内页').click()
            else:
                self.get_page_screenshot()
                self.logger.error('定位搜索框异常')
        except Exception as e:
            self.get_page_screenshot()
            raise e

    def check_release(self,content):
        """
        判断是否发帖成功
        :param content:
        :return:
        """
        try:
            if self.wait(MobileBy.XPATH, '//android.view.View[@text="{}"]'.format(content)):
                return True
            else:
                return False
        except Exception as e:
            self.get_page_screenshot()
            self.logger.error('发帖失败')
            raise e

    def delete_post(self):
        """
        删除帖子
        :return:
        toast:删除成功
        """
        self.wait_element_is_visible(self.more_btn_loc, '更多').click()
        self.wait_element_is_visible(self.edit_btn_loc, '编辑').click()
        self.delay(2)
        self.wait_element_is_visible(self.delete_btn_loc, '删除').click()
        self.wait_element_is_visible(self.confirm_btn_loc, '确定').click()
        try:
            toast = self.get_toast_text()
            return toast
        except Exception as e:
            self.get_page_screenshot()
            self.logger.error('toast定位失败')
            raise e

    def comment_post(self,content):
        """
        评论帖子
        :param content:
        :return:
        toast:发布成功
        """
        self.wait_element_is_visible(self.comment_input_loc, '点击评论输入框').click()
        self.wait_element_is_visible(self.comment_input_loc2, '输入内容').send_keys(content)
        self.delay(1)
        self.wait_element_is_visible(self.send_icon_loc, '发送').click()
        try:
            toast = self.get_toast_text()
            return toast
        except Exception as e:
            self.get_page_screenshot()
            self.logger.error('toast定位失败')
            raise e
