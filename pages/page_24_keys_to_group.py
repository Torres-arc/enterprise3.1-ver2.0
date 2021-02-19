# -*- coding: utf-8 -*-
# @Time    : 2020/12/15 16:59
# @Author  : Torres
# @File    : page_24_keys_to_group.py
from time import sleep

from selenium.webdriver.common.by import By
from commons.base_page import BasePage


class KeysToGroup(BasePage):
    """元素定位信息"""
    # 关键词拉群页面
    _btn_keys_to_group_page = (By.XPATH, '//li[text()="关键词拉群"]')
    # 活动名称列表
    _texts_act_names = (By.CSS_SELECTOR, 'tbody tr td:nth-child(2) div')
    # 关键词列表
    _texts_key_words = 'tbody tr:nth-child(%s) td:nth-child(3) div[aria-describedby] span[class*="info"]'
    # 群聊列表
    _texts_group_name = 'tbody tr td:nth-child(4) div[class*="overflow"] span'
    # 下载
    _btn_download = (By.XPATH, '//span[text()="下载"]/..')
    # 编辑
    _btn_edit = (By.XPATH, '//span[text()="编辑"]/..')
    # 删除
    _btn_delete = (By.XPATH, '//span[text()="删除"]/..')
    # 删除确认按钮
    _btn_confirm_delete = (By.CSS_SELECTOR, 'div[aria-hidden="false"] button+button')
    # 新建关键词拉群
    _btn_create = (By.XPATH, '//span[text()="新建关键词拉群"]/..')
    # 活动名称搜索框
    _input_search_act_name = (By.CSS_SELECTOR, 'input[placeholder="请输入活动名称"]')
    # 页码数
    _text_page_num = (By.CSS_SELECTOR, '.el-pager li:last-child')
    # 翻页按钮
    _btn_next_page = (By.CSS_SELECTOR, '.btn-next')

    # 新建页面
    # 活动名称输入框
    _input_act_name = (By.CSS_SELECTOR, 'input.el-input__inner')
    # 添加关键词按钮
    _btn_add_keys = (By.XPATH, '//span[text()="添加关键词"]/..')
    # 关键词输入框
    _input_key_words = (By.CSS_SELECTOR, 'input[placeholder="请输入关键词"]')
    # 关键词输入确认按钮
    _btn_confirm_keys = (By.CSS_SELECTOR, 'div[aria-label="关键词"] div[class*="foot"] button+button')
    # 关键词移除按钮
    _btn_remove_keys = (By.CSS_SELECTOR, 'span i[class*="el-icon-close"]')
    # 入群引导语输入框
    _input_guide = (By.CSS_SELECTOR, 'textarea')
    # 选择群活码按钮
    _btn_add_group_code = (By.CSS_SELECTOR, '.group-code-box i')
    # 群活码搜索框
    _input_search_group_code = (By.CSS_SELECTOR, 'div[aria-label="选择群活码"] input[placeholder="请输入关键词"]')
    # 群活码搜索按钮
    _btn_search_code = (By.XPATH, '//span[text()="查询"]/..')
    # 群活码选择按钮
    _btn_select_code = (By.CSS_SELECTOR, 'div[aria-label="选择群活码"] input.el-radio__original')
    # 群活码确定按钮
    _btn_confirm_code = (By.CSS_SELECTOR, 'div[aria-label="选择群活码"] .el-dialog__footer button:last-child')
    # 新建确定按钮
    _btn_confirm = (By.XPATH, '//span[text()="确定"]/..')

    """元素定位层"""
    # 关键词拉群页面
    def get_btn_keys_to_group_page(self):
        return self.find_Element(self._btn_keys_to_group_page)
    # 活动名称列表
    def get_texts_act_names(self):
        return self.find_Elements(self._texts_act_names)
    # 关键词列表
    def get_texts_key_words(self, index):
        return self.find_eles_replace('css', self._texts_key_words, str(index))
    # 群聊列表
    def get_texts_group_name(self, index):
        return self.find_ele_replace('css', self._texts_group_name, str(index))
    # 下载
    def get_btn_download(self):
        return self.find_Element(self._btn_download)
    # 编辑
    def get_btn_edit(self):
        return self.find_Element(self._btn_edit)
    # 删除
    def get_btn_delete(self):
        return self.find_Element(self._btn_delete)
    # 删除确认按钮
    def get_btn_confirm_delete(self):
        return self.find_Element(self._btn_confirm_delete)
    # 新建关键词拉群
    def get_btn_create(self):
        return self.find_Element(self._btn_create)
    # 活动名称搜索框
    def get_input_search_act_name(self):
        return self.find_Element(self._input_search_act_name)
    # 页码数
    def get_text_page_num(self):
        return self.find_Element(self._text_page_num)
    # 翻页按钮
    def get_btn_next_page(self):
        return self.find_Element(self._btn_next_page)

    # 新建页面
    # 活动名称输入框
    def get_input_act_name(self):
        return self.find_Element(self._input_act_name)
    # 添加关键词按钮
    def get_btn_add_keys(self):
        return self.find_Element(self._btn_add_keys)
    # 关键词输入框
    def get_input_key_words(self):
        return self.find_Element(self._input_key_words)
    # 关键词输入确认按钮
    def get_btn_confirm_keys(self):
        return self.find_Element(self._btn_confirm_keys)
    # 关键词移除按钮
    def get_btn_remove_keys(self):
        return self.find_Element(self._btn_remove_keys)
    # 入群引导语输入框
    def get_input_guide(self):
        return self.find_Element(self._input_guide)
    # 选择群活码按钮
    def get_btn_add_group_code(self):
        return self.find_Element(self._btn_add_group_code)
    # 群活码搜索框
    def get_input_search_group_code(self):
        return self.find_Element(self._input_search_group_code)
    # 群活码搜索按钮
    def get_btn_search_code(self):
        return self.find_Element(self._btn_search_code)
    # 群活码选择按钮
    def get_btn_select_code(self):
        return self.find_Element(self._btn_select_code)
    # 群活码确定按钮
    def get_btn_confirm_code(self):
        return self.find_Element(self._btn_confirm_code)
    # 新建确定按钮
    def get_btn_confirm(self):
        return self.find_Element(self._btn_confirm)

    """元素操作层"""
    # 关键词拉群页面
    def click_btn_keys_to_group_page(self):
        return self.click_element(self.get_btn_keys_to_group_page())
    # 活动名称列表
    def gettexts_texts_act_names(self):
        return self.get_elements_values(self.get_texts_act_names())
    # 关键词列表
    def gettexts_texts_key_words(self, index):
        return self.get_elements_values(self.get_texts_key_words(index))
    # 群聊列表
    def gettexts_texts_group_name(self, index):
        return self.get_element_value(self.get_texts_group_name(index))
    # 下载
    def click_btn_download(self):
        return self.click_element(self.get_btn_download())
    # 编辑
    def click_btn_edit(self):
        return self.click_element(self.get_btn_edit())
    # 删除
    def click_btn_delete(self):
        return self.click_element(self.get_btn_delete())
    # 删除确认按钮
    def click_btn_confirm_delete(self):
        return self.click_element(self.get_btn_confirm_delete())
    # 新建关键词拉群
    def click_btn_create(self):
        return self.click_element(self.get_btn_create())
    # 活动名称搜索框
    def sendkeys_input_search_act_name(self, value):
        return self.send_keys(self.get_input_search_act_name(), value)
    # 页码数
    def gettexts_text_page_num(self):
        return self.get_element_value(self.get_text_page_num())
    # 翻页按钮
    def click_btn_next_page(self):
        return self.click_element(self.get_btn_next_page())

    # 新建页面
    # 活动名称输入框
    def sendkeys_input_act_name(self, value):
        return self.send_keys(self.get_input_act_name(), value)
    # 添加关键词按钮
    def click_btn_add_keys(self):
        return self.click_element(self.get_btn_add_keys())
    # 关键词输入框
    def sendkeys_input_key_words(self, value):
        return self.send_keys(self.get_input_key_words(), value)
    # 关键词输入确认按钮
    def click_btn_confirm_keys(self):
        return self.click_element(self.get_btn_confirm_keys())
    # 关键词移除按钮
    def click_btn_remove_keys(self):
        return self.click_element(self.get_btn_remove_keys())
    # 入群引导语输入框
    def sendkeys_input_guide(self, value):
        return self.send_keys(self.get_input_guide(), value)
    # 选择群活码按钮
    def click_btn_add_group_code(self):
        return self.click_element(self.get_btn_add_group_code())
    # 群活码搜索框
    def sendkeys_input_search_group_code(self, value):
        return self.send_keys(self.get_input_search_group_code(), value)
    # 群活码搜索按钮
    def click_btn_search_code(self):
        return self.click_element(self.get_btn_search_code())
    # 群活码选择按钮
    def click_btn_select_code(self):
        return self.move_click_element(self.get_btn_select_code())
    # 群活码确定按钮
    def click_btn_confirm_code(self):
        return self.click_element(self.get_btn_confirm_code())
    # 新建确定按钮
    def click_btn_confirm(self):
        return self.click_element(self.get_btn_confirm())

    """业务层"""
    def switch_to_current(self):
        self.click_btn_keys_to_group_page()
        sleep(2)

    def search_by_name(self, name):
        self.sendkeys_input_search_act_name(name)
        sleep(1)
        self.tap_keyboard('enter')
        self.tap_keyboard('enter')
        sleep(5)
        pages = int(self.gettexts_text_page_num())  # 页码
        count = 1
        while pages > 0 and count <= 3:
            try:
                namelist = self.gettexts_texts_act_names()  # 搜索目标
            except TimeoutError:
                try:
                    self.check_exist_in_page('暂无数据')  # 无数据时的页面信息
                except Exception as e:
                    raise e
                else:
                    ele = self.find_Element(By.XPATH, '//span[text()="暂无数据"]')  # 无数据时的页面信息
                    rect = self.locate_element(ele)
                    self.GetScreen('按时间搜索，无数据', rect=rect)
                    print('搜索条件下无数据')
            except Exception as e:
                raise e
            else:  # 存在数据，进行验证
                count = 1  # 计数列表第几个
                for i in namelist:
                    try:
                        keylist = self.gettexts_texts_key_words(count)
                        keylist.append(i)
                        self.check_exist_in_lists(name, ",".join(keylist))
                    except AssertionError as e:
                        ele = self.find_Element(By.XPATH, '//div[text()="{}"]'.format(i))
                        rect = self.locate_element(ele)
                        self.GetScreen('按日期搜索，错误', rect=rect)
                        print('搜索条件与数据不匹配')
                        raise e
            self.click_btn_next_page()  # 翻页
            sleep(2)
            pages -= 1
            count += 1

    def create_activity(self, name, keys, guide, code, gname):
        self.click_btn_create()
        sleep(2)
        self.sendkeys_input_act_name(name)
        sleep(2)
        for i in keys:
            self.click_btn_add_keys()
            sleep(2)
            self.sendkeys_input_key_words(i)
            sleep(2)
            self.click_btn_confirm_keys()
            sleep(2)
        sleep(2)
        self.sendkeys_input_guide(guide)
        sleep(2)
        self.click_btn_add_group_code()
        sleep(2)
        self.sendkeys_input_search_group_code(code)
        sleep(2)
        self.click_btn_search_code()
        sleep(2)
        self.click_btn_select_code()
        sleep(2)
        self.click_btn_confirm_code()
        sleep(2)
        self.click_btn_confirm()
        sleep(5)
        self.assert_Equal(name, (self.gettexts_texts_act_names())[0])
        keylist = self.gettexts_texts_key_words(1)
        keylist.sort()
        keys.sort()
        self.assert_Equal(keylist, keys)
        group = self.gettexts_texts_group_name(1)
        if len(group) == 1:
            group = group[0]
        self.assert_Equal(group[:-5], gname)

    def edit_act(self, ename, ekeys, eguide):
        self.click_btn_edit()
        sleep(2)
        self.sendkeys_input_act_name(ename)
        sleep(2)
        count = 1
        while True:
            if count >= 6:
                break
            self.click_btn_remove_keys()
            sleep(1)
            count += 1
        sleep(2)
        for i in ekeys:
            self.click_btn_add_keys()
            sleep(2)
            self.sendkeys_input_key_words(i)
            sleep(2)
            self.click_btn_confirm_keys()
            sleep(2)
        self.sendkeys_input_guide(eguide)
        sleep(2)
        self.click_btn_confirm()
        sleep(5)
        self.assert_Equal(ename, (self.gettexts_texts_act_names())[0])
        keylist = self.gettexts_texts_key_words(1)
        keylist.sort()
        ekeys.sort()
        self.assert_Equal(keylist, ekeys)

    def delete_act(self, name):
        nlist = self.gettexts_texts_act_names()
        self.assert_Equal(nlist[0], name)
        sleep(1)
        self.click_btn_delete()
        sleep(2)
        self.click_btn_confirm_delete()
        sleep(2)
        self.check_exist_in_page('删除成功')
        sleep(3)
        self.check_not_exist_in_page(name)
