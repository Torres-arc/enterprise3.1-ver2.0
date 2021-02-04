import unittest
from pages.page_05_send_record import sendRecord_page
from pages.login_page import LoginPage
from commons.log import log
from BeautifulReport import BeautifulReport
from commons.driver_setup import *
import os


# @unittest.skip("先跳过")
class SeacrchBysender(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = driver_config()
        cls.driver.implicitly_wait(5)
        LoginPage(cls.driver).login()
        log().info('开始执行:群发记录页面的自动化测试')

    @classmethod
    def tearDownClass(cls):
        log().info('执行结束:群发记录页面的自动化测试')
        cls.driver.quit()


    @BeautifulReport.add_test_img('test_02_serachBytext')
    def test_02_serachBytext(self):
        """群发记录->通过消息内容查询，断言消息内容"""
        log().info('开始执行:用例-通过消息内容查询')
        sendRecord_page(self.driver).searchBytext('自动化测试')
        log().info('执行结束:用例-通过消息内容查询')

    @BeautifulReport.add_test_img('test_03_serachBytype')
    def test_03_serachBytype(self):
        """群发记录->通过群发类型查询，断言群发类型"""
        log().info('开始执行:用例-通过群发类型查询')
        self.driver.refresh()
        sendRecord_page(self.driver).searchBytype()
        log().info('执行结束:用例-通过群发类型查询')

    @BeautifulReport.add_test_img('test_04_serachBytime')
    def test_04_serachBytime(self):
        """群发记录->通过创建时间查询，断言创建时间"""
        log().info('开始执行:用例-通过创建时间查询')
        self.driver.refresh()
        sendRecord_page(self.driver).searchBytime('2020-11-26', '2020-11-26')
        log().info('执行结束:用例-通过创建时间查询')

    @BeautifulReport.add_test_img('test_05_reset')
    def test_05_reset(self):
        """群发记录->重置功能,断言a<=b"""
        log().info('开始执行:用例-重置功能')
        self.driver.refresh()
        sendRecord_page(self.driver).reset('群发自动测试')
        log().info('执行结束:用例-重置功能')


if __name__ == '__main__':
    unittest.main()
