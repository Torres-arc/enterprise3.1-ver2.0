import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.page_01_clients import ClientPage
from commons.base_page import BasePage
from commons.driver_setup import *
from config.readConfig import *
from BeautifulReport import BeautifulReport
from commons.log import log


class TestClients(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = driver_config()
        cls.driver.implicitly_wait(5)
        LoginPage(cls.driver).login()
        log().info('开始执行:客户页面的自动化测试')
        ClientPage(cls.driver).switch_to_current()
    @classmethod
    def tearDownClass(cls):
        log().info('执行结束:客户页面的自动化测试')
        cls.driver.quit()
    def save_img(self, img_name):
        self.driver.get_screenshot_as_file('{}\\{}.png'.format(os.path.abspath('img'), img_name))

    # def test_02_monkey(self):
    #     ClientPage(self.driver).monkeys()

    # @unittest.skip('1')
    # @BeautifulReport.add_test_img('test_01_searchByClientName')
    def test_01_searchByClientName(self):
        """测试按照客户姓名查询"""
        log().info('开始执行:用例-按客户姓名查询')
        # self.save_img('test_01_searchByClientName')
        ClientPage(self.driver).search_by_name(clientpage.name)
        log().info('执行结束:用例-按客户姓名查询')
        self.driver.refresh()

    # @unittest.skip('1')
    # # @BeautifulReport.add_test_img('test_02_searchByAdder')
    def test_02_searchByAdder(self):
        """测试按照客户添加人查询"""
        self.driver.refresh()
        log().info('开始执行:用例-按客户添加人查询')
        ClientPage(self.driver).search_by_adder(clientpage.adder)
        log().info('执行结束:用例-按客户添加人查询')
        self.driver.refresh()
        # custom_page(self.driver).search_by_adder('云书')

    # @unittest.skip('1')
    # @BeautifulReport.add_test_img('test_03_searchByTag')
    def test_03_searchByTag(self):
        """测试按照客户标签查询"""
        self.driver.refresh()
        log().info('开始执行:用例-按客户标签查询')
        ClientPage(self.driver).search_by_tag(clientpage.tag_group31, clientpage.tag31)
        log().info('执行结束:用例-按客户标签查询')
        self.driver.refresh()

    # @unittest.skip('1')
    # @BeautifulReport.add_test_img('test_04_buttonReset')
    # def test_04_buttonReset(self):
    #     """测试重置功能"""
    #     self.driver.refresh()
    #     log().info('开始执行:用例-查询条件重置功能')
    #     ClientPage(self.driver).reset(clientpage.name)
    #     log().info('执行结束:用例-查询条件重置功能')
    #     self.driver.refresh()

    # @unittest.skip('1')
    # @BeautifulReport.add_test_img('test_05_remindTags')
    # def test_05_remindTags(self):
    #     """测试提醒打标签"""
    #     self.driver.refresh()
    #     log().info('开始执行:用例-批量提醒打标签功能')
    #     ClientPage(self.driver).remind_tags(clientpage.adder)
    #     log().info('执行结束:用例-批量提醒打标签')
    #     self.driver.refresh()

    # @unittest.skip('1')
    # def test_06_exportClientsList(self):
    #     """测试导出客户列表"""
    #     self.driver.refresh()
    #     log().info('开始执行:用例-导出客户列表')
    #     ClientPage(self.driver).export_clients_list()
    #     log().info('执行结束:用例-导出客户列表')
    #     self.driver.refresh()


if __name__ == '__main__':
    unittest.main()
