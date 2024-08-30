# !/usr/bin/env python3.8
# encoding: utf-8
# Time:2023/8/15 16:10
# Author:xiaobin
# File:conftest.py
# Software:PyCharm

import pytest
import settings
from appium import webdriver
from page_objects.navigation_page import NavigationPage
from page_objects.login_page import LoginPage
from page_objects.My_page import MyPage
from page_objects.Game_page import GamePage
from page_objects.Recovery_page import RecoveryPage
from page_objects.IM_page import IMPage
from page_objects.home_page import HomePage
from common.excel_handler import ExcelHandle

live_data = ExcelHandle().read_data(settings.TEST_DATA_FILE, 'live_slide_data')
init_data = ExcelHandle().read_data(settings.TEST_DATA_FILE, 'init_slide_data')
G_data = ExcelHandle().read_data(settings.TEST_DATA_FILE, 'gamedetails_search_data')
cloud_data = ExcelHandle().read_data(settings.TEST_DATA_FILE, 'cloudgame_search_data')
C_data = ExcelHandle().read_data(settings.TEST_DATA_FILE, 'conmunity_search_data')
role_data = ExcelHandle().read_data(settings.TEST_DATA_FILE, 'roledetails_search_data')
IM_data = ExcelHandle().read_data(settings.TEST_DATA_FILE, 'im_name_data')


@pytest.fixture(scope='class')
def driver():
    """
    打开APP
    :return:
    """
    with webdriver.Remote(
            settings.APPIUM_SERVER_HOST,
            desired_capabilities=settings.DESIRED_CAPS) as session:
        lg = LoginPage(session)
        lg.app_policy()
        yield session


@pytest.fixture(scope='class')
def to_login_page(driver):
    """
    进入到登录页面
    :param driver:
    :return:
    """
    # 1、进入我的页面
    np = NavigationPage(driver)
    np.switch_navigation('我的')
    # 2、进入登录页面
    mp = MyPage(driver)
    mp.enter_login_page()
    yield driver


@pytest.fixture(scope='class')
def login_driver(driver):
    # 1、进入我的页面
    np = NavigationPage(driver)
    np.switch_navigation('我的')
    mp = MyPage(driver)
    a = mp.is_login()
    lg = LoginPage(driver)
    if a:
        mp.enter_login_page()
        lg.login(**settings.TEST_USER)
        lg.delay(2)
    # 2、进入登录页面
    yield driver


@pytest.fixture(scope='class')
def to_download_page(driver):
    """
    进入到游戏下载页面
    :param driver:
    :return:
    """
    # 1、进入我的页面
    np = NavigationPage(driver)
    np.switch_navigation('我的')
    # 2、进入游戏下载页面
    mp = MyPage(driver)
    mp.enter_download_page()
    yield driver


@pytest.fixture(scope='class')
def to_settings_page(driver):
    """
    进入到设置页面
    :param driver:
    :return:
    """
    # 1、进入个人中心页面
    np = NavigationPage(driver)
    np.switch_navigation('我的')
    # 2、进入设置页面
    mp = MyPage(driver)
    mp.enter_settings_page()
    yield driver


@pytest.fixture(scope='class')
def to_message_page(driver):
    """
    进入到消息列表
    :param driver:
    :return:
    """
    # 1、进入个人中心页面
    np = NavigationPage(driver)
    np.switch_navigation('我的')
    # 2、进入消息列表
    mp = MyPage(driver)
    mp.enter_message_page()
    yield driver


@pytest.fixture(scope='class')
def to_home_page(driver):
    """
    进入个人主页
    :param driver:
    :return:
    """
    # 1、进入个人中心页面
    np = NavigationPage(driver)
    np.switch_navigation('我的')
    # 2、进入个人主页
    mp = MyPage(driver)
    mp.enter_homepage()
    yield driver


@pytest.fixture(scope='class')
def to_vouchers_page(driver):
    """
    个人中心进入代金券页面
    :param driver:
    :return:
    """
    # 1、进入个人中心页面
    np = NavigationPage(driver)
    np.switch_navigation('我的')
    # 2、进入代金券页面
    mp = MyPage(driver)
    mp.enter_vouchers_page()
    yield driver


@pytest.fixture(scope='class')
def to_vouchers_page2(driver):
    """
    月卡进入代金券页面
    :param driver:
    :return:
    """
    # 1、进入个人中心页面
    np = NavigationPage(driver)
    np.switch_navigation('我的')
    # 2、进入代金券页面
    mp = MyPage(driver)
    mp.enter_vouchers_page2()
    yield driver


@pytest.fixture(scope='class')
def to_recharge_page(driver):
    """
    进入余额充值页面
    :param driver:
    :return:
    """
    # 1、进入个人中心页面
    np = NavigationPage(driver)
    np.switch_navigation('我的')
    # 2、进入余额充值页面
    mp = MyPage(driver)
    mp.enter_recharge_page()
    yield driver


@pytest.fixture(scope='class')
def to_monthcard_page(driver):
    """
    个人中心进入到月卡页面
    :param driver:
    :return:
    """
    # 1、进入我的页面
    np = NavigationPage(driver)
    np.switch_navigation('我的')
    # 2、进入月卡页面
    mp = MyPage(driver)
    mp.enter_monthcard_page()
    yield driver


@pytest.fixture(scope='class')
def to_monthcard_payment(driver):
    """
    进入到月卡支付页面
    :param driver:
    :return:
    """
    # 1、进入我的页面
    np = NavigationPage(driver)
    np.switch_navigation('我的')
    # 2、进入月卡支付页面
    mp = MyPage(driver)
    mp.enter_monthcard_payment()
    yield driver


@pytest.fixture(scope='class')
def to_played_page(driver):
    """
    进入我玩过的
    :param driver:
    :return:
    """
    # 1、进入个人中心
    np = NavigationPage(driver)
    np.switch_navigation('我的')
    # 2、点击我玩过的
    mp = MyPage(driver)
    mp.enter_played_page()
    yield driver


@pytest.fixture(scope='class')
def to_onhook_page(driver):
    """
    进入到云挂机卡片页
    :param driver:
    :return:
    """
    # 1、进入个人中心
    np = NavigationPage(driver)
    np.switch_navigation('我的')
    # 2、进入云挂机卡片页面
    mp = MyPage(driver)
    mp.enter_onhook_page()
    yield driver


@pytest.fixture(scope='class')
def to_onhook_pament(driver):
    """
    进入到云挂机卡片页
    :param driver:
    :return:
    """
    # 1、进入个人中心
    np = NavigationPage(driver)
    np.switch_navigation('我的')
    # 2、进入云挂机支付页面
    mp = MyPage(driver)
    mp.enter_onhook_payment()
    yield driver


@pytest.fixture(scope='class')
def to_fastplay_page(driver):
    """
    进入到快玩卡片页
    :param driver:
    :return:
    """
    # 1、进入个人中心
    np = NavigationPage(driver)
    np.switch_navigation('我的')
    # 2、进入快玩卡片页面
    mp = MyPage(driver)
    mp.enter_fastpaly_page()
    yield driver


@pytest.fixture(scope='class')
def to_monthcard_page2(driver):
    """
    首页进入到月卡页面
    :param driver:
    :return:
    """
    # 1、进入首页
    np = NavigationPage(driver)
    np.switch_navigation('游戏')
    # 2、进入月卡页面
    gp = GamePage(driver)
    gp.enter_monthcard_page()
    yield driver


@pytest.fixture(scope='class')
def to_game_details_page(driver):
    """
    进入游戏详情页
    :param driver:
    :return:
    """
    # 1、进入首页
    np = NavigationPage(driver)
    np.switch_navigation('游戏')
    # 2、搜索游戏
    gp = GamePage(driver)
    gp.enter_search_page(**eval(G_data[0]['request_data']))
    # 3、进入游戏详情页
    gp.enter_details_page()
    yield driver


@pytest.fixture(scope='class')
def to_cloudgame_page(driver):
    """
    进入到云玩页面
    :param driver:
    :return:
    """
    # 1、进入首页
    np = NavigationPage(driver)
    np.switch_navigation('游戏')
    # 2、搜索游戏
    gp = GamePage(driver)
    gp.enter_search_page(**eval(cloud_data[0]['request_data']))
    # 3、进入游戏详情页
    gp.enter_details_page()
    # 4、点击云玩
    gp.click_cloudgame()
    yield driver


@pytest.fixture(scope='class')
def to_community_page2(driver):
    """
    进入游戏社区页
    :param driver:
    :return:
    """
    # 1、进入首页
    np = NavigationPage(driver)
    np.switch_navigation('游戏')
    # 2、搜索游戏
    gp = GamePage(driver)
    gp.enter_search_page(**eval(C_data[0]['request_data']))
    # 4、进入游戏社区页
    gp.enter_community_page()
    yield driver


@pytest.fixture(scope='class')
def to_community_page(driver):
    """
    进入游戏社区页
    :param driver:
    :return:
    """
    # 1、进入个人中心
    np = NavigationPage(driver)
    np.switch_navigation('我的')
    # 2、进入游戏社区页
    hp = HomePage(driver)
    hp.enter_community_page(**eval(C_data[1]['request_data']))
    yield driver


@pytest.fixture(scope='class')
def to_live_page(driver):
    """
    首页直播分栏
    :param driver:
    :return:
    """
    # 1、进入首页
    np = NavigationPage(driver)
    np.switch_navigation('游戏')
    # 2、点击直播分栏
    gp = GamePage(driver)
    gp.enter_live_page(**eval(live_data[0]['request_data']))
    yield driver


@pytest.fixture(scope='class')
def to_firstlaunch_page(driver):
    """
    点击今日首发
    :param driver:
    :return:
    """
    # 1、进入首页
    np = NavigationPage(driver)
    np.switch_navigation('游戏')
    # 2、点击今日首发
    gp = GamePage(driver)
    gp.enter_firstlaunch_page()
    yield driver


@pytest.fixture(scope='class')
def to_sign_page(driver):
    """
    首页签到页面
    :param driver:
    :return:
    """
    # 1、进入首页
    np = NavigationPage(driver)
    np.switch_navigation('游戏')
    # 2、点击签到
    gp = GamePage(driver)
    gp.enter_sign_page()
    yield driver


@pytest.fixture(scope='class')
def to_im_page(driver):
    """
    进入指定群聊
    :param driver:
    :return:
    """
    # 1、点击群聊列表
    np = NavigationPage(driver)
    np.switch_navigation('群聊')
    # 2、进入指定群聊
    im = IMPage(driver)
    im.enter_im_page(**eval(IM_data[0]['request_data']))
    im.delay(3)
    yield driver


@pytest.fixture(scope='class')
def to_role_details_page(driver):
    """
    进入角色详情页
    :param driver:
    :return:
    """
    # 1、进入回收页面
    np = NavigationPage(driver)
    np.switch_navigation('回收')
    # 2、进入角色详情页
    rp = RecoveryPage(driver)
    rp.enter_roles_details(**eval(role_data[0]['request_data']))
    yield driver


@pytest.fixture(scope='class')
def to_role_payment(driver):
    """
    进入角色购买页
    :param driver:
    :return:
    """
    # 1、进入回收页面
    np = NavigationPage(driver)
    np.switch_navigation('回收')
    # 2、进入角色详情页
    rp = RecoveryPage(driver)
    rp.enter_roles_payment(**eval(role_data[0]['request_data']))
    yield driver


@pytest.fixture(scope='class')
def to_init_page(driver):
    """
    进入开局号列表页
    :param driver:
    :return:
    """
    # 1、进入回收页面
    np = NavigationPage(driver)
    np.switch_navigation('回收')
    # 2、进入开局号列表页
    rp = RecoveryPage(driver)
    rp.enter_init_list(**eval(init_data[0]['request_data']))
    yield driver


@pytest.fixture(scope='class')
def to_init_payment(driver):
    """
    进入开局号支付页
    :param driver:
    :return:
    """
    # 1、进入回收页面
    np = NavigationPage(driver)
    np.switch_navigation('回收')
    # 2、进入开局号详情页
    rp = RecoveryPage(driver)
    rp.enter_init_list(**eval(init_data[0]['request_data']))
    rp.enter_init_payment()
    yield driver
