from selenium.webdriver.common.by import By
from commons.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from time import sleep
import os


# 员工活码
class WelcomingMessagePage(BasePage):
    """元素定位信息"""
    # 客户营销tab
    _btn_client_marketing_tab = (By.XPATH, '//span[text()="客户营销"]/..')
    # 员工活码页面
    _btn_welcome_page = (By.XPATH, '//li[text()=" 欢迎语 "]')
    # 部门员工tab
    _btn_department_client_tab = (By.XPATH, '//div[text()="部门员工欢迎语"]')

    # 员工欢迎语页面
    # 新建员工欢迎语按钮
    _btn_create_client_welcome = (By.XPATH, '//span[text()="新建员工欢迎语"]/..')
    # 员工欢迎语列表
    _texts_clients_welcome = (By.CSS_SELECTOR, '#pane-0 tbody tr td:first-child div')
    # 员工页面编辑按钮
    _btn_client_edit = (By.CSS_SELECTOR, '#pane-0 tbody tr td:nth-child(4) button')
    # 员工页面删除按钮
    _btn_client_delete = (By.CSS_SELECTOR, '#pane-0 tbody tr td:nth-child(4) button+button')
    # 员工页面删除确认按钮
    _btn_client_delete_confirm = (By.CSS_SELECTOR, '.el-message-box__btns  button+button')
    # 员工页面搜索输入框
    _input_client_search = (By.CSS_SELECTOR, '#pane-0 input[placeholder$="关键词"]')
    # 员工页面查询按钮
    _btn_client_search = (By.CSS_SELECTOR, '#pane-0 .search button')

    # 部门员工欢迎语页面
    # 新建部门员工欢迎语按钮
    _btn_create_department_client_welcome = (By.XPATH, '//span[text()="新建部门员工欢迎语"]/..')
    # 部门员工欢迎语列表
    _texts_department_clients_welcome = (By.CSS_SELECTOR, '#pane-1 tbody tr td:first-child div')
    # 部门员工页面编辑按钮
    _btn_department_client_edit = (By.CSS_SELECTOR, '#pane-1 tbody tr td:nth-child(4) button')
    # 部门员工页面删除按钮
    _btn_department_client_delete = (By.CSS_SELECTOR, '#pane-1 tbody tr td:nth-child(4) button+button')
    # 部门员工页面搜索输入框
    _input_department_client_search = (By.CSS_SELECTOR, '#pane-1 input[placeholder$="关键词"]')
    # 部门员工页面查询按钮
    _btn_department_client_search = (By.CSS_SELECTOR, '#pane-1 .search button')

    # 添加素材按钮
    _btn_add_materials = (By.XPATH, '//div[text()="添加图片/网页/小程序消息"]')
    # 添加图片按钮
    _btn_add_pic = (By.CSS_SELECTOR, '.material-type-list>div')
    # 欢迎语输入框
    _input_welcome = (By.CSS_SELECTOR, 'textarea')
    # 新建按钮
    _btn_create = (By.XPATH, '//span[text()="新建"]/..')
    # 插入客户昵称按钮
    _btn_insert_client_nickname = (By.XPATH, '//span[text()="插入客户昵称"]/..')
    # 添加员工按钮
    _btn_select_staff = (By.XPATH, '//span[text()="添加"]/..')
    # 保存按钮
    _btn_save = (By.XPATH, '//span[text()="保存"]/..')

    # 组织架构
    # 员工搜索输入框
    _input_select_staff = (By.CSS_SELECTOR, 'input[placeholder="请输入关键词"]')
    # 员工节点
    _btn_staff_node = (By.CSS_SELECTOR, '.custom-tree-node')
    # 选择确认按钮
    _btn_confirm = (By.CSS_SELECTOR, 'div[aria-label="组织架构"] div[class$="footer"] button+button')

    """元素定位层"""
    # 客户营销tab
    def get_btn_client_marketing_tab(self):
        return self.find_Element(self._btn_client_marketing_tab)
    # 员工活码页面
    def get_btn_welcome_page(self):
        return self.find_Element(self._btn_welcome_page)
    # 客户群活码tab
    def get_btn_department_client_tab(self):
        return self.find_Element(self._btn_department_client_tab)

    # 员工欢迎语页面
    # 新建员工欢迎语按钮
    def get_btn_create_client_welcome(self):
        return self.find_Element(self._btn_create_client_welcome)
    # 员工欢迎语列表
    def get_texts_clients_welcome(self):
        return self.find_Elements(self._texts_clients_welcome)
    # 员工页面编辑按钮
    def get_btn_client_edit(self):
        return self.find_Element(self._btn_client_edit)
    # 员工页面删除按钮
    def get_btn_client_delete(self):
        return self.find_Element(self._btn_client_delete)
    # 员工页面删除确认按钮
    def get_btn_client_delete_confirm(self):
        return self.find_Element(self._btn_client_delete_confirm)
    # 员工页面搜索输入框
    def get_input_client_search(self):
        return self.find_Element(self._input_client_search)
    # 员工页面查询按钮
    def get_btn_client_search(self):
        return self.find_Element(self._btn_client_search)

    # 部门员工欢迎语页面
    # 新建部门员工欢迎语按钮
    def get_btn_create_department_client_welcome(self):
        return self.find_Element(self._btn_create_department_client_welcome)
    # 部门员工欢迎语列表
    def get_texts_department_clients_welcome(self):
        return self.find_Elements(self._texts_department_clients_welcome)
    # 部门员工页面编辑按钮
    def get_btn_department_client_edit(self):
        return self.find_Element(self._btn_department_client_edit)
    # 部门员工页面删除按钮
    def get_btn_department_client_delete(self):
        return self.find_Element(self._btn_department_client_delete)
    # 部门员工页面搜索输入框
    def get_input_department_client_search(self):
        return self.find_Element(self._input_department_client_search)
    # 部门员工页面查询按钮
    def get_btn_department_client_search(self):
        return self.find_Element(self._btn_department_client_search)

    # 添加素材按钮
    def get_btn_add_materials(self):
        return self.find_Element(self._btn_add_materials)
    # 添加图片按钮
    def get_btn_add_pic(self):
        return self.find_Element(self._btn_add_pic)
    # 欢迎语输入框
    def get_input_welcome(self):
        return self.find_Element(self._input_welcome)
    # 新建按钮
    def get_btn_create(self):
        return self.find_Element(self._btn_create)
    # 插入客户昵称按钮
    def get_btn_insert_client_nickname(self):
        return self.find_Element(self._btn_insert_client_nickname)
    # 添加员工按钮
    def get_btn_select_staff(self):
        return self.find_Element(self._btn_select_staff)
    # 保存按钮
    def get_btn_save(self):
        return self.find_Element(self._btn_save)

    # 组织架构
    # 员工搜索输入框
    def get_input_select_staff(self):
        return self.find_Element(self._input_select_staff)
    # 员工节点
    def get_btn_staff_node(self):
        return self.find_Element(self._btn_staff_node)
    # 选择确认按钮
    def get_btn_confirm(self):
        return self.find_Element(self._btn_confirm)

    """元素操作层"""
    # 客户营销tab
    def click_btn_client_marketing_tab(self):
        return self.click_element(self.get_btn_client_marketing_tab())
    # 员工活码页面
    def click_btn_welcome_page(self):
        return self.click_element(self.get_btn_welcome_page())
    # 客户群活码tab
    def click_btn_department_client_tab(self):
        return self.click_element(self.get_btn_department_client_tab())

    # 员工欢迎语页面
    # 新建员工欢迎语按钮
    def click_btn_create_client_welcome(self):
        return self.click_element(self.get_btn_create_client_welcome())
    # 员工欢迎语列表
    def gettexts_texts_clients_welcome(self):
        return self.get_elements_values(self.get_texts_clients_welcome())
    # 员工页面编辑按钮
    def click_btn_client_edit(self):
        return self.click_element(self.get_btn_client_edit())
    # 员工页面删除按钮
    def click_btn_client_delete(self):
        return self.click_element(self.get_btn_client_delete())
    # 员工页面删除确认按钮
    def click_btn_client_delete_confirm(self):
        return self.click_element(self.get_btn_client_delete_confirm())
    # 员工页面搜索输入框
    def sendkeys_input_client_search(self, value):
        return self.send_keys(self.get_input_client_search(), value)
    # 员工页面查询按钮
    def click_btn_client_search(self):
        return self.click_element(self.get_btn_client_search())

    # 部门员工欢迎语页面
    # 新建部门员工欢迎语按钮
    def click_btn_create_department_client_welcome(self):
        return self.click_element(self.get_btn_create_department_client_welcome())
    # 部门员工欢迎语列表
    def gettexts_texts_department_clients_welcome(self):
        return self.get_elements_values(self.get_texts_department_clients_welcome())
    # 部门员工页面编辑按钮
    def click_btn_department_client_edit(self):
        return self.click_element(self.get_btn_department_client_edit())
    # 部门员工页面删除按钮
    def click_btn_department_client_delete(self):
        return self.click_element(self.get_btn_department_client_delete())
    # 部门员工页面搜索输入框
    def sendkeys_input_department_client_search(self, value):
        return self.send_keys(self.get_input_department_client_search(), value)
    # 部门员工页面查询按钮
    def click_btn_department_client_search(self):
        return self.click_element(self.get_btn_department_client_search())

    # 添加素材按钮
    def click_btn_add_materials(self):
        return self.click_element(self.get_btn_add_materials())
    # 添加图片按钮
    def click_btn_add_pic(self):
        return self.click_element(self.get_btn_add_pic())
    # 欢迎语输入框
    def sendkeys_input_welcome(self, value):
        return self.send_keys(self.get_input_welcome(), value)
    # 新建按钮
    def click_btn_create(self):
        return self.click_element(self.get_btn_create())
    # 插入客户昵称按钮
    def click_btn_insert_client_nickname(self):
        return self.click_element(self.get_btn_insert_client_nickname())
    # 添加员工按钮
    def click_btn_select_staff(self):
        return self.click_element(self.get_btn_select_staff())
    # 保存按钮
    def click_btn_save(self):
        return self.click_element(self.get_btn_save())

    # 组织架构
    # 员工搜索输入框
    def sendkeys_input_select_staff(self, value):
        return self.send_keys(self.get_input_select_staff(), value)
    # 员工节点
    def click_btn_staff_node(self):
        return self.click_element(self.get_btn_staff_node())
    # 选择确认按钮
    def click_btn_confirm(self):
        return self.click_element(self.get_btn_confirm())

    """业务层"""
    def switch_to_current(self):
        self.click_btn_client_marketing_tab()
        sleep(2)
        self.click_btn_welcome_page()
        sleep(3)

    def create_welcome(self, type, msg, staff=None):
        if type == 'client':
            self.click_btn_create_client_welcome()
        elif type == "dep":
            self.click_btn_department_client_tab()
            sleep(2)
            self.click_btn_create_department_client_welcome()
            sleep(2)
            self.click_btn_select_staff()
            sleep(2)
            self.sendkeys_input_select_staff(staff)
            sleep(1)
            self.tap_keyboard('enter')
            sleep(2)
            self.click_btn_staff_node()
            sleep(2)
            self.click_btn_confirm()
        else:
            print("未知的欢迎语类型")
            return
        sleep(2)
        self.sendkeys_input_welcome(msg)
        sleep(2)
        self.click_btn_insert_client_nickname()
        sleep(2)
        self.click_btn_create()
        sleep(2)
        if type == "client":
            wellist = self.gettexts_texts_clients_welcome()
        elif type == "dep":
            wellist = self.gettexts_texts_department_clients_welcome()
        else:
            print("未知的欢迎语类型")
            return
        self.assert_Equal(wellist[0], (msg+'#客户昵称#'))

    def search_key_words(self, type, key):
        if type == "client":
            self.sendkeys_input_client_search(key)
            sleep(2)
            self.click_btn_client_search()
            sleep(2)
            wellist = self.gettexts_texts_clients_welcome()
        elif type == "dep":
            self.click_btn_department_client_tab()
            sleep(2)
            self.sendkeys_input_department_client_search(key)
            sleep(2)
            self.click_btn_department_client_search()
            sleep(2)
            wellist = self.gettexts_texts_department_clients_welcome()
        else:
            print("未知的欢迎语类型")
            return
        for i in wellist:
            self.check_exist_in_lists(key, i)

    def edit_welcome(self, type, edited_msg):
        if type == "client":
            self.click_btn_client_edit()
        elif type == "dep":
            self.click_btn_department_client_tab()
            sleep(2)
            self.click_btn_department_client_edit()
        else:
            print("未知的欢迎语类型")
            return
        sleep(2)
        self.sendkeys_input_welcome(edited_msg)
        sleep(2)
        self.click_btn_save()
        sleep(2)
        if type == "client":
            wellist = self.gettexts_texts_clients_welcome()
        elif type == "dep":
            wellist = self.gettexts_texts_department_clients_welcome()
        else:
            print("未知的欢迎语类型")
            return
        self.assert_Equal(wellist[0], edited_msg)

    def delete_wel(self, type, msg):
        if type == "client":
            self.click_btn_client_delete()
        elif type == "dep":
            self.click_btn_department_client_tab()
            sleep(2)
            self.click_btn_department_client_delete()
        else:
            print("未知的欢迎语类型")
            return
        sleep(2)
        self.click_btn_client_delete_confirm()
        sleep(2)
        self.check_not_exist_in_page(msg)