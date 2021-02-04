# -*- coding: utf-8 -*-
# @Time    : 2020/12/24 10:41
# @Author  : Torres
# @File    : test_23_create_group_by_tags.py

import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.page_23_create_group_by_tags import CreateGroupByTags
from commons.base_page import BasePage
from commons.driver_setup import *
from config.readConfig import creatgroupbytags as cgbt
from commons.log import log


class TestCreateGroupByTags(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = driver_config()
        cls.driver.implicitly_wait(5)
        LoginPage(cls.driver).login()
        log().info('开始执行:老客标签建群页面的自动化测试')
        CreateGroupByTags(cls.driver).switch_to_current()

    @classmethod
    def tearDownClass(cls):
        log().info('执行结束:老客标签建群页面的自动化测试')
        cls.driver.quit()

    def test_01_searchByWayOfSending(self):
        """测试按发送方式搜索"""
        self.driver.refresh()
        log().info('开始执行:用例-按发送方式搜索')
        CreateGroupByTags(self.driver).search_by_way_of_sending()
        log().info('执行结束:用例-按发送方式搜索')

    def test_02_searchByTaskName(self):
        """测试按任务名称搜索"""
        self.driver.refresh()
        log().info('开始执行:用例-按任务名称搜索')
        CreateGroupByTags(self.driver).search_by_name(cgbt.name)
        log().info('执行结束:用例-按任务名称搜索')

    def test_03_reset(self):
        """测试重置功能"""
        self.driver.refresh()
        log().info('开始执行:用例-重置功能')
        CreateGroupByTags(self.driver).reset(cgbt.name)
        log().info('执行结束:用例-重置功能')

    def test_04_creatTask(self):
        """测试创建任务"""
        self.driver.refresh()
        log().info('开始执行:用例-创建任务')
        CreateGroupByTags(self.driver).create_task(cgbt.task_name, cgbt.staff, cgbt.guide, cgbt.code,
                                                   cgbt.stime, cgbt.etime)
        log().info('执行结束:用例-创建任务')

    def test_05_checkDetails(self):
        """测试查看详情"""
        self.driver.refresh()
        log().info('开始执行:用例-查看详情')
        CreateGroupByTags(self.driver).check_details(cgbt.task_name, cgbt.staff, cgbt.stime, cgbt.etime)
        log().info('执行结束:用例-查看详情')
