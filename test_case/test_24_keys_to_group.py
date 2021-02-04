# -*- coding: utf-8 -*-
# @Time    : 2020/12/16 15:07
# @Author  : Torres
# @File    : test_24_keys_to_group.py

import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.page_24_keys_to_group import KeysToGroup
from commons.base_page import BasePage
from commons.driver_setup import *
from config.readConfig import keystogroup as ktg
from commons.log import log


class TestKeysToGroup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = driver_config()
        cls.driver.implicitly_wait(5)
        LoginPage(cls.driver).login()
        log().info('开始执行:xx页面的自动化测试')
        KeysToGroup(cls.driver).switch_to_current()

    @classmethod
    def tearDownClass(cls):
        log().info('执行结束:xx页面的自动化测试')
        cls.driver.quit()

    def test_01_searchByName(self):
        """测试按任务活动名称搜索"""
        log().info('开始执行:用例-按任务活动名称搜索')
        KeysToGroup(self.driver).search_by_name(ktg.search_name)
        self.driver.refresh()
        log().info('执行结束:用例-按任务活动名称搜索')

    def test_02_createAct(self):
        """测试创建新客自动拉群"""
        log().info('开始执行:用例-创建新客自动拉群')
        self.driver.refresh()
        KeysToGroup(self.driver).create_activity(ktg.name, ktg.keys, ktg.guide, ktg.code, ktg.group_name)
        self.driver.refresh()
        log().info('执行结束:用例-创建新客自动拉群')

    def test_03_editAct(self):
        """测试编辑活动"""
        log().info('开始执行:用例-编辑活动')
        self.driver.refresh()
        KeysToGroup(self.driver).edit_act(ktg.ename, ktg.keys2, ktg.eguide)
        self.driver.refresh()
        log().info('执行结束:用例-编辑活动')

    def test_04_deleteAct(self):
        """测试删除活动"""
        log().info('开始执行:用例-删除活动')
        self.driver.refresh()
        KeysToGroup(self.driver).delete_act(ktg.ename)
        self.driver.refresh()
        log().info('执行结束:用例-删除活动')