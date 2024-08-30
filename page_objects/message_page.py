# !/usr/bin/env python3.8
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: message_page.py
# @Author:hejunrong
# @Time : 2023/11/2 15:30

from common.base_case import BaseCase
from appium.webdriver.common.mobileby import MobileBy
from page_objects.base_page import AppBasePage


class MessagePage(AppBasePage, BaseCase):
    name = '消息页面'

    # 消息通知数量
    message_num_loc = (MobileBy.ID, 'com.smwl.x7market:id/act_messageCenter_message_point_tv')

    # 返回按钮
    back_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/imageview_title_left')

    # 右上角删除
    delete_top_loc = (MobileBy.ID, 'com.smwl.x7market:id/myView_title_rightTitle_tv')

    # 消息内容
    message_content_loc = (MobileBy.ID, 'com.smwl.x7market:id/act_messageanwser_messageinfo_tv')

    # 选择第一条消息
    select_message = (MobileBy.XPATH, '(//android.widget.CheckBox[@resource-id="com.smwl.x7market:id/item_messagecenter_delete_cb"])[1]')

    # 全选
    select_all_message = (MobileBy.ID, 'com.smwl.x7market:id/act_messagecenter_all_cb')

    # 底部删除
    delete_bottom_loc = (MobileBy.ID, 'com.smwl.x7market:id/act_messagecenter_delete_tv')

    # 确定按钮
    comfirm_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/dialog_user_realname_ensure_btn')

    def view_message(self,msg):
        """
        查看消息内容
        :param msg:
        :return:
        """
        message_btn_loc = (MobileBy.XPATH, '//android.widget.TextView[@text="{}"]'.format(msg))
        self.wait_element_is_visible(message_btn_loc, '查看指定消息').click()
        try:
            if self.wait(MobileBy.XPATH,'//android.widget.TextView[@text="系统消息"]') or self.wait(MobileBy.XPATH,'//android.widget.TextView[@text="活动通知"]') or self.wait(MobileBy.XPATH,'//android.widget.TextView[@text="到账提醒"]') or self.wait(MobileBy.XPATH,'//android.widget.TextView[@text="群聊通知"]') or self.wait(MobileBy.XPATH,'//android.widget.TextView[@text="推广信息"]'):
                text = self.wait_element_is_visible(self.message_content_loc, '获取控件文本').get_text()
                self.wait_element_is_visible(self.back_btn_loc, '返回').click()
                return text
            else:
                self.get_page_screenshot()
                self.logger.error('消息内页异常')
        except Exception as e:
            self.get_page_screenshot()
            raise e

    def delete_one_message(self,msg):
        """
        删除一条消息
        :param msg:
        :return:
        toast:删除成功
        """
        message_btn_loc = (MobileBy.XPATH, '//android.widget.TextView[@text="{}"]'.format(msg))
        self.wait_element_is_visible(self.delete_top_loc, '删除').click()
        self.wait_element_is_visible(message_btn_loc, '选择指定消息').click()
        self.wait_element_is_visible(self.delete_bottom_loc, '确认删除').click()

    def delete_all_message(self):
        """
        批量删除消息
        :return:
        toast:删除成功
        """
        self.wait_element_is_visible(self.delete_top_loc, '删除').click()
        self.wait_element_is_visible(self.select_all_message, '全选').click()
        self.wait_element_is_visible(self.delete_bottom_loc, '确认删除').click()
        if self.wait(MobileBy.ID,'com.smwl.x7market:id/dialog_user_realname_title_tv'):
            self.wait_element_is_visible(self.comfirm_btn_loc, '确定').click()
