from selenium.webdriver.common.by import By
from commons.base_page import BasePage
from time import sleep
from pykeyboard import PyKeyboard


class OrganizationPage(BasePage):
    """元素定位信息"""
    # 组织架构页面
    _btn_org = (By.XPATH, '//li[text()="组织架构"]')
    # 搜索输入框
    _input_search = (By.CSS_SELECTOR, 'input[placeholder="搜索成员、部门"]')
    # 组织树
    _node_org_tree = (By.CSS_SELECTOR, '.scope-tree-node')
    # 员工姓名
    _staff_name = (By.CSS_SELECTOR, '.user-title ww-open-data')

    """元素定位层"""
    # 获取组织架构页面按钮
    def get_btn_org(self):
        return self.find_Element(self._btn_org)
    # 获取搜索输入框
    def get_input_search(self):
        return self.find_Element(self._input_search)
    # 获取组织树节点
    def get_node_org_tree(self):
        return self.find_Element(self._node_org_tree)
    # 获取员工姓名元素
    def get_staff_name(self):
        return self.find_Element(self._staff_name)

    """元素操作层"""
    # 点击组织架构页面按钮
    def click_btn_org(self):
        return self.click_element(self.get_btn_org())
    # 输入信息搜索输入框
    def sendkey_input_search(self, value):
        return self.send_keys(self.get_input_search(), value)
    # 点击组织树节点
    def click_node_org_tree(self):
        return self.click_element(self.get_node_org_tree())
    # 获取员工姓名
    def gettext_staff_name(self):
        return self.get_staff_name().get_attribute('openid')

    """业务层"""
    def switch_to_current(self):
        sleep(2)
        self.click_btn_org()
        sleep(3)

    def search_staff(self, name):
        self.sendkey_input_search(name)
        k = PyKeyboard()
        k.tap_key(k.enter_key)
        sleep(2)
        self.click_node_org_tree()
        sleep(2)
        self.assert_Equal(name, self.get_userid_info(self.gettext_staff_name()))
