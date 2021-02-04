import unittest
from selenium import webdriver

from commons.driver_setup import driver_config
from pages.login_page import LoginPage
from pages.page_50_loss_remind import LossRemind
from commons.base_page import BasePage
from config.readConfig import *
from BeautifulReport import BeautifulReport
from commons.log import log

'''云晗编写'''
@unittest.skip('1')
class TestLossRemind(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = driver_config()
        cls.driver.implicitly_wait(5)
        LoginPage(cls.driver).login()
        LossRemind(cls.driver).click_btn_loss_remind()
        log().info('开始执行:流失提醒页面的自动化测试')
    @classmethod
    def tearDownClass(cls):
        log().info('执行结束:流失提醒页面的自动化测试')
        cls.driver.quit()

    def test_01_searchByClientName(self):
        """测试按照客户姓名查询"""
        log().info('开始执行:用例-按客户姓名查询')
        LossRemind(self.driver).search_by_name(lossremindpage.name)
        log().info('执行结束:用例-按客户姓名查询')
        self.driver.refresh()

    # def test_02_searchByAdder(self):
    #     """测试按照客户添加人查询"""
    #     self.driver.refresh()
    #     log().info('开始执行:用例-按客户添加人查询')
    #     LossRemind(self.driver).search_by_adder(lossremindpage.adder)
    #     log().info('执行结束:用例-按客户添加人查询')
    #     self.driver.refresh()

    def test_03_searchByTag(self):
        """测试按照客户标签查询"""
        self.driver.refresh()
        log().info('开始执行:用例-按客户标签查询')
        LossRemind(self.driver).search_by_tag(lossremindpage.tag_group, lossremindpage.tag)
        log().info('执行结束:用例-按客户标签查询')
        self.driver.refresh()

    def test_04_buttonReset(self):
        """测试重置功能"""
        self.driver.refresh()
        log().info('开始执行:用例-查询条件重置功能')
        LossRemind(self.driver).reset(lossremindpage.name)
        log().info('执行结束:用例-查询条件重置功能')
        self.driver.refresh()

if __name__ == '__main__':
    unittest.main()