from selenium.webdriver.common.by import By
from commons.base_page import BasePage
from selenium.webdriver.common.keys import Keys
import os
from time import sleep
from pykeyboard import PyKeyboard


# 客户群活码
class ClientGroupCodePage(BasePage):
    # 元素定位信息
    # 点击跳转到客户群活码页面
    _btn_client_group_code_page = (By.XPATH, '(//li[text()="客户群活码"])')

    # 添加
    # 新建客户群活码
    _btn_add_client_group_code = (By.XPATH, '//span[text()="新建客户群活码 "]/..')
    # 开始创建按钮
    _btn_create = (By.XPATH, '//span[text()="开始创建"]')
    # 添加活动头像按钮
    _btn_activity_picture = (By.CSS_SELECTOR, 'div[class="el-upload el-upload--text"]')
    # 活动名称
    _input_activity_name = (By.XPATH, '//input[@placeholder="给客户群起个名字"]')
    # 活动场景
    _input_activity_scene = (By.XPATH, '//textarea[@placeholder="给客户群使用的活动场景做个备注"]')
    # 引导语
    _input_leadding_words = (By.XPATH, '//textarea[@placeholder="请输入引导语"]')
    # 无法进群提示
    _btn_prompt = (By.XPATH, '//span[@class="el-switch__core"]')
    # 下一步
    _btn_next_step1 = (By.XPATH, '//span[text()="下一步"]/..')
    # 添加实际群码
    _btn_add_reality_group_code = (By.XPATH, '//span[text()="添加实际群码"]/..')
    # 实际群码
    _btn_reality_group_code = (By.CSS_SELECTOR, 'div[aria-label="添加实际群码"] i[class*="el-icon-p"]')
    # 群名称
    _input_group_name = (By.CSS_SELECTOR, 'label[for="name"]+div input')
    # 有效期
    _input_expire_data = (By.CSS_SELECTOR, 'input[placeholder="选择有效期"]')
    # 扫码次数限制
    _input_code_scanning_limit = (By.CSS_SELECTOR, 'input[placeholder="请输入扫码次数限制"]')
    # 确定按钮
    _btn_sure = (By.XPATH, '//span[text()="确 定"]')
    # 返回活码页面
    _btn_back_main = (By.CSS_SELECTOR, '.el-icon-back')
    # 下一步
    _btn_next_step2 = (By.XPATH, '(//span[text()="下一步"]/..)[2]')
    # 点击完成
    _btn_finish = (By.XPATH, '//span[text()="完成"]')

    # 点击更多按钮
    _btn_more = (By.XPATH, '//span[text()="更多"]')
    # 更多==》管理实际群码
    _btn_sure_edit_reality_group_code = (By.XPATH, '//ul[@x-placement]/li[text()="管理实际群码"]')
    # 编辑按钮
    _btn_edit_code = (By.XPATH, '//span[text()="编辑"]/..')
    # 群名称文本
    _text_group_name = (By.CSS_SELECTOR, 'tbody td:nth-child(2)>div')
    # 有效期
    _text_effect_date = (By.CSS_SELECTOR, 'tbody td:nth-child(3)>div')
    # 扫码限制
    _text_scan_limit = (By.CSS_SELECTOR, 'tbody td:nth-child(5)>div')
    # 返回按钮
    _btn_back_client_group_code_page = (By.XPATH, '//i[@class="el-icon-back"]')

    # 更多==》编辑
    _btn_edit_client_group_code_page = (By.XPATH, '//ul[@x-placement]/li[text()="编辑"]')
    # 编辑确认按钮
    _btn_edit_confirm = (By.XPATH, '//span[text()="确认"]/..')
    # 更多==》删除
    _btn_delete_client_group_code_ = (By.XPATH, '//ul[@x-placement]/li[text()="删除"]')
    # 删除确认
    _btn_confirm_delete_client_group_code = (By.CSS_SELECTOR, '.el-message-box__btns>button:last-child')
    # 复制链接
    _btn_copy_interlinking = (By.XPATH, '//span[text()="复制链接"]')
    # 查询
    _input_search_client_group_code = (By.XPATH, '//input[@placeholder="请输入关键词"]')
    # 活动名称
    _texts_assert_search_message = (By.XPATH, '//tbody/tr/td[2]/div')
    # 活动场景
    _texts_act_scene = (By.XPATH, '//tbody/tr/td[3]/div')

    '''元素定位层'''
    # 点击跳转到客户群活码页面
    def get_client_group_code_page(self):
        return self.find_Element(self._btn_client_group_code_page)
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
    # 添加实际群码
    def get_btn_add_reality_group_code(self):
        return self.find_Element(self._btn_add_reality_group_code)
    # 实际群码
    def get_btn_reality_group_code(self):
        return self.find_Element(self._btn_reality_group_code)
    # 群名称
    def get_input_group_name(self):
        return self.find_Element(self._input_group_name)
    # 有效期
    def get_input_expire_data(self):
        return self.find_Element(self._input_expire_data)
    # 扫码次数限制
    def get_input_code_scanning_limit(self):
        return self.find_Element(self._input_code_scanning_limit)
    # 确定按钮
    def get_btn_sure(self):
        return self.find_Element(self._btn_sure)
    # 下一步
    def get_btn_next_step2(self):
        return self.find_Element(self._btn_next_step2)
    # 返回活码页面
    def get_btn_back_main(self):
        return self.find_Element(self._btn_back_main)
    # 点击完成
    def get_btn_finish(self):
        return self.find_Element(self._btn_finish)
    # 点击更多按钮
    def get_btn_more(self):
        return self.find_Element(self._btn_more)
    # 更多==》管理实际群码
    def get_btn_sure_edit_reality_group_code(self):
        return self.find_Element(self._btn_sure_edit_reality_group_code)
    # 编辑按钮
    def get_btn_edit_code(self):
        return self.find_Element(self._btn_edit_code)
    # 群名称文本
    def get_text_group_name(self):
        return self.find_Element(self._text_group_name)
    # 有效期
    def get_text_effect_date(self):
        return self.find_Element(self._text_effect_date)
    # 扫码限制
    def get_text_scan_limit(self):
        return self.find_Element(self._text_scan_limit)
    # 返回按钮
    def get_btn_back_client_group_code_page(self):
        return self.find_Element(self._btn_back_client_group_code_page)
    # 更多==》编辑
    def get_btn_edit_client_group_code_page(self):
        return self.find_Element(self._btn_edit_client_group_code_page)
    # 编辑确认按钮
    def get_btn_edit_confirm(self):
        return self.find_Element(self._btn_edit_confirm)
    # 更多==》删除
    def get_btn_delete_client_group_code_(self):
        return self.find_Element(self._btn_delete_client_group_code_)
    # 删除确认
    def get_btn_confirm_delete_client_group_code(self):
        return self.find_Element(self._btn_confirm_delete_client_group_code)
    # 复制链接
    def get_btn_copy_interlinking(self):
        return self.find_Element(self._btn_copy_interlinking)
    # 查询
    def get_input_search_client_group_code(self):
        return self.find_Element(self._input_search_client_group_code)
    def get_texts_assert_search_message(self):
        return self.find_Elements(self._texts_assert_search_message)
    # 活动场景
    def get_texts_act_scene(self):
        return self.find_Elements(self._texts_act_scene)

    """元素操作层"""
    # 点击跳转到客户群活码页面
    def click_client_group_code_page(self):
        return self.click_element(self.get_client_group_code_page())
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
    # 添加实际群码
    def click_btn_add_reality_group_code(self):
        return self.click_element(self.get_btn_add_reality_group_code())
    # 实际群码
    def click_btn_reality_group_code(self):
        return self.click_element(self.get_btn_reality_group_code())
    # 群名称
    def sendkeys_input_group_name(self, value):
        return self.send_keys(self.get_input_group_name(), value)
    # 有效期
    def sendkeys_input_expire_data(self, value):
        return self.send_keys(self.get_input_expire_data(), value)
    # 扫码次数限制
    def sendkeys_input_code_scanning_limit(self, value):
        return self.send_keys(self.get_input_code_scanning_limit(), value)
    # 确定按钮
    def click_btn_sure(self):
        return self.click_element(self.get_btn_sure())
    # 下一步
    def click_btn_next_step2(self):
        return self.click_element(self.get_btn_next_step2())
    # 返回活码页面
    def click_btn_back_main(self):
        return self.click_element(self.get_btn_back_main())
    # 点击完成
    def click_btn_finish(self):
        return self.click_element(self.get_btn_finish())
    # 点击更多按钮
    def click_btn_more(self):
        return self.click_element(self.get_btn_more())
    # 更多==》管理实际群码
    def click_btn_sure_edit_reality_group_code(self):
        return self.click_element(self.get_btn_sure_edit_reality_group_code())
    # 编辑按钮
    def click_btn_edit_code(self):
        return self.click_element(self.get_btn_edit_code())
    # 群名称文本
    def gettexts_text_group_name(self):
        return self.get_element_value(self.get_text_group_name())
    # 有效期
    def gettexts_text_effect_date(self):
        return self.get_element_value(self.get_text_effect_date())
    # 扫码限制
    def gettexts_text_scan_limit(self):
        return self.get_element_value(self.get_text_scan_limit())
    # 返回按钮
    def click_btn_back_client_group_code_page(self):
        return self.click_element(self.get_btn_back_client_group_code_page())
    # 更多==》编辑
    def click_btn_edit_client_group_code_page(self):
        return self.click_element(self.get_btn_edit_client_group_code_page())
    # 编辑确认按钮
    def click_btn_edit_confirm(self):
        return self.click_element(self.get_btn_edit_confirm())
    # 更多==》删除
    def click_btn_delete_client_group_code_(self):
        return self.click_element(self.get_btn_delete_client_group_code_())
    # 删除确认
    def click_btn_confirm_delete_client_group_code(self):
        return self.click_element(self.get_btn_confirm_delete_client_group_code())
    # 复制链接
    def click_btn_copy_interlinking(self):
        return self.click_element(self.get_btn_copy_interlinking())
    # 查询
    def sendkeys_input_search_client_group_code(self, value):
        return self.send_keys(self.get_input_search_client_group_code(), value)
    def gettexts_texts_assert_search_message(self):
        return self.get_elements_values(self.get_texts_assert_search_message())
    # 活动场景
    def gettexts_texts_act_scene(self):
        return self.get_elements_values(self.get_texts_act_scene())

    """业务层"""
    def switch_to_current(self):
        self.click_client_group_code_page()
        sleep(3)

    def add_client_group_code(self, act_name, act_scene, guide, group_name, date, limit):
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
        sleep(4)
        self.sendkeys_input_group_name(group_name)
        sleep(1)
        self.sendkeys_input_expire_data(date)
        sleep(1)
        self.sendkeys_input_code_scanning_limit(limit)
        sleep(1)
        self.click_btn_sure()
        sleep(2)
        self.click_btn_next_step2()
        sleep(2)
        self.click_btn_finish()
        sleep(2)
        self.check_exist_in_page(act_name)
        self.check_exist_in_page(act_scene)

    def manage_reality_code(self, group_name, date, limit):
        self.click_btn_more()
        sleep(2)
        self.click_btn_sure_edit_reality_group_code()
        sleep(2)
        self.click_btn_edit_code()
        sleep(2)
        self.sendkeys_input_group_name(group_name)
        sleep(1)
        self.sendkeys_input_expire_data(date)
        sleep(1)
        self.sendkeys_input_code_scanning_limit(limit)
        sleep(1)
        self.click_btn_sure()
        sleep(2)
        gname = self.gettexts_text_group_name()
        edate = self.gettexts_text_effect_date()
        elimit = self.gettexts_text_scan_limit()
        try:
            self.assert_Equal(gname, group_name)
            self.assert_Equal(date, edate)
            self.assert_Equal(limit, elimit)
        except AssertionError as e:
            print('断言失败', e)
        except Exception as e:
            print('出现预计外的错误', e)
        finally:
            self.click_btn_back_main()
        sleep(2)

    def search_by_keys(self, key):
        self.sendkeys_input_search_client_group_code(key)
        sleep(1)
        self.tap_keyboard('enter')
        sleep(2)
        actnames = self.gettexts_texts_assert_search_message()
        actscenes = self.gettexts_texts_act_scene()
        text = []
        for i in range(len(actnames)):
            text.append([])
            text[i].append(actnames[i])
            text[i].append(actscenes[i])
        for i in text:
            st = ','.join(i)
            self.check_exist_in_lists(key, st)

    def edit_client_group_code(self, act_name, act_scene):
        self.sendkeys_input_search_client_group_code('自动化测试场景')
        sleep(1)
        self.tap_keyboard('enter')
        sleep(2)
        self.click_btn_more()
        sleep(2)
        self.click_btn_edit_client_group_code_page()
        sleep(2)
        self.sendkeys_input_activity_name(act_name)
        sleep(1)
        self.sendkeys_input_activity_scene(act_scene)
        sleep(2)
        self.click_btn_edit_confirm()
        sleep(1.5)
        self.check_exist_in_page('保存成功')
        self.sendkeys_input_search_client_group_code(act_name)
        sleep(1)
        self.tap_keyboard('enter')
        sleep(3)
        acn = self.gettexts_texts_assert_search_message()
        acs = self.gettexts_texts_act_scene()
        lists = list(zip(acn, acs))
        for i in lists:
            self.assert_Equal(i[0], act_name)
            self.assert_Equal(i[1], act_scene)

    def delete_code(self, target):
        self.sendkeys_input_search_client_group_code('自动化测试场景')
        sleep(1)
        self.tap_keyboard('enter')
        sleep(2)
        self.click_btn_more()
        sleep(2)
        self.click_btn_delete_client_group_code_()
        sleep(2)
        self.click_btn_confirm_delete_client_group_code()
        sleep(1.5)
        self.check_exist_in_page('删除成功！')
        self.sendkeys_input_search_client_group_code('自动化测试场景')
        sleep(1)
        self.tap_keyboard('enter')
        sleep(2)
        self.check_not_exist_in_page('target')
