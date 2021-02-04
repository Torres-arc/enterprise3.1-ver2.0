import unittest
from selenium import webdriver

from commons.driver_setup import driver_config
from pages.login_page import LoginPage
from pages.page_17_chat_toolbar import ChatToolbarPage
from commons.base_page import BasePage
from config.readConfig import *
from commons.log import log
from BeautifulReport import BeautifulReport


class TestChatToolbar(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = driver_config()
        cls.driver.implicitly_wait(5)
        LoginPage(cls.driver).login()
        ChatToolbarPage(cls.driver).switch_to_current()
        log().info('开始执行:聊天工具栏 页面的自动化测试')
    @classmethod
    def tearDownClass(cls):
        log().info('执行结束:聊天工具栏 页面的自动化测试')
        cls.driver.quit()

    # @unittest.skip('1')
    def test_01_getnum(self):
        """验证抓取素材数量"""
        log().info('开始执行:用例-验证抓取素材数量')
        ChatToolbarPage(self.driver).check_num()
        log().info('执行结束:用例-验证抓取素材数量')
        self.driver.refresh()

    def test_02_check_button(self):
        """验证抓取开关正常"""
        self.driver.refresh()
        log().info('开始执行:用例-验证抓取开关正常')
        ChatToolbarPage(self.driver).check_btn_open()
        log().info('执行结束:用例-验证抓取开关正常')


if __name__ == '__main__':
    unittest.main()
