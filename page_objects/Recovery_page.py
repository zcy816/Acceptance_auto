# !/usr/bin/env python3.8
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: Recovery_page.py
# @Author:hejunrong
# @Time : 2023/10/17 19:05

from appium.webdriver.common.mobileby import MobileBy
from page_objects.base_page import AppBasePage


class RecoveryPage(AppBasePage):
    name = '回收页面'

    # 购买按钮
    emption_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/deal_home_purchase_layout')

    # 回收按钮
    recovery_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/deal_home_recycle_layout')

    # 出售按钮
    sell_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/deal_home_sell_layout')

    # 开局号按钮
    init_account_loc = (MobileBy.ID, 'com.smwl.x7market:id/deal_home_init_account_layout')

    # 记录按钮
    record_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/deal_home_record_layout')

    # 搜索游戏框
    search_game = (MobileBy.ID, 'com.smwl.x7market:id/search_content')

    # 搜索按钮
    search_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/searchFrag_search')

    # 角色信息列表
    role_list = (MobileBy.ID, 'com.smwl.x7market:id/item_choice_sellgame_top_rl')

    # 角色详情页
    role_details = (MobileBy.XPATH,'(//android.widget.TextView[@resource-id="com.smwl.x7market:id/item_frag_deal_buyaccount_tv_describe"])[1]')

    # 角色购买
    role_buy_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/roledetail_btn_buy')

    # 已阅读买家须知
    already_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/dialog_shouchong_iv')

    # 购买(小号)
    s_buy_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/dialog_deal_notices_btn_ensure')

    # 继续购买
    continue_buy_loc = (MobileBy.ID, 'com.smwl.x7market:id/dialog_user_realname_ensure_btn')

    # 开局号详情页
    init_account_details = (MobileBy.XPATH, '(//android.view.ViewGroup[@resource-id="com.smwl.x7market:id/root_cl"])[1]')

    # 游戏区服
    game_district = (MobileBy.XPATH, '(//android.widget.TextView[@resource-id="com.smwl.x7market:id/select_tv"])[1]')

    # 指定区服
    designative_district = (MobileBy.XPATH, '//android.widget.TextView[contains(@text,"Q247")]')

    # 购买(开局号)
    i_buy_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/init_account_buy')

    # 我知道了
    know_btn_loc = (MobileBy.XPATH, '//android.widget.TextView[@text="我知道了"]')

    # 右上角提醒toast
    remind_toast = (MobileBy.ID, 'com.smwl.x7market:id/item_normal_hint_tv')

    def enter_emption_page(self):
        """
        进入购买页面
        :return:
        """
        self.wait_element_is_visible(self.emption_btn_loc, '进入购买页面').click()

    def enter_recovery_page(self):
        """
        进入回收页面
        :return:
        """
        self.wait_element_is_visible(self.recovery_btn_loc, '进入回收页面').click()

    def enter_sell_page(self):
        """
        进入出售页面
        :return:
        """
        self.wait_element_is_visible(self.sell_btn_loc, '进入出售页面').click()

    def enter_initaccount_page(self):
        """
        进入开局号页面
        :return:
        """
        self.wait_element_is_visible(self.init_account_loc, '进入开局号页面').click()

    def enter_record_page(self):
        """
        进入记录页面
        :return:
        """
        self.wait_element_is_visible(self.record_btn_loc, '进入记录页面').click()

    def enter_roles_details(self, gamename):
        """
        进入角色详情页
        :param gamename:
        :return:
        """
        self.wait_element_is_visible(self.emption_btn_loc, '购买').click()
        self.wait_element_is_visible(self.search_game, '搜索游戏').send_keys(gamename)
        self.wait_element_is_visible(self.search_btn_loc, '点击搜索').click()
        self.wait_element_is_visible(self.role_list, '进入角色信息列表').click()
        self.wait_element_is_visible(self.role_details, '进入角色详情页').click()

    def enter_roles_payment(self, gamename):
        """
        进入角色购买支付页
        :param gamename:
        :return:
        """
        self.wait_element_is_visible(self.emption_btn_loc, '购买').click()
        self.wait_element_is_visible(self.search_game, '搜索游戏').send_keys(gamename)
        self.wait_element_is_visible(self.search_btn_loc, '点击搜索').click()
        self.wait_element_is_visible(self.role_list, '进入角色信息列表').click()
        self.wait_element_is_visible(self.role_details, '进入角色详情页').click()
        self.wait_element_is_visible(self.role_buy_btn_loc, '角色购买').click()
        if self.wait(MobileBy.ID, 'com.smwl.x7market:id/dialog_deal_notices_title'):
            self.wait_element_is_visible(self.s_buy_btn_loc, '购买').click()
            if self.get_toast_msg():
                self.wait_element_is_visible(self.already_btn_loc, '已阅读买家须知').click()
                self.wait_element_is_visible(self.s_buy_btn_loc, '购买').click()
            if self.wait(MobileBy.ID, 'com.smwl.x7market:id/dialog_user_realname_ensure_btn'):
                self.wait_element_is_visible(self.continue_buy_loc, '继续购买').click()
            self.logger.info('跳转支付页面正常')
        else:
            self.get_page_screenshot()
            self.logger.error('跳转支付页面异常')

    def enter_init_list(self, gamename):
        """
        进入开局号游戏列表页
        :param gamename:
        :return:
        """
        self.wait_element_is_visible(self.init_account_loc, '进入开局号页面').click()
        # 根据游戏名称进入指定游戏列表页
        action = '进入{}开局号列表页'.format(gamename)
        loc = (MobileBy.XPATH, '//android.widget.TextView[@text="{}"]'.format(gamename))
        self.scroll_to_capture_element(gamename)
        self.wait_element_is_visible(loc, action).click()
        # 关闭开局号列表页弹窗
        if self.wait(MobileBy.XPATH, '//android.widget.TextView[@text="开局号特殊说明"]'):
            self.wait_element_is_visible(self.know_btn_loc, '我知道了').click()
            if self.wait(MobileBy.ID, 'com.smwl.x7market:id/item_normal_hint_tv'):
                self.wait_element_is_visible(self.remind_toast, '去掉右上角提醒toast').click()
        else:
            # 关闭开局号列表toast
            if self.wait(MobileBy.ID, 'com.smwl.x7market:id/item_normal_hint_tv'):
                self.wait_element_is_visible(self.remind_toast, '去掉右上角提醒toast').click()

    def enter_init_payment(self):
        """
        进入开局号支付页
        :return:
        """
        self.wait_element_is_visible(self.game_district, '下拉选择区服').click()
        self.wait_element_is_visible(self.designative_district, '选择指定区服').click()
        self.wait_element_is_visible(self.init_account_details, '进入开局号详情页').click()
        if self.wait(MobileBy.XPATH, '//android.widget.TextView[@text="开局号详情"]'):
            self.wait_element_is_visible(self.i_buy_btn_loc, '购买').click()
            if self.wait(MobileBy.ID, 'com.smwl.x7market:id/dialog_user_realname_title_tv'):
                self.wait_element_is_visible(self.continue_buy_loc, '继续购买').click()
                self.logger.info('跳转支付页面')
        else:
            self.get_page_screenshot()
            self.logger.error('跳转支付页面失败')
