import unittest
from selenium import webdriver

from commons.driver_setup import driver_config
from pages.login_page import LoginPage
from pages.page_12_material_web import MaterialWebPage
from commons.base_page import BasePage
from config.readConfig import *
from BeautifulReport import BeautifulReport
from commons.log import log


class TestMaterialWeb(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = driver_config()
        cls.driver.implicitly_wait(5)
        LoginPage(cls.driver).login()
        MaterialWebPage(cls.driver).switch_to_current()
        log().info('开始执行:素材中心-网页 页面的自动化测试')

    @classmethod
    def tearDownClass(cls):
        log().info('执行结束:素材中心-网页 页面的自动化测试')
        cls.driver.quit()

    # @unittest.skip('1')
    def test_01_addGroup(self):
        """测试添加分组"""
        self.driver.refresh()
        log().info('开始执行:用例-添加分组')
        MaterialWebPage(self.driver).add_group(materialwebpage.group)
        self.driver.refresh()
        log().info('执行结束:用例-添加分组')

    # @unittest.skip('1')
    def test_02_addCustomizeWeb(self):
        """测试添加自定义网页"""
        self.driver.refresh()
        log().info('开始执行:用例-添加自定义网页')
        MaterialWebPage(self.driver).add_customize_web(title=materialwebpage.title1,
                                                       summary=materialwebpage.summary1,
                                                       pic_path=materialwebpage.path1,
                                                       group=materialwebpage.group,
                                                       main=materialwebpage.main)
        self.driver.refresh()
        log().info('执行结束:用例-添加自定义网页')

    # @unittest.skip('1')
    def test_03_addExternalLinkWeb(self):
        """测试添加外链网页"""
        self.driver.refresh()
        log().info('开始执行:用例-添加外链网页')
        MaterialWebPage(self.driver).add_external_link_web(title=materialwebpage.title2,
                                                           summary=materialwebpage.summary2,
                                                           pic_path=materialwebpage.path2,
                                                           group=materialwebpage.group,
                                                           link=materialwebpage.link)
        self.driver.refresh()
        log().info('执行结束:用例-添加外链网页')

    # @unittest.skip('1')
    def test_04_editWeb(self):
        """测试编辑网页"""
        self.driver.refresh()
        log().info('开始执行:用例-编辑网页')
        MaterialWebPage(self.driver).edit_web(title1=materialwebpage.title1,
                                              summaryc=materialwebpage.summary_changed,
                                              group=materialwebpage.group)
        self.driver.refresh()
        log().info('执行结束:用例-编辑网页')

    # @unittest.skip('1')
    def test_06_deleteWeb(self):
        """测试删除网页"""
        self.driver.refresh()
        log().info('开始执行:用例-删除网页')
        MaterialWebPage(self.driver).delete_web(title1=materialwebpage.title1,
                                                group=materialwebpage.group)
        MaterialWebPage(self.driver).delete_web(title1=materialwebpage.title2,
                                                group=materialwebpage.group)
        self.driver.refresh()
        log().info('执行结束:用例-删除网页')

    # @unittest.skip('1')
    def test_05_searchWeb(self):
        """测试搜索网页"""
        self.driver.refresh()
        log().info('开始执行:用例-搜索网页')
        MaterialWebPage(self.driver).search_web(title=materialwebpage.pattitle)
        self.driver.refresh()
        log().info('执行结束:用例-搜索网页')

    # @unittest.skip('1')
    def test_07_addChildGroup(self):
        """测试添加子分类"""
        self.driver.refresh()
        log().info('开始执行:用例-添加子分类')
        MaterialWebPage(self.driver).add_child_group(materialwebpage.group, materialwebpage.cgroup)
        self.driver.refresh()
        log().info('执行结束:用例-添加子分类')

    def test_08_deleteGroup(self):
        """测试删除分组"""
        self.driver.refresh()
        log().info('开始执行:用例-测试删除分组')
        MaterialWebPage(self.driver).delete_group(materialwebpage.group, materialwebpage.cgroup)
        self.driver.refresh()
        log().info('执行结束:用例-测试删除分组')


if __name__ == '__main__':
    unittest.main()
