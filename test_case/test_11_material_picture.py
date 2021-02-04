import unittest
from time import sleep
from pages.login_page import LoginPage
from commons.log import log
from commons.driver_setup import *
from BeautifulReport import BeautifulReport

from pages.page_11_material_picture import PicPage


class MaterialPic(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = driver_config()
        cls.driver.implicitly_wait(5)
        LoginPage(cls.driver).login()
        log().info('开始执行:客户页面的自动化测试')
        PicPage(cls.driver).switch_to_current()

    @classmethod
    def tearDownClass(cls):
        log().info('执行结束:客户页面的自动化测试')
        cls.driver.quit()

    def test_01_add_group(self):
        '''图片->添加分组'''
        log().info('开始执行:用例-添加分组')
        PicPage(self.driver).add_group()
        PicPage(self.driver).check_add_group()
        self.driver.refresh()
        log().info('执行结束:用例-添加分组')

    def test_02_add_pic(self):
        '''图片->添加图片'''
        log().info('开始执行:用例-添加图片')
        PicPage(self.driver).add_pic()
        PicPage(self.driver).check_add_pic()
        self.driver.refresh()
        log().info('执行结束:用例-添加图片')

    def test_03_search_pic(self):
        '''图片->搜索图片'''
        log().info('开始执行:用例-搜索图片')
        PicPage(self.driver).search_pic()
        PicPage(self.driver).check_search_pic()
        self.driver.refresh()
        log().info('执行结束:用例-搜索图片')

    def test_04_move_group(self):
        '''图片->移动分组'''
        log().info('开始执行:用例-移动分组')
        PicPage(self.driver).move_group()
        PicPage(self.driver).check_move_group()
        self.driver.refresh()
        log().info('执行结束:用例-移动分组')

    def test_05_edit_pic(self):
        '''图片->编辑图片'''
        log().info('开始执行:用例-编辑图片')
        PicPage(self.driver).edit_pic()
        PicPage(self.driver).check_edit_pic()
        self.driver.refresh()
        log().info('执行结束:用例-编辑图片')

    def test_06_del_pic(self):
        '''图片->删除图片'''
        log().info('开始执行:用例-删除图片')
        PicPage(self.driver).del_pic()
        PicPage(self.driver).check_del_pic()
        self.driver.refresh()
        log().info('执行结束:用例-删除图片')

    def test_07_new_group_add_child(self):
        '''图片->新建分组,添加子分类'''
        log().info('开始执行:用例-新建分组,添加子分类')
        PicPage(self.driver).new_group_add_child()
        PicPage(self.driver).check_new_group_add_child()
        self.driver.refresh()
        log().info('执行结束:用例-新建分组,添加子分类')

    def test_08_del_new_group(self):
        '''图片->删除分组'''
        log().info('开始执行:用例-删除分组')
        PicPage(self.driver).del_new_group()
        PicPage(self.driver).check_del_new_group()
        self.driver.refresh()
        log().info('执行结束:用例-删除分组')


if __name__ == '__main__':
    unittest.main()
