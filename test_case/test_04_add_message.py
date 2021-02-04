import unittest
from pages.page_04_add_message import AddmessagePage
from pages.login_page import LoginPage
from commons.log import log
from BeautifulReport import BeautifulReport
from commons.driver_setup import *
from config.readConfig import addmessagepage as amp
import os


# @unittest.skip('1')
class AddMessage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = driver_config()
        cls.driver.implicitly_wait(5)
        LoginPage(cls.driver).login()
        AddmessagePage(cls.driver).switch_to_current()
        log().info('开始执行:新增群发页面的自动化测试')

    @classmethod
    def tearDownClass(cls):
        log().info('执行结束:新增群发页面的自动化测试')
        cls.driver.quit()

    # def save_img(self, img_name):
    #     self.driver.get_screenshot_as_file('{}/{}.png'.format((os.path.abspath('img')), img_name))

    def test_01_addmessage_wb(self):
        """新增群发->发送给客户->文本内容"""
        log().info('开始执行:用例-发送给客户->文本内容')
        self.driver.get('https://platform.wshoto.com/co/message/add-group-send')
        AddmessagePage(self.driver).send_message('client', 'text', amp.msg, amp.sender)
        self.driver.get('https://platform.wshoto.com/co/message/add-group-send')
        log().info('执行结束:用例-发送给客户->文本内容')

    def test_02_addmessage_web(self):
        """新增群发->发送给客户->网页内容"""
        log().info('开始执行:用例-发送给客户->网页内容')
        self.driver.get('https://platform.wshoto.com/co/message/add-group-send')
        AddmessagePage(self.driver).send_message('client', 'web', amp.msg, amp.sender)
        self.driver.get('https://platform.wshoto.com/co/message/add-group-send')
        log().info('执行结束:用例-发送给客户->网页内容')

    def test_03_addmessage_pic(self):
        """新增群发->发送给客户->图片内容"""
        log().info('开始执行:用例-发送给客户->图片内容')
        self.driver.get('https://platform.wshoto.com/co/message/add-group-send')
        AddmessagePage(self.driver).send_message('client', 'pic', amp.msg, amp.sender)
        self.driver.get('https://platform.wshoto.com/co/message/add-group-send')
        log().info('执行结束:用例-发送给客户->图片内容')

    def test_04_addmessage_pos(self):
        """新增群发->发送给客户->海报内容"""
        log().info('开始执行:用例-发送给客户->海报内容')
        self.driver.get('https://platform.wshoto.com/co/message/add-group-send')
        AddmessagePage(self.driver).send_message('client', 'poster', amp.msg, amp.sender)
        self.driver.get('https://platform.wshoto.com/co/message/add-group-send')
        log().info('执行结束:用例-发送给客户->海报内容')

    def test_05_addmessage_mini(self):
        """新增群发->发送给客户->小程序内容"""
        log().info('开始执行:用例-发送给客户->小程序内容')
        self.driver.get('https://platform.wshoto.com/co/message/add-group-send')
        AddmessagePage(self.driver).send_message('client', 'mini', amp.msg, amp.sender)
        self.driver.get('https://platform.wshoto.com/co/message/add-group-send')
        log().info('执行结束:用例-发送给客户->小程序内容')

    def test_06_addmessage_text_group(self):
        """新增群发->发送给客户群->文本内容"""
        log().info('开始执行:用例-发送给客户群->文本内容')
        self.driver.get('https://platform.wshoto.com/co/message/add-group-send')
        AddmessagePage(self.driver).send_message('group', 'text', amp.msg, amp.sender)
        self.driver.get('https://platform.wshoto.com/co/message/add-group-send')
        log().info('执行结束:用例-发送给客户群->文本内容')

    def test_07_addmessage_web_group(self):
        """新增群发->发送给客户群->网页内容"""
        log().info('开始执行:用例-发送给客户群->网页内容')
        self.driver.get('https://platform.wshoto.com/co/message/add-group-send')
        AddmessagePage(self.driver).send_message('group', 'web', amp.msg, amp.sender)
        self.driver.get('https://platform.wshoto.com/co/message/add-group-send')
        log().info('执行结束:用例-发送给客户群->网页内容')

    def test_08_addmessage_pic_group(self):
        """新增群发->发送给客户群->图片内容"""
        log().info('开始执行:用例-发送给客户群->图片内容')
        self.driver.get('https://platform.wshoto.com/co/message/add-group-send')
        AddmessagePage(self.driver).send_message('group', 'pic', amp.msg, amp.sender)
        self.driver.get('https://platform.wshoto.com/co/message/add-group-send')
        log().info('执行结束:用例-发送给客户群->图片内容')

    def test_09_addmessage_pos_group(self):
        """新增群发->发送给客户群->海报内容"""
        log().info('开始执行:用例-发送给客户群->海报内容')
        self.driver.get('https://platform.wshoto.com/co/message/add-group-send')
        AddmessagePage(self.driver).send_message('group', 'poster', amp.msg, amp.sender)
        self.driver.get('https://platform.wshoto.com/co/message/add-group-send')
        log().info('执行结束:用例-发送给客户群->海报内容')

    def test_10_addmessage_mini_group(self):
        """新增群发->发送给客户群->小程序内容"""
        log().info('开始执行:用例-发送给客户群->小程序内容')
        self.driver.get('https://platform.wshoto.com/co/message/add-group-send')
        AddmessagePage(self.driver).send_message('group', 'mini', amp.msg, amp.sender)
        self.driver.get('https://platform.wshoto.com/co/message/add-group-send')
        log().info('执行结束:用例-发送给客户群->小程序内容')


if __name__ == '__main__':
    unittest.main()
