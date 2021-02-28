from pages.page_08_welcoming_message import WelcomingMessagePage
import unittest
from selenium import webdriver
from config.readConfig import welcomingmsgpage as wmp
from pages.login_page import LoginPage
from commons.log import log


# 欢迎语
class EmployeeWelcomingMessage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)
        LoginPage(cls.driver).login()
        WelcomingMessagePage(cls.driver).switch_to_current()
        log().info('开始执行:欢迎语页面的自动化测试')
    @classmethod
    def tearDownClass(cls):
        log().info('执行结束:欢迎语页面的自动化测试')
        cls.driver.quit()

    # @unittest.skip('1')
    def test_01_addEmwelcomingmessage(self,):
        """测试员工欢迎语_添加"""
        log().info('开始执行:用例-员工欢迎语_添加')
        WelcomingMessagePage(self.driver).create_welcome('client', wmp.msg)
        log().info('执行结束:用例-员工欢迎语_添加')

    def test_02_searchClientWel(self,):
        """测试员工欢迎语_搜索"""
        log().info('开始执行:用例-员工欢迎语_搜索')
        WelcomingMessagePage(self.driver).search_key_words('client', wmp.key)
        log().info('执行结束:用例-员工欢迎语_搜索')

    # @unittest.skip('1')
    def test_03_editEmwelcomingmessage(self,):
        """测试员工欢迎语_编辑"""
        self.driver.refresh()
        log().info('开始执行:用例-员工欢迎语_编辑')
        WelcomingMessagePage(self.driver).edit_welcome('client', wmp.edited_msg)
        self.driver.refresh()
        log().info('执行结束:用例-员工欢迎语_编辑')

    # @unittest.skip('1')
    def test_04_deleteEmwelcomingmessage(self,):
        """测试员工欢迎语_删除"""
        self.driver.refresh()
        log().info('开始执行:用例-员工欢迎语_删除')
        WelcomingMessagePage(self.driver).delete_wel('client', wmp.edited_msg)
        self.driver.refresh()
        log().info('执行结束:用例-员工欢迎语_删除')

    # @unittest.skip('1')
    def test_05_addDeptemwelcomingmessage(self,):
        """测试部门员工欢迎语_添加"""
        self.driver.refresh()
        log().info('开始执行:用例-部门员工欢迎语_添加')
        WelcomingMessagePage(self.driver).create_welcome('dep', wmp.msg, staff=wmp.staff)
        self.driver.refresh()
        log().info('执行结束:用例-部门员工欢迎语_添加')

    def test_06_searchDepClientWel(self,):
        """测试部门员工欢迎语_搜索"""
        log().info('开始执行:用例-部门员工欢迎语_搜索')
        WelcomingMessagePage(self.driver).search_key_words('dep', wmp.key)
        log().info('执行结束:用例-部门员工欢迎语_搜索')

    # @unittest.skip('1')
    def test_05_editDeptemwelcomingmessage(self,):
        """测试部门员工欢迎语_编辑"""
        self.driver.refresh()
        log().info('开始执行:用例-部门员工欢迎语_编辑')
        WelcomingMessagePage(self.driver).edit_welcome('dep', wmp.edited_msg)
        self.driver.refresh()
        log().info('执行结束:用例-部门员工欢迎语_编辑')

    # @unittest.skip('1')
    def test_06_deleteDeptemwelcomingmessage(self,):
        """测试部门员工欢迎语_删除"""
        self.driver.refresh()
        log().info('开始执行:用例-部门员工欢迎语_删除')
        WelcomingMessagePage(self.driver).edit_welcome('dep', wmp.edited_msg)
        self.driver.refresh()
        log().info('执行结束:用例-部门员工欢迎语_删除')


if __name__ == '__main__':
    unittest.main()
