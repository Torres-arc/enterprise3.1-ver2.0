from selenium.webdriver.common.by import By
from commons.base_page import BasePage
from time import sleep
from pykeyboard import PyKeyboard
from pymouse import PyMouse


class ClientTags(BasePage):
    """元素定位信息"""
    # 本页面元素
    # 客户管理tab
    _btn_client_manage_tab = (By.XPATH, '//span[text()="客户管理"]/..')
    # 客户页面
    _btn_client_tag_page = (By.XPATH, '//li[text()=" 客户标签 "]')
    # 新建标签组按钮
    _btn_create_tag_group = (By.XPATH, '//span[text()="新建标签组"]/..')
    # 标签组名称列表
    _texts_list_tag_group = (By.CSS_SELECTOR, 'tbody>tr>td:first-child div')
    # 特定标签组的编辑按钮
    _btn_spcecify_edit = 'tbody>tr:nth-child({})>td:last-child button:first-child'
    # 特定标签组的删除按钮
    _btn_specify_delete = 'tbody>tr:nth-child({})>td:last-child button+button'

    # 标签窗口
    # 标签组名称输入框
    _input_tag_group_name = (By.XPATH, '//form[@class="el-form"]/div[1]/div[2]/div/input')
    # 添加标签按钮
    _btn_add_tag = (By.XPATH, '//span[text()="+ 添加标签"]/..')
    # 标签输入框
    _input_tag = (By.XPATH, '//form[@class="el-form"]/div[2]/div[2]/div/input')
    # 确定按钮
    _btn_confirm = (By.XPATH, '//div[@class="el-dialog__footer"]/div/button[2]')
    # 现有标签列表
    _texts_list_tags_exist = (By.XPATH, '//div[@class="el-form-item__content"]/span/span')
    # 标签删除按钮
    _btn_delete_tag = '//div[@class="el-form-item__content"]/span/span[{}]/i'

    # 删除提示窗口
    # 确定按钮
    _btn_delete_sure = (By.XPATH, '//div[@class="el-message-box__btns"]/button[2]')

    '''元素定位层'''
    # 本页面元素
    # 客户管理tab
    def get_btn_client_manage_tab(self):
        return self.find_Element(self._btn_client_manage_tab)
    # 客户页面
    def get_btn_client_tag_page(self):
        return self.find_Element(self._btn_client_tag_page)
    # 新建标签组按钮
    def get_btn_create_tag_group(self):
        return self.find_Element(self._btn_create_tag_group)
    # 标签组名称列表
    def get_texts_list_tag_group(self):
        return self.find_Elements(self._texts_list_tag_group)
    # 特定标签组的编辑按钮
    def get_btn_spcecify_edit(self, index):
        return self.find_Element((By.CSS_SELECTOR, self._btn_spcecify_edit.format(index)))
    # 特定标签组的删除按钮
    def get_btn_specify_delete(self, index):
        return self.find_Element((By.CSS_SELECTOR, self._btn_specify_delete.format(index)))

    # 标签窗口
    # 标签组名称输入框
    def get_input_tag_group_name(self):
        return self.find_Element(self._input_tag_group_name)
    # 添加标签按钮
    def get_btn_add_tag(self):
        return self.find_Element(self._btn_add_tag)
    # 标签输入框
    def get_input_tag(self):
        return self.find_Element(self._input_tag)
    # 确定按钮
    def get_btn_confirm(self):
        return self.find_Element(self._btn_confirm)
    # 现有标签列表
    def get_texts_list_tags_exist(self):
        return self.find_Elements(self._texts_list_tags_exist)
    # 标签删除按钮
    def get_btn_delete_tag(self, index):
        return self.find_Element((By.XPATH, self._btn_delete_tag.format(index)))

    # 删除提示窗口
    # 确定按钮
    def get_btn_delete_sure(self):
        return self.find_Element(self._btn_delete_sure)

    '''元素操作层'''
    # 本页面元素
    # 客户管理tab
    def click_btn_client_manage_tab(self):
        return self.click_element(self.get_btn_client_manage_tab())
    # 客户页面
    def click_btn_client_tag_page(self):
        return self.click_element(self.get_btn_client_tag_page())
    # 新建标签组按钮
    def click_btn_create_tag_group(self):
        return self.click_element(self.get_btn_create_tag_group())
    # 标签组名称列表
    def gettexts_texts_list_tag_group(self):
        return self.get_elements_values(self.get_texts_list_tag_group())
    # 特定标签组的编辑按钮
    def click_btn_spcecify_edit(self, index):
        return self.click_element(self.get_btn_spcecify_edit(index))
    # 特定标签组的删除按钮
    def click_btn_specify_delete(self, index):
        return self.click_element(self.get_btn_specify_delete(index))

    # 标签窗口
    # 标签组名称输入框
    def sendkeys_input_tag_group_name(self, value):
        return self.send_keys(self.get_input_tag_group_name(), value)
    # 添加标签按钮
    def click_btn_add_tag(self):
        return self.click_element(self.get_btn_add_tag())
    # 标签输入框
    def sendkeys_input_tag(self, value):
        return self.send_keys(self.get_input_tag(), value)
    # 确定按钮
    def click_btn_confirm(self):
        return self.click_element(self.get_btn_confirm())
    # 现有标签列表
    def gettexts_texts_list_tags_exist(self):
        return self.get_elements_values(self.get_texts_list_tags_exist())
    # 标签删除按钮
    def click_btn_delete_tag(self, index):
        return self.click_element(self.get_btn_delete_tag(index))

    # 删除提示窗口
    # 确定按钮
    def click_btn_delete_sure(self):
        return self.click_element(self.get_btn_delete_sure())

    '''业务层'''
    def switch_to_current(self):
        self.click_btn_client_manage_tab()  # 跳转至客户管理tab
        sleep(1)
        self.click_btn_client_tag_page()  # 进入客户页面
        sleep(3)

    def enter_edit_by_name(self, name):
        taglist = self.gettexts_texts_list_tag_group()
        m = 1
        self.check_exist_in_lists(name, taglist)
        for tagname in taglist:
            if name == tagname:
                self.click_btn_spcecify_edit(str(m))
            m += 1

    def add_tag_group(self, tag_group, tag):
        self.click_btn_create_tag_group()
        sleep(2)
        self.sendkeys_input_tag_group_name(tag_group)
        n = 0
        while n < len(tag):
            self.click_btn_add_tag()
            sleep(1)
            self.sendkeys_input_tag(tag[n])
            k = PyKeyboard()
            k.tap_key(k.enter_key)
            sleep(1)
            n += 1
        self.click_btn_confirm()
        sleep(3)
        taglist = self.gettexts_texts_list_tag_group()
        m = 1
        self.check_exist_in_lists(tag_group, taglist)
        for tagname in taglist:
            if tag_group == tagname:
                self.click_btn_spcecify_edit(str(m))
                sleep(2)
                a = self.gettexts_texts_list_tags_exist()
                a.sort()
                tag.sort()
                self.assert_Equal(a, tag)
            m += 1
        sleep(2)

    def edit_tag_group(self, tag_group, dtag, atag, tag2):
        self.enter_edit_by_name(tag_group)
        sleep(2)
        a = self.gettexts_texts_list_tags_exist()
        n = 1
        self.check_exist_in_lists(dtag, a)
        for tag in a:
            if tag == dtag:
                self.click_btn_delete_tag(n)
                break
            n += 1
        sleep(2)
        self.click_btn_add_tag()
        sleep(2)
        self.sendkeys_input_tag(atag)
        sleep(1)
        k = PyKeyboard()
        k.tap_key(k.enter_key)
        sleep(2)
        self.click_btn_confirm()
        sleep(2)
        self.enter_edit_by_name(tag_group)
        sleep(2)
        a = self.gettexts_texts_list_tags_exist()
        a.sort()
        tag2.sort()
        self.assert_Equal(a, tag2)
        sleep(3)

    def delete_tag_group(self, tag_group):
        sleep(2)
        taglist = self.gettexts_texts_list_tag_group()
        m = 1
        self.check_exist_in_lists(tag_group, taglist)
        for tagname in taglist:
            if tag_group == tagname:
                self.click_btn_specify_delete(m)
                sleep(2)
                self.click_btn_delete_sure()
                sleep(3)
                break
            m += 1
        taglist = self.gettexts_texts_list_tag_group()
        self.check_exist_not_in_lists(tag_group, taglist)










