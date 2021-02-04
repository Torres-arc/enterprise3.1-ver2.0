from pages.page_07_client_groups_code import ClientGroupCodePage
import unittest
from commons.driver_setup import *
from commons.log import log
from config.readConfig import *
from pages.login_page import LoginPage


# 员工活码
class AddEmployeeCode(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = driver_config()
        cls.driver.implicitly_wait(5)
        LoginPage(cls.driver).login()
        ClientGroupCodePage(cls.driver).click_client_group_code_page()
        log().info('开始执行:客户群活码页面的自动化测试')
    @classmethod
    def tearDownClass(cls):
        log().info('执行结束:客户群活码页面的自动化测试')
        cls.driver.quit()

    # @unittest.skip('1')
    def test_01_addClientgroupcode(self,):
        """测试添加客户群活码"""
        log().info('开始执行:用例-添加客户群活码')
        ClientGroupCodePage(self.driver).add_client_group_code(act_name=clientgroupcodepage.actname,
                                                               act_scene=clientgroupcodepage.actscene,
                                                               group_name=clientgroupcodepage.groupname,
                                                               guide=clientgroupcodepage.guide,
                                                               date=clientgroupcodepage.date,
                                                               limit=clientgroupcodepage.limit)
        self.driver.refresh()
        log().info('执行结束:用例-添加客户群活码')

    # @unittest.skip('1')
    def test_02_manageClientgroupcode(self):
        """测试管理客户群活码"""
        self.driver.refresh()
        log().info('开始执行:用例-管理客户群活码')
        ClientGroupCodePage(self.driver).manage_reality_code(group_name=clientgroupcodepage.editgname,
                                                             date=clientgroupcodepage.date2,
                                                             limit=clientgroupcodepage.limit2)
        self.driver.refresh()
        log().info('执行结束:用例-管理客户群活码')

    # @unittest.skip('1')
    def test_03_editClientgroupcode(self,):
        """测试编辑客户群活码"""
        self.driver.refresh()
        log().info('开始执行:用例-编辑客户群活码')
        ClientGroupCodePage(self.driver).edit_client_group_code(act_name=clientgroupcodepage.actname1,
                                                                act_scene=clientgroupcodepage.actscene1)
        self.driver.refresh()
        log().info('执行结束:用例-编辑客户群活码')

    # @unittest.skip('1')
    def test_04_deleteClientgroupcode(self,):
        """测试删除客户群活码"""
        self.driver.refresh()
        log().info('开始执行:用例-删除客户群活码')
        ClientGroupCodePage(self.driver).delete_code(clientgroupcodepage.actname1)
        self.driver.refresh()
        log().info('执行结束:用例-删除客户群活码')

    # @unittest.skip('1')
    def test_05_selectClientgroupcode(self,):
        """测试查询客户群活码"""
        self.driver.refresh()
        log().info('开始执行:用例-查询客户群活码')
        ClientGroupCodePage(self.driver).search_by_keys(clientgroupcodepage.search_key)
        self.driver.refresh()
        log().info('执行结束:用例-查询客户群活码')


if __name__ == '__main__':
    unittest.main()
