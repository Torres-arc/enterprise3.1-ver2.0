import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.page_03_client_tags import ClientTags
from commons.base_page import BasePage
from config.readConfig import *
from commons.log import log
from BeautifulReport import BeautifulReport


@unittest.skip('1')
class TestClientTags(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)
        LoginPage(cls.driver).login()
        ClientTags(cls.driver).switch_to_current()
        log().info('开始执行:客户标签页面的自动化测试')
    @classmethod
    def tearDownClass(cls):
        log().info('执行结束:客户标签页面的自动化测试')
        cls.driver.quit()

    # @unittest.skip('1')
    def test_01_addNewTagGroup(self):
        """测试新建标签组"""
        log().info('开始执行:用例-新建标签组')
        ClientTags(self.driver).add_tag_group(clienttagpage.tag_group, clienttagpage.tag)
        log().info('执行结束:用例-新建标签组')
        self.driver.refresh()

    # @unittest.skip('1')
    def test_02_editTagGroup(self):
        """测试编辑标签组"""
        self.driver.refresh()
        log().info('开始执行:用例-编辑标签组')
        ClientTags(self.driver).edit_tag_group(clienttagpage.tag_group,
                                               clienttagpage.delete,
                                               clienttagpage.add,
                                               tag2=clienttagpage.tagn)
        log().info('执行结束:用例-编辑标签组')
        self.driver.refresh()

    def test_03_deleteTagGroup(self):
        """测试删除标签组"""
        self.driver.refresh()
        log().info('开始执行:用例-删除标签组')
        ClientTags(self.driver).delete_tag_group(clienttagpage.tag_group)
        log().info('执行结束:用例-删除标签组')


if __name__ == '__main__':
    unittest.main()
