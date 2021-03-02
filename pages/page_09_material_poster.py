from selenium.webdriver.common.by import By
from commons.base_page import BasePage
from time import sleep
from pymouse import PyMouse
import os


class PosterPage(BasePage):
    """元素定位信息"""
    # 客户营销tab
    _btn_client_marketing_tab = (By.XPATH, '//span[text()="客户营销"]/..')
    # 海报素材页面
    _btn_material_poster_page = (By.XPATH, '//li[text()=" 海报素材 "]')

    # 编辑分类按钮
    _btn_edit_group = (By.CSS_SELECTOR, '.edit_btn')
    # 添加主分类
    _btn_add_main_group = (By.XPATH, '//span[text()="+ 添加分类"]/..')
    # 添加子分类按钮
    _btn_add_child_group = (By.XPATH, '(//span[text()="+ 添加分类"]/..)[2]')
    # 添加海报按钮
    _btn_add_poster = (By.XPATH, '//span[text()="添加海报"]/..')
    # 移动分组按钮
    _btn_move_group = (By.XPATH, '//span[text()="移动分组"]/..')
    # 删除按钮
    _btn_delete_poster = (By.XPATH, '//span[text()="删除"]/..')
    # 点击具体分类
    _btn_select_specify_group = '//span[text()="{}"]/..'
    # 全选勾选框
    _btn_all_select = (By.CSS_SELECTOR, '.action-part span')
    # 海报选择勾选框
    _btn_check_poster = (By.CSS_SELECTOR, '.post-des .el-checkbox__inner')
    # 分类删除按钮
    _btn_delete_group = '//span[text()="{}"]/following-sibling::i'
    # 海报搜索输入框
    _input_poster_search = (By.CSS_SELECTOR, 'input[placeholder="搜索海报素材"]')
    # 海报查询按钮
    _btn_search = (By.XPATH, '//span[text()="查 询"]/..')
    # 编辑完成按钮
    _btn_edit_complete = (By.XPATH, '//span[text()="完成"]/..')
    # 删除确认按钮
    _btn_delete_confirm = (By.CSS_SELECTOR, '.el-message-box__btns button+button')
    # 移动分组输入框按钮
    _btn_input_move_group = (By.CSS_SELECTOR, 'input[placeholder="请选择"]')
    # 移动分组选择框
    _text_select_move_group = '//span[text()="{}"]/../label/..'
    # 移动分组选择框
    _btn_select_move_group = '//span[text()="{}"]/../label'
    # 移动分组选择按钮
    _btn_move_group_confirm = (By.XPATH, '//span[text()="确定"]/..')
    # # 移动分组二次确认按钮
    # _btn_move_group_twice_confirm = ()
    # 海报块
    _btn_poster = (By.CSS_SELECTOR, 'div[role="group"]')
    # 海报编辑按钮
    _btn_edit_poster = (By.CSS_SELECTOR, 'i[class="el-tooltip el-icon-edit item"]')
    # 海报分类名称输入框
    _input_poster_group_name = (By.CSS_SELECTOR, '.catagory__list input')
    # 主分类名称列表
    _texts_main_groups = (By.CSS_SELECTOR, 'div[class="main-catagory__wrap"] .catagory__list>span span')
    # 子分类名称列表
    _texts_child_groups = (By.CSS_SELECTOR, 'div[class="main-catagory__wrap sub__wrap"] .catagory__list>span span')
    # 海报名称列表
    _texts_poster_name = (By.CSS_SELECTOR, '.text-limit')

    # 新建页面
    # 海报名称输入框
    _input_poster_name = (By.CSS_SELECTOR, 'input[placeholder="请输入海报名称"]')
    # 海报分类输入框
    _btn_poster_groups = (By.CSS_SELECTOR, 'input[placeholder="请选择"]')
    # 海报分类选择
    _btn_select_poster_group = '//span[text()="{}"]/../label'
    # 背景图片选择
    _btn_upload_pic = (By.XPATH, '//div[text()="上传图片"]')
    # 分类选择面板第一项
    _text_first_group = (By.CSS_SELECTOR, 'div[role="menu"]')
    # 保存按钮
    _btn_save = (By.XPATH, '//span[text()="保存"]/..')

    '''元素定位层'''
    # 客户营销tab
    def get_btn_client_marketing_tab(self):
        return self.find_Element(self._btn_client_marketing_tab)
    # 海报素材页面
    def get_btn_material_poster_page(self):
        return self.find_Element(self._btn_material_poster_page)
    # 编辑分类按钮
    def get_btn_edit_group(self):
        return self.find_Element(self._btn_edit_group)
    # 添加主分类
    def get_btn_add_main_group(self):
        return self.find_Element(self._btn_add_main_group)
    # 添加子分类按钮
    def get_btn_add_child_group(self):
        return self.find_Element(self._btn_add_child_group)
    # 添加海报按钮
    def get_btn_add_poster(self):
        return self.find_Element(self._btn_add_poster)
    # 移动分组按钮
    def get_btn_move_group(self):
        return self.find_Element(self._btn_move_group)
    # 删除按钮
    def get_btn_delete_poster(self):
        return self.find_Element(self._btn_delete_poster)
    # 点击具体分类
    def get_btn_select_specify_group(self, value):
        return self.find_Element((By.XPATH, self._btn_select_specify_group.format(value)))
    # 全选勾选框
    def get_btn_all_select(self):
        return self.find_Element(self._btn_all_select)
    # 海报选择勾选框
    def get_btn_check_poster(self):
        return self.find_Element(self._btn_check_poster)
    # 分类删除按钮
    def get_btn_delete_group(self, value):
        return self.find_Element((By.XPATH, self._btn_delete_group.format(value)))
    # 海报搜索输入框
    def get_input_poster_search(self):
        return self.find_Element(self._input_poster_search)
    # 海报查询按钮
    def get_btn_search(self):
        return self.find_Element(self._btn_search)
    # 编辑完成按钮
    def get_btn_edit_complete(self):
        return self.find_Element(self._btn_edit_complete)
    # 删除确认按钮
    def get_btn_delete_confirm(self):
        return self.find_Element(self._btn_delete_confirm)
    # 移动分组输入框按钮
    def get_btn_input_move_group(self):
        return self.find_Element(self._btn_input_move_group)
        # 移动分组选择框
    def get_text_select_move_group(self, value):
        return self.find_Element((By.XPATH, self._text_select_move_group.format(value)))
    # 移动分组选择框
    def get_btn_select_move_group(self, value):
        return self.find_Element((By.XPATH, self._btn_select_move_group.format(value)))
    # 移动分组选择按钮
    def get_btn_move_group_confirm(self):
        return self.find_Element(self._btn_move_group_confirm)
    # 海报块
    def get_btn_poster(self):
        return self.find_Element(self._btn_poster)
    # 海报编辑按钮
    def get_btn_edit_poster(self):
        return self.find_Element(self._btn_edit_poster)
    # 海报分类名称输入框
    def get_input_poster_group_name(self):
        return self.find_Element(self._input_poster_group_name)
    # 主分类名称列表
    def get_texts_main_groups(self):
        return self.find_Elements(self._texts_main_groups)
    # 子分类名称列表
    def get_texts_child_groups(self):
        return self.find_Elements(self._texts_child_groups)
    # 海报名称列表
    def get_texts_poster_name(self):
        return self.find_Elements(self._texts_poster_name)

    # 新建页面
    # 海报名称输入框
    def get_input_poster_name(self):
        return self.find_Element(self._input_poster_name)
    # 海报分类输入框
    def get_btn_poster_groups(self):
        return self.find_Element(self._btn_poster_groups)
    # 海报分类选择
    def get_btn_select_poster_group(self, value):
        return self.find_Element((By.XPATH, self._btn_select_poster_group.format(value)))
    # 背景图片选择
    def get_btn_upload_pic(self):
        return self.find_Element(self._btn_upload_pic)
    # 分类选择面板第一项
    def get_text_first_group(self):
        return self.find_Element(self._text_first_group)
    # 保存按钮
    def get_btn_save(self):
        return self.find_Element(self._btn_save)

    '''元素操作层'''
    # 客户营销tab
    def click_btn_client_marketing_tab(self):
        return self.click_element(self.get_btn_client_marketing_tab())
    # 海报素材页面
    def click_btn_material_poster_page(self):
        return self.click_element(self.get_btn_material_poster_page())
    # 编辑分类按钮
    def click_btn_edit_group(self):
        return self.click_element(self.get_btn_edit_group())
    # 添加主分类
    def click_btn_add_main_group(self):
        return self.click_element(self.get_btn_add_main_group())
    # 添加子分类按钮
    def click_btn_add_child_group(self):
        return self.click_element(self.get_btn_add_child_group())
    # 添加海报按钮
    def click_btn_add_poster(self):
        return self.click_element(self.get_btn_add_poster())
    # 移动分组按钮
    def click_btn_move_group(self):
        return self.click_element(self.get_btn_move_group())
    # 删除按钮
    def click_btn_delete_poster(self):
        return self.click_element(self.get_btn_delete_poster())
    # 点击具体分类
    def click_btn_select_specify_group(self, value):
        return self.click_element(self.get_btn_select_specify_group(value))
    # 全选勾选框
    def click_btn_all_select(self):
        return self.click_element(self.get_btn_all_select())
    # 海报选择勾选框
    def click_btn_check_poster(self):
        return self.click_element(self.get_btn_check_poster())
    # 分类删除按钮
    def click_btn_delete_group(self, value):
        return self.click_element(self.get_btn_delete_group(value))
    # 海报搜索输入框
    def sendkeys_input_poster_search(self, value):
        return self.send_keys(self.get_input_poster_search(), value)
    # 海报查询按钮
    def click_btn_search(self):
        return self.click_element(self.get_btn_search())
    # 编辑完成按钮
    def click_btn_edit_complete(self):
        return self.click_element(self.get_btn_edit_complete())
    # 删除确认按钮
    def click_btn_delete_confirm(self):
        return self.click_element(self.get_btn_delete_confirm())
    # 移动分组输入框按钮
    def click_btn_input_move_group(self):
        return self.click_element(self.get_btn_input_move_group())
    # 移动分组选择框
    def click_btn_select_move_group(self, value):
        return self.click_element(self.get_btn_select_move_group(value))
    # 移动分组选择按钮
    def click_btn_move_group_confirm(self):
        return self.click_element(self.get_btn_move_group_confirm())
    # 海报块
    def move_btn_poster(self):
        return self.move_to_element(self.get_btn_poster())
    # 海报编辑按钮
    def click_btn_edit_poster(self):
        return self.click_element(self.get_btn_edit_poster())
    # 海报分类名称输入框
    def sendkdys_input_poster_group_name(self, value):
        return self.send_keys(self.get_input_poster_group_name(), value)
    # 主分类名称列表
    def gettexts_texts_main_groups(self):
        return self.get_elements_values(self.get_texts_main_groups())
    # 子分类名称列表
    def gettexts_texts_child_groups(self):
        return self.get_elements_values(self.get_texts_child_groups())
    # 海报名称列表
    def gettexts_texts_poster_name(self):
        return self.get_elements_values(self.get_texts_poster_name())

    # 新建页面
    # 海报名称输入框
    def sendkeys_input_poster_name(self, value):
        return self.send_keys(self.get_input_poster_name(), value)
    # 海报分类输入框
    def click_btn_poster_groups(self):
        return self.click_element(self.get_btn_poster_groups())
    # 海报分类选择
    def click_btn_select_poster_group(self, value):
        return self.click_element(self.get_btn_select_poster_group(value))
    # 背景图片选择
    def click_btn_upload_pic(self):
        return self.click_element(self.get_btn_upload_pic())
    # 保存按钮
    def click_btn_save(self):
        return self.click_element(self.get_btn_save())

    '''业务层'''
    def switch_to_current(self):
        sleep(2)
        self.click_btn_client_marketing_tab()
        sleep(2)
        self.click_btn_material_poster_page()
        sleep(2)

    def create_group(self, group):
        self.click_btn_edit_group()
        sleep(2)
        self.click_btn_add_main_group()
        sleep(2)
        self.sendkdys_input_poster_group_name(group)
        sleep(2)
        self.click_btn_edit_complete()
        sleep(2)
        group_list = self.gettexts_texts_main_groups()
        self.check_exist_in_lists(group, group_list)

    def create_poster(self, group, poster):
        self.click_btn_add_poster()
        sleep(2)
        self.sendkeys_input_poster_name(poster)
        sleep(2)
        self.click_btn_poster_groups()
        sleep(2)
        self.click_element(self.get_text_first_group())
        sleep(1)
        self.scroll_screen(self.get_text_select_move_group(group))
        sleep(1)
        self.click_element(self.get_text_select_move_group(group))
        sleep(1)
        self.click_btn_select_poster_group(group)
        sleep(2)
        m = PyMouse()
        x_dim, y_dim = m.screen_size()
        m.click(x_dim // 2, y_dim // 2)
        self.click_btn_upload_pic()
        sleep(1)
        path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '\\materials\\pic\\photo.png'
        self.tap_keyboard('shift')
        sleep(1)
        self.control_keyboard(path)
        sleep(1)
        self.tap_keyboard('enter')
        sleep(2)
        self.click_btn_save()
        sleep(2)
        self.check_exist_in_page(poster)

    def search_poster(self, poster):
        self.sendkeys_input_poster_search(poster)
        sleep(2)
        self.click_btn_search()
        sleep(2)
        name_list = self.gettexts_texts_poster_name()
        for i in name_list:
            self.check_exist_in_lists(poster, i)

    def move_group(self, poster, group):
        self.sendkeys_input_poster_search(poster)
        sleep(2)
        self.click_btn_search()
        sleep(2)
        self.click_btn_all_select()
        sleep(2)
        self.click_btn_move_group()
        sleep(2)
        self.click_btn_input_move_group()
        sleep(2)
        self.click_element(self.get_text_first_group())
        sleep(1)
        self.scroll_screen(self.get_text_select_move_group(group))
        sleep(1)
        self.click_element(self.get_text_select_move_group(group))
        sleep(1)
        self.click_btn_select_move_group(group)
        sleep(2)
        self.click_btn_move_group_confirm()
        sleep(2)
        self.click_btn_delete_confirm()
        sleep(2)
        self.click_btn_select_specify_group(group)
        sleep(2)
        self.check_exist_in_page(poster)

    def edit_poster(self, poster_edited, group):
        self.click_btn_select_specify_group(group)
        sleep(2)
        self.move_btn_poster()
        sleep(2)
        self.click_btn_edit_poster()
        sleep(2)
        self.sendkeys_input_poster_name(poster_edited)
        sleep(2)
        self.click_btn_save()
        sleep(2)
        self.check_exist_in_page(poster_edited)

    def delete_poster(self, poster, group):
        self.click_btn_select_specify_group(group)
        sleep(2)
        self.click_btn_all_select()
        sleep(2)
        self.click_btn_delete_poster()
        sleep(2)
        self.click_btn_delete_confirm()
        sleep(2)
        self.check_not_exist_in_page(poster)

    def create_child_group(self, group, child_group):
        self.click_btn_select_specify_group(group)
        sleep(2)
        self.click_btn_edit_group()
        sleep(2)
        self.click_btn_add_child_group()
        sleep(2)
        self.sendkdys_input_poster_group_name(child_group)
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