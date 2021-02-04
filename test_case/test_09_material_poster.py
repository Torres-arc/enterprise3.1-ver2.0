import unittest
from time import sleep
from pages.page_09_material_poster import PosterPage
from pages.login_page import LoginPage
from commons.log import log
from commons.driver_setup import *
from BeautifulReport import BeautifulReport


class MaterialPoster(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = driver_config()
        cls.driver.implicitly_wait(5)
        LoginPage(cls.driver).login()
        log().info('开始执行:客户页面的自动化测试')
        PosterPage(cls.driver).switch_to_current()

    @classmethod
    def tearDownClass(cls):
        log().info('执行结束:客户页面的自动化测试')
        cls.driver.quit()

    def test_01_add_group(self):
        '''海报->添加分组'''
        log().info('开始执行:用例-添加分组')
        PosterPage(self.driver).add_group()
        PosterPage(self.driver).check_add_group()
        self.driver.refresh()
        log().info('执行结束:用例-添加分组')

    def test_02_add_poster(self):
        '''海报->添加海报'''
        log().info('开始执行:用例-添加海报')
        PosterPage(self.driver).add_poster()
        PosterPage(self.driver).check_add_poster()
        self.driver.refresh()
        log().info('执行结束:用例-添加海报')

    def test_03_search_poster(self):
        '''海报->搜索海报'''
        log().info('开始执行:用例-搜索海报')
        PosterPage(self.driver).search_poster()
        PosterPage(self.driver).check_search_poster()
        self.driver.refresh()
        log().info('执行结束:用例-搜索海报')

    def test_04_move_group(self):
        '''海报->移动分组'''
        log().info('开始执行:用例-移动分组')
        PosterPage(self.driver).move_group()
        PosterPage(self.driver).check_move_group()
        self.driver.refresh()
        log().info('执行结束:用例-移动分组')

    def test_05_edit_poster(self):
        '''海报->编辑海报'''
        log().info('开始执行:用例-编辑海报')
        PosterPage(self.driver).edit_poster()
        PosterPage(self.driver).check_edit_poster()
        self.driver.refresh()
        log().info('执行结束:用例-编辑海报')

    def test_06_del_poster(self):
        '''海报->删除海报'''
        log().info('开始执行:用例-删除海报')
        PosterPage(self.driver).del_poster()
        PosterPage(self.driver).check_del_poster()
        self.driver.refresh()
        log().info('执行结束:用例-删除海报')

    def test_07_new_group_add_child(self):
        '''海报->新建分组,添加子分类'''
        log().info('开始执行:用例-新建分组,添加子分类')
        PosterPage(self.driver).new_group_add_child()
        PosterPage(self.driver).check_new_group_add_child()
        self.driver.refresh()
        log().info('执行结束:用例-新建分组,添加子分类')

    def test_08_del_new_group(self):
        '''海报->删除分组'''
        log().info('开始执行:用例-删除分组')
        PosterPage(self.driver).del_new_group()
        PosterPage(self.driver).check_del_new_group()
        self.driver.refresh()
        log().info('执行结束:用例-删除分组')


if __name__ == '__main__':
    unittest.main()
