# !/usr/bin/env python3.8
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: init_account_page.py
# @Author:hejunrong
# @Time : 2023/11/6 12:28

from common.base_case import BaseCase
from appium.webdriver.common.mobileby import MobileBy
from page_objects.base_page import AppBasePage


class InitAccountPage(AppBasePage, BaseCase):
    name = '开局号'

    # 游戏区服
    choose_game_district = (MobileBy.XPATH, '//android.widget.TextView[contains(@text,"游戏区服")]')

    # 角色分类
    choose_role_sort = (MobileBy.XPATH, '//android.widget.TextView[contains(@text,"分类")]')

    # 完成
    finish_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/classify_list_finish_tv')

    # 返回
    back_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/myView_title_back_iv')

    # 更多
    more_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/myView_title_detail_more_iv')

    # 规则说明
    rule_description_loc = (MobileBy.XPATH, '//android.widget.TextView[@text="规则说明"]')

    # 规则内容
    rule_content_loc = (MobileBy.XPATH,'(//android.widget.TextView[@resource-id="com.smwl.x7market:id/arena_rule_content"])[1]')

    # 上架提醒
    list_remind_loc = (MobileBy.XPATH, '//android.widget.TextView[@text="上架提醒"]')

    # 添加提醒
    add_remind_loc = (MobileBy.ID, 'com.smwl.x7market:id/add_reminder_button_ll')

    # 提交
    submit_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/choose_role_commit_tv')

    # 上架提醒内容
    remind_content_loc = (MobileBy.XPATH,'(//android.widget.TextView[@resource-id="com.smwl.x7market:id/content_tv"])[3]')

    # 设置
    set_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/remind_set_tv')

    # 删除
    delete_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/modify_shelf_remind_delete_tv')

    # 删除提醒内容
    delete_remind_content = (MobileBy.XPATH, '//android.widget.TextView[@text="您还没有添加上架提醒"]')

    def switch_district(self, district):
        """
        游戏区服筛选
        :param district:
        :return:
        """
        action = '选择游戏区服：{}'.format(district)
        game_district_loc = (MobileBy.XPATH, '//android.widget.TextView[@text="{}"]'.format(district))
        text1 = self.wait_element_is_visible(self.choose_game_district, '获取控件文本1').get_text()
        self.wait_element_is_visible(self.choose_game_district, '下拉游戏区服').click()
        self.wait_element_is_visible(game_district_loc, action).click()
        self.delay(2)
        text2 = self.wait_element_is_visible(self.choose_game_district, '获取控件文本2').get_text()
        return text1, text2

    def switch_role(self, role):
        """
        角色分类筛选
        :param role:
        :return:
        """
        action = '选择角色：{}'.format(role)
        game_role_loc = (MobileBy.XPATH, '//android.widget.TextView[@text="{}"]'.format(role))
        text1 = self.wait_element_is_visible(self.choose_role_sort, '获取控件文本').get_text()
        self.wait_element_is_visible(self.choose_role_sort, '下拉角色分类').click()
        self.wait_element_is_visible(game_role_loc,action).click()
        self.wait_element_is_visible(self.finish_btn_loc, '完成').click()
        self.delay(2)
        text2 = self.wait_element_is_visible(self.choose_role_sort, '获取控件文本').get_text()
        return text1, text2

    def rule_description(self):
        """
        规则说明
        :return:
        """
        self.wait_element_is_visible(self.more_btn_loc, '更多').click()
        self.wait_element_is_visible(self.rule_description_loc, '规则说明').click()
        text = self.wait_element_is_visible(self.rule_content_loc, '获取控件文本').get_text()
        self.wait_element_is_visible(self.back_btn_loc, '返回开局号列表').click()
        return text

    def list_remind(self, district, role):
        """
        添加上架提醒
        :param district:
        :param role:
        :return:
        """
        district_loc = (MobileBy.XPATH, '//android.widget.TextView[@text="{}"]'.format(district))
        role_loc = (MobileBy.XPATH, '//android.widget.TextView[@text="{}"]'.format(role))
        self.wait_element_is_visible(self.more_btn_loc, '更多').click()
        self.wait_element_is_visible(self.list_remind_loc, '上架提醒').click()
        self.wait_element_is_visible(self.add_remind_loc, '添加提醒').click()
        self.wait_element_is_visible(district_loc, '选择区服').click()
        self.wait_element_is_visible(role_loc, '选择角色').click()
        self.wait_element_is_visible(self.submit_btn_loc, '提交').click()
        text = self.wait_element_is_visible(self.remind_content_loc, '获取控件文本').get_text()
        return text

    def delete_remind(self):
        """
        删除上架提醒
        :return:
        """
        self.wait_element_is_visible(self.set_btn_loc, '设置').click()
        self.wait_element_is_visible(self.delete_btn_loc, '删除').click()
        text = self.wait_element_is_visible(self.delete_remind_content, '获取控件文本').get_text()
        return text
