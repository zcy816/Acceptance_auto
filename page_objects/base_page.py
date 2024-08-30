# !/usr/bin/env python3.8
# encoding: utf-8
# Time:2023/8/6 17:17
# Author:xiaobin
# File:base_page.py
# Software:PyCharm

import os
import re
import time
import subprocess
import settings
from common import logger
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction

# import pytesseract
# from PIL import Image


class BasePage:
    """
    页面类的基类
    1、定位 等待 - 定位
    2、点击 等待 - 定位 - 点击
    3、输入 等待 - 定位 - 输入
    4、获取元素文本 等待 - 定位 - 获取文本
    5、获取属性 等待 - 定位 - 获取属性
    6、窗口切换
    7、失败截图

    等待是显示等待结合 time.sleep
    需要有日志
    需要链式编程
    """

    name = 'base页面'
    logger = logger
    settings = settings

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.element = None
        self.locator = None
        self.action = ''

    def delay(self, num):
        """
        延迟num秒，可以是浮点数 1表示1秒 0.5表示0.5秒
        :param num:
        :return:
        """
        time.sleep(num)
        return self

    def wait_element_is_visible(self, locator, action='', **kwargs):
        """
        等待元素可见,渲染出来
        :param locator: 定位信息 tuple(by, exp)
        :param action: 操作说明 str
        :param kwargs: timeout, poll_frequency
        :return:
        """
        self.locator = locator
        self.action = action
        try:
            timeout = kwargs.get('timeout', self.settings.DEFAULT_TIMEOUT)
            poll_frequency = kwargs.get('poll_frequency', 0.1)
            self.element = WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.visibility_of_element_located(locator)
            )
        except Exception as e:
            # 记录日志
            self.logger.error(
                '在{}，{}操作的时候，等待{}元素可见【失败】'.format(self.name, self.action, self.locator)
            )
            # 失败保存当前截图
            raise e
        else:
            self.logger.info(
                '在{}，{}操作的时候，等待{}元素可见【成功】'.format(self.name, action, locator)
            )
            return self

    def wait_element_is_presence(self, locator, action='', **kwargs):
        """
        等待元素在dom树中出现
        :param locator:
        :param action:
        :param kwargs:
        :return:
        """
        self.locator = locator
        self.action = action
        try:
            timeout = kwargs.get('timeout', self.settings.DEFAULT_TIMEOUT)
            poll_frequency = kwargs.get('poll_frequency', 0.5)
            self.element = WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.presence_of_element_located(locator))
        except Exception as e:
            # 记录日志
            self.logger.error(
                '在{}，{}操作的时候，等待{}元素可见【失败】'.format(self.name, action, locator)
            )
            # 失败保存当前截图
            raise e
        else:
            self.logger.info(
                '在{}，{}操作的时候，等待{}元素可见【成功】'.format(self.name, action, locator)
            )
            return self

    def wait(self, loc, vaule):
        """
        等待元素出现
        :param loc:
        :param vaule:
        :return:
        """
        try:
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element(loc, vaule))
            return True
        except Exception as e:
            return False

    def long_wait(self, loc, vaule):
        """
        长时间等待元素出现
        :param loc:
        :param vaule:
        :return:
        """
        try:
            WebDriverWait(self.driver, 60).until(lambda x: x.find_element(loc, vaule))
            return True
        except Exception as e:
            return False

    def send_keys(self, content):
        """
        输入内容
        :param content:
        :return:
        """
        if self.element is None:
            raise RuntimeError('不能在wait前调用元素上的方法')

        try:
            # 先清空内容
            self.element.clear()
            self.element.send_keys(content)
        except Exception as e:
            self.get_page_screenshot()
            self.logger.error(
                '在{}, {}操作的时候，对{}元素输入{}【失败】'.format(self.name, self.action, self.locator, content))
            self.logger.error(e)
        else:
            self.logger.info(
                '在{}, {}操作的时候，对{}元素输入{}【成功】'.format(self.name, self.action, self.locator, content))
        finally:
            self.__clear_cache()

    def click(self):
        """
        :return:
        """
        if self.element is None:
            raise RuntimeError('不能在wait前调用元素上的方法')

        try:
            self.element.click()
        except Exception as e:
            self.get_page_screenshot()
            self.logger.error(
                '在{}，{}操作的时候，对{}元素点击【失败】'.format(self.name, self.action, self.locator)
            )
            raise e
        else:
            self.logger.info(
                '在{}，{}操作的时候，对{}元素点击【成功】'.format(self.name, self.action, self.locator)
            )
        finally:
            self.__clear_cache()

    def get_element(self):
        if self.element is None:
            raise RuntimeError('不能在wait前调用元素上的方法')

        try:
            return self.element
        except Exception as e:
            raise e
        finally:
            self.__clear_cache()

    def get_text(self):
        """
        获取元素的text
        :return:
        """
        if self.element is None:
            raise RuntimeError('不能在wait前调用元素上的方法')
        try:
            text = self.element.text
        except Exception as e:
            self.get_page_screenshot()
            self.logger.error(
                '在{}，{}操作的时候，获取{}元素的text【失败】'.format(self.name, self.action, self.locator)
            )
            raise e
        else:
            self.logger.info(
                '在{}，{}操作的时候，获取{}元素的text【成功】'.format(self.name, self.action, self.locator)
            )
            return text
        finally:
            self.__clear_cache()

    def get_attr(self, name):
        """
        获取元素的属性
        :param name:
        :return:
        """
        if self.element is None:
            raise RuntimeError('不能在wait前调用元素上的方法')

        try:
            attr = self.element.get_attribute(name)
        except Exception as e:
            self.get_page_screenshot()
            self.logger.error(
                '在{}，{}操作的时候，获取{}元素的{}属性【失败】'.format(self.name, self.action, self.locator, name)
            )
            raise e
        else:
            self.logger.info(
                '在{}，{}操作的时候，获取{}元素的text【成功】'.format(self.name, self.action, self.locator, name)
            )
            return attr
        finally:
            self.__clear_cache()

    def get_page_screenshot(self):
        """
        获取报错时的页面截图，命名规范 xx页面_xx操作_截图时间.png
        :param self:
        :return:
        """
        # 1、拼接错误截图的路径
        img_path = os.path.join(self.settings.ERROR_SCREENSHOT_DIR,
                                "{}_{}_{}.png".format(self.name, self.action,
                                                      datetime.now().strftime('%Y-%m-%d %H-%M-%S')))
        if self.driver.save_screenshot(img_path):
            self.logger.info('生成错误截图：{} 【成功】'.format(img_path))
        else:
            self.logger.info('生成错误截图：{} 【失败】'.format(img_path))

    def __clear_cache(self):
        """
        清空wait的缓存，让动作链之间相隔离
        :return:
        """
        self.element = None
        self.element = None
        self.action = ''

    def switch_to_new_window(self, handle=None, action=''):
        """
        切换到新的窗口
        :param handle:
        :param action:
        :return:
        """
        self.aciton = action
        try:
            if handle:
                self.driver.switch_to.window(handle)
            else:
                original_window = self.driver.current_window_handle
                for handle in self.driver.window_handles:
                    if handle != original_window:
                        self.driver.switch_to.window(handle)
                        break
        except Exception as e:
            self.get_page_screenshot()
            self.logger.error(
                '在{}，{}操作的时候，切换到窗口{}【失败】'.format(self.name, self.action, handle)
            )
            raise e
        else:
            self.logger.lnfo(
                '在{}，{}操作的时候，切换到窗口{}【成功】'.format(self.name, self.action, handle)
            )
        finally:
            self.action = ''

    def click_element_by_js(self):
        """
        通过js点击元素
        :return:
        """
        if self.element is None:
            raise RuntimeError('不能在wait方法之前调用元素上的方法')
        try:
            self.driver.execute_script('arguments[0].click()', self.element)
        except Exception as e:
            self.logger.exception(
                '在{}，{}操作的时候，切换到窗口{}【失败】'.format(self.name, self.action, self.locator)
            )
            self.get_page_screenshot()
            raise e
        else:
            self.logger.info(
                '在{}，{}操作的时候，点击元素{}【成功】'.format(self.name, self.action, self.locator)
            )
        finally:
            self.__clear_cache()


class AppBasePage(BasePage):
    name = 'app base 页面'

    def get_toast_text(self, timeout=5, poll_frequency=0.1):
        """
        从页面源码中获取所有toast消息的文本
        :param timeout: 最大等待时间
        :param poll_frequency: 轮询间隔
        :return: 所有toast消息的文本列表
        """
        end_time = time.time() + timeout
        all_toast_texts = []
        while True:
            try:
                page_source = self.driver.page_source
                matches = re.findall(r'class="android.widget.Toast" text="(.*?)"', page_source)
                if matches:
                    all_toast_texts.extend(matches)
                    text = '\n'.join(all_toast_texts)
                    print("\n\n===============toast文本如下：================")
                    print(text)
                    return text
                else:
                    if time.time() > end_time:
                        print("\n\n===============页面源码如下：================")
                        print(page_source)
                        raise Exception('捕获toast超时：未找到toast文本')
                    time.sleep(poll_frequency)
            except Exception as e:
                self.get_page_screenshot()
                self.logger.error('捕获toast文本失败')
                raise e

    def get_toast_msg(self, action='', timeout=3, poll_frequency=0.1):
        """
        获取toast信息
        :param action: 操作描述
        :param timeout: 最大等待时间，默认3秒
        :param poll_frequency: 轮询间隔，默认0.1秒
        :return: toast消息的文本
        """
        self.loc = ('xpath', '//*[@class="android.widget.Toast"]')
        self.action = action

        try:
            # 使用WebDriverWait进行动态等待
            toast_element = WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.presence_of_element_located(self.loc)
            )
            text = toast_element.text
            self.logger.info(f'在{self.name}页面，{self.action}操作时，获取toast信息成功')
            return text
        except Exception as e:
            self.logger.error(f'在{self.name}页面，{self.action}操作时，获取toast信息失败，错误信息：{e}')
            self.get_page_screenshot()
            raise e

    def swipe_by_direction(self, direct='up', distance=200, duration=0, action=''):
        """
        按方向滑动
        :param direct: up、down、left、right
        :param distance: 滑动距离，像素，int
        :param duration: 滑动时间，毫秒
        :param action: 动作说明
        :return:
        """
        # 获取屏幕的尺寸
        size = self.driver.get_window_size()
        self.action = action
        start_x = size['width'] // 2
        start_y = size['height'] * 2 // 3
        direct = direct.strip().lower()
        if direct == 'up':
            end_x = start_x
            end_y = start_y - distance
        elif direct == 'down':
            end_x = start_x
            end_y = start_y + distance
        elif direct == 'left':
            end_x = start_x - distance
            end_y = start_y
        elif direct == 'right':
            end_x = start_x + distance
            end_y = start_y
        else:
            raise ValueError('请输入正确的方向')
        try:
            self.driver.swipe(start_x, start_y, end_x, end_y, duration)
        except Exception as e:
            self.get_page_screenshot()
            self.logger.error(
                '在{}页面，{}操作的时候，向{}滑动{}像素时失败'.format(self.name, self.action, direct, distance))
            raise e
        else:
            self.logger.info(
                '在{}页面，{}操作的时候，向{}滑动{}像素时成功'.format(self.name, self.action, direct, distance))
        finally:
            self.action = ''

    def swipe_by_coordinates_and_direction(self, start_x: int, start_y: int, direction: str, distance: int, duration: int) -> None:
        """
        按指定坐标和方向滑动指定距离和指定时长
        :param start_x: 起始x坐标
        :param start_y: 起始y坐标
        :param direction: 滑动方向，'up'、'down'、'left'、'right'
        :param distance: 滑动距离
        :param duration: 滑动时长，单位毫秒
        :return: None
        """
        action = TouchAction(self.driver)
        direction = direction.strip().lower()

        if direction == 'up':
            end_x = start_x
            end_y = start_y - distance
        elif direction == 'down':
            end_x = start_x
            end_y = start_y + distance
        elif direction == 'left':
            end_x = start_x - distance
            end_y = start_y
        elif direction == 'right':
            end_x = start_x + distance
            end_y = start_y
        else:
            raise ValueError('请输入正确的方向')

        try:
            action.press(x=start_x, y=start_y).wait(ms=duration).move_to(x=end_x, y=end_y).release().perform()
        except Exception as e:
            self.logger.error(
                f"从坐标 ({start_x}, {start_y}) 向 {direction} 滑动 {distance} 距离失败，错误信息：{str(e)}")
            raise
        else:
            self.logger.info(f"从坐标 ({start_x}, {start_y}) 向 {direction} 滑动 {distance} 距离成功")

    def clear_message(self):
        """
        清空通知栏
        :return:
        """
        # 通知栏消息
        clear_btn_loc = (MobileBy.ID, 'com.android.systemui:id/dismiss_view')

        # 打开通知栏
        self.driver.open_notifications()
        try:
            if self.wait(MobileBy.ID, 'com.android.systemui:id/dismiss_view'):
                self.wait_element_is_visible(clear_btn_loc, '清空通知栏消息').click()
            else:
                # 关闭通知栏
                self.driver.press_keycode(4)
        except Exception as e:
            self.logger.error('通知栏清理消息异常')
            raise e

    def get_code(self):
        """
        获取短信验证码
        :return:
        """
        # 打开通知栏
        self.driver.open_notifications()
        self.delay(15)
        dx = self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "验证码用于登录")]')
        code = ', '.join(re.findall(r'\d{6}', dx.text))
        self.logger.info("---- 获取到的验证码是{} ----".format(code))
        self.driver.press_keycode(4)
        return code

    def set_press_code(self, num):
        """
        通过键盘操作，仅支持安卓设备
        :return:
        """
        num = int(num)
        if num == 0:
            self.driver.press_keycode(7)
        elif num == 1:
            self.driver.press_keycode(8)
        elif num == 2:
            self.driver.press_keycode(9)
        elif num == 3:
            self.driver.press_keycode(10)
        elif num == 4:
            self.driver.press_keycode(11)
        elif num == 5:
            self.driver.press_keycode(12)
        elif num == 6:
            self.driver.press_keycode(13)
        elif num == 7:
            self.driver.press_keycode(14)
        elif num == 8:
            self.driver.press_keycode(15)
        elif num == 9:
            self.driver.press_keycode(16)
        else:
            logger.error('输入的数字有误')

    def scroll_to_capture_element(self, ele):
        """
        滑动捕获指定元素
        :param ele:
        :return:
        """
        action = '滑动捕获{}元素'.format(ele)
        directions = ['down', 'up']  # 先向下滚动，再向上滚动
        for direction in directions:
            page_source = ''
            while True:
                try:
                    if self.wait(MobileBy.XPATH, '//android.widget.TextView[@text="{}"]'.format(ele)):
                        break
                    else:
                        # 如果页面源码没有变化，表示已经滚动到底部或顶部，跳出循环
                        new_page_source = self.driver.page_source
                        if new_page_source == page_source:
                            break
                        page_source = new_page_source

                    # 没有找到就滑动
                    self.swipe_by_direction(direction, action=action, duration=200, distance=500)
                    self.delay(1)
                except Exception as e:
                    self.logger.error('在滑动和查找时发生错误: {}'.format(e))
                    raise e

    def restart_app(self):
        """
        重新启动APP,杀死进程
        :return:
        """
        subprocess.Popen("adb shell am force-stop com.smwl.x7market", shell=True, stdout=subprocess.PIPE)
        subprocess.Popen("adb shell am start -n com.smwl.x7market/.activity.SplashActivity", shell=True,stdout=subprocess.PIPE)
        while True:
            if self.long_wait(MobileBy.XPATH, '//android.widget.TextView[@text="推荐"]'):
                self.logger.info('APP重启成功')
                break
            else:
                continue

    def return_app(self):
        """
        返回APP，不杀死进程
        :return:
        """
        subprocess.Popen("adb shell am start -n com.smwl.x7market/.activity.SplashActivity", shell=True,stdout=subprocess.PIPE)
        self.delay(1)

    def clear_channels(self):
        """
        清理支付渠道进程
        :return:
        """
        subprocess.Popen("adb shell am force-stop com.unionpay", shell=True, stdout=subprocess.PIPE)
        subprocess.Popen("adb shell am force-stop com.eg.android.AlipayGphone", shell=True, stdout=subprocess.PIPE)
        subprocess.Popen("adb shell am force-stop com.tencent.mm", shell=True, stdout=subprocess.PIPE)
        self.delay(1)

    def return_desktop(self):
        """
        返回手机桌面
        :return:
        """
        self.delay(1)
        subprocess.Popen("adb shell input keyevent KEYCODE_HOME", shell=True,stdout=subprocess.PIPE)

    def return_home(self):
        """
        返回APP首页
        :return:
        """
        while True:
            try:
                subprocess.Popen("adb shell input keyevent KEYCODE_BACK", shell=True, stdout=subprocess.PIPE)
                if self.wait(MobileBy.XPATH, '//*[@text="游戏"]') and self.wait(MobileBy.XPATH, '//*[@text="群聊"]') and self.wait(MobileBy.XPATH, '//*[@text="回收"]') and self.wait(MobileBy.XPATH, '//*[@text="我的"]'):
                    break
                else:
                    continue
            except Exception as e:
                self.get_page_screenshot()
                self.logger.error('返回APP首页异常')
                raise e

    def clear_fastplay(self):
        """
        清除快玩启动器进程
        :return:
        """
        subprocess.Popen("adb shell am force-stop com.smwl.auxiliary64bit", shell=True, stdout=subprocess.PIPE)
        subprocess.Popen("adb shell am force-stop com.smwl.x7market", shell=True, stdout=subprocess.PIPE)
        self.delay(3)
        subprocess.Popen("adb shell am start -n com.smwl.x7market/.activity.SplashActivity", shell=True,stdout=subprocess.PIPE)
        self.delay(3)

    def check_login(self):
        """
        校验登录状态
        """
        # 我的按钮
        my_loc = (MobileBy.XPATH, '//android.widget.TextView[@text="我的"]')
        # 登录按钮
        login_loc = (MobileBy.ID, 'com.smwl.x7market:id/user_login_arrow_iv')
        self.wait_element_is_visible(my_loc, '我的').click()
        try:
            if self.wait(MobileBy.XPATH, '//android.widget.TextView[@text="未登录"]'):
                self.wait_element_is_visible(login_loc, '登录').click()
                return False
            else:
                return True
        except Exception as e:
            self.logger.error('登录状态异常')
            raise e

    def check_monthcard_type(self):
        """
        判断用户是否开通月卡
        :return:
        """
        if self.wait(MobileBy.XPATH, '//android.widget.TextView[@text="未开通"]'):
            return True
        else:
            return False

    def click_coordinates(self, x: int, y: int) -> None:
        """
        点击指定坐标
        :param x: x坐标
        :param y: y坐标
        :return: None
        """
        self.logger.info(f"开始点击坐标 ({x}, {y})")
        try:
            TouchAction(self.driver).tap(x=x, y=y).perform()
        except Exception as e:
            self.logger.error(f"点击坐标 ({x}, {y}) 失败，错误信息：{str(e)}")
            raise
        else:
            self.logger.info(f"点击坐标 ({x}, {y}) 成功")

    # def ocr_crop_and_save(self, image_path, pixel_coordinates, output_path):
    #     """
    #     ocr 指定坐标截图识别功能
    #     :param image_path: 指定图片路径
    #     :param pixel_coordinates: 需要截图的坐标,已列表传入[1,2,3,4]
    #     :param output_path: 输出存放截图的路径
    #     :return:
    #     """
    #
    #     name = self.driver.save_screenshot('./screenshots/image')
    #
    #     image_path = ''
    #     image = Image.open(image_path)
    #     cropped_image = image.crop(
    #         (pixel_coordinates[0], pixel_coordinates[1], pixel_coordinates[2], pixel_coordinates[3]))
    #     cropped_image.save(output_path)
    #     cropped_text = pytesseract.image_to_string(cropped_image)
    #     return cropped_text
