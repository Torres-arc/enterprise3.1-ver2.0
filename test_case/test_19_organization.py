import unittest
from selenium import webdriver

from commons.driver_setup import driver_config
from pages.login_page import LoginPage
from pages.page_19_organization import OrganizationPage
from commons.base_page import BasePage
from config.readConfig import *
from commons.log import log
from BeautifulReport import BeautifulReport


class TestOrganization(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = driver_config()
        cls.driver.implicitly_wait(5)
        LoginPage(cls.driver).login()
        OrganizationPage(cls.driver).switch_to_current()
        log().info('开始执行:组织架构 页面的自动化测试')
    @classmethod
    def tearDownClass(cls):
        log().info('执行结束 组织架构 页面的自动化测试')
        cls.driver.quit()

    def test_01_searchStaff(self):
        """测试搜索员工"""
        log().info('开始执行:用例-按关键词查询')
        OrganizationPage(self.driver).search_staff(organizationpage.name)
        log().info('执行结束:用例-按关键词查询')


if __name__ == '__main__':
    unittest.main()
