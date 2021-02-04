import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.page_100_red_record import Redrecord
from commons.base_page import BasePage
from config.readConfig import *
from BeautifulReport import BeautifulReport

@unittest.skip('1')
class TestRedrecord(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)
        LoginPage(cls.driver).login()
        Redrecord(cls.driver).click_btn_red_record()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01_btn_search(self):
        """红包记录查询-选择云晗-进行查询"""
        Redrecord(self.driver).search_send_man()
        self.driver.refresh()


if __name__ == '__main__':
    unittest.main()
