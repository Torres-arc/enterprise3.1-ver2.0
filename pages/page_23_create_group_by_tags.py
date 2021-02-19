# -*- coding: utf-8 -*-
# @Time    : 2020/12/17 11:28
# @Author  : Torres
# @File    : page_23_create_group_by_tags.py
from time import sleep

from selenium.webdriver.common.by import By
from commons.base_page import BasePage


class CreateGroupByTags(BasePage):
    """元素定位信息"""
    # 老客标签建群页面
    _btn_create_group_by_tags_page = (By.XPATH, '//li[text()="老客标签建群"]')
    # 发送方式选择框
    _btn_search_send_way = (By.CSS_SELECTOR, 'input[readonly]')
    # 个人群发选择
    _btn_search_personal = (By.XPATH, '//span[text()="个人群发"]/..')
    # 企业群发选择
    _btn_search_enterprise = (By.XPATH, '//span[text()="企业群发"]/..')
    # 任务名称输入框
    _input_search_task_name = (By.CSS_SELECTOR, 'input[placeholder*="任务"]')
    # 查找按钮
    _btn_search = (By.XPATH, '//span[text()="查找"]/..')
    # 重置按钮
    _btn_reset = (By.XPATH, '//span[text()="重置"]/..')
    # 任务名称列表
    _texts_tasks_names = (By.CSS_SELECTOR, 'tbody tr td:nth-child(1) div')
    # 发送方式列表
    _texts_send_ways = (By.CSS_SELECTOR, 'tbody tr td:nth-child(2) div')
    # 标签列表
    _texts_tags = (By.CSS_SELECTOR, 'tbody tr:nth-child(%s) td:nth-child(4) div[aria-describedby] span[class*="info"]')
    # 详情按钮
    _btn_details = (By.XPATH, '//span[text()="详情"]/..')
    # 删除按钮
    _btn_delete = (By.XPATH, '//span[text()="删除"]/..')
    # 删除确认按钮
    _btn_confirm_delete = (By.CSS_SELECTOR, 'div[aria-hidden="false"] button+button')
    # 新建标签建群按钮
    _btn_create_task = (By.XPATH, '//span[text()="新建标签建群"]/..')
    # 总数量
    _text_total_num = (By.CSS_SELECTOR, '.el-pagination__total')
    # 翻页按钮
    _btn_next_page = (By.CSS_SELECTOR, '.btn-next')
    # 页面数
    _text_page = (By.CSS_SELECTOR, '.el-pager li:last-child')

    # 新建界面
    # 任务名称输入框
    _input_task_name = (By.CSS_SELECTOR, 'input[type]')
    # 发送范围修改按钮
    _btn_edit_send_range = (By.XPATH, '//span[text()="修改"]/..')
    # 按照条件筛选客户按钮
    _btn_flit_client = (By.XPATH, '//span[text()="按照条件筛选客户"]/preceding-sibling::span')
    # 添加人选择框
    _btn_select_adder = (By.CSS_SELECTOR, 'div.select-user-box')
    # 员工搜索框
    _input_search_staff = (By.CSS_SELECTOR, 'input[placeholder="请输入关键词"]')
    # 员工节点按钮
    _btn_select_staff_node = (By.CSS_SELECTOR, '.custom-tree-node')
    # 确定员工按钮
    _btn_confirm_staff = (By.CSS_SELECTOR, 'div[aria-label="选择添加人"] .el-dialog__footer button:last-child')
    # 添加标签按钮
    _btn_add_tag = (By.XPATH, '//span[text()="添加标签"]/..')
    # 标签选择按钮1
    _btn_tag_select1 = (By.CSS_SELECTOR, 'li.tag')
    # 标签选择按钮2
    _btn_tag_select2 = (By.CSS_SELECTOR, 'li.tag:nth-child(2)')
    # 标签确认按钮
    _btn_confirm_tag = (By.CSS_SELECTOR, 'div[aria-label="选择标签"] .el-dialog__body+.el-dialog__footer button:last-child')
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
    # 发送范围确认按钮
    _btn_confirm_send_range = (By.CSS_SELECTOR, 'div[aria-label="选择发送客户"]>.el-dialog__footer button:last-child')
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
    # 发送方式-企业
    _btn_send_by_enterprise = (By.XPATH, '//span[text()="企业群发"]/preceding-sibling::span')
    # 发送方式-个人
    _btn_send_by_personal = (By.XPATH, '//span[text()="个人群发"]/preceding-sibling::span')
    # 发送按钮
    _btn_send = (By.XPATH, '//span[text()="通知成员发送"]/..')

    # 详情页面
    # 添加人
    _text_adder = (By.CSS_SELECTOR, 'main ww-open-data')
    # 添加时间
    _text_add_time = (By.XPATH, '//span[text()="添加时间："]/following-sibling::span')

    """元素定位层"""
    # 老客标签建群页面
    def get_btn_create_group_by_tags_page(self):
        return self.find_Element(self._btn_create_group_by_tags_page)
    # 发送方式选择框
    def get_btn_search_send_way(self):
        return self.find_Element(self._btn_search_send_way)
    # 个人群发选择
    def get_btn_search_personal(self):
        return self.find_Element(self._btn_search_personal)
    # 企业群发选择
    def get_btn_search_enterprise(self):
        return self.find_Element(self._btn_search_enterprise)
    # 任务名称输入框
    def get_input_search_task_name(self):
        return self.find_Element(self._input_search_task_name)
    # 查找按钮
    def get_btn_search(self):
        return self.find_Element(self._btn_search)
    # 重置按钮
    def get_btn_reset(self):
        return self.find_Element(self._btn_reset)
    # 任务名称列表
    def get_texts_tasks_names(self):
        return self.find_Elements(self._texts_tasks_names)
    # 发送方式列表
    def get_texts_send_ways(self):
        return self.find_Elements(self._texts_send_ways)
    # 标签列表
    def get_texts_tags(self):
        return self.find_Elements(self._texts_tags)
    # 详情按钮
    def get_btn_details(self):
        return self.find_Element(self._btn_details)
    # 删除按钮
    def get_btn_delete(self):
        return self.find_Element(self._btn_delete)
    # 删除确认按钮
    def get_btn_confirm_delete(self):
        return self.find_Element(self._btn_confirm_delete)
    # 新建标签建群按钮
    def get_btn_create_task(self):
        return self.find_Element(self._btn_create_task)
    # 总数量
    def get_text_total_num(self):
        return self.find_Element(self._text_total_num)
    # 翻页按钮
    def get_btn_next_page(self):
        return self.find_Element(self._btn_next_page)
    # 页面数
    def get_text_page(self):
        return self.find_Element(self._text_page)

    # 新建界面
    # 任务名称输入框
    def get_input_task_name(self):
        return self.find_Element(self._input_task_name)
    # 发送范围修改按钮
    def get_btn_edit_send_range(self):
        return self.find_Element(self._btn_edit_send_range)
    # 按照条件筛选客户按钮
    def get_btn_flit_client(self):
        return self.find_Element(self._btn_flit_client)
    # 添加人选择框
    def get_btn_select_adder(self):
        return self.find_Element(self._btn_select_adder)
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
    # 标签选择按钮1
    def get_btn_tag_select1(self):
        return self.find_Element(self._btn_tag_select1)
    # 标签选择按钮2
    def get_btn_tag_select2(self):
        return self.find_Element(self._btn_tag_select2)
    # 标签确认按钮
    def get_btn_confirm_tag(self):
        return self.find_Element(self._btn_confirm_tag)
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
    # 发送范围确认按钮
    def get_btn_confirm_send_range(self):
        return self.find_Element(self._btn_confirm_send_range)
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
    # 发送方式-企业
    def get_btn_send_by_enterprise(self):
        return self.find_Element(self._btn_send_by_enterprise)
    # 发送方式-个人
    def get_btn_send_by_personal(self):
        return self.find_Element(self._btn_send_by_personal)
    # 发送按钮
    def get_btn_send(self):
        return self.find_Element(self._btn_send)

    # 详情页面
    # 添加人
    def get_text_adder(self):
        return self.find_Element(self._text_adder)
    # 添加时间
    def get_text_add_time(self):
        return self.find_Element(self._text_add_time)

    """元素操作层"""
    # 老客标签建群页面
    def click_btn_create_group_by_tags_page(self):
        return self.click_element(self.get_btn_create_group_by_tags_page())
    # 发送方式选择框
    def click_btn_search_send_way(self):
        return self.click_element(self.get_btn_search_send_way())
    # 个人群发选择
    def click_btn_search_personal(self):
        return self.click_element(self.get_btn_search_personal())
    # 企业群发选择
    def click_btn_search_enterprise(self):
        return self.click_element(self.get_btn_search_enterprise())
    # 任务名称输入框
    def sendkeys_input_search_task_name(self, value):
        return self.send_keys(self.get_input_search_task_name(), value)
    # 查找按钮
    def click_btn_search(self):
        return self.click_element(self.get_btn_search())
    # 重置按钮
    def click_btn_reset(self):
        return self.click_element(self.get_btn_reset())
    # 任务名称列表
    def gettexts_texts_tasks_names(self):
        return self.get_elements_values(self.get_texts_tasks_names())
    # 发送方式列表
    def gettexts_texts_send_ways(self):
        return self.get_elements_values(self.get_texts_send_ways())
    # 标签列表
    def gettexts_texts_tags(self):
        return self.get_elements_values(self.get_texts_tags())
    # 详情按钮
    def click_btn_details(self):
        return self.click_element(self.get_btn_details())
    # 删除按钮
    def click_btn_delete(self):
        return self.click_element(self.get_btn_delete())
    # 删除确认按钮
    def click_btn_confirm_delete(self):
        return self.click_element(self.get_btn_confirm_delete())
    # 新建标签建群按钮
    def click_btn_create_task(self):
        return self.click_element(self.get_btn_create_task())
    # 总数量
    def gettexts_text_total_num(self):
        return self.get_element_value(self.get_text_total_num())
    # 翻页按钮
    def click_btn_next_page(self):
        return self.click_element(self.get_btn_next_page())
    # 页面数
    def gettexts_text_page(self):
        return self.get_element_value(self.get_text_page())

    # 新建界面
    # 任务名称输入框
    def sendkeys_input_task_name(self, value):
        return self.send_keys(self.get_input_task_name(), value)
    # 发送范围修改按钮
    def click_btn_edit_send_range(self):
        return self.click_element(self.get_btn_edit_send_range())
    # 按照条件筛选客户按钮
    def click_btn_flit_client(self):
        return self.click_element(self.get_btn_flit_client())
    # 添加人选择框
    def click_btn_select_adder(self):
        return self.click_element(self.get_btn_select_adder())
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
    # 标签选择按钮1
    def gettext_btn_tag_select1(self):
        return self.get_element_value(self.get_btn_tag_select1())
    def click_btn_tag_select1(self):
        return self.click_element(self.get_btn_tag_select1())
    # 标签选择按钮2
    def gettext_btn_tag_select2(self):
        return self.get_element_value(self.get_btn_tag_select2())
    def click_btn_tag_select2(self):
        return self.click_element(self.get_btn_tag_select2())
    # 标签确认按钮
    def click_btn_confirm_tag(self):
        return self.click_element(self.get_btn_confirm_tag())
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
    # 发送范围确认按钮
    def click_btn_confirm_send_range(self):
        return self.click_element(self.get_btn_confirm_send_range())
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
    # 发送方式-企业
    def click_btn_send_by_enterprise(self):
        return self.click_element(self.get_btn_send_by_enterprise())
    # 发送方式-个人
    def click_btn_send_by_personal(self):
        return self.click_element(self.get_btn_send_by_personal())
    # 发送按钮
    def click_btn_send(self):
        return self.click_element(self.get_btn_send())

    # 详情页面
    # 添加人
    def gettext_text_adder(self):
        return self.get_text_adder().get_attribute('openid')
    # 添加时间
    def gettext_text_add_time(self):
        return self.get_element_value(self.get_text_add_time())

    """业务层"""
    def switch_to_current(self):
        self.click_btn_create_group_by_tags_page()
        sleep(3)

    def search_by_way_of_sending(self):
        self.click_btn_search_send_way()
        sleep(2)
        self.click_btn_search_enterprise()
        sleep(1)
        self.click_btn_search()
        sleep(2)
        page_num = self.gettexts_text_page()
        pages = int(page_num)  # 页码
        count = 1
        while pages > 0 and count <= 3:
            try:
                ways_list = self.gettexts_texts_send_ways()  # 搜索目标
            except TimeoutError:
                try:
                    self.check_exist_in_page('暂无数据')  # 无数据时的页面信息
                except Exception as e:
                    raise e
                else:
                    ele = self.find_Element(By.XPATH, '//span[text()="暂无数据"]')  # 无数据时的页面信息
                    rect = self.locate_element(ele)
                    self.GetScreen('按发送方式搜索，无数据', rect=rect)
                    print('搜索条件下无数据')
            except Exception as e:
                raise e
            else:  # 存在数据，进行验证
                for i in ways_list:
                    try:
                        self.assert_Equal(i, '企业群发')
                    except AssertionError as e:
                        ele = self.find_Element(By.XPATH, '//div[text()=" {} "]'.format(i))
                        rect = self.locate_element(ele)
                        self.GetScreen('按发送方式搜索，错误', rect=rect)
                        print('搜索条件与数据不匹配')
                        raise e
            self.click_btn_next_page()  # 翻页
            pages -= 1
            count += 1

    def search_by_name(self, name):
        self.sendkeys_input_search_task_name(name)
        sleep(2)
        self.click_btn_search()
        sleep(2)
        page_num = self.gettexts_text_page()
        pages = int(page_num)  # 页码
        count = 1
        while pages > 0 and count <= 3:
            try:
                ways_list = self.gettexts_texts_tasks_names()  # 搜索目标
            except TimeoutError:
                try:
                    self.check_exist_in_page('暂无数据')  # 无数据时的页面信息
                except Exception as e:
                    raise e
                else:
                    ele = self.find_Element(By.XPATH, '//span[text()="暂无数据"]')  # 无数据时的页面信息
                    rect = self.locate_element(ele)
                    self.GetScreen('按发送方式搜索，无数据', rect=rect)
                    print('搜索条件下无数据')
            except Exception as e:
                raise e
            else:  # 存在数据，进行验证
                for i in ways_list:
                    try:
                        self.check_exist_in_lists(name, i)
                    except AssertionError as e:
                        ele = self.find_Element(By.XPATH, '//div[text()="{}"]'.format(i))
                        rect = self.locate_element(ele)
                        self.GetScreen('按发送方式搜索，错误', rect=rect)
                        print('搜索条件与数据不匹配')
                        raise e
            self.click_btn_next_page()  # 翻页
            pages -= 1
            count += 1

    def reset(self, name):
        sleep(3)
        ori_num = self.gettexts_text_total_num()
        self.sendkeys_input_search_task_name(name)
        sleep(2)
        self.click_btn_search()
        sleep(2)
        cur_num = self.gettexts_text_total_num()
        self.assert_Not_Equal(ori_num, cur_num)
        self.click_btn_reset()
        sleep(2)
        new_num = self.gettexts_text_total_num()
        self.assert_Equal(ori_num, new_num)

    def create_task(self, name, staff, guide, code, stime, etime):
        self.click_btn_create_task()
        sleep(2)
        self.sendkeys_input_task_name(name)
        sleep(2)
        self.click_btn_edit_send_range()
        sleep(2)
        self.click_btn_flit_client()
        sleep(2)
        self.click_btn_select_adder()
        sleep(2)
        self.sendkeys_input_search_staff(staff)
        sleep(2)
        self.tap_keyboard('enter')
        self.tap_keyboard('enter')
        sleep(2)
        self.click_btn_select_staff_node()
        sleep(2)
        self.click_btn_confirm_staff()
        sleep(2)
        # self.click_btn_add_tag()
        # sleep(2)
        # tag1 = self.gettext_btn_tag_select1()
        # self.click_btn_tag_select1()
        # sleep(1)
        # tag2 = self.gettext_btn_tag_select2()
        # self.click_btn_tag_select2()
        # sleep(2)
        # self.click_btn_confirm_tag()
        # sleep(2)
        self.click_btn_add_time()
        self.sendkeys_input_start_time(stime)
        sleep(1)
        # self.sendkeys_input_start_time_time('00:00:00')
        sleep(1)
        self.sendkeys_input_end_time(etime)
        # sleep(2)
        # self.sendkeys_input_end_time_time('00:00:00')
        sleep(2)
        self.click_btn_confirm_date()
        sleep(2)
        self.click_btn_confirm_send_range()
        sleep(2)
        self.sendkeys_input_guide(guide)
        sleep(2)
        self.click_btn_add_group_code()
        sleep(2)
        self.sendkeys_input_search_group_code(code)
        sleep(1)
        self.click_btn_search_code()
        sleep(2)
        self.click_btn_select_code()
        sleep(2)
        self.click_btn_confirm_code()
        sleep(2)
        self.click_btn_send_by_personal()
        sleep(2)
        self.click_btn_send()
        sleep(7)
        self.switch_to_current()
        sleep(5)
        self.check_exist_in_page(name)

    def check_details(self, name, staff, stime, etime):
        names = self.gettexts_texts_tasks_names()
        count = 0
        while True:
            if names[count] == name:
                self.click_btn_details()
                break
        uid = self.gettext_text_adder()
        uname = self.get_userid_info(uid)
        self.assert_Equal(uname, staff)
        add_time = self.gettext_text_add_time()
        self.assert_Equal(stime, (add_time.split(' - '))[0])
        self.assert_Equal(etime, (add_time.split(' - '))[1])

