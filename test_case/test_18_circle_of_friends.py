import unittest
from selenium import webdriver

from commons.driver_setup import driver_config
from pages.login_page import LoginPage
from pages.page_18_circle_of_friends import CircleOfFriendsPage
from commons.base_page import BasePage
from config.readConfig import *
from BeautifulReport import BeautifulReport
from commons.log import log


class TestCircleOfFriends(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = driver_config()
        cls.driver.implicitly_wait(5)
        LoginPage(cls.driver).login()
        CircleOfFriendsPage(cls.driver).switch_to_current()
        log().info('开始执行:朋友圈 页面的自动化测试')

    @classmethod
    def tearDownClass(cls):
        log().info('执行结束:朋友圈 页面的自动化测试')
        cls.driver.quit()

    # @unittest.skip('1')
    def test_01_searchByKeys(self):
        """测试按关键词查询"""
        log().info('开始执行:用例-按关键词查询')
        CircleOfFriendsPage(self.driver).search_by_keys(circleoffriends.key)
        self.driver.refresh()
        log().info('执行结束:用例-按关键词查询')

    # @unittest.skip('1')
    def test_02_searchByTime(self):
        """测试按发布时间查询"""
        self.driver.refresh()
        log().info('开始执行:用例-按发布时间查询')
        CircleOfFriendsPage(self.driver).search_by_release_time(circleoffriends.start_time, circleoffriends.end_time)
        self.driver.refresh()
        log().info('执行结束:用例-按发布时间查询')

    # @unittest.skip('1')
    def test_03_addReleaseNews(self):
        """测试发布动态"""
        self.driver.refresh()
        log().info('开始执行:用例-发布动态')
        CircleOfFriendsPage(self.driver).add_release_news(circleoffriends.staff, circleoffriends.msg)
        self.driver.refresh()
        log().info('执行结束:用例-发布动态')

    # @unittest.skip('1')
    def test_04_editReleaseNews(self):
        """测试编辑动态"""
        self.driver.refresh()
        log().info('开始执行:用例-编辑动态')
        CircleOfFriendsPage(self.driver).edit_release_news(staff=circleoffriends.staff,
                                                           msg1=circleoffriends.msg,
                                                           msg2=circleoffriends.msg2)
        self.driver.refresh()
        log().info('执行结束:用例-编辑动态')

    def test_05_deleteReleaseNews(self):
        """测试删除动态"""
        self.driver.refresh()
        log().info('开始执行:用例-删除动态')
        CircleOfFriendsPage(self.driver).delete_release_news(staff=circleoffriends.staff,
                                                             msg=circleoffriends.msg2)
        self.driver.refresh()
        log().info('执行结束:用例-删除动态')


if __name__ == '__main__':
    unittest.main()
