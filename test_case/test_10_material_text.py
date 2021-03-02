import unittest
from time import sleep
from pages.login_page import LoginPage
from commons.log import log
from commons.driver_setup import *
from pages.page_10_material_text import TextPage
from config.readConfig import materialtextpage as mtp


class MaterialText(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = driver_config()
        cls.driver.implicitly_wait(5)
        LoginPage(cls.driver).login()
        log().info('开始执行:客户页面的自动化测试')
        TextPage(cls.driver).switch_to_current()
        sleep(2)

    @classmethod
    def tearDownClass(cls):
        log().info('执行结束:客户页面的自动化测试')
        cls.driver.quit()

    def test_01_add_group(self):
        """文本->添加分组"""
        log().info('开始执行:用例-添加分组')
        TextPage(self.driver).create_group(mtp.group)
        TextPage(self.driver).create_group(mtp.group2)
        self.driver.refresh()
        log().info('执行结束:用例-添加分组')

    def test_02_add_text(self):
        """文本->添加文本"""
        log().info('开始执行:用例-添加文本')
        TextPage(self.driver).create_text(mtp.group, mtp.msg)
        self.driver.refresh()
        log().info('执行结束:用例-添加文本')

    def test_03_search_text(self):
        """文本->搜索文本"""
        log().info('开始执行:用例-搜索文本')
        TextPage(self.driver).search_text(mtp.msg)
        self.driver.refresh()
        log().info('执行结束:用例-搜索文本')

    def test_04_move_group(self):
        """文本->移动分组"""
        log().info('开始执行:用例-移动分组')
        TextPage(self.driver).move_group(mtp.msg, mtp.group, mtp.group2)
        self.driver.refresh()
        log().info('执行结束:用例-移动分组')

    def test_05_edit_text(self):
        """文本->编辑文本"""
        log().info('开始执行:用例-编辑文本')
        TextPage(self.driver).edit_text(mtp.msg2, mtp.group2)
        self.driver.refresh()
        log().info('执行结束:用例-编辑文本')

    def test_06_del_text(self):
        """文本->删除文本"""
        log().info('开始执行:用例-删除文本')
        TextPage(self.driver).delete_text(mtp.msg2, mtp.group2)
        self.driver.refresh()
        log().info('执行结束:用例-删除文本')

    def test_07_createChildGroup(self):
        """文本->新建分组,添加子分类"""
        log().info('开始执行:用例-新建分组,添加子分类')
        TextPage(self.driver).create_child_group(mtp.group2, mtp.child_group)
        self.driver.refresh()
        log().info('执行结束:用例-新建分组,添加子分类')

    def test_08_deleteChildGroup(self):
        """海报->删除子分组"""
        log().info('开始执行:用例-删除子分组')
        TextPage(self.driver).delete_child_group(mtp.group2, mtp.child_group)
        self.driver.refresh()
        log().info('执行结束:用例-删除子分组')

    def test_09_del_new_group(self):
        """文本->删除分组"""
        log().info('开始执行:用例-删除分组')
        TextPage(self.driver).delete_group(mtp.group)
        TextPage(self.driver).delete_group(mtp.group2)
        self.driver.refresh()
        log().info('执行结束:用例-删除分组')


if __name__ == '__main__':
    unittest.main()
