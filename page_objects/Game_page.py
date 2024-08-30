# !/usr/bin/env python3.8
# encoding: utf-8
# Time:2023/9/13 10:23
# Author:xiaobin
# File:Game_page.py
# Software:PyCharm

from common.base_case import BaseCase
from page_objects.base_page import AppBasePage
from appium.webdriver.common.mobileby import MobileBy


class GamePage(AppBasePage, BaseCase):
    name = 'APP首页'

    # 推荐分栏
    recommend_column_loc = (MobileBy.XPATH, '//android.widget.TextView[@text="推荐"]')

    # 预约分栏
    reserve_column_loc = (MobileBy.XPATH, '//android.widget.TextView[@text="预约"]')

    # 直播分栏
    live_column_loc = (MobileBy.XPATH, '//android.widget.TextView[@text="弹幕游戏"]')

    # 直播分栏画面
    live_frame_loc = (MobileBy.XPATH, '(//android.widget.TextView[@resource-id="com.smwl.x7market:id/living_tv"])[1]')

    # 排行榜分栏
    rank_column_loc = (MobileBy.XPATH, '//android.widget.TextView[@text="排行榜"]')

    # 新游分栏
    newgames_column_loc = (MobileBy.XPATH, '//android.widget.TextView[@text="新游"]')

    # 小7月卡按钮
    monthcard_btn_loc = (MobileBy.XPATH, '//android.widget.TextView[@text="小7月卡"]')

    # 右上角签到按钮
    sign_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/sign_in_transition_iv')

    # 密码登录按钮
    login_tv = (MobileBy.XPATH, '//android.widget.TextView[@text="密码登录"]')

    # 今日首发
    first_launch = (MobileBy.ID, 'com.smwl.x7market:id/first_rl')

    # 搜索游戏框
    search_game_loc = (MobileBy.ID, 'com.smwl.x7market:id/search_content')

    # 搜索按钮
    search_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/searchFrag_search')

    # 游戏详情页
    game_details = (MobileBy.XPATH, '//android.widget.ListView/android.widget.LinearLayout[1]')

    # 顶部社区导航栏
    community_loc = (MobileBy.XPATH, '//android.widget.TextView[@text="社区999+"]')

    # 详情页云玩按钮
    cloud_game_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/game_detail_cloud_game_ll')

    # 我知道了
    know_btn_loc = (MobileBy.XPATH, '//android.widget.TextView[@text="我知道了"]')

    def click_recommend_column(self):
        """
        点击推荐分栏
        :return:
        """
        self.wait_element_is_visible(self.recommend_column_loc, '推荐').click()

    def click_reservation_column(self):
        """
        点击预约分栏
        :return:
        """
        self.wait_element_is_visible(self.reserve_column_loc, '预约').click()

    def enter_live_page(self, gamename):
        """
        点击直播分栏
        :return:
        """
        self.wait_element_is_visible(self.live_column_loc, '直播').click()
        action = '进入{}直播列表页'.format(gamename)
        loc = (MobileBy.XPATH, '//android.widget.TextView[contains(@text,"{}")]'.format(gamename))
        flag = True
        self.swipe_by_direction('down', action=action, duration=800, distance=500)
        while flag:
            # 1、先获取当前页面的xml
            page_source = self.driver.page_source
            # 2、先找一下对应直播
            try:
                if self.wait(MobileBy.XPATH, '//android.widget.TextView[contains(@text,"{}")]'.format(gamename)):
                    break
                else:
                    # 3、没有找到就向上滑
                    self.swipe_by_direction('up', action=action, duration=300, distance=500)
                    self.delay(1)
                    # 再比较当前页面xml有没有变化
                    temp = self.driver.page_source
                    # 表示滑到开局号游戏列表页面顶部
                    if page_source == temp:
                        break
            except Exception as e:
                self.logger.error('没有找到对应直播')
                raise e
        self.wait_element_is_visible(loc, action).click()
        if self.wait(MobileBy.ID,'com.smwl.x7market:id/blessingBagCountDownTopCl'):
            self.click_coordinates(530,300)

    def click_reserve_column(self):
        """
        点击排行榜分栏
        :return:
        """
        self.wait_element_is_visible(self.rank_column_loc, '排行榜').click()

    def click_newgames_column(self):
        """
        点击新游分栏
        :return:
        """
        self.wait_element_is_visible(self.newgames_column_loc, '新游').click()

    def enter_monthcard_page(self):
        """
        进入月卡页面
        :return:
        """
        self.wait_element_is_visible(self.monthcard_btn_loc, '小7月卡').click()
        if self.wait(MobileBy.ID, 'com.smwl.x7market:id/tv_month_game_vouchers_title'):
            self.wait_element_is_visible(self.know_btn_loc, '我知道了').click()

    def enter_sign_page(self):
        """
        进入签到
        :return:
        """
        self.wait_element_is_visible(self.sign_btn_loc, '签到').click()

    def enter_firstlaunch_page(self):
        """
        进入今日首发游戏详情页
        :return:
        """
        self.delay(1)
        self.wait_element_is_visible(self.first_launch, '今日首发').click()

    def enter_search_page(self, gamename):
        """
        搜索游戏
        :param gamename:
        :return:
        """
        self.wait_element_is_visible(self.search_game_loc, '进入搜索内页').click()
        self.wait_element_is_visible(self.search_game_loc, '输入游戏名称').send_keys(gamename)
        self.wait_element_is_visible(self.search_btn_loc, '搜索').click()

    def enter_details_page(self):
        """
        进入游戏详情页
        :return:
        """
        self.wait_element_is_visible(self.game_details, '进入游戏详情页').click()

    def enter_community_page(self):
        """
        进入社区
        :return:
        """
        self.wait_element_is_visible(self.game_details, '进入游戏详情页').click()
        self.wait_element_is_visible(self.community_loc, '进入玩家圈子').click()

    def click_cloudgame(self):
        """
        点击云玩
        :return:
        """
        self.wait_element_is_visible(self.cloud_game_btn_loc, '点击云玩').click()
