# !/usr/bin/env python3.8
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: live_page.py
# @Author:hejunrong
# @Time : 2023/10/30 14:59

from common.base_case import BaseCase
from appium.webdriver.common.mobileby import MobileBy
from page_objects.base_page import AppBasePage


class LivePage(AppBasePage, BaseCase):
    name = '直播页面'

    # 直播输入框
    live_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/live_bottom_tv')

    # 键盘输入框
    live_input_loc = (MobileBy.ID, 'com.smwl.x7market:id/live_et')

    # 发送
    send_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/live_send_tv')

    # 违规发言icon
    alert_message_loc = (MobileBy.ID, 'com.smwl.x7market:id/message_item_alert')

    # 收起底部
    retract_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/game_live_clean_cl')

    # 直播礼物
    live_gift_loc = (MobileBy.ID, 'com.smwl.x7market:id/live_bottom_gift_iv')

    # 赠送
    give_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/choosed_action_gift_text')

    # 平台币
    price_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/total_price_tv')

    # 确定
    confirm_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/confirm_action')

    # 支付密码
    password_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/smallhao_alertdialog_tv_message')

    # 确认支付
    ensure_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/alertdialog_btn_ensure')

    # 直播群聊
    live_group_loc = (MobileBy.ID, 'com.smwl.x7market:id/live_bottom_group_iv')

    # 加入群聊
    join_group_loc = (MobileBy.ID, 'com.smwl.x7market:id/fan_group_join_tv')
    join_group_loc2 = (MobileBy.ID, 'com.smwl.x7market:id/live_recommend_game_no_discounts_tv')

    # 群聊更多
    more_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/toolbar_right_iv')

    # 退出群聊
    exit_group_loc = (MobileBy.ID, 'com.smwl.x7market:id/team_member_teamState_btn')

    # 确定退出
    confirm_exit_loc = (MobileBy.ID, 'com.smwl.x7market:id/dialog_user_realname_ensure_btn')

    # 群聊文本
    live_in_group = (MobileBy.ID, 'com.smwl.x7market:id/yunXin_messageEdit_editTextMessage_et')

    # 详情页
    detail_icon_loc = (MobileBy.ID, 'com.smwl.x7market:id/live_bottom_game_cl')

    # 详情页文本
    detail_content_loc = (MobileBy.XPATH,'//android.widget.TextView[@text="详情"]')

    # 返回
    back_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/myView_title_back_iv')

    # 直播设置
    live_settings_loc = (MobileBy.ID, 'com.smwl.x7market:id/x7_game_live_setting_iv')

    # 礼物特效
    gift_effect_loc = (MobileBy.XPATH,'//android.widget.TextView[@text="礼物特效"]')

    # 暂不开启
    cancel_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/dialog_open_overlay_permission_cancel_btn')

    # 直播反馈
    live_feedback_loc = (MobileBy.XPATH,'//android.widget.TextView[@text="直播反馈"]')

    # 反馈输入框
    feedback_input_loc = (MobileBy.ID, 'com.smwl.x7market:id/live_feedback_et')

    # 提交
    commit_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/live_feedback_commit_tv')

    # 直播分享
    share_btn_loc = (MobileBy.XPATH,'//android.widget.TextView[@text="分享"]')

    # 复制链接
    shark_link_loc = (MobileBy.ID, 'com.smwl.x7market:id/live_share_link_tv')

    def live_speak(self, msg):
        """
        直播发言
        :return:
        """
        try:
            if self.long_wait(MobileBy.ID, 'com.smwl.x7market:id/live_bottom_tv'):
                self.wait_element_is_visible(self.live_btn_loc, '点击输入框').click()
                self.wait_element_is_visible(self.live_input_loc, '直播发言').send_keys(msg)
                self.wait_element_is_visible(self.send_btn_loc, '发送').click()
                self.wait_element_is_visible(self.retract_btn_loc, '收起底部键盘').click()
            else:
                self.get_page_screenshot()
                self.logger.error("定位直播输入框异常")
        except Exception as e:
            self.get_page_screenshot()
            raise e

    def alert_message(self):
        """
        判断是否发言违规
        :return:
        """
        if self.wait(MobileBy.ID, 'com.smwl.x7market:id/message_item_alert'):
            return True
        else:
            while True:
                self.swipe_by_coordinates_and_direction(300, 2000, 'up', 300,1000)
                if self.wait(MobileBy.ID, 'com.smwl.x7market:id/message_item_alert'):
                    return True
                else:
                    continue

    def live_gift(self, password):
        """
        直播送礼
        :param password:
        :return:
        toast: XXX赠送成功
        """
        self.wait_element_is_visible(self.live_gift_loc, '直播送礼').click()
        self.wait_element_is_visible(self.give_btn_loc, '赠送').click()
        self.wait_element_is_visible(self.price_btn_loc, '平台币').click()
        try:
            toast = self.get_toast_text()
            self.logger.info("未设置支付密码")
            return toast
        except Exception as e:
            if self.wait(MobileBy.ID, 'com.smwl.x7market:id/smallhao_alertdialog_tv_title'):
                self.wait_element_is_visible(self.password_btn_loc, '输入支付密码').send_keys(password)
                self.wait_element_is_visible(self.ensure_btn_loc, '确认支付').click()
                toast = self.get_toast_msg()
                return toast
            else:
                self.get_page_screenshot()
                self.logger.error("定位toast异常")
                raise e

    def live_group(self):
        """
        直播入群
        :return:
        """
        self.wait_element_is_visible(self.live_group_loc, '直播群聊').click()
        if self.wait(MobileBy.ID, 'com.smwl.x7market:id/fan_group_join_tip_tv'):
            self.wait_element_is_visible(self.join_group_loc, '加入群聊').click()
            if self.wait(MobileBy.ID, 'com.smwl.x7market:id/dialog_open_overlay_permission_title_tv'):
                self.wait_element_is_visible(self.cancel_btn_loc, '暂不开启').click()
            self.delay(1)
            text = self.wait_element_is_visible(self.live_in_group, '获取控件文本').get_text()
            return text
        elif self.wait(MobileBy.ID, 'com.smwl.x7market:id/dialog_open_overlay_permission_title_tv'):
            self.wait_element_is_visible(self.cancel_btn_loc, '暂不开启').click()
            self.delay(1)
            text = self.wait_element_is_visible(self.live_in_group, '获取控件文本').get_text()
            return text
        else:
            text = self.wait_element_is_visible(self.live_in_group, '获取控件文本').get_text()
            return text

    def exit_group(self):
        """
        退出群聊
        :return:
        toast:您已退群
        """
        self.wait_element_is_visible(self.more_btn_loc,'更多').click()
        self.scroll_to_capture_element('退出群聊')
        while True:
            self.wait_element_is_visible(self.exit_group_loc, '退出群聊').click()
            if self.wait(MobileBy.ID, 'com.smwl.x7market:id/dialog_user_realname_title_tv'):
                break
            else:
                continue
        self.wait_element_is_visible(self.confirm_exit_loc, '确认退出').click()
        try:
            toast = self.get_toast_text()
            return toast
        except Exception as e:
            self.get_page_screenshot()
            raise e

    def close_gift_effect(self):
        """
        关闭礼物特效
        :return:
        toast:已关闭礼物特效
        """
        self.wait_element_is_visible(self.live_settings_loc, '直播更多').click()
        self.wait_element_is_visible(self.gift_effect_loc, '关闭礼物特效').click()
        if self.wait(MobileBy.XPATH,'//*[@class="android.widget.Toast"]'):
            pass
        else:
            self.wait_element_is_visible(self.gift_effect_loc, '关闭礼物特效').click()

    def jump_detailpage(self):
        """
        跳转详情页
        :return:
        """
        if self.wait(MobileBy.ID, 'com.smwl.x7market:id/live_bottom_game_cl'):
            self.wait_element_is_visible(self.detail_icon_loc,'详情页按钮').click()
            if self.long_wait(MobileBy.XPATH,'//android.widget.TextView[@text="详情"]'):
                text = self.wait_element_is_visible(self.detail_content_loc, '获取控件文本').get_text()
                self.wait_element_is_visible(self.back_btn_loc, '返回直播内页').click()
                return text
            else:
                self.get_page_screenshot()
                self.logger.error("跳转详情页异常")
        else:
            self.get_page_screenshot()
            self.logger.error("该直播未配置详情页按钮")

    def enter_live_feedback(self):
        """
        进入直播反馈页面
        :return:
        """
        self.wait_element_is_visible(self.live_settings_loc, '直播更多').click()
        self.wait_element_is_visible(self.live_feedback_loc, '直播反馈').click()

    def live_feedback(self, content):
        """
        直播反馈
        :param content:
        :return:
        toast:请输入六个字以上的问题描述。
        toast:感谢您的反馈
        """
        self.wait_element_is_visible(self.feedback_input_loc, '输入内容').send_keys(content)
        self.wait_element_is_visible(self.commit_btn_loc, '提交').click()
        try:
            toast = self.get_toast_text()
            return toast
        except Exception as e:
            self.get_page_screenshot()
            self.logger.error("定位toast异常")
            raise e

    def share_link(self):
        """
        分享链接
        :return:
        toast:链接已复制手机剪切板~
        """
        self.wait_element_is_visible(self.live_settings_loc, '直播更多').click()
        while True:
            self.wait_element_is_visible(self.share_btn_loc, '直播分享').click()
            if self.wait(MobileBy.ID, 'com.smwl.x7market:id/live_share_link_tv'):
                break
            else:
                continue
        self.wait_element_is_visible(self.shark_link_loc, '复制链接').click()
        try:
            toast = self.get_toast_msg()
            return toast
        except Exception as e:
            self.get_page_screenshot()
            self.logger.error("定位toast异常")
            raise e
