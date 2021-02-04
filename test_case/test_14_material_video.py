import unittest
from selenium import webdriver

from commons.driver_setup import driver_config
from pages.login_page import LoginPage
from pages.page_14_material_video import MaterialVideoPage
from commons.base_page import BasePage
from config.readConfig import *
from BeautifulReport import BeautifulReport
from commons.log import log


class TestMaterialvideo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = driver_config()
        cls.driver.implicitly_wait(5)
        LoginPage(cls.driver).login()
        MaterialVideoPage(cls.driver).switch_to_current()
        log().info('开始执行:素材中心-网页 页面的自动化测试')

    @classmethod
    def tearDownClass(cls):
        log().info('执行结束:素材中心-网页 页面的自动化测试')
        cls.driver.quit()

    def test_01_AddGroup(self):
        """测试添加分组"""
        log().info('开始执行:用例-添加分组')
        MaterialVideoPage(self.driver).add_group(materialvideopage.group)
        self.driver.refresh()
        log().info('执行结束:用例-添加分组')

    # @unittest.skip('1')
    def test_02_addvideo(self):
        """测试添加视频"""
        log().info('开始执行:用例-添加视频')
        MaterialVideoPage(self.driver).add_video(group=materialvideopage.group,
                                                 path=materialvideopage.path,
                                                 ppath=materialwebpage.path1,
                                                 sum=materialvideopage.sum,
                                                 name=materialvideopage.name)
        self.driver.refresh()
        log().info('执行结束:用例-添加视频')

    # @unittest.skip('1')
    def test_03_editVideo(self):
        """测试编辑视频"""
        self.driver.refresh()
        log().info('开始执行:用例-编辑视频')
        MaterialVideoPage(self.driver).edit_video(name=materialvideopage.name,
                                                  sum2=materialvideopage.sum2)
        self.driver.refresh()
        log().info('执行结束:用例-编辑视频')

    def test_04_deleteVideo(self):
        """测试删除视频"""
        self.driver.refresh()
        log().info('开始执行:用例-删除视频')
        MaterialVideoPage(self.driver).delete_video(name=materialvideopage.name)
        self.driver.refresh()
        log().info('执行结束:用例-删除视频')

    def test_05_deleteGroup(self):
        """测试删除分组"""
        self.driver.refresh()
        log().info('开始执行:用例-测试删除分组')
        MaterialVideoPage(self.driver).delete_group(materialvideopage.group)
        self.driver.refresh()
        log().info('执行结束:用例-测试删除分组')


if __name__ == '__main__':
    unittest.main()
