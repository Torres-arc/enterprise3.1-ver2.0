# -*- coding: utf-8 -*-
# @Time    : 2020/12/16 16:10
# @Author  : Torres
# @File    : page_25_group_sop.py
from time import sleep

from selenium.webdriver.common.by import By
from commons.base_page import BasePage


class GroupSOP(BasePage):
    """元素定位信息"""
    # 群SOP页面
    _btn_group_sop_page = (By.XPATH, '//li[text()="群SOP"]')
    # 规则名称列表
    _texts_rule_names = (By.CSS_SELECTOR, 'tbody tr td:nth-child(1) div')
    # 创建人列表
    _texts_key_words = 'tbody tr td:nth-child(2) ww-open-data"]'
    # 详情
    _btn_detail = (By.XPATH, '//span[text()="详情"]/..')
    # 编辑
    _btn_edit = (By.XPATH, '//span[text()="编辑"]/..')
    # 删除
    _btn_delete = (By.XPATH, '//span[text()="删除"]/..')
    # 删除确认按钮
    _btn_confirm_delete = (By.CSS_SELECTOR, 'div[aria-hidden="false"] button+button')
    # 创建规则按钮
    _btn_create = (By.XPATH, '//span[text()="创建规则"]/..')
    # 规则名称搜索框
    _input_search_act_name = (By.CSS_SELECTOR, 'input[placeholder="请输入规则名称"]')
    # 页码数
    _text_page_num = (By.CSS_SELECTOR, '.el-pager li:last-child')
    # 翻页按钮
    _btn_next_page = (By.CSS_SELECTOR, '.btn-next')

    # 新建页面
    # 规则名称输入框
    _input_act_name = (By.CSS_SELECTOR, 'input.el-input__inner')
    # 选择群聊按钮
    _btn_choose_group = (By.XPATH, '//span[text()="选择群聊"]/..')
    # 删除群聊按钮
    _btn_delete_group = (By.CSS_SELECTOR, '.choose-group-box>span>i')
    # 关键词输入框
    _input_key_words = (By.CSS_SELECTOR, 'input[placeholder="请输入关键词"]')
    # 群聊查询按钮
    _btn_search_group = (By.XPATH, '//span[text()="查询"]/..')
    # 群聊选择框
    _btn_select_group = (By.CSS_SELECTOR, '.el-checkbox__inner')
    # 群聊确定按钮
    _btn_confirm_group = (By.CSS_SELECTOR, 'div[aria-label="添加群聊"] .el-dialog__footer button+button')
    # 添加推送按钮
    _btn_add_msg = (By.XPATH, '//span[text()="添加推送"]/..')
    # 修改推送按钮
    _btn_edit_msg = (By.XPATH, '//span[text()="修改"]/..')
    # 推送内容输入框
    _input_send_name = (By.XPATH, '//label[text()="内容名称"]/following-sibling::div/div/input')
    # 添加时间选择框
    _btn_add_time = (By.CSS_SELECTOR, 'input[placeholder="起始时间"]')
    # 开始日期输入框
    _input_start_time = (By.CSS_SELECTOR, 'input[placeholder="开始日期"]')
    # 开始时间输入框
    _input_start_time_time = (By.CSS_SELECTOR, 'input[placeholder="开始时间"]')
    # 结束日期输入框
    _input_end_time = (By.CSS_SELECTOR, 'input[placeholder="结束日期"]')
    # 结束时间输入框
    _input_end_time_time = (By.CSS_SELECTOR, 'input[placeholder="结束时间"]')
    # 日期确认按钮
    _btn_confirm_date = (By.CSS_SELECTOR, '.el-picker-panel__footer button+button')
    # 消息输入框
    _input_msg = (By.CSS_SELECTOR, 'textarea[placeholder="直接开始输入..."]')
    # 素材确认按钮
    _btn_confirm_msg = (By.CSS_SELECTOR, 'div[class="el-form-item el-form-item--small"] button')
    # 新建确定按钮
    _btn_confirm = (By.XPATH, '//span[text()=" 确定 "]/..')

    # 详情页面
    # 规则名称
    _text_detail_rule_name = (By.XPATH, '//label[text()="规则名称"]/following-sibling::div/span')
    # 执行群聊
    _text_detail_group_name = (By.XPATH, '//label[text()="执行群聊"]/following-sibling::div/span')
    # 开始时间
    _text_detail_start_time = (By.XPATH, '//span[text()="至"]/preceding-sibling::span')
    # 结束时间
    _text_detail_end_time = (By.XPATH, '//span[text()="至"]/following-sibling::span')
    # 推送名称
    _text_detail_msg_name = (By.CSS_SELECTOR, '.left')
    # 推送内容
    _text_detail_msg = (By.CSS_SELECTOR, '.text')

    """元素定位层"""
    # 群SOP页面
    def get_btn_group_sop_page(self):
        return self.find_Element(self._btn_group_sop_page)
    # 规则名称列表
    def get_texts_rule_names(self):
        return self.find_Elements(self._texts_rule_names)
    # 创建人列表
    def get_texts_key_words(self):
        return self.find_Elements(self._texts_key_words)
    # 详情
    def get_btn_detail(self):
        return self.find_Element(self._btn_detail)
    # 编辑
    def get_btn_edit(self):
        return self.find_Element(self._btn_edit)
    # 删除
    def get_btn_delete(self):
        return self.find_Element(self._btn_delete)
    # 删除确认按钮
    def get_btn_confirm_delete(self):
        return self.find_Element(self._btn_confirm_delete)
    # 创建规则按钮
    def get_btn_create(self):
        return self.find_Element(self._btn_create)
    # 规则名称搜索框
    def get_input_search_act_name(self):
        return self.find_Element(self._input_search_act_name)
    # 页码数
    def get_text_page_num(self):
        return self.find_Element(self._text_page_num)
    # 翻页按钮
    def get_btn_next_page(self):
        return self.find_Element(self._btn_next_page)

    # 新建页面
    # 规则名称输入框
    def get_input_act_name(self):
        return self.find_Element(self._input_act_name)
    # 选择群聊按钮
    def get_btn_choose_group(self):
        return self.find_Element(self._btn_choose_group)
    # 删除群聊按钮
    def get_btn_delete_group(self):
        return self.find_Element(self._btn_delete_group)
    # 关键词输入框
    def get_input_key_words(self):
        return self.find_Element(self._input_key_words)
    # 群聊查询按钮
    def get_btn_search_group(self):
        return self.find_Element(self._btn_search_group)
    # 群聊选择框
    def get_btn_select_group(self):
        return self.find_Element(self._btn_select_group)
    # 群聊确定按钮
    def get_btn_confirm_group(self):
        return self.find_Element(self._btn_confirm_group)
    # 添加推送按钮
    def get_btn_add_msg(self):
        return self.find_Element(self._btn_add_msg)
    # 修改推送按钮
    def get_btn_edit_msg(self):
        return self.find_Element(self._btn_edit_msg)
    # 推送内容输入框
    def get_input_send_name(self):
        return self.find_Element(self._input_send_name)
    # 添加时间选择框
    def get_btn_add_time(self):
        return self.find_Element(self._btn_add_time)
    # 开始日期输入框
    def get_input_start_time(self):
        return self.find_Element(self._input_start_time)
    # 开始时间输入框
    def get_input_start_time_time(self):
        return self.find_Element(self._input_start_time_time)
    # 结束日期输入框
    def get_input_end_time(self):
        return self.find_Element(self._input_end_time)
    # 结束时间输入框
    def get_input_end_time_time(self):
        return self.find_Element(self._input_end_time_time)
    # 日期确认按钮
    def get_btn_confirm_date(self):
        return self.find_Element(self._btn_confirm_date)
    # 消息输入框
    def get_input_msg(self):
        return self.find_Element(self._input_msg)
    # 素材确认按钮
    def get_btn_confirm_msg(self):
        return self.find_Element(self._btn_confirm_msg)
    # 新建确定按钮
    def get_btn_confirm(self):
        return self.find_Element(self._btn_confirm)

    # 详情页面
    # 规则名称
    def get_text_detail_rule_name(self):
        return self.find_Element(self._text_detail_rule_name)
    # 执行群聊
    def get_text_detail_group_name(self):
        return self.find_Element(self._text_detail_group_name)
    # 开始时间
    def get_text_detail_start_time(self):
        return self.find_Element(self._text_detail_start_time)
    # 结束时间
    def get_text_detail_end_time(self):
        return self.find_Element(self._text_detail_end_time)
    # 推送内容名称
    def get_text_detail_msg_name(self):
        return self.find_Element(self._text_detail_msg_name)
    # 推送内容正文
    def get_text_detail_msg(self):
        return self.find_Element(self._text_detail_msg)

    """元素操作层"""
    # 群SOP页面
    def click_btn_group_sop_page(self):
        return self.click_element(self.get_btn_group_sop_page())
    # 规则名称列表
    def gettexts_texts_rule_names(self):
        return self.get_elements_values(self.get_texts_rule_names())
    # 创建人列表
    def gettexts_texts_key_words(self):
        tlist = []
        for i in self.get_texts_key_words():
            tlist.append(i.get_attribute("openid"))
        return tlist
    # 详情
    def click_btn_detail(self):
        return self.click_element(self.get_btn_detail())
    # 编辑
    def click_btn_edit(self):
        return self.click_element(self.get_btn_edit())
    # 删除
    def click_btn_delete(self):
        return self.click_element(self.get_btn_delete())
    # 删除确认按钮
    def click_btn_confirm_delete(self):
        return self.click_element(self.get_btn_confirm_delete())
    # 创建规则按钮
    def click_btn_create(self):
        return self.click_element(self.get_btn_create())
    # 规则名称搜索框
    def sendkeys_input_search_act_name(self, value):
        return self.send_keys(self.get_input_search_act_name(), value)
    # 页码数
    def gettexts_text_page_num(self):
        return self.get_element_value(self.get_text_page_num())
    # 翻页按钮
    def click_btn_next_page(self):
        return self.click_element(self.get_btn_next_page())

    # 新建页面
    # 规则名称输入框
    def sendkeys_input_act_name(self, value):
        return self.send_keys(self.get_input_act_name(), value)
    # 选择群聊按钮
    def click_btn_choose_group(self):
        return self.click_element(self.get_btn_choose_group())
    # 删除群聊按钮
    def click_btn_delete_group(self):
        return self.click_element(self.get_btn_delete_group())
    # 关键词输入框
    def sendkeys_input_key_words(self, value):
        return self.send_keys(self.get_input_key_words(), value)
    # 群聊查询按钮
    def click_btn_search_group(self):
        return self.click_element(self.get_btn_search_group())
    # 群聊选择框
    def click_btn_select_group(self):
        return self.click_element(self.get_btn_select_group())
    # 群聊确定按钮
    def click_btn_confirm_group(self):
        return self.click_element(self.get_btn_confirm_group())
    # 添加推送按钮
    def click_btn_add_msg(self):
        return self.click_element(self.get_btn_add_msg())
    # 修改推送按钮
    def click_btn_edit_msg(self):
        return self.click_element(self.get_btn_edit_msg())
    # 推送内容输入框
    def sendkeys_input_send_name(self, value):
        return self.send_keys(self.get_input_send_name(), value)
    # 添加时间选择框
    def click_btn_add_time(self):
        return self.click_element(self.get_btn_add_time())
    # 开始日期输入框
    def sendkeys_input_start_time(self, value):
        return self.send_keys(self.get_input_start_time(), value)
    # 开始时间输入框
    def sendkeys_input_start_time_time(self, value):
        return self.send_keys(self.get_input_start_time_time(), value)
    # 结束日期输入框
    def sendkeys_input_end_time(self, value):
        return self.send_keys(self.get_input_end_time(), value)
    # 结束时间输入框
    def sendkeys_input_end_time_time(self, value):
        return self.send_keys(self.get_input_end_time_time(), value)
    # 日期确认按钮
    def click_btn_confirm_date(self):
        return self.click_element(self.get_btn_confirm_date())
    # 消息输入框
    def sendkeys_input_msg(self, value):
        return self.send_keys(self.get_input_msg(), value)
    # 素材确认按钮
    def click_btn_confirm_msg(self):
        return self.click_element(self.get_btn_confirm_msg())
    # 新建确定按钮
    def click_btn_confirm(self):
        return self.click_element(self.get_btn_confirm())

    # 详情页面
    # 规则名称
    def gettexts_text_detail_rule_name(self):
        return self.get_element_value(self.get_text_detail_rule_name())
    # 执行群聊
    def gettexts_text_detail_group_name(self):
        return self.get_element_value(self.get_text_detail_group_name())
    # 开始时间
    def gettexts_text_detail_start_time(self):
        return self.get_element_value(self.get_text_detail_start_time())
    # 结束时间
    def gettexts_text_detail_end_time(self):
        return self.get_element_value(self.get_text_detail_end_time())
    # 推送内容名称
    def gettexts_text_detail_msg_name(self):
        return self.get_element_value(self.get_text_detail_msg_name())
    # 推送内容正文
    def gettexts_text_detail_msg(self):
        return self.get_element_value(self.get_text_detail_msg())

    """业务层"""
    def switch_to_current(self):
        self.click_btn_group_sop_page()
        sleep(3)

    def search_by_name(self, name):
        self.sendkeys_input_search_act_name(name)
        sleep(2)
        self.tap_keyboard('enter')
        sleep(3)
        pages = int(self.gettexts_text_page_num())  # 页码
        count = 1
        while pages > 0 and count <= 3:
            try:
                namelist = self.gettexts_texts_rule_names()  # 搜索目标
            except TimeoutError:
                try:
                    self.check_exist_in_page('暂无数据')  # 无数据时的页面信息
                except Exception as e:
                    raise e
                else:
                    print('搜索条件下无数据')
            except Exception as e:
                raise e
            else:  # 存在数据，进行验证
                for i in namelist:
                    try:
                        self.check_exist_in_lists(name, i)
                    except AssertionError as e:
                        print('搜索条件与数据不匹配')
                        raise e
            self.click_btn_next_page()  # 翻页
            sleep(2)
            pages -= 1
            count += 1

    def create_rule(self, name, group, msg_name, stime, etime, msg):
        self.click_btn_create()
        sleep(2)
        self.sendkeys_input_act_name(name)
        sleep(2)
        self.click_btn_choose_group()
        sleep(2)
        self.sendkeys_input_key_words(group)
        sleep(1)
        self.click_btn_search_group()
        sleep(2)
        self.click_btn_select_group()
        sleep(2)
        self.click_btn_confirm_group()
        sleep(2)
        self.click_btn_add_msg()
        sleep(2)
        self.sendkeys_input_send_name(msg_name)
        sleep(2)
        self.click_btn_add_time()
        self.sendkeys_input_start_time(stime)
        sleep(1)
        self.sendkeys_input_start_time_time('00:00:00')
        sleep(1)
        self.sendkeys_input_end_time(etime)
        sleep(2)
        self.sendkeys_input_end_time_time('00:00:00')
        sleep(2)
        self.click_btn_confirm_date()
        sleep(2)
        self.sendkeys_input_msg(msg)
        sleep(2)
        self.click_btn_confirm_msg()
        sleep(2)
        self.click_btn_confirm()
        sleep(5)
        namelist = self.gettexts_texts_rule_names()
        self.assert_Equal(name, namelist[0])

    def check_details(self, name, group, msg_name, stime, etime, msg):
        self.click_btn_detail()
        sleep(2)
        self.assert_Equal(name, self.gettexts_text_detail_rule_name())
        self.assert_Equal(group, self.gettexts_text_detail_group_name())
        self.assert_Equal(msg_name, self.gettexts_text_detail_msg_name())
        self.assert_Equal(msg, self.gettexts_text_detail_msg())
        self.assert_Equal(stime, ((self.gettexts_text_detail_start_time()).split(' '))[0])
        self.assert_Equal(etime, ((self.gettexts_text_detail_end_time()).split(' '))[0])
        sleep(2)

    def edit_rule(self, name, group, msg_name, stime, etime, msg):
        self.click_btn_edit()
        sleep(2)
        self.sendkeys_input_act_name(name)
        sleep(2)
        self.click_btn_delete_group()
        sleep(2)
        self.click_btn_choose_group()
        sleep(2)
        self.sendkeys_input_key_words(group)
        sleep(1)
        self.click_btn_search_group()
        sleep(2)
        self.click_btn_select_group()
        sleep(2)
        self.click_btn_confirm_group()
        sleep(2)
        self.click_btn_edit_msg()
        sleep(2)
        self.sendkeys_input_send_name(msg_name)
        sleep(2)
        self.click_btn_add_time()
        self.sendkeys_input_start_time(stime)
        sleep(1)
        self.sendkeys_input_start_time_time('00:00:00')
        sleep(1)
        self.sendkeys_input_end_time(etime)
        sleep(2)
        self.sendkeys_input_end_time_time('00:00:00')
        sleep(2)
        self.click_btn_confirm_date()
        sleep(2)
        self.sendkeys_input_msg(msg)
        sleep(2)
        self.click_btn_confirm_msg()
        sleep(2)
        self.click_btn_confirm()
        sleep(5)
        namelist = self.gettexts_texts_rule_names()
        self.assert_Equal(name, namelist[0])