import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.page_02_client_groups import ClientGroupsPage
from commons.base_page import BasePage
from config.readConfig import *
from commons.log import log
from commons.driver_setup import driver_config
from BeautifulReport import BeautifulReport


class TestClientGroups(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = driver_config()
        cls.driver.implicitly_wait(5)
        LoginPage(cls.driver).login()
        ClientGroupsPage(cls.driver).switch_to_current()
        log().info('开始执行:客户群页面的自动化测试')

    @classmethod
    def tearDownClass(cls):
        log().info('执行结束:客户群页面的自动化测试')
        cls.driver.quit()

    # @unittest.skip('1')
    def test_01_searchByGroupName(self):
        """测试按照客户群名查询"""
        self.driver.refresh()
        log().info('开始执行:用例-按照客户群名查询')
        ClientGroupsPage(self.driver).search_by_name(clientgrouppage.name)
        log().info('执行结束:用例-按照客户群名查询')
        self.driver.refresh()

    # @unittest.skip('1')
    def test_02_searchByMasterName(self):
        """测试按群主名查询"""
        self.driver.refresh()
        log().info('开始执行:用例-按群主名查询')
        ClientGroupsPage(self.driver).search_by_master(clientgrouppage.master_name)
        log().info('执行结束:用例-按群主名查询')
        self.driver.refresh()

    # @unittest.skip('1')
    def test_03_searchByCreateTime(self):
        """测试按创建时间查询"""
        self.driver.refresh()
        log().info('开始执行:用例-按创建时间查询')
        ClientGroupsPage(self.driver).search_by_create_time(clientgrouppage.start_time, clientgrouppage.end_time)
        log().info('执行结束:用例-按创建时间查询')
        self.driver.refresh()

    # # @unittest.skip('1')
    # def test_04_buttonReset(self):
    #     """测试重置功能"""
    #     self.driver.refresh()
    #     log().info('开始执行:用例-重置功能')
    #     ClientGroupsPage(self.driver).reset(clientgrouppage.name)
    #     log().info('执行结束:用例-重置功能')
    #
    # def test_05_exportGroupsList(self):
    #     """测试导出客户群列表"""
    #     self.driver.refresh()
    #     log().info('开始执行:用例-导出客户群列表')
    #     ClientGroupsPage(self.driver).export_groups_list()
    #     log().info('执行结束:用例-导出客户群列表')


if __name__ == '__main__':
    unittest.main()
