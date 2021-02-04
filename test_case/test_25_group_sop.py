# -*- coding: UTF-8 -*-
# @Time    : 2021/1/5 10:22 
# @Author  : Torres 
# @File    : test_25_group_sop.py

import unittest
from pages.login_page import LoginPage
from pages.page_25_group_sop import GroupSOP
from commons.driver_setup import *
from config.readConfig import groupsop as gs
from commons.log import log


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = driver_config()
        cls.driver.implicitly_wait(5)
        LoginPage(cls.driver).login()
        GroupSOP(cls.driver).switch_to_current()
        log().info('开始执行:客户群页面的自动化测试')

    @classmethod
    def tearDownClass(cls):
        log().info('执行结束:客户群页面的自动化测试')
        cls.driver.quit()

    def test_01_searchByGroupName(self):
        """测试按照规则名查询"""
        self.driver.refresh()
        log().info('开始执行:用例-按照规则名查询')
        GroupSOP(self.driver).search_by_name(gs.search_name)
        log().info('执行结束:用例-按照规则名查询')
        self.driver.refresh()

    def test_02_createRule(self):
        """测试创建规则"""
        self.driver.refresh()
        log().info('开始执行:用例-测试创建规则')
        GroupSOP(self.driver).create_rule(gs.name, gs.group, gs.msg_name, gs.stime, gs.etime, gs.msg)
        log().info('执行结束:用例-测试创建规则')
        self.driver.refresh()

    def test_03_checkDetailInfo(self):
        """测试查看规则详情"""
        self.driver.refresh()
        log().info('开始执行:用例-测试查看规则详情')
        GroupSOP(self.driver).check_details(gs.name, gs.group, gs.msg_name, gs.stime, gs.etime, gs.msg)
        log().info('执行结束:用例-测试查看规则详情')
        self.driver.refresh()

    def test_04_editRule(self):
        """测试编辑规则"""
        self.driver.refresh()
        log().info('开始执行:用例-测试编辑规则')
        GroupSOP(self.driver).edit_rule(gs.ename, gs.egroup, gs.emsg_name, gs.estime, gs.eetime, gs.emsg)
        log().info('执行结束:用例-测试编辑规则')
        self.driver.refresh()


if __name__ == '__main__':
    unittest.main()
