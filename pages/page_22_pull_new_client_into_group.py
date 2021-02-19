# -*- coding: utf-8 -*-
# @Time    : 2020/12/4 10:03
# @Author  : Torres
# @File    : page_22_pull_new_client_into_group.py
from time import sleep

from selenium.webdriver.common.by import By
from commons.base_page import BasePage


class PullNewClientIntoGroup(BasePage):
    """元素定位信息"""
    # 新客自动拉群页面
    _btn_pull_new_client_page = (By.XPATH, '//li[text()="新客自动拉群"]')
    # 活动名称列表
    _texts_act_names = (By.CSS_SELECTOR, 'tbody tr td:nth-child(2) div')
    # 详情
    _btn_detail = (By.XPATH, '//span[text()="详情"]/..')
    # 下载
    _btn_download = (By.XPATH, '//span[text()="下载"]/..')
    # 更多
    _btn_more = (By.XPATH, '//span[text()="更多"]/..')
    # 编辑
    _btn_edit = (By.CSS_SELECTOR, 'ul[x-placement] li')
    # 删除
    _btn_delete = (By.CSS_SELECTOR, 'ul[x-placement] li+li')
    # 删除确认按钮
    _btn_confirm_delete = (By.CSS_SELECTOR, '.el-message-box div[class*="btn"] button+button')
    # 新建自动拉群
    _btn_create = (By.XPATH, '//span[text()="新建自动拉群"]/..')
    # 活动名称搜索框
    _input_search_act_name = (By.CSS_SELECTOR, 'input[placeholder="请输入活动名称"]')
    # 页码数
    _text_page_num = (By.CSS_SELECTOR, '.el-pager li:last-child')
    # 翻页按钮
    _btn_next_page = (By.CSS_SELECTOR, '.btn-next')

    # 新建页面
    # 活动名称输入框
    _input_act_name = (By.CSS_SELECTOR, 'input.el-input__inner')
    # 选择员工按钮
    _btn_select_staff = (By.XPATH, '//span[text()=" 选择员工"]/..')
    # 员工修改按钮
    _btn_edit_staff = (By.XPATH, '//span[text()="修改"]/..')
    # 取消员工按钮
    _btn_remove_staff = (By.CSS_SELECTOR, 'span[class="custom-tree-node between"]')
    # 员工搜索框
    _input_search_staff = (By.CSS_SELECTOR, 'input[placeholder="请输入关键词"]')
    # 员工节点按钮
    _btn_select_staff_node = (By.CSS_SELECTOR, '.custom-tree-node')
    # 确定员工按钮
    _btn_confirm_staff = (By.CSS_SELECTOR, 'div[aria-label="选择添加人"] .el-dialog__footer button:last-child')
    # 添加标签按钮
    _btn_add_tag = (By.XPATH, '//span[text()="添加标签"]/..')
    # 标签修改按钮
    _btn_edit_tag = (By.XPATH, '(//span[text()="修改"]/..)[2]')
    # 取消标签按钮
    _btn_remove_tag = (By.CSS_SELECTOR, 'li[class="tag select"]')
    # 标签选择按钮1
    _btn_tag_select1 = (By.CSS_SELECTOR, 'li.tag')
    # 标签选择按钮2
    _btn_tag_select2 = (By.CSS_SELECTOR, 'li.tag:nth-child(2)')
    # 标签确认按钮
    _btn_confirm_tag = (By.CSS_SELECTOR, 'div[aria-label="选择标签"] .el-dialog__body+.el-dialog__footer button:last-child')
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

    # 详情页面
    # 使用成员
    _text_detail_user = (By.CSS_SELECTOR, '.el-form-item__content ww-open-data')
    # 客户标签
    _texts_detail_tags = (By.XPATH, '//label[text()="客户标签"]/following-sibling::div/span')
    # 入群引导语
    _text_detail_guide = (By.XPATH, '//label[text()="入群引导语"]/following-sibling::div')
    # 群聊详情
    _text_detail_info = (By.XPATH, '//label[text()="群聊详情"]/following-sibling::div/span')

    """元素定位层"""
    # 新客自动拉群页面
    def get_btn_pull_new_client_page(self):
        return self.find_Element(self._btn_pull_new_client_page)
    # 活动名称列表
    def get_texts_act_names(self):
        return self.find_Elements(self._texts_act_names)
    # 详情
    def get_btn_detail(self):
        return self.find_Element(self._btn_detail)
    # 下载
    def get_btn_download(self):
        return self.find_Element(self._btn_download)
    # 更多
    def get_btn_more(self):
        return self.find_Element(self._btn_more)
    # 编辑
    def get_btn_edit(self):
        return self.find_Element(self._btn_edit)
    # 删除
    def get_btn_delete(self):
        return self.find_Element(self._btn_delete)
    # 删除确认按钮
    def get_btn_confirm_delete(self):
        return self.find_Element(self._btn_confirm_delete)
    # 新建自动拉群
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
    # 选择员工按钮
    def get_btn_select_staff(self):
        return self.find_Element(self._btn_select_staff)
    # 员工修改按钮
    def get_btn_edit_staff(self):
        return self.find_Element(self._btn_edit_staff)
    # 取消员工按钮
    def get_btn_remove_staff(self):
        return self.find_Element(self._btn_remove_staff)
    # 员工搜索框
    def get_input_search_staff(self):
        return self.find_Element(self._input_search_staff)
    # 员工节点按钮
    def get_btn_select_staff_node(self):
        return self.find_Element(self._btn_select_staff_node)
    # 确定员工按钮
    def get_btn_confirm_staff(self):
        return self.find_Element(self._btn_confirm_staff)
    # 添加标签按钮
    def get_btn_add_tag(self):
        return self.find_Element(self._btn_add_tag)
    # 标签修改按钮
    def get_btn_edit_tag(self):
        return self.find_Element(self._btn_edit_tag)
    # 取消标签按钮
    def get_btn_remove_tag(self):
        return self.find_Element(self._btn_remove_tag)
    # 标签选择按钮1
    def get_btn_tag_select1(self):
        return self.find_Element(self._btn_tag_select1)
    # 标签选择按钮2
    def get_btn_tag_select2(self):
        return self.find_Element(self._btn_tag_select2)
    # 标签确认按钮
    def get_btn_confirm_tag(self):
        return self.find_Element(self._btn_confirm_tag)
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

    # 详情页面
    # 使用成员
    def get_text_detail_user(self):
        return self.find_Element(self._text_detail_user)
    # 客户标签
    def get_texts_detail_tags(self):
        return self.find_Elements(self._texts_detail_tags)
    # 入群引导语
    def get_text_detail_guide(self):
        return self.find_Element(self._text_detail_guide)
    # 群聊详情
    def get_text_detail_info(self):
        return self.find_Element(self._text_detail_info)

    """元素操作层"""
    # 新客自动拉群页面
    def click_btn_pull_new_client_page(self):
        return self.click_element(self.get_btn_pull_new_client_page())
    # 活动名称列表
    def gettexts_texts_act_names(self):
        return self.get_elements_values(self.get_texts_act_names())
    # 详情
    def click_btn_detail(self):
        return self.click_element(self.get_btn_detail())
    # 下载
    def click_btn_download(self):
        return self.click_element(self.get_btn_download())
    # 更多
    def click_btn_more(self):
        return self.click_element(self.get_btn_more())
    # 编辑
    def click_btn_edit(self):
        return self.click_element(self.get_btn_edit())
    # 删除
    def click_btn_delete(self):
        return self.click_element(self.get_btn_delete())
    # 删除确认按钮
    def click_btn_confirm_delete(self):
        return self.click_element(self.get_btn_confirm_delete())
    # 新建自动拉群
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
    # 选择员工按钮
    def click_btn_select_staff(self):
        return self.click_element(self.get_btn_select_staff())
    # 员工修改按钮
    def click_btn_edit_staff(self):
        return self.click_element(self.get_btn_edit_staff())
    # 取消员工按钮
    def click_btn_remove_staff(self):
        return self.click_element(self.get_btn_remove_staff())
    # 员工搜索框
    def sendkeys_input_search_staff(self, value):
        return self.send_keys(self.get_input_search_staff(), value)
    # 员工节点按钮
    def click_btn_select_staff_node(self):
        return self.click_element(self.get_btn_select_staff_node())
    # 确定员工按钮
    def click_btn_confirm_staff(self):
        return self.click_element(self.get_btn_confirm_staff())
    # 添加标签按钮
    def click_btn_add_tag(self):
        return self.click_element(self.get_btn_add_tag())
    # 标签修改按钮
    def click_btn_edit_tag(self):
        return self.click_element(self.get_btn_edit_tag())
    # 取消标签按钮
    def click_btn_remove_tag(self):
        return self.click_element(self.get_btn_remove_tag())
    # 标签选择按钮1
    def click_btn_tag_select1(self):
        return self.click_element(self.get_btn_tag_select1())
    def gettexts_btn_tag_select1(self):
        return self.get_element_value(self.get_btn_tag_select1())
    # 标签选择按钮2
    def click_btn_tag_select2(self):
        return self.click_element(self.get_btn_tag_select2())
    def gettexts_btn_tag_select2(self):
        return self.get_element_value(self.get_btn_tag_select2())
    # 标签确认按钮
    def click_btn_confirm_tag(self):
        return self.click_element(self.get_btn_confirm_tag())
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

    # 详情页面
    # 使用成员
    def gettexts_text_detail_user(self):
        return self.get_text_detail_user().get_attribute('openid')
    # 客户标签
    def gettexts_texts_detail_tags(self):
        return self.get_elements_values(self.get_texts_detail_tags())
    # 入群引导语
    def gettexts_text_detail_guide(self):
        return self.get_element_value(self.get_text_detail_guide())
    # 群聊详情
    def gettexts_text_detail_info(self):
        return self.get_element_value(self.get_text_detail_info())

    """业务层"""
    def switch_to_current(self):
        self.click_btn_pull_new_client_page()
        sleep(2)

    def search_by_name(self, name):
        self.sendkeys_input_search_act_name(name)
        sleep(1)
        self.tap_keyboard('enter')
        self.tap_keyboard('enter')
        sleep(3)
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
                for i in namelist:
                    try:
                        self.check_exist_in_lists(name, i)
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

    def create_activity(self, name, staff, guide, code):
        self.click_btn_create()
        sleep(2)
        self.sendkeys_input_act_name(name)
        sleep(2)
        self.click_btn_select_staff()
        sleep(2)
        self.sendkeys_input_search_staff(staff)
        sleep(1)
        self.tap_keyboard('enter')
        sleep(2)
        self.click_btn_select_staff_node()
        sleep(2)
        self.click_btn_confirm_staff()
        sleep(2)
        self.click_btn_add_tag()
        sleep(2)
        text1 = self.gettexts_btn_tag_select1()
        self.click_btn_tag_select1()
        sleep(1)
        text2 = self.gettexts_btn_tag_select2()
        self.click_btn_tag_select2()
        sleep(1)
        taglist = [text1, text2]
        self.set_ini('pull_new_client', 'taglist', ' '.join(taglist))
        self.click_btn_confirm_tag()
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

    def check_details(self, user, taglist, guide, code):
        sleep(2)
        self.click_btn_detail()
        sleep(2)
        openid = self.gettexts_text_detail_user()
        user1 = self.get_userid_info(openid)
        self.assert_Equal(user, user1)
        taglist.sort()
        tlist = self.gettexts_texts_detail_tags()
        tlist.sort()
        self.assert_Equal(taglist, tlist)
        self.assert_Equal(guide, self.gettexts_text_detail_guide())
        self.assert_Equal(code, (self.gettexts_text_detail_info())[:-5])
        sleep(3)

    def edit_act(self, ename, euser, eguide):
        self.click_btn_more()
        sleep(2)
        self.click_btn_edit()
        sleep(2)
        self.sendkeys_input_act_name(ename)
        sleep(2)
        self.click_btn_edit_staff()
        sleep(2)
        self.click_btn_remove_staff()
        sleep(2)
        self.sendkeys_input_search_staff(euser)
        sleep(1)
        self.tap_keyboard('enter')
        sleep(2)
        self.click_btn_select_staff_node()
        sleep(2)
        self.click_btn_confirm_staff()
        sleep(2)
        self.click_btn_edit_tag()
        sleep(2)
        self.click_btn_remove_tag()
        sleep(1)
        self.click_btn_remove_tag()
        sleep(2)
        text1 = self.gettexts_btn_tag_select1()
        self.click_btn_tag_select1()
        sleep(1)
        text2 = self.gettexts_btn_tag_select2()
        self.click_btn_tag_select2()
        sleep(1)
        taglist = [text1, text2]
        self.set_ini('pull_new_client', 'taglist', ' '.join(taglist))
        self.click_btn_confirm_tag()
        sleep(2)
        self.sendkeys_input_guide(eguide)
        sleep(2)
        self.click_btn_confirm()
        sleep(3)
        self.click_btn_detail()
        sleep(2)
        openid = self.gettexts_text_detail_user()
        user1 = self.get_userid_info(openid)
        self.assert_Equal(euser, user1)
        taglist.sort()
        tlist = self.gettexts_texts_detail_tags()
        tlist.sort()
        self.assert_Equal(taglist, tlist)
        self.assert_Equal(eguide, self.gettexts_text_detail_guide())
        sleep(3)

    def delete_act(self, name):
        nlist = self.gettexts_texts_act_names()
        self.assert_Equal(nlist[0], name)
        self.click_btn_more()
        sleep(2)
        self.click_btn_delete()
        sleep(2)
        self.click_btn_confirm_delete()
        sleep(2)
        self.check_exist_in_page('删除成功')
        sleep(2)
        self.check_not_exist_in_page(name)

