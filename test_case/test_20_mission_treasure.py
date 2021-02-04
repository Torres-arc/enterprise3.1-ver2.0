import unittest
from selenium import webdriver

from commons.driver_setup import driver_config
from pages.login_page import LoginPage
from pages.page_20_mission_treasure import MissionTreasure
from commons.base_page import BasePage
from config.readConfig import missiontreasure as mt
from commons.log import log
from BeautifulReport import BeautifulReport


class TestMissionTreasure(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = driver_config()
        cls.driver.implicitly_wait(5)
        LoginPage(cls.driver).login()
        MissionTreasure(cls.driver).switch_to_current()
        log().info('开始执行:任务宝页面的自动化测试')
    @classmethod
    def tearDownClass(cls):
        log().info('执行结束:任务宝页面的自动化测试')
        cls.driver.quit()

    def test_01_searchByName(self):
        """测试按任务活动名称搜索"""
        log().info('开始执行:用例-按任务活动名称搜索')
        MissionTreasure(self.driver).search_by_name(mt.name)
        self.driver.refresh()
        log().info('执行结束:用例-按任务活动名称搜索')

    def test_02_searchByDate(self):
        """测试按任务活动时间搜索"""
        log().info('开始执行:用例-按任务活动时间搜索')
        self.driver.refresh()
        MissionTreasure(self.driver).search_by_date(mt.stime, mt.etime)
        self.driver.refresh()
        log().info('执行结束:用例-按任务活动时间搜索')

    def test_03_resetSearch(self):
        """测试重置搜索条件"""
        log().info('开始执行:用例-测试重置搜索条件')
        self.driver.refresh()
        MissionTreasure(self.driver).reset(mt.name)
        self.driver.refresh()
        log().info('执行结束:用例-测试重置搜索条件')

    def test_04_addMission(self):
        """测试新建任务宝"""
        log().info('开始执行:用例-测试新建任务宝')
        self.driver.refresh()
        MissionTreasure(self.driver).create_mission(cname=mt.mname,
                                                    guide=mt.guide,
                                                    people=mt.people,
                                                    user=mt.user,
                                                    msg=mt.msg,
                                                    code=mt.code,
                                                    link=mt.link,
                                                    path=mt.path,
                                                    rule=mt.rule,
                                                    welcome=mt.welcome)
        self.driver.refresh()
        log().info('执行结束:用例-测试新建任务宝')

