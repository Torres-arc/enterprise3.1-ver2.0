from selenium.webdriver.common.by import By
from commons.base_page import BasePage
from selenium.webdriver.common.keys import Keys
import os
from time import sleep
from pykeyboard import PyKeyboard


# 客户群活码
class ClientGroupCodePage(BasePage):
    # 元素定位信息
    # 客户营销tab
    _btn_client_marketing_tab = (By.XPATH, '//span[text()="客户营销"]/..')
    # 员工活码页面
    _btn_employee_code_page = (By.XPATH, '//li[text()="创建活码"]')
    # 客户群活码tab
    _btn_client_group_tab = (By.XPATH, '//div[text()="客户群活码"]')
    # 关键词输入框
    _input_key_words = (By.CSS_SELECTOR, 'input[placeholder="请输入关键词"]')
    # 查询按钮
    _btn_search = (By.XPATH, '(//span[text()="查 询"]/..)[2]')
    # 管理群聊
    _btn_manage_client_group = (By.XPATH, '//span[text()="管理群聊"]/..')
    # 进入详情页
    _btn_enter_details = (By.CSS_SELECTOR, '#pane-2 tbody tr')
    # 活动名称列表
    _texts_act_names = (By.CSS_SELECTOR, '#pane-2 tbody tr td:nth-child(2)')
    # 活动场景列表
    _texts_act_scenes = (By.CSS_SELECTOR, '#pane-2 tbody tr td:nth-child(3)')

    # 添加
    # 新建客户群活码
    _btn_add_client_group_code = (By.XPATH, '//span[text()=" 新建客户群活码 "]/..')
    # 开始创建按钮
    _btn_create = (By.XPATH, '//span[text()="开始新建"]')
    # 添加活动头像按钮
    _btn_activity_picture = (By.CSS_SELECTOR, 'div[class="el-upload el-upload--text"]')
    # 活动名称
    _input_activity_name = (By.XPATH, '//input[@placeholder="给客户群起个名字"]')
    # 活动场景
    _input_activity_scene = (By.XPATH, '//input[@placeholder="给客户群使用的活动场景做个备注"]')
    # 引导语
    _input_leadding_words = (By.XPATH, '//input[@placeholder="可在二维码跳转页面展示社群介绍、入群引导等内容"]')
    # 无法进群提示
    _btn_prompt = (By.CSS_SELECTOR, '.el-switch__core')
    # 下一步
    _btn_next_step1 = (By.XPATH, '//span[text()="下一步 "]/..')
    # 修改确认按钮
    _btn_edit_confirm = (By.XPATH, '//span[text()="确认"]/..')
    # 添加实际群码
    _btn_add_reality_group_code = (By.XPATH, '//span[text()="添加群二维码"]/..')
    # 实际群码
    _btn_reality_group_code = (By.CSS_SELECTOR, 'div[aria-label="添加群聊"] i[class*="el-icon-p"]')
    # 选择客户群按钮
    _btn_select_client_group = (By.XPATH, '//span[text()="选择客户群"]/..')
    # 群名称
    _input_group_name = (By.CSS_SELECTOR, 'input[placeholder="请输入群名"]')
    # 查询按钮
    _btn_search_client_group = (By.XPATH, '//span[text()="查询"]/..')
    # 选择具体客户群
    _btn_select_specify_group = (By.CSS_SELECTOR, '.el-table__row')
    # 客户群确定按钮
    _btn_client_group_confirm = (By.CSS_SELECTOR, 'div[aria-label="选择客户群"] .el-dialog__footer button+button')
    # 有效期
    _input_expire_date = (By.CSS_SELECTOR, 'input[placeholder="选择日期"]')
    # 确定按钮
    _btn_sure = (By.XPATH, '//span[text()="确 定"]')
    # 下一步
    _btn_next_step2 = (By.XPATH, '//span[text()="下一步"]/..')
    # 点击完成
    _btn_finish = (By.CSS_SELECTOR, '.create-code-success button')


    # 详情页面
    # 编辑按钮
    _btn_edit_code = (By.XPATH, '//span[text()="编 辑"]/..')
    # 删除按钮
    _btn_delect = (By.XPATH, '//span[text()="删 除"]/..')
    # 删除确认按钮
    _btn_delect_confirm = (By.CSS_SELECTOR, 'div[class$="btns"] button+button')
    # 群名称文本
    _text_group_name = (By.CSS_SELECTOR, 'tbody td:nth-child(1)>div')
    # 有效期
    _text_effect_date = (By.CSS_SELECTOR, 'tbody td:nth-child(3)>div')
    # 引导语
    _text_guide = (By.XPATH, '//div[text()="引导语："]/following-sibling::div')
    # 活动名称
    _text_act_name = (By.CSS_SELECTOR, 'div.title')
    # 活动内容
    _text_act_info = (By.XPATH, '//div[text()="活动内容："]/following-sibling::div')

    # 管理群聊页面
    # 编辑按钮
    _btn_manage_edit = (By.XPATH, '//span[text()="编辑"]/..')
    # 群名称
    _text_manage_group_name = (By.CSS_SELECTOR, 'tr td:nth-child(2) div')
    # 有效期
    _text_active_date = (By.CSS_SELECTOR, 'tr td:nth-child(4) div span')


    '''元素定位层'''
    # 元素定位信息
    # 客户营销tab
    def get_btn_client_marketing_tab(self):
        return self.find_Element(self._btn_client_marketing_tab)
    # 员工活码页面
    def get_btn_employee_code_page(self):
        return self.find_Element(self._btn_employee_code_page)
    # 客户群活码tab
    def get_btn_client_group_tab(self):
        return self.find_Element(self._btn_client_group_tab)
    # 关键词输入框
    def get_input_key_words(self):
        return self.find_Element(self._input_key_words)
    # 查询按钮
    def get_btn_search(self):
        return self.find_Element(self._btn_search)
    # 管理群聊
    def get_btn_manage_client_group(self):
        return self.find_Element(self._btn_manage_client_group)
    # 进入详情页
    def get_btn_enter_details(self):
        return self.find_Element(self._btn_enter_details)
    # 活动名称列表
    def get_texts_act_names(self):
        return self.find_Elements(self._texts_act_names)
    # 活动场景列表
    def get_texts_act_scenes(self):
        return self.find_Elements(self._texts_act_scenes)

    # 添加
    # 新建客户群活码
    def get_btn_add_client_group_code(self):
        return self.find_Element(self._btn_add_client_group_code)
    # 开始创建按钮
    def get_btn_create(self):
        return self.find_Element(self._btn_create)
    # 添加活动头像按钮
    def get_btn_activity_picture(self):
        return self.find_Element(self._btn_activity_picture)
    # 活动名称
    def get_input_activity_name(self):
        return self.find_Element(self._input_activity_name)
    # 活动场景
    def get_input_activity_scene(self):
        return self.find_Element(self._input_activity_scene)
    # 引导语
    def get_input_leadding_words(self):
        return self.find_Element(self._input_leadding_words)
    # 无法进群提示
    def get_btn_prompt(self):
        return self.find_Element(self._btn_prompt)
    # 下一步
    def get_btn_next_step1(self):
        return self.find_Element(self._btn_next_step1)
    # 修改确认按钮
    def get_btn_edit_confirm(self):
        return self.find_Element(self._btn_edit_confirm)
    # 添加实际群码
    def get_btn_add_reality_group_code(self):
        return self.find_Element(self._btn_add_reality_group_code)
    # 实际群码
    def get_btn_reality_group_code(self):
        return self.find_Element(self._btn_reality_group_code)
    # 选择客户群按钮
    def get_btn_select_client_group(self):
        return self.find_Element(self._btn_select_client_group)
    # 群名称
    def get_input_group_name(self):
        return self.find_Element(self._input_group_name)
    # 查询按钮
    def get_btn_search_client_group(self):
        return self.find_Element(self._btn_search_client_group)
    # 选择具体客户群
    def get_btn_select_specify_group(self):
        return self.find_Element(self._btn_select_specify_group)
    # 客户群确定按钮
    def get_btn_client_group_confirm(self):
        return self.find_Element(self._btn_client_group_confirm)
    # 有效期
    def get_input_expire_date(self):
        return self.find_Element(self._input_expire_date)
    # 确定按钮
    def get_btn_sure(self):
        return self.find_Element(self._btn_sure)
    # 下一步
    def get_btn_next_step2(self):
        return self.find_Element(self._btn_next_step2)
    # 点击完成
    def get_btn_finish(self):
        return self.find_Element(self._btn_finish)

    # 详情页面
    # 编辑按钮
    def get_btn_edit_code(self):
        return self.find_Element(self._btn_edit_code)
    # 删除按钮
    def get_btn_delect(self):
        return self.find_Element(self._btn_delect)
    # 删除确认按钮
    def get_btn_delect_confirm(self):
        return self.find_Element(self._btn_delect_confirm)
    # 群名称文本
    def get_text_group_name(self):
        return self.find_Element(self._text_group_name)
    # 有效期
    def get_text_effect_date(self):
        return self.find_Element(self._text_effect_date)
    # 引导语
    def get_text_guide(self):
        return self.find_Element(self._text_guide)
    # 活动名称
    def get_text_act_name(self):
        return self.find_Element(self._text_act_name)
    # 活动内容
    def get_text_act_info(self):
        return self.find_Element(self._text_act_info)

    # 管理实际群码页面
    # 编辑按钮
    def get_btn_manage_edit(self):
        return self.find_Element(self._btn_manage_edit)
    # 群名称
    def get_text_manage_group_name(self):
        return self.find_Element(self._text_manage_group_name)
    # 有效期
    def get_text_active_date(self):
        return self.find_Element(self._text_active_date)

    """元素操作层"""
    # 元素定位信息
    # 客户营销tab
    def click_btn_client_marketing_tab(self):
        return self.click_element(self.get_btn_client_marketing_tab())
    # 员工活码页面
    def click_btn_employee_code_page(self):
        return self.click_element(self.get_btn_employee_code_page())
    # 客户群活码tab
    def click_btn_client_group_tab(self):
        return self.click_element(self.get_btn_client_group_tab())
    # 关键词输入框
    def sendkeys_input_key_words(self, value):
        return self.send_keys(self.get_input_key_words(), value)
    # 查询按钮
    def click_btn_search(self):
        return self.click_element(self.get_btn_search())
    # 管理群聊
    def click_btn_manage_client_group(self):
        return self.click_element(self.get_btn_manage_client_group())
    # 进入详情页
    def click_btn_enter_details(self):
        return self.click_element(self.get_btn_enter_details())
    # 活动名称列表
    def gettexts_texts_act_names(self):
        return self.get_elements_values(self.get_texts_act_names())
    # 活动场景列表
    def gettexts_texts_act_scenes(self):
        return self.get_elements_values(self.get_texts_act_scenes())

    # 添加
    # 新建客户群活码
    def click_btn_add_client_group_code(self):
        return self.click_element(self.get_btn_add_client_group_code())
    # 开始创建按钮
    def click_btn_create(self):
        return self.click_element(self.get_btn_create())
    # 添加活动头像按钮
    def click_btn_activity_picture(self):
        return self.click_element(self.get_btn_activity_picture())
    # 活动名称
    def sendkeys_input_activity_name(self, value):
        return self.send_keys(self.get_input_activity_name(), value)
    # 活动场景
    def sendkeys_input_activity_scene(self, value):
        return self.send_keys(self.get_input_activity_scene(), value)
    # 引导语
    def sendkeys_input_leadding_words(self, value):
        return self.send_keys(self.get_input_leadding_words(), value)
    # 无法进群提示
    def click_btn_prompt(self):
        return self.click_element(self.get_btn_prompt())
    # 下一步
    def click_btn_next_step1(self):
        return self.click_element(self.get_btn_next_step1())
    # 修改确认按钮
    def click_btn_edit_confirm(self):
        return self.click_element(self.get_btn_edit_confirm())
    # 添加实际群码
    def click_btn_add_reality_group_code(self):
        return self.click_element(self.get_btn_add_reality_group_code())
    # 实际群码
    def click_btn_reality_group_code(self):
        return self.click_element(self.get_btn_reality_group_code())
    # 选择客户群按钮
    def click_btn_select_client_group(self):
        return self.click_element(self.get_btn_select_client_group())
    # 群名称
    def sendkeys_input_group_name(self, value):
        return self.send_keys(self.get_input_group_name(), value)
    # 查询按钮
    def click_btn_search_client_group(self):
        return self.click_element(self.get_btn_search_client_group())
    # 选择具体客户群
    def click_btn_select_specify_group(self):
        return self.click_element(self.get_btn_select_specify_group())
    # 客户群确定按钮
    def click_btn_client_group_confirm(self):
        return self.click_element(self.get_btn_client_group_confirm())
    # 有效期
    def sendkeys_input_expire_date(self, value):
        return self.send_keys(self.get_input_expire_date(), value)
    # 确定按钮
    def click_btn_sure(self):
        return self.click_element(self.get_btn_sure())
    # 下一步
    def click_btn_next_step2(self):
        return self.click_element(self.get_btn_next_step2())
    # 点击完成
    def click_btn_finish(self):
        return self.click_element(self.get_btn_finish())

    # 详情页面
    # 编辑按钮
    def click_btn_edit_code(self):
        return self.click_element(self.get_btn_edit_code())
    # 删除按钮
    def click_btn_delect(self):
        return self.click_element(self.get_btn_delect())
    # 删除确认按钮
    def click_btn_delect_confirm(self):
        return self.click_element(self.get_btn_delect_confirm())
    # 群名称文本
    def gettexts_text_group_name(self):
        return self.get_element_value(self.get_text_group_name())
    # 有效期
    def gettexts_text_effect_date(self):
        return self.get_element_value(self.get_text_effect_date())
    # 引导语
    def gettexts_text_guide(self):
        return self.get_element_value(self.get_text_guide())
    # 活动名称
    def gettexts_text_act_name(self):
        return self.get_element_value(self.get_text_act_name())
    # 活动内容
    def gettexts_text_act_info(self):
        return self.get_element_value(self.get_text_act_info())

    # 管理实际群码页面
    # 编辑按钮
    def click_btn_manage_edit(self):
        return self.click_element(self.get_btn_manage_edit())
    # 群名称
    def gettexts_text_manage_group_name(self):
        return self.get_element_value(self.get_text_manage_group_name())
    # 有效期
    def gettexts_text_active_date(self):
        return self.get_element_value(self.get_text_active_date())

    """业务层"""
    def switch_to_current(self):
        self.click_btn_client_marketing_tab()
        sleep(2)
        self.click_btn_client_group_tab()
        sleep(3)

    def add_client_group_code(self, act_name, act_scene, guide, group_name, date):
        self.click_btn_add_client_group_code()
        sleep(2)
        self.click_btn_create()
        sleep(2)
        self.click_btn_activity_picture()
        sleep(2)
        path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)) + '\\materials\\pic\\photo.png')
        self.tap_keyboard('shift')
        self.control_keyboard(path)
        self.tap_keyboard('enter')
        sleep(4)
        self.sendkeys_input_activity_name(act_name)
        sleep(1)
        self.sendkeys_input_activity_scene(act_scene)
        sleep(1)
        self.sendkeys_input_leadding_words(guide)
        sleep(1)
        self.click_btn_prompt()
        sleep(1)
        self.click_btn_next_step1()
        sleep(3)
        self.click_btn_add_reality_group_code()
        sleep(2)
        self.click_btn_reality_group_code()
        sleep(2)
        path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)) + '\\materials\\pic\\groupcode.jpg')
        self.tap_keyboard('shift')
        self.control_keyboard(path)
        self.tap_keyboard('enter')
        sleep(3)
        self.click_btn_select_client_group()
        sleep(2)
        self.sendkeys_input_group_name(group_name)
        sleep(2)
        self.click_btn_search_client_group()
        sleep(2)
        self.click_btn_select_specify_group()
        sleep(2)
        self.click_btn_client_group_confirm()
        sleep(2)
        self.sendkeys_input_expire_date(date)
        sleep(2)
        self.click_btn_sure()
        sleep(2)
        self.click_btn_next_step2()
        sleep(2)
        self.force_scroll_screen()
        self.click_btn_finish()
        sleep(3)
        self.check_exist_in_page(act_name)
        self.check_exist_in_page(act_scene)

    def manage_reality_code(self, group_name, date):
        self.click_btn_manage_client_group()
        sleep(2)
        self.click_btn_manage_edit()
        sleep(2)
        self.click_btn_select_client_group()
        sleep(2)
        self.sendkeys_input_group_name(group_name)
        sleep(2)
        self.click_btn_search_client_group()
        sleep(2)
        self.click_btn_select_specify_group()
        sleep(2)
        self.click_btn_client_group_confirm()
        sleep(2)
        self.sendkeys_input_expire_date(date)
        sleep(1)
        self.click_btn_sure()
        sleep(2)
        gname = self.gettexts_text_manage_group_name()
        edate = self.gettexts_text_active_date()
        try:
            self.assert_Equal(gname, group_name)
            self.assert_Equal(date, edate)
        except AssertionError as e:
            print('断言失败', e)
        except Exception as e:
            print('出现预计外的错误', e)
        finally:
            self.switch_to_current()
        sleep(2)

    def search_by_keys(self, key):
        self.sendkeys_input_key_words(key)
        sleep(2)
        self.click_btn_search()
        sleep(2)
        actnames = self.gettexts_texts_act_names()
        actscenes = self.gettexts_texts_act_scenes()
        text = []
        for i in range(len(actnames)):
            text.append([])
            text[i].append(actnames[i])
            text[i].append(actscenes[i])
        for i in text:
            st = ','.join(i)
            self.check_exist_in_lists(key, st)

    def edit_client_group_code(self, act_name, act_scene):
        self.sendkeys_input_key_words('自动化测试场景')
        sleep(2)
        self.click_btn_search()
        sleep(2)
        self.click_btn_enter_details()
        sleep(2)
        self.click_btn_edit_code()
        sleep(2)
        self.sendkeys_input_activity_name(act_name)
        sleep(1)
        self.sendkeys_input_activity_scene(act_scene)
        sleep(2)
        self.click_btn_edit_confirm()
        sleep(1.5)
        self.check_exist_in_page('保存成功')
        sleep(3)
        acn = self.gettexts_text_act_name()
        acs = self.gettexts_text_act_info()
        self.assert_Equal(acn, act_name)
        self.assert_Equal(acs, act_scene)

    def delete_code(self, target):
        self.sendkeys_input_key_words('自动化测试场景')
        sleep(2)
        self.click_btn_search()
        sleep(2)
        self.click_btn_enter_details()
        sleep(2)
        self.click_btn_delect()
        sleep(2)
        self.click_btn_delect_confirm()
        sleep(1.5)
        self.check_exist_in_page('删除成功！')
        self.sendkeys_input_key_words('自动化测试场景')
        sleep(2)
        self.click_btn_search()
        sleep(2)
        self.check_not_exist_in_page('target')
