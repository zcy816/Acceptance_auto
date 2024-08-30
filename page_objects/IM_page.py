# !/usr/bin/env python3.8
# encoding: utf-8
# Time:2023/9/18 15:15
# Author:xiaobin
# File:IM_page.py
# Software:PyCharm

from appium.webdriver.common.mobileby import MobileBy
from page_objects.base_page import AppBasePage
from appium.webdriver.common.touch_action import TouchAction


class IMPage(AppBasePage):
    name = '群聊页面'

    # 群聊输入框
    im_input_loc = (MobileBy.ID, 'com.smwl.x7market:id/yunXin_messageEdit_editTextMessage_et')

    # 发送按钮
    send_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/yunXin_messageEdit_commit_tv')

    # 撤回按钮
    withdraw_btn_loc = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="com.smwl.x7market:id/item_tv" and @text="撤回"]')

    # 删除按钮
    delete_btn_loc = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="com.smwl.x7market:id/item_tv" and @text="删除"]')

    # 表情按钮
    emoji_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/yunXin_messageEdit_emoji_iv')

    # emoji通用表情
    universal_emoji_loc = (MobileBy.XPATH, '//androidx.viewpager.widget.ViewPager[@resource-id="com.smwl.x7market:id/scrPlugin"]/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]')

    # 自定义表情
    customize_emoji = (MobileBy.XPATH, '//android.widget.ImageButton[2]')

    # 添加按钮
    add_btn_loc = (MobileBy.XPATH, '//android.widget.GridView/android.widget.LinearLayout[1]')

    # 添加表情
    add_emoji_loc = (MobileBy.XPATH, '//android.widget.GridView[@resource-id="com.smwl.x7market:id/act_x7FaceManage_gridView"]/android.widget.RelativeLayout[1]')

    # 一键获取
    request_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/request_tv')

    # 允许
    allow_btn_loc = (MobileBy.ID, 'com.android.packageinstaller:id/permission_allow_button')

    # 选择图片
    select_picture = (MobileBy.XPATH, '(//android.widget.FrameLayout[@resource-id="com.smwl.x7market:id/picker_photo_grid_item_select_hotpot"])[1]')

    # 确定按钮
    confirm_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/x7_album_community_send_tv')

    # 整理按钮
    sort_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/toolbar_right_operate_tv')

    # 选择表情
    select_emoji = (MobileBy.XPATH, '(//android.widget.CheckBox[@resource-id="com.smwl.x7market:id/item_x7FaceManage_checkBox"])[1]')

    # 删除表情
    delete_emoji_loc = (MobileBy.ID, 'com.smwl.x7market:id/act_x7FaceManage_delete_tv')

    # 返回按钮
    back_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/toolbar_back_iv')

    # 图片
    picture_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/yunXin_messageEdit_addPic_iv')

    # 发送图片
    send_picture_loc = (MobileBy.ID, 'com.smwl.x7market:id/x7_album_send_image_number_tv')

    # 列表右上角按钮
    operate_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/act_myGroup_more_operate_iv')

    # 创建群聊
    create_im_loc = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView')

    # 搜索群聊
    search_im_loc = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.TextView')

    # 群聊更多
    more_btn_loc = (MobileBy.ID, 'com.smwl.x7market:id/toolbar_right_iv')

    # 领取
    receive_gift_loc = (MobileBy.ID, 'com.smwl.x7market:id/credit_gift_look')

    def enter_im_page(self, name):
        """
        根据群聊名称进入指定群聊页面
        :param name:
        :return:
        """
        self.scroll_to_capture_element(name)
        action = '进入群聊：{}'.format(name)
        loc = (MobileBy.XPATH, '//android.widget.TextView[@text="{}"]'.format(name))
        try:
            self.wait_element_is_visible(loc,action).click()
        except Exception as e:
            self.logger.error('未找到群聊：{}'.format(name))
            raise Exception('未找到群聊：{}'.format(name)) from e

    def enter_im_detail(self):
        """
        进入群聊详情页
        :return:
        """
        self.wait_element_is_visible(self.more_btn_loc, '更多').click()

    def create_im(self):
        """
        创建群聊
        :return:
        """
        self.wait_element_is_visible(self.operate_btn_loc, '右上角操作').click()
        self.wait_element_is_visible(self.create_im_loc, '创建群聊').click()

    def search_im(self):
        """
        搜索群聊
        :return:
        """
        self.wait_element_is_visible(self.operate_btn_loc, '右上角操作').click()
        self.wait_element_is_visible(self.search_im_loc, '搜索群聊').click()

    def send_messages(self, msg):
        """
        发送消息/通用表情
        :param msg: 消息内容
        :return:
        """
        try:
            self.wait_element_is_visible(self.im_input_loc, '群聊输入框').send_keys(msg)
            self.wait_element_is_visible(self.send_btn_loc, '发送消息').click()
            self.delay(1)
        except Exception as e:
            self.get_page_screenshot()
            self.logger.error('定位群聊输入框异常')
            raise e

    def withdraw_messages(self, msg):
        """
        撤回消息/通用表情
        :param msg: 被撤回的消息内容
        :return:
        """
        while True:
            try:
                # 被撤回的消息/通用表情
                el = self.driver.find_element(MobileBy.XPATH, ('//android.widget.TextView[@text="{}"]'.format(msg)))
                TouchAction(self.driver).long_press(el).perform()
                # 等待撤回按钮出现
                if self.wait(MobileBy.ID, 'com.smwl.x7market:id/message_long_press_rv'):
                    break
                else:
                    continue
            except Exception as e:
                self.get_page_screenshot()
                self.logger.error('定位群聊输入框异常')
                raise e

        self.wait_element_is_visible(self.withdraw_btn_loc, '撤回按钮').click()
        toast = self.get_toast_msg()
        self.logger.info('消息/通用表情撤回成功')
        self.delay(1)
        return toast

    def delete_message(self, msg):
        """
        删除违规消息
        :param msg: 被删除的消息内容
        :return:
        """
        while True:
            try:
                # 被删除的消息
                el = self.driver.find_element(MobileBy.XPATH, ('//android.widget.TextView[@text="{}"]'.format(msg)))
                TouchAction(self.driver).long_press(el).perform()
                # 等待删除按钮出现
                if self.wait(MobileBy.ID, 'com.smwl.x7market:id/message_long_press_rv'):
                    break
                else:
                    continue
            except Exception as e:
                self.get_page_screenshot()
                self.logger.error('定位群聊输入框异常')
                raise e

        self.wait_element_is_visible(self.delete_btn_loc, '删除按钮').click()
        self.logger.info('违规消息删除成功')
        self.delay(1)

    def add_emoji(self):
        """
        添加自定义表情
        :return:
        toast:成功添加1张图片到我的收藏
        """
        try:
            self.wait_element_is_visible(self.emoji_btn_loc, '表情').click()
            self.wait_element_is_visible(self.customize_emoji, '自定义表情').click()
            self.wait_element_is_visible(self.add_btn_loc, '添加').click()
            self.wait_element_is_visible(self.add_emoji_loc, '添加表情').click()
            if self.wait(MobileBy.XPATH, '//android.widget.TextView[@text="小7手游需获取如下权限"]'):
                self.wait_element_is_visible(self.request_btn_loc, '一键获取').click()
                self.wait_element_is_visible(self.allow_btn_loc, '允许').click()
            self.wait_element_is_visible(self.select_picture, '选择图片').click()
            self.wait_element_is_visible(self.confirm_btn_loc, '确定').click()
            toast = self.get_toast_msg()
            return toast
        except Exception as e:
            self.get_page_screenshot()
            self.logger.error('添加表情失败')
            raise e

    def delete_emoji(self):
        """
        删除自定义表情
        :return:
        toast:成功删除1个表情
        """
        self.wait_element_is_visible(self.sort_btn_loc, '整理').click()
        self.wait_element_is_visible(self.select_emoji, '选择表情').click()
        self.wait_element_is_visible(self.delete_emoji_loc, '删除表情').click()
        try:
            toast = self.get_toast_msg()
            self.wait_element_is_visible(self.back_btn_loc, '返回群聊聊天页').click()
            return toast
        except Exception as e:
            self.get_page_screenshot()
            self.logger.error('删除表情失败')
            raise e

    def send_picture(self):
        """
        发送图片
        :return:
        """
        try:
            self.wait_element_is_visible(self.picture_btn_loc, '图片').click()
            self.wait_element_is_visible(self.select_picture, '选择图片').click()
            self.wait_element_is_visible(self.send_picture_loc, '发送图片').click()
            self.delay(5)
        except Exception as e:
            self.get_page_screenshot()
            self.logger.error('定位群聊图片栏异常')
            raise e

    def withdraw_picture(self):
        """
        撤回图片
        :return:
        """
        while True:
            try:
                # 被撤回的图片
                el = self.driver.find_element(MobileBy.ID, 'com.smwl.x7market:id/message_item_thumb_thumbnail')
                TouchAction(self.driver).long_press(el).perform()
                # 等待撤回按钮出现
                if self.wait(MobileBy.ID, 'com.smwl.x7market:id/message_long_press_rv'):
                    break
                else:
                    continue
            except Exception as e:
                self.get_page_screenshot()
                self.logger.error('定位群聊输入框异常')
                raise e

        self.wait_element_is_visible(self.withdraw_btn_loc, '撤回按钮').click()
        toast = self.get_toast_msg()
        self.logger.info('图片撤回成功')
        self.delay(1)
        return toast

    def verify_message(self, msg):
        """
        校验消息/通用表情发送状态
        :param msg:
        :return:
        """
        try:
            if self.wait(MobileBy.XPATH, '//android.widget.TextView[@text="{}"]'.format(msg)):
                self.logger.info('发送成功')
                return True
            else:
                self.get_page_screenshot()
                self.logger.error('找不到发送的消息/通用表情')
        except Exception as e:
            self.get_page_screenshot()
            self.logger.error('发送异常')
            raise e

    def verify_alert_message(self):
        """
        校验是否发言违规/发送失败
        :return:
        """
        try:
            if self.wait(MobileBy.ID, 'com.smwl.x7market:id/message_item_alert'):
                self.logger.info('存在违规icon')
                return True
            else:
                self.logger.info('找不到违规icon')
                return False
        except Exception as e:
            self.get_page_screenshot()
            self.logger.error('违规消息发送异常')
            raise e

    def verify_picture(self):
        """
        校验图片发送状态
        :return:
        """
        try:
            if self.wait(MobileBy.ID,'com.smwl.x7market:id/message_item_thumb_thumbnail') and self.wait(MobileBy.ID,'com.smwl.x7market:id/message_item_portrait_right'):
                self.logger.info('图片发送成功')
                return True
            else:
                self.get_page_screenshot()
                self.logger.error('找不到发送的图片')
        except Exception as e:
            self.get_page_screenshot()
            self.logger.error('图片发送异常')
            raise e
