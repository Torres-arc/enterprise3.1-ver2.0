from pages.page_08_welcoming_message import WelcomingMessagePage
import unittest
from selenium import webdriver
from commons.base_page import BasePage
from config.readConfig import *
from pages.login_page import LoginPage
from commons.log import log

# 欢迎语
class EmployeeWelcomingMessage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)
        LoginPage(cls.driver).login()
        WelcomingMessagePage(cls.driver).click_welcoming_message_page()
        log().info('开始执行:欢迎语页面的自动化测试')
    @classmethod
    def tearDownClass(cls):
        log().info('执行结束:欢迎语页面的自动化测试')
        cls.driver.quit()

    # @unittest.skip('1')
    def test_01_addEmwelcomingmessage(self,):
        """测试员工欢迎语_添加"""
        log().info('开始执行:用例-员工欢迎语_添加')
        WelcomingMessagePage(self.driver).addEmmessage()
        self.driver.refresh()
        log().info('执行结束:用例-员工欢迎语_添加')

    # @unittest.skip('1')
    def test_02_editEmwelcomingmessage(self,):
        """测试员工欢迎语_编辑"""
        self.driver.refresh()
        log().info('开始执行:用例-员工欢迎语_编辑')
        WelcomingMessagePage(self.driver).editEmmessage()
        self.driver.refresh()
        log().info('执行结束:用例-员工欢迎语_编辑')

    # @unittest.skip('1')
    def test_03_deleteEmwelcomingmessage(self,):
        """测试员工欢迎语_删除"""
        self.driver.refresh()
        log().info('开始执行:用例-员工欢迎语_删除')
        WelcomingMessagePage(self.driver).deleteEmmessage()
        self.driver.refresh()
        log().info('执行结束:用例-员工欢迎语_删除')

    # @unittest.skip('1')
    def test_04_addDeptemwelcomingmessage(self,):
        """测试部门员工欢迎语_添加"""
        self.driver.refresh()
        log().info('开始执行:用例-部门员工欢迎语_添加')
        WelcomingMessagePage(self.driver).addDeptemmessage('云书')
        self.driver.refresh()
        log().info('执行结束:用例-部门员工欢迎语_添加')

    # @unittest.skip('1')
    def test_05_editDeptemwelcomingmessage(self,):
        """测试部门员工欢迎语_编辑"""
        self.driver.refresh()
        log().info('开始执行:用例-部门员工欢迎语_编辑')
        WelcomingMessagePage(self.driver).editDeptemmessage()
        self.driver.refresh()
        log().info('执行结束:用例-部门员工欢迎语_编辑')

    # @unittest.skip('1')
    def test_06_deleteDeptemwelcomingmessage(self,):
        """测试部门员工欢迎语_删除"""
        self.driver.refresh()
        log().info('开始执行:用例-部门员工欢迎语_删除')
        WelcomingMessagePage(self.driver).deleteDeptemmessage()
        self.driver.refresh()
        log().info('执行结束:用例-部门员工欢迎语_删除')

    # def test_07_addCpwelcomingmessage(self,):
    #     """测试客户群欢迎语_添加"""
    #     self.driver.refresh()
    #     log().info('开始执行:用例-客户群欢迎语_添加')
    #     WelcomingMessagePage(self.driver).addCpmessage()
    #     self.driver.refresh()
    #     log().info('执行结束:用例-客户群欢迎语_添加')
    #
    # def test_08_editCpwelcomingmessage(self,):
    #     """测试客户群欢迎语_编辑"""
    #     self.driver.refresh()
    #     log().info('开始执行:用例-客户群欢迎语_编辑')
    #     WelcomingMessagePage(self.driver).editCpmessage()
    #     self.driver.refresh()
    #     log().info('执行结束:用例-客户群欢迎语_编辑')
    #
    # def test_09_deleteCpwelcomingmessage(self,):
    #     """测试客户群欢迎语_删除"""
    #     self.driver.refresh()
    #     log().info('开始执行:用例-客户群欢迎语_删除')
    #     WelcomingMessagePage(self.driver).deleteCpmessage()
    #     log().info('执行结束:用例-客户群欢迎语_删除')


if __name__ == '__main__':
    unittest.main()
