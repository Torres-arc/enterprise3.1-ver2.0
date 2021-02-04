from selenium.webdriver.common.by import By
from commons.base_page import BasePage
from time import sleep
from pykeyboard import PyKeyboard
from commons.log import log
import os


class MaterialAudioPage(BasePage):
    """元素定位信息"""
    # 基础页面
    # 跳转页面
    _btn_audio = (By.XPATH, '//li[text()="语音"]')
    # 添加语音按钮
    _btn_add_audio = (By.XPATH, '//span[text()="添加语音"]/..')
    # 编辑按钮
    _btn_edit = ('css', 'a[download="%s"]+button')
    # 删除按钮
    _btn_delete = ('css', 'a[download="%s.amr"]+button+button')
    # 新增分组按钮
    _btn_add_group = (By.CSS_SELECTOR, 'div.left-menu-box i.el-icon-plus')
    # 分组名输入框
    _input_group = (By.CSS_SELECTOR, '.el-dialog__body input')
    # 确定按钮
    _btn_confirm = (By.XPATH, '//div[@class="dialog-footer"]/button[2]')
    # 编辑素材输入框
    _input_edit_audio = (By.CSS_SELECTOR, 'input[placeholder="请输入素材名称"]')
    # 分组名字列表
    _list_group_name = (By.XPATH, '//span[@class="department-name"]')
    # 特定分组
    _specify_group = ('xpath', '//span[text()="%s"]')
    # 特定分组编辑按钮
    _btn_specify_group_edit = ('xpath', '//span[text()="%s"]/../../div')

    # 分组编辑弹窗
    # 添加子分组按钮
    _btn_add_child_group = (By.CSS_SELECTOR, 'ul[x-placement] :nth-child(2)')
    # 修改名称按钮
    _btn_change_group_name = (By.CSS_SELECTOR, 'ul[x-placement] :nth-child(3)')
    # 删除分组按钮
    _btn_delete_group = (By.CSS_SELECTOR, 'ul[x-placement] :nth-child(4)')
    # 删除分组确定按钮
    _btn_delete_group_confirm = (By.CSS_SELECTOR, 'div[aria-label="删除分类"] div[class$="btns"] button:last-child')

    # 添加语音页面
    # 语音分类下拉框
    _btn_audio_classify = (By.CSS_SELECTOR, 'div.el-form-item__content input[placeholder]')
    # 语音分类选择
    _btn_select_group1 = ('xpath', '//span[text()="%s"]')
    _btn_select_group2 = '../label'
    # 上传语音按钮
    _btn_upload = (By.XPATH, '//div[text()=" 上传语音"]')
    # 添加完成按钮
    _btn_complete = (By.XPATH, '//span[text()="完 成"]/..')
    # 确认提交按钮
    _btn_confirm_commit = (By.CSS_SELECTOR, 'div.el-message-box__btns :nth-child(2)')


    """元素定位层"""
    # 基础页面
    # 跳转页面
    def get_btn_audio(self):
        return self.find_Element(self._btn_audio)
    # 添加语音按钮
    def get_btn_add_audio(self):
        return self.find_Element(self._btn_add_audio)
    # 编辑按钮
    def get_btn_edit(self, index):
        return self.find_ele_replace(self._btn_edit[0], self._btn_edit[1], index)
    # 删除按钮
    def get_btn_delete(self, index):
        return self.find_ele_replace(self._btn_delete[0], self._btn_delete[1], index)
    # 新增分组按钮
    def get_btn_add_group(self):
        return self.find_Element(self._btn_add_group)
    # 分组名输入框
    def get_input_group(self):
        return self.find_Element(self._input_group)
    # 确定按钮
    def get_btn_confirm(self):
        return self.find_Element(self._btn_confirm)
    # 获取分组名字列表
    def get_list_group_name(self):
        return self.find_Elements(self._list_group_name)
    # 编辑素材输入框
    def get_input_edit_audio(self):
        return self.find_Element(self._input_edit_audio)
    # 获取特定分组
    def get_specify_group(self, group):
        return self.find_ele_replace(self._specify_group[0], self._specify_group[1], group)
    # 获取特定分组的编辑按钮
    def get_btn_specify_group_edit(self, group):
        return self.find_ele_replace(self._btn_specify_group_edit[0], self._btn_specify_group_edit[1], group)

    # 分组编辑弹窗
    # 添加子分组按钮
    def get_btn_add_child_group(self):
        return self.find_Element(self._btn_add_child_group)
    # 修改名称按钮
    def get_btn_change_group_name(self):
        return self.find_Element(self._btn_change_group_name)
    # 删除分组按钮
    def get_btn_delete_group(self):
        return self.find_Element(self._btn_delete_group)
    # 删除分组确定按钮
    def get_btn_delete_group_confirm(self):
        return self.find_Element(self._btn_delete_group_confirm)

    # 添加语音页面
    # 语音分类下拉框
    def get_btn_audio_classify(self):
        return self.find_Element(self._btn_audio_classify)
    # 语音分类选择
    def get_btn_select_group1(self, group):
        return self.find_eles_replace(self._btn_select_group1[0], self._btn_select_group1[1], group)
    def get_btn_select_group2(self, group):
        ele = self.get_btn_select_group1(group)
        return ele[-1].find_element(By.XPATH, self._btn_select_group2)
    # def get_btn_select_class1(self, group):
    #     return self.find_ele_replace(self._btn_select_class[0], self._btn_select_class[1], group)
    # 上传语音按钮
    def get_btn_upload(self):
        return self.find_Element(self._btn_upload)
    # 添加完成按钮
    def get_btn_complete(self):
        return self.find_Element(self._btn_complete)
    # 确认提交按钮
    def get_btn_confirm_commit(self):
        return self.find_Element(self._btn_confirm_commit)

    """元素操作层"""
    # 基础页面
    # 跳转页面
    def click_btn_audio(self):
        return self.click_element(self.get_btn_audio())
    # 添加语音按钮
    def click_btn_add_audio(self):
        return self.click_element(self.get_btn_add_audio())
    # 编辑按钮
    def click_btn_edit(self, index):
        return self.click_element(self.get_btn_edit(index))
    # 删除按钮
    def click_btn_delete(self, index):
        return self.click_element(self.get_btn_delete(index))
    # 新增分组按钮
    def click_btn_add_group(self):
        return self.click_element(self.get_btn_add_group())
    # 分组名输入框
    def sendkeys_input_group(self, value):
        return self.send_keys(self.get_input_group(), value)
    # 确定按钮
    def click_btn_confirm(self):
        return self.click_element(self.get_btn_confirm())
    # 获取文本分组名字列表
    def gettext_list_group_name(self):
        return self.get_elements_values(self.get_list_group_name())
    # 编辑素材输入框
    def sendkey_input_edit_audio(self, value):
        return self.send_keys(self.get_input_edit_audio(), value)
    # 点击特定分组
    def click_specify_group(self, group):
        return self.move_click_element(self.get_specify_group(group))
        # 点击特定分组的编辑按钮
    def click_btn_specify_group_edit(self, group):
        return self.move_click_element(self.get_btn_specify_group_edit(group))

    # 分组编辑弹窗
    # 添加子分组按钮
    def click_btn_add_child_group(self):
        return self.click_element(self.get_btn_add_child_group())
    # 修改名称按钮
    def click_btn_change_group_name(self):
        return self.click_element(self.get_btn_change_group_name())
    # 删除分组按钮
    def click_btn_delete_group(self):
        return self.click_element(self.get_btn_delete_group())
    # 删除分组确定按钮
    def click_btn_delete_group_confirm(self):
        return self.click_element(self.get_btn_delete_group_confirm())

    # 添加语音页面
    # 语音分类下拉框
    def click_btn_audio_classify(self):
        return self.move_click_element(self.get_btn_audio_classify())
    # 语音分类选择
    def click_btn_select_class(self, group):
        return self.move_click_element(self.get_btn_select_group2(group))
    # 上传语音按钮
    def click_btn_upload(self):
        return self.move_click_element(self.get_btn_upload())
    # 添加完成按钮
    def click_btn_complete(self):
        return self.click_element(self.get_btn_complete())
    # 确认提交按钮
    def click_btn_confirm_commit(self):
        return self.click_element(self.get_btn_confirm_commit())

    """业务层"""
    def switch_to_current(self):
        sleep(2)
        self.click_btn_audio()
        sleep(3)

    def add_audio(self, path, group, name1):
        path1 = os.path.abspath(os.path.dirname(os.path.dirname(__file__)) + path)
        k = PyKeyboard()
        self.click_btn_add_audio()
        sleep(2)
        self.click_btn_audio_classify()
        sleep(1)
        self.click_btn_select_class(group)
        sleep(1)
        self.click_btn_audio_classify()
        sleep(1)
        self.click_btn_upload()
        sleep(2)
        k.tap_key(k.shift_key)
        k.type_string(path1)
        sleep(1)
        k.tap_key(k.enter_key)
        sleep(4)
        self.click_btn_complete()
        sleep(2)
        self.click_btn_confirm_commit()
        sleep(1.5)
        self.check_exist_in_page('添加成功')
        self.check_exist_in_page(name1)

    def edit_audio(self, name1, name2):
        self.click_btn_edit(name1)
        sleep(2)
        self.sendkey_input_edit_audio(name2)
        sleep(1)
        self.click_btn_confirm_commit()
        sleep(1.5)
        self.check_exist_in_page(name2)
        self.check_exist_in_page("修改成功")

    def delete_audio(self, name2):
        self.click_btn_delete(name2)
        sleep(2)
        self.click_btn_confirm_commit()
        sleep(2)
        self.check_not_exist_in_page((name2+'.amr'))
        self.check_exist_in_page('删除成功')

    def add_group(self, group_name):
        self.click_btn_add_group()
        sleep(2)
        self.sendkeys_input_group(group_name)
        sleep(1)
        self.click_btn_confirm()
        sleep(2)
        lists = self.gettext_list_group_name()
        self.check_exist_in_lists(group_name, lists)

    def delete_group(self, group):
        self.click_specify_group(group)
        sleep(1.5)
        self.click_btn_specify_group_edit(group)
        sleep(3)
        self.click_btn_delete_group()
        sleep(2)
        self.click_btn_delete_group_confirm()
        sleep(2)
        self.check_not_exist_in_page(group)
