import unittest
from selenium import webdriver

from commons.driver_setup import driver_config
from pages.login_page import LoginPage
from pages.page_21_group_fission import GroupFission
from config.readConfig import missiontreasure as mt
from commons.log import log


class TestGroupFission(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = driver_config()
        cls.driver.implicitly_wait(5)
        LoginPage(cls.driver).login()
        GroupFission(cls.driver).switch_to_current()
        log().info('开始执行:群裂变页面的自动化测试')

    @classmethod
    def tearDownClass(cls):
        log().info('执行结束:群裂变页面的自动化测试')
        cls.driver.quit()

    def test_01_searchByName(self):
        """测试按任务活动名称搜索"""
        log().info('开始执行:用例-按任务活动名称搜索')
        GroupFission(self.driver).search_by_name(mt.name)
        self.driver.refresh()
        log().info('执行结束:用例-按任务活动名称搜索')

    def test_02_searchByDate(self):
        """测试按任务活动时间搜索"""
        log().info('开始执行:用例-按任务活动时间搜索')
        self.driver.refresh()
        GroupFission(self.driver).search_by_date(mt.stime, mt.etime)
        self.driver.refresh()
        log().info('执行结束:用例-按任务活动时间搜索')

    def test_03_resetSearch(self):
        """测试重置搜索条件"""
        log().info('开始执行:用例-测试重置搜索条件')
        self.driver.refresh()
        GroupFission(self.driver).reset(mt.name)
        self.driver.refresh()
        log().info('执行结束:用例-测试重置搜索条件')

    def test_04_addMission(self):
        """测试新建任务宝"""
        log().info('开始执行:用例-测试新建任务宝')
        self.driver.refresh()
        GroupFission(self.driver).create_mission(cname=mt.mname,
                                                 guide=mt.guide,
                                                 people=mt.people,
                                                 user=mt.user,
                                                 msg=mt.msg,
                                                 code=mt.code,
                                                 link=mt.link,
                                                 path=mt.path,
                                                 rule=mt.rule)
        self.driver.refresh()
        log().info('执行结束:用例-测试新建任务宝')
