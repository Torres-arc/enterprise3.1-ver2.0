import unittest
from selenium import webdriver

from commons.driver_setup import driver_config
from pages.login_page import LoginPage
from pages.page_13_material_audio import MaterialAudioPage
from commons.base_page import BasePage
from config.readConfig import *
from BeautifulReport import BeautifulReport
from commons.log import log


class TestMaterialAudio(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = driver_config()
        cls.driver.implicitly_wait(5)
        LoginPage(cls.driver).login()
        MaterialAudioPage(cls.driver).switch_to_current()
        log().info('开始执行:素材中心-网页 页面的自动化测试')

    @classmethod
    def tearDownClass(cls):
        log().info('执行结束:素材中心-网页 页面的自动化测试')
        cls.driver.quit()

    # @unittest.skip('1')
    def test_01_AddGroup(self):
        """测试添加分组"""
        log().info('开始执行:用例-添加分组')
        MaterialAudioPage(self.driver).add_group(materialaudiopage.group)
        self.driver.refresh()
        log().info('执行结束:用例-添加分组')

    # @unittest.skip('1')
    def test_02_addAudio(self):
        """测试添加音频"""
        log().info('开始执行:用例-添加音频')
        MaterialAudioPage(self.driver).add_audio(path=materialaudiopage.path,
                                                 group=materialaudiopage.group,
                                                 name1=materialaudiopage.name1)
        self.driver.refresh()
        log().info('执行结束:用例-添加音频')

    # @unittest.skip('1')
    def test_03_editAudio(self):
        """测试编辑音频"""
        self.driver.refresh()
        log().info('开始执行:用例-编辑音频')
        MaterialAudioPage(self.driver).edit_audio(name1=materialaudiopage.name1,
                                                  name2=materialaudiopage.name2)
        self.driver.refresh()
        log().info('执行结束:用例-编辑音频')

    def test_04_deleteAudio(self):
        """测试删除音频"""
        self.driver.refresh()
        log().info('开始执行:用例-删除音频')
        MaterialAudioPage(self.driver).delete_audio(name2=materialaudiopage.name2)
        log().info('执行结束:用例-删除音频')

    def test_05_deleteGroup(self):
        """测试删除分组"""
        self.driver.refresh()
        log().info('开始执行:用例-测试删除分组')
        MaterialAudioPage(self.driver).delete_group(materialaudiopage.group)
        log().info('执行结束:用例-测试删除分组')


if __name__ == '__main__':
    unittest.main()
