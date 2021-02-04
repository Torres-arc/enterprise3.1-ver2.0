# -*- coding: utf-8 -*-
# @Time    : 2020/12/14 15:17
# @Author  : Torres
# @File    : test_22_pull_new_client_into_group.py

import unittest
from imp import reload

from selenium import webdriver
from pages.login_page import LoginPage
from pages.page_22_pull_new_client_into_group import PullNewClientIntoGroup
import config.readConfig as rc
from commons.driver_setup import *
from config.readConfig import pullnewclient as pnc
from commons.log import log


class TestPullNewClientIntoGroup(unittest.TestCase):
    lista = []
    @classmethod
    def setUpClass(cls):
        cls.driver = driver_config()
        cls.driver.implicitly_wait(5)
        LoginPage(cls.driver).login()
        log().info('开始执行:新客自动拉群页面的自动化测试')
        PullNewClientIntoGroup(cls.driver).switch_to_current()

    @classmethod
    def tearDownClass(cls):
        log().info('执行结束:新客自动拉群页面的自动化测试')
        cls.driver.quit()

    def test_01_searchByName(self):
        """测试按任务活动名称搜索"""
        log().info('开始执行:用例-按任务活动名称搜索')
        PullNewClientIntoGroup(self.driver).search_by_name(pnc.search_name)
        self.driver.refresh()
        log().info('执行结束:用例-按任务活动名称搜索')

    def test_02_createAct(self):
        """测试创建新客自动拉群"""
        log().info('开始执行:用例-创建新客自动拉群')
        self.driver.refresh()
        self.lista = PullNewClientIntoGroup(self.driver).create_activity(pnc.name, pnc.user, pnc.guide, pnc.code)
        self.driver.refresh()
        log().info('执行结束:用例-创建新客自动拉群')

    def test_03_checkDetails(self):
        """测试查看详情"""
        log().info('开始执行:用例-查看详情')
        reload(rc)
        self.driver.refresh()
        PullNewClientIntoGroup(self.driver).check_details(pnc.user, rc.pullnewclient.taglist, pnc.guide, pnc.group_name)
        self.driver.refresh()
        log().info('执行结束:用例-查看详情')

    def test_04_editAct(self):
        """测试编辑活动"""
        log().info('开始执行:用例-编辑活动')
        reload(rc)
        self.driver.refresh()
        PullNewClientIntoGroup(self.driver).edit_act(pnc.ename, pnc.euser, pnc.eguide)
        self.driver.refresh()
        log().info('执行结束:用例-编辑活动')

    def test_05_deleteAct(self):
        """测试删除活动"""
        log().info('开始执行:用例-删除活动')
        reload(rc)
        self.driver.refresh()
        PullNewClientIntoGroup(self.driver).delete_act(pnc.ename)
        self.driver.refresh()
        log().info('执行结束:用例-删除活动')