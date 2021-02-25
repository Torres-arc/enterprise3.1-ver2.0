

from imp import reload
from pages.page_06_client_code import ClientCodePage
import unittest
from commons.base_page import BasePage
import config.readConfig as rc
from config.readConfig import clientcodepage as ccp
from commons.driver_setup import *
from commons.log import log
from pages.login_page import LoginPage


# 员工活码
class AddEmployeeCode(unittest.TestCase):
    isPassed = True

    @classmethod
    def setUpClass(cls):
        cls.driver = driver_config()
        cls.driver.implicitly_wait(5)
        LoginPage(cls.driver).login()
        ClientCodePage(cls.driver).switch_to_current()
        log().info('开始执行:员工活码页面的自动化测试')

    @classmethod
    def tearDownClass(cls):
        log().info('执行结束:员工活码页面的自动化测试')
        cls.driver.quit()

    # @unittest.skip('1')
    def test_01_searchByUser(self):
        """测试按使用员工搜索"""
        self.driver.refresh()
        log().info('开始执行:用例-测试按使用员工搜索')
        ClientCodePage(self.driver).search_by_user(ccp.user)
        self.driver.refresh()
        log().info('执行结束:用例-测试按使用员工搜索')

    # @unittest.skip('1')
    def test_02_searchByActScene(self):
        """测试按活动场景搜索"""
        self.driver.refresh()
        log().info('开始执行:用例-测试按活动场景搜索')
        ClientCodePage(self.driver).search_by_type('scene', '测试')
        self.driver.refresh()
        log().info('执行结束:用例-测试按活动场景搜索')

    # @unittest.skip('1')
    def test_03_searchByCreator(self):
        """测试按创建人搜索"""
        self.driver.refresh()
        log().info('开始执行:用例-测试按创建人搜索')
        ClientCodePage(self.driver).search_by_type('creator', ccp.creator)
        self.driver.refresh()
        log().info('执行结束:用例-测试按创建人搜索')

    # @unittest.skip('1')
    def test_04_searchByCreateTime(self):
        """测试按创建时间搜索"""
        self.driver.refresh()
        log().info('开始执行:用例-测试按创建时间搜索')
        ClientCodePage(self.driver).search_by_create_time(ccp.stime, ccp.etime)
        self.driver.refresh()
        log().info('执行结束:用例-测试按创建时间搜索')

    # @unittest.skip('1')
    def test_05_addSingleClientWebCode(self):
        """测试添加单人活码-网页"""
        self.driver.refresh()
        log().info('开始执行:用例-测试添加单人活码-网页')
        try:
            ClientCodePage(self.driver).add_code(ccp.actscene,
                                                 ccp.welcome,
                                                 'web',
                                                 ccp.web_msg,
                                                 'single',
                                                 ccp.user)
        except:
            self.isPassed = False
        self.driver.refresh()
        log().info('执行结束:用例-测试添加单人活码-网页')

    @unittest.skipIf(isPassed is False, '未成功创建活码，请重试')
    # @unittest.skip('1')
    def test_06_checkCodeInfo(self):
        """测试查看详情功能"""
        self.driver.refresh()
        log().info('开始执行:用例-测试查看详情功能')
        reload(rc)
        ClientCodePage(self.driver).check_code_info(
            [ccp.actscene, rc.clientcodepage.taglist, ccp.welcome])
        ClientCodePage(self.driver).switch_to_current()
        log().info('执行结束:用例-测试查看详情功能')

    @unittest.skipIf(isPassed is False, '未成功创建活码，请重试')
    # @unittest.skip('1')
    def test_07_editCode(self):
        """测试编辑活码功能"""
        self.driver.refresh()
        log().info('开始执行:用例-测试编辑活码功能')
        ClientCodePage(self.driver).edit_code(ccp.actscene2, ccp.welcome2)
        self.driver.refresh()
        log().info('执行结束:用例-测试编辑活码功能')

    @unittest.skipIf(isPassed is False, '未成功创建活码，请重试')
    @unittest.skip('1')
    def test_08_integratedTest(self):
        """测试前后端集成，验证欢迎语标签功能"""
        self.driver.refresh()
        log().info('开始执行:用例-前后端集成，验证欢迎语标签功能')
        ClientCodePage(self.driver).integrated_test()
        self.driver.refresh()
        log().info('执行结束:用例-前后端集成，验证欢迎语标签功能')

    # @unittest.skip('1')
    @unittest.skipIf(isPassed is False, '未成功创建活码，请重试')
    def test_09_deleteCode(self):
        """测试删除单个活码"""
        self.driver.refresh()
        log().info('开始执行:用例-测试删除单个活码')
        ClientCodePage(self.driver).search_by_type('scene', ccp.actscene)
        ClientCodePage(self.driver).delete_code()
        self.driver.refresh()
        log().info('执行结束:用例-测试删除单个活码')

    # @unittest.skip('1')
    def test_10_addSingleClientPicCode(self):
        """测试添加单人活码-图片"""
        self.driver.refresh()
        log().info('开始执行:用例-测试添加单人活码-图片')
        ClientCodePage(self.driver).add_code((ccp.actscene + '1'),
                                             ccp.welcome,
                                             'pic',
                                             ccp.picpath,
                                             'single',
                                             ccp.user)
        self.driver.refresh()
        log().info('执行结束:用例-测试添加单人活码-图片')

    # @unittest.skip('1')
    def test_11_addSingleClientMiniCode(self):
        """测试添加单人活码-小程序"""
        self.driver.refresh()
        log().info('开始执行:用例-测试添加单人活码-小程序')
        ClientCodePage(self.driver).add_code((ccp.actscene + '2'),
                                             ccp.welcome,
                                             'mini',
                                             ccp.web_msg,
                                             'single',
                                             ccp.user)
        self.driver.refresh()
        log().info('执行结束:用例-测试添加单人活码-小程序')

    # @unittest.skip('1')
    def test_12_addBatchSingleClientMiniCode(self):
        """测试添加批量单人活码-小程序"""
        self.driver.refresh()
        log().info('开始执行:用例-测试添加批量单人活码-小程序')
        ClientCodePage(self.driver).add_code((ccp.actscene + '3'),
                                             ccp.welcome,
                                             'mini',
                                             ccp.web_msg,
                                             'batch',
                                             ccp.user,
                                             ccp.user2)
        self.driver.refresh()
        log().info('执行结束:用例-测试添加批量单人活码-小程序')

    # @unittest.skip('1')
    def test_13_addBatchSingleClientPicCode(self):
        """测试添加批量单人活码-图片"""
        self.driver.refresh()
        log().info('开始执行:用例-测试添加批量单人活码-图片')
        ClientCodePage(self.driver).add_code((ccp.actscene + '4'),
                                             ccp.welcome,
                                             'pic',
                                             ccp.picpath,
                                             'batch',
                                             ccp.user,
                                             ccp.user2)
        self.driver.refresh()
        log().info('执行结束:用例-测试添加批量单人活码-图片')

    # @unittest.skip('1')
    def test_14_addBatchSingleClientWebCode(self):
        """测试添加批量单人活码-网页"""
        self.driver.refresh()
        log().info('开始执行:用例-测试添加批量单人活码-网页')
        ClientCodePage(self.driver).add_code((ccp.actscene + '5'),
                                             ccp.welcome,
                                             'web',
                                             ccp.web_msg,
                                             'batch',
                                             ccp.user,
                                             ccp.user2)
        self.driver.refresh()
        log().info('执行结束:用例-测试添加批量单人活码-网页')

    # @unittest.skip('1')
    def test_15_addMultiClientWebCode(self):
        """测试添加多人活码-网页"""
        self.driver.refresh()
        log().info('开始执行:用例-测试添加多人活码-网页')
        ClientCodePage(self.driver).add_code((ccp.actscene + '6'),
                                             ccp.welcome,
                                             'web',
                                             ccp.web_msg,
                                             'multi',
                                             ccp.user,
                                             ccp.user2)
        self.driver.refresh()
        log().info('执行结束:用例-测试添加多人活码-网页')

    # @unittest.skip('1')
    def test_16_addMultiClientMiniCode(self):
        """测试添加多人活码-小程序"""
        self.driver.refresh()
        log().info('开始执行:用例-测试添加多人活码-小程序')
        ClientCodePage(self.driver).add_code((ccp.actscene + '7'),
                                             ccp.welcome,
                                             'mini',
                                             ccp.web_msg,
                                             'multi',
                                             ccp.user,
                                             ccp.user2)
        self.driver.refresh()
        log().info('执行结束:用例-测试添加多人活码-小程序')

    # @unittest.skip('1')
    def test_17_addMultiClientPicCode(self):
        """测试添加多人活码-图片"""
        self.driver.refresh()
        log().info('开始执行:用例-测试添加多人活码-图片')
        ClientCodePage(self.driver).add_code((ccp.actscene + ' 8'),
                                             ccp.welcome,
                                             'pic',
                                             ccp.picpath,
                                             'multi',
                                             ccp.user,
                                             ccp.user2)
        self.driver.refresh()
        log().info('执行结束:用例-测试添加多人活码-图片')

    # @unittest.skip('1')
    def test_18_deleteCodeInBatch(self):
        """测试批量删除活码"""
        self.driver.refresh()
        log().info('开始执行:用例-测试批量删除活码')
        ClientCodePage(self.driver).delete_code_in_batch()
        self.driver.refresh()
        log().info('执行结束:用例-测试批量删除活码')


if __name__ == '__main__':
    unittest.main()
