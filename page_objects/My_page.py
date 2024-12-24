# !/usr/bin/env python3.8
# encoding: utf-8
# Time:2023/8/16 17:14
# Author:xiaobin
# File:My_page.py
# Software:PyCharm

import random
from appium.webdriver.common.mobileby import MobileBy
from page_objects.base_page import AppBasePage


class MyPage(AppBasePage):
    name = '我的页面'

    # 进入登录页面的按钮
    login_page_loc = (MobileBy.XPATH, '//android.widget.TextView[@text="未登录"]')

    # 进入设置页面的按钮
    settings_btn_loc = (MobileBy.ID, 'com.smwl.x7market.internation1:id/set_ll')

    # nickname 定位
    nick_name_loc = (MobileBy.ID, 'com.smwl.x7market:id/user_name_tv')

    # 小7月卡按钮
    monthcard_btn_loc = (MobileBy.XPATH, '//android.widget.TextView[@text="小7月卡"]')

    # 联系客服按钮
    service_btn_loc = (MobileBy.XPATH, '//android.widget.TextView[@text="联系客服"]')

    # 有奖任务按钮
    award_btn_loc = (MobileBy.XPATH, '//android.widget.TextView[@text="有奖任务"]')

    # 试玩有奖按钮
    trial_award = (MobileBy.XPATH, '//android.widget.TextView[@text="试玩有奖"]')

    # 邀请有奖按钮
    invite_award = (MobileBy.XPATH, '//android.widget.TextView[@text="邀请有奖"]')

    # 绑定微信有奖按钮
    bind_award = (MobileBy.XPATH, '//android.widget.TextView[@text="微信绑定有奖"]')

    # 关闭登陆弹窗
    close_login_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/login_close_iv')

    # 下载管理
    download_management_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/download_iv')

    # 消息
    message_btn_loc = (MobileBy.XPATH, '//android.widget.TextView[@text="消息"]')

    # 个人主页
    personal_homepage = (MobileBy.ID, 'com.smwl.x7market:id/user_login_arrow_iv')

    # 代金券
    voucher_btn_loc = (MobileBy.ID, "com.smwl.x7market:id/vouchers_tv")

    # 余额
    balance_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/balance_tv')

    # 两周内
    two_weeks_loc = (MobileBy.XPATH, '//android.widget.TextView[@text="两周内"]')

    # 总时长
    total_duration_loc = (MobileBy.XPATH, '//android.widget.TextView[@text="总时长"]')

    # 我玩过的
    played_btn_loc = (MobileBy.XPATH, '//android.widget.TextView[@text="我玩过的"]')

    # 预约的
    reservation_btn_loc = (MobileBy.XPATH, '//android.widget.TextView[@text="预约的"]')

    # 云挂机
    cloud_onhook_loc = (MobileBy.XPATH, '//android.widget.TextView[@text="云挂机"]')

    # 双开
    double_open_loc = (MobileBy.XPATH, '//android.widget.TextView[@text="双开"]')

    # 6元无门槛券按钮
    nothreshold_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/already_bought_daily_title_tv')

    # 月卡立返券按钮
    rebate_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/already_bought_immediately_title_tv')

    # 随机选择代金券
    voucher = [nothreshold_btn_loc, rebate_btn_loc]

    # 周卡按钮
    weekly_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/weekly_card_cl')

    # 月卡按钮
    month_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/month_card_right_price_tv')

    # 随机选卡
    card = [weekly_btn_loc, month_btn_loc]

    # 购买/续费
    buycard_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/btn_buy_card')

    # 我知道了
    know_btn_loc = (MobileBy.XPATH, '//android.widget.TextView[@text="我知道了"]')

    # 购买(云挂机)
    cloud_buy_loc = (MobileBy.ID, 'com.smwl.x7market:id/fragment_cloud_on_hook_purchase_device_tv')

    # 前往购买(云挂机)
    go_buy_loc = (MobileBy.ID, 'com.smwl.x7market:id/no_support_cloud_game_sure_tv')

    # 天卡
    day_card_loc = (MobileBy.XPATH,'(//android.widget.RelativeLayout[@resource-id="com.smwl.x7market:id/back_rl"])[1]')

    # 周卡
    week_card_loc = (MobileBy.XPATH,'(//android.widget.RelativeLayout[@resource-id="com.smwl.x7market:id/back_rl"])[2]')

    # 月卡
    month_card_loc = (MobileBy.XPATH,'(//android.widget.RelativeLayout[@resource-id="com.smwl.x7market:id/back_rl"])[3]')

    # 季卡
    season_card_loc = (MobileBy.XPATH,'(//android.widget.RelativeLayout[@resource-id="com.smwl.x7market:id/back_rl"])[4]')

    # 随机选卡
    cloud_card = [day_card_loc,week_card_loc,month_card_loc,season_card_loc]

    def enter_login_page(self):
        """
        进入登录页面
        :return:
        """
        self.wait_element_is_visible(self.login_page_loc, '进入登录页面').click()

    def is_login(self):
        """
        判断登陆状态
        :return:
        """
        if self.wait(MobileBy.XPATH, '//android.widget.TextView[@text="未登录"]'):
            return True
        else:
            return False

    def enter_settings_page(self):
        """
        进入设置页面
        :return:
        """
        self.wait_element_is_visible(self.settings_btn_loc, '进入设置页面').click()

    def get_nick_name(self):
        """
        获取用户昵称
        :return:
        """
        return self.wait_element_is_visible(self.nick_name_loc, '获取用户昵称').get_text()

    def enter_homepage(self):
        """
        进入个人主页
        :return:
        """
        self.wait_element_is_visible(self.personal_homepage, '个人主页').click()

    def enter_message_page(self):
        """
        进入消息列表
        :return:
        """
        self.wait_element_is_visible(self.message_btn_loc, '消息').click()

    def enter_vouchers_page(self):
        """
        进入代金券页面
        :return:
        """
        self.wait_element_is_visible(self.voucher_btn_loc, '代金券').click()

    def enter_vouchers_page2(self):
        """
        月卡进入代金券页面
        :return:
        """
        self.wait_element_is_visible(self.monthcard_btn_loc, '小7月卡').click()
        if self.wait(MobileBy.ID, 'com.smwl.x7market:id/tv_month_game_vouchers_title'):
            self.wait_element_is_visible(self.know_btn_loc, '我知道了').click()
        v = random.choice(self.voucher)
        self.wait_element_is_visible(v, '代金券').click()

    def enter_monthcard_payment(self):
        """
        进入月卡支付页面
        :return:
        """
        self.wait_element_is_visible(self.monthcard_btn_loc, '小7月卡').click()
        if self.wait(MobileBy.ID, 'com.smwl.x7market:id/tv_month_game_vouchers_title'):
            self.wait_element_is_visible(self.know_btn_loc, '我知道了').click()
        if self.wait(MobileBy.XPATH,'//android.widget.TextView[@text="已开通"]'):
            self.wait_element_is_visible(self.buycard_btn_loc, '续费').click()
            self.scroll_to_capture_element('银联在线')
        else:
            c = random.choice(self.card)
            self.wait_element_is_visible(c, '随机选卡').click()
            self.wait_element_is_visible(self.buycard_btn_loc, '购买').click()

    def enter_recharge_page(self):
        """
        进入充值页面
        :return:
        """
        self.wait_element_is_visible(self.balance_btn_loc, '余额').click()
        self.delay(3)
        if self.wait(MobileBy.ID, "com.smwl.x7market:id/pay_way_choose_title"):
            self.logger.info('充值页面正常')
        else:
            self.get_page_screenshot()
            self.logger.info('充值页面异常')

    def enter_monthcard_page(self):
        """
        进入月卡页面
        :return:
        """
        self.wait_element_is_visible(self.monthcard_btn_loc, '小7月卡').click()
        if self.wait(MobileBy.ID, 'com.smwl.x7market:id/tv_month_game_vouchers_title'):
            self.wait_element_is_visible(self.know_btn_loc, '我知道了').click()

    def enter_service_page(self):
        """
        进入联系客服页面
        :return:
        """
        self.wait_element_is_visible(self.service_btn_loc, '联系客服').click()
        if self.wait(MobileBy.XPATH, '//android.widget.TextView[@text="密码登录"]'):
            self.wait_element_is_visible(self.close_login_btn_loc, '关闭登陆弹窗').click()

    def enter_trial_page(self):
        """
        进入试玩有奖页面
        :return:
        """
        self.wait_element_is_visible(self.award_btn_loc, '有奖任务').click()
        self.wait_element_is_visible(self.trial_award, '试玩有奖').click()

    def enter_invite_page(self):
        """
        进入邀请有奖页面
        :return:
        """
        self.wait_element_is_visible(self.award_btn_loc, '有奖任务').click()
        self.wait_element_is_visible(self.invite_award, '邀请有奖').click()

    def enter_bind_page(self):
        """
        进入绑定微信有奖页面
        :return:
        """
        self.wait_element_is_visible(self.award_btn_loc, '有奖任务').click()
        self.wait_element_is_visible(self.bind_award, '绑定微信有奖').click()

    def enter_download_page(self):
        """
        进入下载管理
        :return:
        """
        self.wait_element_is_visible(self.download_management_btn_loc, '下载管理').click()

    def enter_played_page(self):
        """
        进入我玩过的页面
        :return:
        """
        self.wait_element_is_visible(self.played_btn_loc, '我玩过的').click()
        if self.wait(MobileBy.XPATH, '//android.widget.TextView[@text="总时长"]'):
            self.wait_element_is_visible(self.total_duration_loc, '总时长').click()
            self.delay(3)

    def enter_reservation_page(self):
        """
        进入预约的页面
        :return:
        """
        self.wait_element_is_visible(self.reservation_btn_loc, '预约的').click()

    def enter_onhook_page(self):
        """
        进入云挂机卡片
        :return:
        """
        self.wait_element_is_visible(self.cloud_onhook_loc, '云挂机').click()

    def enter_onhook_payment(self):
        """
        进入云挂机购买页面
        :return:
        """
        self.wait_element_is_visible(self.cloud_onhook_loc, '云挂机').click()
        self.wait_element_is_visible(self.cloud_buy_loc, '购买').click()
        if self.wait(MobileBy.ID, 'com.smwl.x7market:id/no_support_cloud_game_title_tv'):
            self.wait_element_is_visible(self.go_buy_loc, '前往购买').click()
        c = random.choice(self.cloud_card)
        self.wait_element_is_visible(c,'随机选卡').click()
        self.scroll_to_capture_element('银联在线')

    def enter_fastpaly_page(self):
        """
        进入快玩卡片页
        :return:
        """
        self.wait_element_is_visible(self.double_open_loc, '双开').click()
