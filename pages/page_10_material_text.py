import os

from selenium.webdriver.common.by import By
from commons.base_page import BasePage
from time import sleep
from pymouse import PyMouse


class TextPage(BasePage):
    """元素定位信息"""
    # 客户营销tab
    _btn_client_marketing_tab = (By.XPATH, '//span[text()="客户营销"]/..')
    # 海报素材页面
    _btn_material_others_page = (By.XPATH, '//li[text()=" 其他素材 "]')
    # 文本页面按钮
    _btn_text_page = (By.XPATH, '//p[text()="文本"]/..')

    # 添加文本按钮
    _btn_add_text = (By.XPATH, '//span[text()="添加文本"]/..')
    # 搜索文本输入框
    _input_search_text = (By.CSS_SELECTOR, 'input[placeholder="搜索文本素材"]')
    # 查询按钮
    _btn_search = (By.XPATH, '//span[text()="查询"]/..')
    # 批量导入按钮
    _btn_export_in_batch = (By.XPATH, '//span[text()="批量导入"]/..')
    # 编辑分类按钮
    _btn_edit_group = (By.CSS_SELECTOR, '.edit_btn')
    # 添加主分类
    _btn_add_main_group = (By.XPATH, '//span[text()="+ 添加分类"]/..')
    # 添加子分类按钮
    _btn_add_child_group = (By.XPATH, '(//span[text()="+ 添加分类"]/..)[2]')
    # 移动分组按钮
    _btn_move_group = (By.XPATH, '//span[text()="移动分组"]/..')
    # 删除按钮
    _btn_delete_text = (By.XPATH, '//span[text()="删除"]/..')
    # 点击具体分类
    _btn_select_specify_group = '//span[text()="{}"]/..'
    # 全选勾选框
    _btn_all_select = (By.CSS_SELECTOR, '.header_sel_wrap span')
    # 文本选择勾选框
    _btn_check_text = (By.CSS_SELECTOR, 'div[role="group"] label')
    # 分类删除按钮
    _btn_delete_group = '//span[text()="{}"]/following-sibling::i'
    # 编辑完成按钮
    _btn_edit_complete = (By.XPATH, '//span[text()="完成"]/..')
    # 删除确认按钮
    _btn_delete_confirm = (By.CSS_SELECTOR, '.el-message-box__btns button+button')
    # 移动分组输入框按钮
    _btn_input_move_group = (By.CSS_SELECTOR, 'input[placeholder="请选择"]')
    # 移动分组文本组块
    _btn_move_group_text_groups = (By.XPATH, '(//div[@class="el-cascader-menu__wrap el-scrollbar__wrap"])[2]')
    # 移动分组选择框
    _text_select_move_group = '//span[text()="{}"]/../label/..'
    # 移动分组选择框
    _btn_select_move_group = '//span[text()="{}"]/../label'
    # 移动分组选择按钮
    _btn_move_group_confirm = (By.XPATH, '//span[text()="确定"]/..')
    # 文本编辑按钮
    _btn_edit_text = (By.XPATH, '//span[text()="编辑"]/..')
    # 文本分类名称输入框
    _input_text_group_name = (By.CSS_SELECTOR, '.catagory__list input')
    # 主分类名称列表
    _texts_main_groups = (By.CSS_SELECTOR, 'div[class="main-catagory__wrap"] .catagory__list>span span')
    # 子分类名称列表
    _texts_child_groups = (By.CSS_SELECTOR, 'div[class="main-catagory__wrap sub__wrap"] .catagory__list>span span')
    # 文本内容列表
    _texts_text_name = (By.CSS_SELECTOR, 'table tr td:nth-child(2) div')

    # 新建页面
    # 文本分类选择框
    _btn_select_group = (By.CSS_SELECTOR, 'div[aria-label] input[placeholder="请选择"]')
    # 文本组块
    _btn_text_groups = (By.CSS_SELECTOR, 'div[class="el-cascader-panel"] ul li')
    # 文本分类选择
    _btn_select_text_group = '(//span[text()="{}"]/../label)[2]'
    # 文本分组div块
    _text_select_text_group = '(//span[text()="{}"]/../label/..)[2]'
    # 文本内容输入框
    _input_text_msg = (By.CSS_SELECTOR, 'textarea')
    # 保存按钮
    _btn_save = (By.XPATH, '(//span[text()="确 定"]/..)[2]')

    '''元素定位层'''
    # 客户营销tab
    def get_btn_client_marketing_tab(self):
        return self.find_Element(self._btn_client_marketing_tab)
    # 海报素材页面
    def get_btn_material_others_page(self):
        return self.find_Element(self._btn_material_others_page)
    # 文本页面按钮
    def get_btn_text_page(self):
        return self.find_Element(self._btn_text_page)
    # 添加文本按钮
    def get_btn_add_text(self):
        return self.find_Element(self._btn_add_text)
    # 搜索文本输入框
    def get_input_search_text(self):
        return self.find_Element(self._input_search_text)
    # 查询按钮
    def get_btn_search(self):
        return self.find_Element(self._btn_search)
    # 批量导入按钮
    def get_btn_export_in_batch(self):
        return self.find_Element(self._btn_export_in_batch)
    # 编辑分类按钮
    def get_btn_edit_group(self):
        return self.find_Element(self._btn_edit_group)
    # 添加主分类
    def get_btn_add_main_group(self):
        return self.find_Element(self._btn_add_main_group)
    # 添加子分类按钮
    def get_btn_add_child_group(self):
        return self.find_Element(self._btn_add_child_group)
    # 移动分组按钮
    def get_btn_move_group(self):
        return self.find_Element(self._btn_move_group)
    # 删除按钮
    def get_btn_delete_text(self):
        return self.find_Element(self._btn_delete_text)
    # 点击具体分类
    def get_btn_select_specify_group(self, value):
        return self.find_Element((By.XPATH, self._btn_select_specify_group.format(value)))
    # 全选勾选框
    def get_btn_all_select(self):
        return self.find_Element(self._btn_all_select)
    # 文本选择勾选框
    def get_btn_check_text(self):
        return self.find_Element(self._btn_check_text)
    # 分类删除按钮
    def get_btn_delete_group(self, value):
        return self.find_Element((By.XPATH, self._btn_delete_group.format(value)))
    # 编辑完成按钮
    def get_btn_edit_complete(self):
        return self.find_Element(self._btn_edit_complete)
    # 删除确认按钮
    def get_btn_delete_confirm(self):
        return self.find_Element(self._btn_delete_confirm)
    # 移动分组输入框按钮
    def get_btn_input_move_group(self):
        return self.find_Element(self._btn_input_move_group)
    # 移动分组文本组块
    def get_btn_move_group_text_groups(self):
        return self.find_Element(self._btn_move_group_text_groups)
    # 移动分组选择框
    def get_text_select_move_group(self, value):
        return self.find_Element((By.XPATH, self._text_select_move_group.format(value)))
    # 移动分组选择框
    def get_btn_select_move_group(self, value):
        return self.find_Element((By.XPATH, self._btn_select_move_group.format(value)))
    # 移动分组选择按钮
    def get_btn_move_group_confirm(self):
        return self.find_Element(self._btn_move_group_confirm)
    # 文本编辑按钮
    def get_btn_edit_text(self):
        return self.find_Element(self._btn_edit_text)
    # 文本分类名称输入框
    def get_input_text_group_name(self):
        return self.find_Element(self._input_text_group_name)
    # 主分类名称列表
    def get_texts_main_groups(self):
        return self.find_Elements(self._texts_main_groups)
    # 子分类名称列表
    def get_texts_child_groups(self):
        return self.find_Elements(self._texts_child_groups)
    # 文本内容列表
    def get_texts_text_name(self):
        return self.find_Elements(self._texts_text_name)

    # 新建页面
    # 文本分类选择框
    def get_btn_select_group(self):
        return self.find_Element(self._btn_select_group)
    # 文本组块
    def get_btn_text_groups(self):
        return self.find_Element(self._btn_text_groups)
    # 文本分类选择
    def get_btn_select_text_group(self, value):
        return self.find_Element((By.XPATH, self._btn_select_text_group.format(value)))
    # 文本分组块
    def get_text_select_text_group(self, value):
        return self.find_Element((By.XPATH, self._text_select_text_group.format(value)))
    # 文本内容输入框
    def get_input_text_msg(self):
        return self.find_Element(self._input_text_msg)
    # 保存按钮
    def get_btn_save(self):
        return self.find_Element(self._btn_save)

    '''元素操作层'''
    # 客户营销tab
    def click_btn_client_marketing_tab(self):
        return self.click_element(self.get_btn_client_marketing_tab())
    # 海报素材页面
    def click_btn_material_others_page(self):
        return self.click_element(self.get_btn_material_others_page())
    # 文本页面按钮
    def click_btn_text_page(self):
        return self.click_element(self.get_btn_text_page())
    # 添加文本按钮
    def click_btn_add_text(self):
        return self.click_element(self.get_btn_add_text())
    # 搜索文本输入框
    def sendkeys_input_search_text(self, value):
        return self.send_keys(self.get_input_search_text(), value)
    # 查询按钮
    def click_btn_search(self):
        return self.click_element(self.get_btn_search())
    # 批量导入按钮
    def click_btn_export_in_batch(self):
        return self.click_element(self.get_btn_export_in_batch())
    # 编辑分类按钮
    def click_btn_edit_group(self):
        return self.click_element(self.get_btn_edit_group())
    # 添加主分类
    def click_btn_add_main_group(self):
        return self.click_element(self.get_btn_add_main_group())
    # 添加子分类按钮
    def click_btn_add_child_group(self):
        return self.click_element(self.get_btn_add_child_group())
    # 移动分组按钮
    def click_btn_move_group(self):
        return self.click_element(self.get_btn_move_group())
    # 删除按钮
    def click_btn_delete_text(self):
        return self.click_element(self.get_btn_delete_text())
    # 点击具体分类
    def click_btn_select_specify_group(self, value):
        return self.click_element(self.get_btn_select_specify_group(value))
    # 全选勾选框
    def click_btn_all_select(self):
        return self.click_element(self.get_btn_all_select())
    # 文本选择勾选框
    def click_btn_check_text(self):
        return self.click_element(self.get_btn_check_text())
    # 分类删除按钮
    def click_btn_delete_group(self, value):
        return self.click_element(self.get_btn_delete_group(value))
    # 编辑完成按钮
    def click_btn_edit_complete(self):
        return self.click_element(self.get_btn_edit_complete())
    # 删除确认按钮
    def click_btn_delete_confirm(self):
        return self.click_element(self.get_btn_delete_confirm())
    # 移动分组输入框按钮
    def click_btn_input_move_group(self):
        return self.click_element(self.get_btn_input_move_group())
    # 移动分组文本组块
    def click_btn_move_group_text_groups(self):
        return self.click_element(self.get_btn_move_group_text_groups())
    # 移动分组选择框
    def click_text_select_move_group(self, value):
        return self.click_element(self.get_text_select_move_group(value))
    # 移动分组选择框
    def click_btn_select_move_group(self, value):
        return self.click_element(self.get_btn_select_move_group(value))
    # 移动分组选择按钮
    def click_btn_move_group_confirm(self):
        return self.click_element(self.get_btn_move_group_confirm())
    # 文本编辑按钮
    def click_btn_edit_text(self):
        return self.click_element(self.get_btn_edit_text())
    # 文本分类名称输入框
    def sendkeys_input_text_group_name(self, value):
        return self.send_keys(self.get_input_text_group_name(), value)
    # 主分类名称列表
    def gettexts_texts_main_groups(self):
        return self.get_elements_values(self.get_texts_main_groups())
    # 子分类名称列表
    def gettexts_texts_child_groups(self):
        return self.get_elements_values(self.get_texts_child_groups())
    # 文本内容列表
    def gettexts_texts_text_name(self):
        return self.get_elements_values(self.get_texts_text_name())

    # 新建页面
    # 文本分类选择框
    def click_btn_select_group(self):
        return self.click_element(self.get_btn_select_group())
    # 文本组块
    def click_btn_text_groups(self):
        return self.click_element(self.get_btn_text_groups())
    # 文本分类选择
    def click_btn_select_text_group(self, value):
        return self.click_element(self.get_btn_select_text_group(value))
    # 文本分组块
    def click_text_select_text_group(self, value):
        return self.click_element(self.get_text_select_text_group(value))
    # 文本内容输入框
    def sendkeys_input_text_msg(self, value):
        return self.send_keys(self.get_input_text_msg(), value)
    # 保存按钮
    def click_btn_save(self):
        return self.click_element(self.get_btn_save())

    '''业务层'''
    def switch_to_current(self):
        sleep(2)
        self.click_btn_client_marketing_tab()
        sleep(2)
        self.click_btn_material_others_page()
        sleep(2)
        self.click_btn_text_page()
        sleep(2)

    def create_group(self, group):
        self.click_btn_edit_group()
        sleep(2)
        self.click_btn_add_main_group()
        sleep(2)
        self.sendkeys_input_text_group_name(group)
        sleep(2)
        self.click_btn_edit_complete()
        sleep(2)
        group_list = self.gettexts_texts_main_groups()
        self.check_exist_in_lists(group, group_list)

    def create_text(self, group, msg):
        self.click_btn_add_text()
        sleep(2)
        self.click_btn_select_group()
        sleep(2)
        # self.click_btn_text_groups()
        # sleep(1)
        self.scroll_screen(self.get_text_select_text_group(group))
        sleep(1)
        self.click_text_select_text_group(group)
        sleep(1)
        self.click_text_select_text_group(group)
        sleep(1)
        self.click_btn_select_text_group(group)
        sleep(2)
        m = PyMouse()
        x_dim, y_dim = m.screen_size()
        m.click(x_dim // 2, y_dim // 2)
        sleep(1)
        self.sendkeys_input_text_msg(msg)
        sleep(2)
        self.click_btn_save()
        sleep(2)
        self.check_exist_in_page(msg)

    def search_text(self, msg):
        self.sendkeys_input_search_text(msg)
        sleep(2)
        self.click_btn_search()
        sleep(2)
        name_list = self.gettexts_texts_text_name()
        self.check_exist_in_lists(msg, name_list)

    def move_group(self, msg, group, group2):
        self.click_btn_select_specify_group(group)
        sleep(2)
        self.click_btn_all_select()
        sleep(2)
        self.click_btn_move_group()
        sleep(2)
        self.click_btn_input_move_group()
        sleep(2)
        self.scroll_screen(self.get_text_select_move_group(group2))
        sleep(1)
        self.click_text_select_move_group(group2)
        sleep(1)
        self.click_text_select_move_group(group2)
        sleep(1)
        self.click_btn_select_move_group(group2)
        sleep(2)
        self.click_btn_move_group_confirm()
        sleep(2)
        self.click_btn_delete_confirm()
        sleep(2)
        self.click_btn_select_specify_group(group2)
        sleep(2)
        self.check_exist_in_page(msg)

    def edit_text(self, msg2, group):
        self.click_btn_select_specify_group(group)
        sleep(2)
        self.click_btn_edit_text()
        sleep(2)
        self.sendkeys_input_text_msg(msg2)
        sleep(2)
        self.click_btn_save()
        sleep(2)
        self.check_exist_in_page(msg2)

    def delete_text(self, msg, group):
        self.click_btn_select_specify_group(group)
        sleep(2)
        self.click_btn_all_select()
        sleep(2)
        self.click_btn_delete_text()
        sleep(2)
        self.click_btn_delete_confirm()
        sleep(2)
        self.check_not_exist_in_page(msg)

    def create_child_group(self, group, child_group):
        self.click_btn_select_specify_group(group)
        sleep(2)
        self.click_btn_edit_group()
        sleep(2)
        self.click_btn_add_child_group()
        sleep(2)
        self.sendkeys_input_text_group_name(child_group)
        sleep(2)
        self.click_btn_edit_complete()
        sleep(2)
        namelist = self.gettexts_texts_child_groups()
        self.check_exist_in_lists(child_group, namelist)

    def delete_child_group(self, group, child_group):
        self.click_btn_select_specify_group(group)
        sleep(2)
        self.click_btn_edit_group()
        sleep(2)
        self.click_btn_delete_group(child_group)
        sleep(2)
        self.click_btn_delete_confirm()
        sleep(2)
        self.click_btn_edit_complete()
        sleep(2)
        self.check_not_exist_in_page(child_group)

    def delete_group(self, group):
        self.click_btn_edit_group()
        sleep(2)
        self.click_btn_delete_group(group)
        sleep(2)
        self.click_btn_delete_confirm()
        sleep(2)
        self.click_btn_edit_complete()
        sleep(1)
        grouplist = self.gettexts_texts_main_groups()
        self.check_exist_not_in_lists(group, grouplist)
        sleep(2)
