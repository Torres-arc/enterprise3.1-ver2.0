from commons.driver_setup import driver_config
from pages.page_16_material_small_routine import SmallRoutineMaterialPage
import unittest
from selenium import webdriver
from commons.base_page import BasePage
from config.readConfig import *
from commons.log import log
from pages.login_page import LoginPage


# 欢迎语
class DocuemntMaterial(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = driver_config()
        cls.driver.implicitly_wait(5)
        LoginPage(cls.driver).login()
        SmallRoutineMaterialPage(cls.driver).click_small_routine_material_page()
        log().info('开始执行:素材中心-小程序 页面的自动化测试')
    @classmethod
    def tearDownClass(cls):
        log().info('执行结束:素材中心-小程序 页面的自动化测试')
        cls.driver.quit()

    def test_01_addSmallroutinematerial(self,):
        """测试小程序素材_添加"""
        log().info('开始执行:用例-小程序素材_添加')
        SmallRoutineMaterialPage(self.driver).addSmallroutine()
        self.driver.refresh()
        log().info('执行结束:用例-小程序素材_添加')


    def test_02_editSmallroutinematerial(self,):
        """测试小程序素材_编辑"""
        self.driver.refresh()
        log().info('开始执行:用例-小程序素材_编辑')
        SmallRoutineMaterialPage(self.driver).editSmallroutine()
        self.driver.refresh()
        log().info('执行结束:用例-小程序素材_编辑')

    def test_03_deleteSmallroutinematerial(self,):
        """测试小程序素材_删除"""
        self.driver.refresh()
        log().info('开始执行:用例-小程序素材_删除')
        SmallRoutineMaterialPage(self.driver).deleteSmallroutine()
        log().info('执行结束:用例-小程序素材_删除')


if __name__ == '__main__':
    unittest.main()