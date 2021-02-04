from commons.base_page import BasePage
from time import sleep
import os
from commons.log import log
from pykeyboard import PyKeyboard
from selenium import webdriver
from selenium.webdriver.common.by import By


class MaterialWebPage(BasePage):
    """元素定位信息"""
    # 基础页面
    # 跳转页面
    _btn_web = (By.XPATH, '//li[text()="网页"]')
    # 添加网页按钮
    _btn_add_web = (By.XPATH, '//span[text()="添加网页"]')
    # 新增分组按钮
    _btn_add_group = (By.XPATH, '//i[@class="el-icon-plus"]')
    # 素材搜索框
    _input_material = (By.XPATH, '//input[@placeholder="搜索网页素材"]')
    # 分组名字列表
    _list_group_name = (By.XPATH, '//span[@class="department-name"]')
    # 特定分组
    _specify_group = ('xpath', '//span[text()="%s"]')
    # 特定分组编辑按钮
    _btn_specify_group_edit = ('xpath', '//span[text()="%s"]/../../div')
    # 网页素材模块
    _web_water_fall_title = (By.CSS_SELECTOR, '.picture-text-title')
    _web_water_fall_sum = (By.CSS_SELECTOR, '.picture-text-desc')
    _web_btn_edit = (By.CSS_SELECTOR, '[class="el-tooltip el-icon-edit item"]')
    _web_btn_delete = (By.CSS_SELECTOR, '[class="el-tooltip el-icon-delete item"]')
    _web_module = (By.CSS_SELECTOR, '.el-checkbox-group')
    # 删除按钮
    _btn_sure = (By.XPATH, '//div[@class="el-message-box__btns"]/button[2]')
    # # 网页标题
    # _text_title_web = ('xpath', '//div[@class="picture-text-title"]/div[text()="%s"]')
    # # 网页摘要
    # _text_sum_web = ('xpath', '//div[@class="picture-text-desc"]/div[text()="%s"]')

    # 分组编辑弹窗
    # 添加子分组按钮
    _btn_add_child_group = (By.CSS_SELECTOR, 'ul[x-placement] :nth-child(2)')
    # 修改名称按钮
    _btn_change_group_name = (By.CSS_SELECTOR, 'ul[x-placement] :nth-child(3)')
    # 删除分组按钮
    _btn_delete_group = (By.CSS_SELECTOR, 'ul[x-placement] :nth-child(4)')
    # 删除分组确定按钮
    _btn_delete_group_confirm = (By.CSS_SELECTOR, 'div[aria-label="删除分类"] div[class$="btns"] button:last-child')

    # 子分类输入框
    _input_child_group = (By.CSS_SELECTOR, 'div[aria-label] div.el-input input')
    # 子分类确定按钮
    _btn_confirm_child_group = (By.XPATH, '//span[text()="确 定"]/..')

    # 添加分组页面
    # 分组名输入框
    _input_add_group_first = (By.XPATH, '//div[@class="el-form-item__content"]/div/input')
    # 确定按钮
    _btn_confirm = (By.XPATH, '//div[@class="el-dialog__footer"]/div/button[2]')

    # 添加网页页面
    # 自定义网页类型选择
    _btn_select_customize_web = (By.XPATH, '//div[@class="el-form-item__content"]/label[1]/span[1]')
    # 外链网页类型选择
    _btn_select_external_link_web = (By.XPATH, '//div[@class="el-form-item__content"]/label[2]/span[1]')
    # 网页标题输入框
    _input_web_title = (By.XPATH, '//input[@placeholder="请输入标题"]')
    # 网页分类下拉框
    _select_web_classify = (By.XPATH, '//label[text()="网页分类"]/../div/div/div[1]/input')
    # 下拉框分组选择
    _btn_select_group1 = ('xpath', '//span[text()="%s"]')
    _btn_select_group2 = '../label'
    # '//span[text()="测试分组1"]/../label'
    # By.CSS_SELECTOR, 'div[x-placement] li>label'
    # 封面图上传按钮
    _btn_upload_pic = (By.XPATH, '//div[@class="el-upload__text"]')
    # 摘要输入框
    _input_summary = (By.XPATH, '//textarea[@class="el-textarea__inner"]')
    # 正文输入框
    _input_main = (By.XPATH, '//div[@class="ql-editor ql-blank"]')
    # 完成按钮
    _btn_complete = (By.XPATH, '//span[text()="完 成"]')
    # 外链输入框
    _input_external_link = (By.XPATH, '//label[text()="外链"]/../div/div/input')

    """元素定位层"""
    # 基础页面
    # 获取跳转按钮
    def get_btn_web(self):
        return self.find_Element(self._btn_web)
    # 获取添加网页按钮
    def get_btn_add_web(self):
        return self.find_Element(self._btn_add_web)
    # 获取新增分组按钮
    def get_btn_add_group(self):
        return self.find_Element(self._btn_add_group)
    # 获取素材搜索框
    def get_input_material(self):
        return self.find_Element(self._input_material)
    # 获取分组名字列表
    def get_list_group_name(self):
        return self.find_Elements(self._list_group_name)
    # 获取特定分组
    def get_specify_group(self, group):
        return self.find_ele_replace(self._specify_group[0], self._specify_group[1], group)
    # 获取特定网页标题
    def get_text_title_web(self):
        return self.find_Elements(self._web_water_fall_title)
    # 获取特定网页摘要
    def get_text_sum_web(self):
        return self.find_Elements(self._web_water_fall_sum)
    # 获取编辑网页按钮
    def get_btn_edit(self):
        return self.find_Elements(self._web_btn_edit)
    # 获取删除网页按钮
    def get_btn_delete(self):
        return self.find_Elements(self._web_btn_delete)
    # 获取网页模块列表数量
    def get_web_module_dic(self):
        list = self.find_Elements(self._web_module)
        return len(list)
    # 获取确定按钮
    def get_btn_sure(self):
        return self.find_Element(self._btn_sure)
    # 获取特定分组的编辑按钮
    def get_btn_specify_group_edit(self, group):
        return self.find_ele_replace(self._btn_specify_group_edit[0], self._btn_specify_group_edit[1], group)

    # 分组编辑弹窗
    # 获取添加子分组按钮
    def get_btn_add_child_group(self):
        return self.find_Element(self._btn_add_child_group)
    # 获取修改名称按钮
    def get_btn_change_group_name(self):
        return self.find_Element(self._btn_change_group_name)
    # 获取删除按钮
    def get_btn_delete_group(self):
        return self.find_Element(self._btn_delete_group)
    # 删除分组确定按钮
    def get_btn_delete_group_confirm(self):
        return self.find_Element(self._btn_delete_group_confirm)

    # 子分类输入框
    def get_input_child_group(self):
        return self.find_Element(self._input_child_group)
    # 子分类确定按钮
    def get_btn_confirm_child_group(self):
        return self.find_Element(self._btn_confirm_child_group)

    # 添加分组页面
    # 获取分组名输入框
    def get_input_add_group_first(self):
        return self.find_Element(self._input_add_group_first)
    # 获取确定按钮
    def get_btn_confirm(self):
        return self.find_Element(self._btn_confirm)

    # 添加网页页面
    # 获取自定义网页类型选择
    def get_btn_select_customize_web(self):
        return self.find_Element(self._btn_select_customize_web)
    # 获取外链网页类型选择
    def get_btn_select_external_link_web(self):
        return self.find_Element(self._btn_select_external_link_web)
    # 获取网页标题输入框
    def get_input_web_title(self):
        return self.find_Element(self._input_web_title)
    # 获取网页分类下拉框
    def get_select_web_classify(self):
        return self.find_Element(self._select_web_classify)
    # 获取下拉框分组选择
    def get_btn_select_group1(self, group):
        return self.find_eles_replace(self._btn_select_group1[0], self._btn_select_group1[1], group)
    def get_btn_select_group2(self, group):
        ele = self.get_btn_select_group1(group)
        return ele[-1].find_element(By.XPATH, self._btn_select_group2)
    # 获取封面图上传按钮
    def get_btn_upload_pic(self):
        return self.find_Element(self._btn_upload_pic)
    # 获取摘要输入框
    def get_input_summary(self):
        return self.find_Element(self._input_summary)
    # 获取正文输入框
    def get_input_main(self):
        return self.find_Element(self._input_main)
    # 获取完成按钮
    def get_btn_complete(self):
        return self.find_Element(self._btn_complete)
    # 获取外链输入框
    def get_input_external_link(self):
        return self.find_Element(self._input_external_link)

    """元素操作层"""
    # 基础页面
    # 点击跳转按钮
    def click_btn_web(self):
        return self.click_element(self.get_btn_web())
    # 点击添加网页按钮
    def click_btn_add_web(self):
        return self.click_element(self.get_btn_add_web())
    # 点击新增分组按钮
    def click_btn_add_group(self):
        return self.click_element(self.get_btn_add_group())
    # 输入素材搜索框
    def sendkey_input_material(self, value):
        return self.send_keys(self.get_input_material(), value)
    # 获取文本分组名字列表
    def gettext_list_group_name(self):
        return self.get_elements_values(self.get_list_group_name())
    # 点击特定分组
    def click_specify_group(self, group):
        return self.move_click_element(self.get_specify_group(group))
    # # 点击特定网页元素
    # def click_text_title_web(self, value):
    #     return self.move_click_element(self.get_text_title_web(value))
    # 点击编辑按钮
    def click_btn_edit(self, index):
        return self.click_element(self.get_btn_edit()[index])
    # 点击删除按钮
    def click_btn_delete(self, index):
        return self.click_element(self.get_btn_delete()[index])
    # 获取文本网页标题
    def gettext_web_title(self, index):
        return self.get_element_value(self.get_text_title_web()[index])
    # 获取文本网页摘要
    def gettext_web_sum(self, index):
        return self.get_element_value(self.get_text_sum_web()[index])
    # 点击确定按钮
    def click_btn_sure(self):
        return self.click_element(self.get_btn_sure())
    # 点击特定分组的编辑按钮
    def click_btn_specify_group_edit(self, group):
        return self.move_click_element(self.get_btn_specify_group_edit(group))

    # 分组编辑弹窗
    # 点击添加子分组按钮
    def click_btn_add_child_group(self):
        return self.move_click_element(self.get_btn_add_child_group())
    # 点击修改名称按钮
    def click_btn_change_group_name(self):
        return self.move_click_element(self.get_btn_change_group_name())
    # 点击删除分组按钮
    def click_btn_delete_group(self):
        return self.move_click_element(self.get_btn_delete_group())
    # 删除分组确定按钮
    def click_btn_delete_group_confirm(self):
        return self.click_element(self.get_btn_delete_group_confirm())

    # 输入文本子分类输入框
    def sendkey_input_child_group(self, value):
        return self.send_keys(self.get_input_child_group(), value)
    # 点击子分类确定按钮
    def click_btn_confirm_child_group(self):
        return self.click_element(self.get_btn_confirm_child_group())

    # 添加分组页面
    # 输入分组名输入框
    def sendkey_input_add_group_first(self, value):
        return self.send_keys(self.get_input_add_group_first(), value)
    # 点击确定按钮
    def click_btn_confirm(self):
        return self.click_element(self.get_btn_confirm())

    # 添加网页页面
    # 点击自定义网页类型选择
    def click_btn_select_customize_web(self):
        return self.click_element(self.get_btn_select_customize_web())
    # 点击外链网页类型选择
    def click_btn_select_external_link_web(self):
        return self.click_element(self.get_btn_select_external_link_web())
    # 输入文本网页标题输入框
    def sendkey_input_web_title(self, value):
        return self.send_keys(self.get_input_web_title(), value)
    # 点击网页分类下拉框
    def click_select_web_classify(self):
        return self.click_element(self.get_select_web_classify())
    # # 获取下拉框文本
    # def gettext_select_group(self):
    #     return self.get_elements_values(self.get_btn_select_group1())
    # 点击下拉框分组选择
    def click_btn_select_group(self, group):
        return self.click_element(self.get_btn_select_group2(group))
    # 点击封面图上传按钮
    def click_btn_upload_pic(self):
        return self.click_element(self.get_btn_upload_pic())
    # 输入文本摘要输入框
    def sendkey_input_summary(self, value):
        return self.send_keys(self.get_input_summary(), value)
    # 输入文本正文输入框
    def sendkey_input_main(self, value):
        return self.send_keys(self.get_input_main(), value)
    # 点击完成按钮
    def click_btn_complete(self):
        return self.click_element(self.get_btn_complete())
    # 输入文本外链输入框
    def sendkey_input_external_link(self, value):
        return self.send_keys(self.get_input_external_link(), value)


    """业务层"""
    def switch_to_current(self):
        sleep(2)
        self.click_btn_web()
        sleep(3)

    # 将网页信息列表录入列表
    def get_list_web(self):
        n = 0
        count = self.get_web_module_dic()
        lists = [[] for i in range(count)]
        while n < count:
            lists[n].append(self.gettext_web_title(n))
            lists[n].append(self.gettext_web_sum(n))
            n += 1
        return lists

    def add_group(self, group):
        self.click_btn_add_group()
        sleep(2)
        self.sendkey_input_add_group_first(group)
        sleep(2)
        self.click_btn_confirm()
        sleep(3)
        lists = self.gettext_list_group_name()
        self.check_exist_in_lists(group, lists)
        # os.path.abspath(os.path.dirname(__file__) + self._pic)

    def add_customize_web(self, title, summary, main, group, pic_path):
        path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)) + pic_path)
        k = PyKeyboard()
        self.click_btn_add_web()
        sleep(2)
        self.click_btn_select_customize_web()
        sleep(1)
        self.sendkey_input_web_title(title)
        sleep(1)
        self.click_select_web_classify()
        sleep(2)
        self.click_btn_select_group(group)
        sleep(1)
        self.click_select_web_classify()
        sleep(1)
        self.click_btn_upload_pic()
        sleep(2)
        k.tap_key(k.shift_key)
        k.type_string(path)
        sleep(1)
        k.tap_key(k.enter_key)
        sleep(5)
        self.sendkey_input_summary(summary)
        sleep(1)
        self.sendkey_input_main(main)
        sleep(1)
        self.click_btn_complete()
        sleep(2)
        self.click_specify_group(group)
        sleep(2)
        self.check_exist_in_page(title)
        self.check_exist_in_page(summary)

    def add_external_link_web(self, title, summary, link, group, pic_path):
        path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)) + pic_path)
        k = PyKeyboard()
        self.click_btn_add_web()
        sleep(2)
        self.click_btn_select_external_link_web()
        sleep(1)
        self.sendkey_input_web_title(title)
        sleep(1)
        self.click_select_web_classify()
        sleep(2)
        self.click_btn_select_group(group)
        sleep(1)
        self.click_select_web_classify()
        sleep(1)
        self.click_btn_upload_pic()
        sleep(2)
        k.tap_key(k.shift_key)
        k.type_string(path)
        sleep(1)
        k.tap_key(k.enter_key)
        sleep(5)
        self.sendkey_input_summary(summary)
        sleep(2)
        self.sendkey_input_external_link(link)
        sleep(1)
        self.click_btn_complete()
        sleep(2)
        self.click_specify_group(group)
        sleep(2)
        self.check_exist_in_page(title)
        self.check_exist_in_page(summary)

    def edit_web(self, title1, summaryc, group):
        self.click_specify_group(group)
        sleep(2)
        list = self.get_list_web()
        index = 0
        for n in list:
            if title1 == n[0]:
                self.click_btn_edit(index)
                break
            index += 1
        sleep(2)
        self.sendkey_input_summary(summaryc)
        sleep(1)
        self.click_btn_complete()
        sleep(2)
        self.assert_Equal(self.gettext_web_sum(index), summaryc)

    def delete_web(self, title1, group):
        self.click_specify_group(group)
        sleep(2)
        list = self.get_list_web()
        index = 0
        for n in list:
            if title1 == n[0]:
                self.click_btn_delete(index)
                break
            index += 1
            sleep(2)
        self.click_btn_sure()
        sleep(2)
        self.check_not_exist_in_page(title1)

    def search_web(self, title):
        self.sendkey_input_material(title)
        k = PyKeyboard()
        sleep(2)
        k.tap_key(k.enter_key)
        sleep(2)
        list = self.get_list_web()
        index = 0
        for n in list:
            self.check_exist_in_lists(title, n[0])
            index += 1
        sleep(2)

    def add_child_group(self, pgroup, cgroup):
        self.click_specify_group(pgroup)
        sleep(1)
        self.click_btn_specify_group_edit(pgroup)
        sleep(3)
        self.click_btn_add_child_group()
        sleep(1)
        self.sendkey_input_child_group(cgroup)
        sleep(2)
        self.click_btn_confirm_child_group()
        sleep(2)
        self.check_exist_in_page(cgroup)
        sleep(3)

    def delete_group(self, pgroup, cgroup):
        self.click_specify_group(cgroup)
        sleep(1.5)
        self.click_btn_specify_group_edit(cgroup)
        sleep(3)
        self.click_btn_change_group_name()
        sleep(2)
        self.click_btn_delete_group_confirm()
        sleep(2)
        self.click_specify_group(pgroup)
        sleep(1.5)
        self.click_btn_specify_group_edit(pgroup)
        sleep(3)
        self.click_btn_delete_group()
        sleep(2)
        self.click_btn_delete_group_confirm()
        sleep(2)
        self.check_not_exist_in_page(cgroup)
        self.check_not_exist_in_page(pgroup)




