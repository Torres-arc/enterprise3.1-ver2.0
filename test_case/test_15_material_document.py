from commons.driver_setup import driver_config
from pages.page_15_material_document import DocumentMaterialPage
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
        DocumentMaterialPage(cls.driver).click_document_material_page()
        log().info('开始执行:素材中心-文件 页面的自动化测试')

    @classmethod
    def tearDownClass(cls):
        log().info('执行结束:素材中心-文件 页面的自动化测试')
        cls.driver.quit()

    def test_01_addDocumentmaterial(self,):
        """测试文件素材_添加"""
        log().info('开始执行:用例-文件素材_添加')
        DocumentMaterialPage(self.driver).addDocument()
        self.driver.refresh()
        log().info('执行结束:用例-文件素材_添加')

    def test_02_editDocumentmaterial(self,):
        """测试文件素材_编辑"""
        self.driver.refresh()
        log().info('开始执行:用例-件素材_编辑')
        DocumentMaterialPage(self.driver).editDocument()
        self.driver.refresh()
        log().info('执行结束:用例-件素材_编辑')

    def test_03_deleteDocumentmaterial(self,):
        """测试文件素材_删除"""
        self.driver.refresh()
        log().info('开始执行:用例-文件素材_删除')
        DocumentMaterialPage(self.driver).deleteDocument()
        self.driver.refresh()
        log().info('执行结束:用例-文件素材_删除')


if __name__ == '__main__':
    unittest.main()
