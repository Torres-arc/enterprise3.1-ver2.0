import unittest
from pages.page_09_material_poster import PosterPage
from pages.login_page import LoginPage
from commons.log import log
from commons.driver_setup import *
from config.readConfig import materialposterpage as mpp


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
        """海报->添加分组"""
        log().info('开始执行:用例-添加分组')
        PosterPage(self.driver).create_group(mpp.group)
        PosterPage(self.driver).create_group(mpp.group2)
        self.driver.refresh()
        log().info('执行结束:用例-添加分组')

    def test_02_add_poster(self):
        """海报->添加海报"""
        log().info('开始执行:用例-添加海报')
        PosterPage(self.driver).create_poster(mpp.group, mpp.poster)
        self.driver.refresh()
        log().info('执行结束:用例-添加海报')

    def test_03_search_poster(self):
        """海报->搜索海报"""
        log().info('开始执行:用例-搜索海报')
        PosterPage(self.driver).search_poster(mpp.poster)
        self.driver.refresh()
        log().info('执行结束:用例-搜索海报')

    def test_04_move_group(self):
        """海报->移动分组"""
        log().info('开始执行:用例-移动分组')
        PosterPage(self.driver).move_group(mpp.poster, mpp.group2)
        self.driver.refresh()
        log().info('执行结束:用例-移动分组')

    def test_05_edit_poster(self):
        """海报->编辑海报"""
        log().info('开始执行:用例-编辑海报')
        PosterPage(self.driver).edit_poster(mpp.poster2, mpp.group2)
        self.driver.refresh()
        log().info('执行结束:用例-编辑海报')

    def test_06_del_poster(self):
        """海报->删除海报"""
        log().info('开始执行:用例-删除海报')
        PosterPage(self.driver).delete_poster(mpp.poster2, mpp.group2)
        self.driver.refresh()
        log().info('执行结束:用例-删除海报')

    def test_07_creatChildGroup(self):
        """海报->添加子分类"""
        log().info('开始执行:用例-添加子分类')
        PosterPage(self.driver).create_child_group(mpp.group2, mpp.child_group)
        self.driver.refresh()
        log().info('执行结束:用例-添加子分类')

    def test_08_deleteChildGroup(self):
        """海报->删除子分组"""
        log().info('开始执行:用例-删除子分组')
        PosterPage(self.driver).delete_child_group(mpp.group2, mpp.child_group)
        self.driver.refresh()
        log().info('执行结束:用例-删除子分组')

    def test_09_deleteGroup(self):
        """海报->删除分组"""
        log().info('开始执行:用例-删除分组')
        PosterPage(self.driver).delete_group(mpp.group)
        PosterPage(self.driver).delete_group(mpp.group2)
        self.driver.refresh()
        log().info('执行结束:用例-删除分组')


if __name__ == '__main__':
    unittest.main()
