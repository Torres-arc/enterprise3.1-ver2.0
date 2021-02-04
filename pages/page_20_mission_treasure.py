import datetime
import os
import time

import selenium
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from commons.base_page import BasePage
from time import sleep


class MissionTreasure(BasePage):
    """元素定位信息"""
    # 任务宝页面
    _btn_mission_treasure = (By.XPATH, '//li[text()="任务宝"]')
    # 任务宝名称搜索输入框
    _input_mission_name_search = (By.CSS_SELECTOR, 'input[placeholder="请输入"]')
    # 开始时间
    _input_start_time_search = (By.CSS_SELECTOR, 'input[placeholder="开始时间"]')
    # 结束时间
    _input_end_time_search = (By.CSS_SELECTOR, 'input[placeholder="结束时间"]')
    # 查询按钮
    _btn_search = (By.XPATH, '//span[text()="查询"]/..')
    # 重置按钮
    _btn_reset = (By.XPATH, '//span[text()="重置"]/..')
    # 新建任务按钮
    _btn_create_mission = (By.XPATH, '//span[text()="新建任务"]/..')
    # 任务活动名称
    _texts_mission_names = (By.CSS_SELECTOR, 'tbody tr td:nth-child(1) div')
    # 裂变客户数量
    _texts_clients_num = (By.CSS_SELECTOR, 'tbody tr td:nth-child(2) div')
    # 活动状态
    _texts_mission_status = (By.CSS_SELECTOR, 'tbody tr td:nth-child(3) div')
    # 活动时间
    _texts_mission_times = (By.CSS_SELECTOR, 'table[style] tbody tr td:nth-child(4) div')
    # 详情
    _btn_mission_details = ('css', 'tbody tr:nth-child(%s) td:nth-child(5) button:first-child')
    # 编辑
    _btn_mission_edit = ('css', 'tbody tr:nth-child(%s) td:nth-child(5) button:last-child')
    # 页面数
    _text_page = (By.CSS_SELECTOR, 'ul.el-pager li:last-child')
    # 翻页按钮
    _btn_next_page = (By.CSS_SELECTOR, 'ul.el-pager+button')
    # 任务总数
    _text_mission_num = (By.CSS_SELECTOR, '.el-pagination__total')

    # 活动名称输入框
    _input_mission_name = (By.XPATH, '//label[text()="任务活动名称"]/following-sibling::div/div/input')
    # 引导语输入框
    _input_guide_words = (By.CSS_SELECTOR, 'textarea[placeholder*="裂变"]')
    # 人数输入框
    _input_clients_amount = (By.XPATH, '//div[text()="人"]/preceding-sibling::input')
    # 活动开始时间
    _input_start_time = (By.CSS_SELECTOR, 'input[placeholder="开始日期"]')
    # 结束时间
    _input_end_time = (By.CSS_SELECTOR, 'input[placeholder="结束日期"]')
    # 确定日期
    _btn_confirm_date = (By.CSS_SELECTOR, 'button[class*="link-btn el-button--d"]')

    # 活动发起成员
    # 发起成员选择按钮
    _btn_member_partical_selected = (By.XPATH, '//span[text()="选择成员"]/preceding-sibling::span')
    # 全部按钮
    _btn_member_all_selected = (By.XPATH, '//span[text()="全部"]/preceding-sibling::span')
    # 选择成员按钮
    _btn_select_member = (By.XPATH, '//span[text()="选择成员"]/parent::button')
    # 全部按钮
    _btn_tag_all_selected = (By.XPATH, '(//span[text()="全部"]/preceding-sibling::span)[2]')
    # 客户标签选择按钮
    _btn_tag_partical_selected = (By.XPATH, '//span[text()="选择标签"]/preceding-sibling::span')
    # 选择标签按钮
    _btn_select_tag = (By.XPATH, '//span[text()="选择标签"]/parent::button')

    # 裂变海报
    # 添加海报按钮
    _btn_add_poster = (By.XPATH, '//span[text()="添加海报"]/..')
    # 选择员工按钮
    _btn_select_client = (By.XPATH, '//span[text()="选择员工"]/..')

    # 活动奖励
    # 兑奖码输入框
    _input_redeem_code = (By.CSS_SELECTOR, 'input[placeholder*="数字和英文"]')
    # 兑奖链接输入框
    _input_redeem_link = (By.CSS_SELECTOR, 'input[placeholder*="http"]')
    # 兑奖图片按钮
    _btn_redeem_pic = (By.CSS_SELECTOR, 'div[element-loading-text]>div')
    # 兑奖规则输入框
    _input_redeem_rule = (By.XPATH, '//label[text()="兑奖规则"]/following-sibling::div/div/textarea')

    # 新客欢迎语
    # 欢迎语选择按钮
    _btn_welcoming_select = (By.XPATH, '//span[text()="添加图片/网页/小程序消息"]/..')
    # 图片选择按钮
    _btn_select_pic = (By.XPATH, '//p[text()="图 片"]/../..')
    # 网页选择按钮
    _btn_select_web = (By.XPATH, '//p[text()="网 页"]/../..')
    # 小程序选择按钮
    _btn_select_mini = (By.XPATH, '//p[text()="小程序"]/../..')
    # 欢迎语输入框
    _input_welcoming = (By.CSS_SELECTOR, 'textarea[placeholder*="欢迎语"]')

    # 下发途径
    # 个人群发按钮
    _btn_personal_sender = (By.XPATH, '//span[text()="个人群发助手"]/preceding-sibling::span')
    # 管理员统一群发按钮
    _btn_admin_sender = (By.XPATH, '//span[text()="管理员统一群发消息"]/preceding-sibling::span')

    # 阅读勾选按钮
    _btn_have_read = (By.CSS_SELECTOR, '.el-checkbox__input')
    # 保存按钮
    _btn_save = (By.XPATH, '//span[text()="保存"]/..')

    # 组织架构
    # 员工输入框
    _input_staff = (By.CSS_SELECTOR, 'input[placeholder="请输入关键词"]')
    # 员工节点
    _btn_node_staff = (By.CSS_SELECTOR, 'span.custom-tree-node')
    # 确定按钮
    _btn_confirm_staff = (By.CSS_SELECTOR, 'div[aria-label="选择成员"] div.el-dialog__footer button+button')

    # 标签选择
    # 标签1
    _btn_tag1 = (By.CSS_SELECTOR, 'li.tag:nth-child(1)')
    # 标签2
    _btn_tag2 = (By.CSS_SELECTOR, 'li.tag:nth-child(2)')
    # 确定按钮
    _btn_confirm_tag = (By.CSS_SELECTOR, 'div[aria-label="选择标签"] div.dialog-footer button+button')

    # 海报素材选择
    # 素材输入框
    _input_poster_search = (By.CSS_SELECTOR, 'input[placeholder="搜索素材"]')
    # 海报选择
    _btn_poster_select = (By.CSS_SELECTOR,
                          'div[aria-label="选择海报素材"] div[class*="picture-co"]:nth-child(4) .water-fall-item')
    # 确定按钮
    _btn_confirm_poster = (By.CSS_SELECTOR, 'div[aria-label="选择海报素材"] div.dialog-footer button+button')

    # 添加网页消息
    # 搜索输入框
    _input_web_search = (By.CSS_SELECTOR, 'div[aria-label="添加网页消息"] input[placeholder="搜索素材"]')
    # 网页选择
    _btn_web_select = (By.CSS_SELECTOR, 'div[aria-label="添加网页消息"] .water-fall-item')
    # 确定按钮
    _btn_confirm_web = (By.CSS_SELECTOR, 'div[aria-label="添加网页消息"] div.dialog-footer button+button')

    # 添加小程序消息
    # 搜索输入框
    _input_mini_search = (By.CSS_SELECTOR, 'div[aria-label="添加小程序消息"] input[placeholder="搜索素材"]')
    # 小程序选择
    _btn_mini_select = (By.XPATH, '(//div[@class="water-fall-item"])[3]')
    # 确定按钮
    _btn_confirm_mini = (By.CSS_SELECTOR, 'div[aria-label="添加小程序消息"] div.dialog-footer button+button')

    # 详情页面
    # 活动名称
    _text_mission_name = (By.XPATH, '//div[text()="活动名称："]/following-sibling::div')
    # 引导语
    _text_guide = (By.XPATH, '//div[text()="裂变引导语："]/following-sibling::div')
    # 客户数
    _text_client_num = (By.XPATH, '//div[text()="裂变客户数量："]/following-sibling::div')
    # 活动时间
    _text_act_time = (By.XPATH, '//div[text()="活动时间："]/following-sibling::div')
    # 标签
    _text_tag = (By.XPATH, '//div[text()="客户标签："]/following-sibling::div')
    # 员工
    _text_staff = (By.XPATH, '//div[text()="员工："]/following-sibling::div')
    # 兑奖码
    _text_redeem_code = (By.XPATH, '//div[text()="兑奖码："]/following-sibling::div')
    # 兑奖链接
    _text_redeem_link = (By.XPATH, '//div[text()="兑奖链接："]/following-sibling::div')
    # 兑奖规则
    _text_redeem_rule = (By.XPATH, '//div[text()="兑奖规则："]/following-sibling::div')
    # 欢迎语
    _text_welcome = (By.XPATH, '//div[text()="新客欢迎语："]/following-sibling::div')
    # 下发途径
    _text_distribute_way = (By.XPATH, '//div[text()="活动下发途径："]/following-sibling::div')

    """元素定位层"""
    # 任务宝页面
    def get_btn_mission_treasure(self):
        return self.find_Element(self._btn_mission_treasure)
    # 任务宝名称搜索输入框
    def get_input_mission_name_search(self):
        return self.find_Element(self._input_mission_name_search)
    # 开始时间
    def get_input_start_time_search(self):
        return self.find_Element(self._input_start_time_search)
    # 结束时间
    def get_input_end_time_search(self):
        return self.find_Element(self._input_end_time_search)
    # 查询按钮
    def get_btn_search(self):
        return self.find_Element(self._btn_search)
    # 重置按钮
    def get_btn_reset(self):
        return self.find_Element(self._btn_reset)
    # 新建任务按钮
    def get_btn_create_mission(self):
        return self.find_Element(self._btn_create_mission)
    # 任务活动名称
    def get_texts_mission_names(self):
        return self.find_Elements(self._texts_mission_names)
    # 裂变客户数量
    def get_texts_clients_num(self):
        return self.find_Elements(self._texts_clients_num)
    # 活动状态
    def get_texts_mission_status(self):
        return self.find_Elements(self._texts_mission_status)
    # 活动时间
    def get_texts_mission_times(self):
        return self.find_Elements(self._texts_mission_times)
    # 详情
    def get_btn_mission_details(self, index):
        return self.find_ele_replace(self._btn_mission_details[0], self._btn_mission_details[1], index)
    # 编辑
    def get_btn_mission_edit(self, index):
        return self.find_ele_replace(self._btn_mission_edit[0], self._btn_mission_edit[1], index)
    # 页面数
    def get_text_page(self):
        return self.find_Element(self._text_page)
    # 翻页按钮
    def get_btn_next_page(self):
        return self.find_Element(self._btn_next_page)
    # 任务总数
    def get_text_mission_num(self):
        return self.find_Element(self._text_mission_num)

    # 活动名称输入框
    def get_input_mission_name(self):
        return self.find_Element(self._input_mission_name)
    # 引导语输入框
    def get_input_guide_words(self):
        return self.find_Element(self._input_guide_words)
    # 人数输入框
    def get_input_clients_amount(self):
        return self.find_Element(self._input_clients_amount)
    # 活动开始时间
    def get_input_start_time(self):
        return self.find_Element(self._input_start_time)
    # 结束时间
    def get_input_end_time(self):
        return self.find_Element(self._input_end_time)
    # 确定时间
    def get_btn_confirm_date(self):
        return self.find_Element(self._btn_confirm_date)

    # 活动发起成员
    # 发起成员选择按钮
    def get_btn_member_partical_selected(self):
        return self.find_Element(self._btn_member_partical_selected)
    # 全部按钮
    def get_btn_member_all_selected(self):
        return self.find_Element(self._btn_member_all_selected)
    # 选择成员按钮
    def get_btn_select_member(self):
        return self.find_Element(self._btn_select_member)
    # 全部按钮
    def get_btn_tag_all_selected(self):
        return self.find_Element(self._btn_tag_all_selected)
    # 客户标签选择按钮
    def get_btn_tag_partical_selected(self):
        return self.find_Element(self._btn_tag_partical_selected)
    # 选择标签按钮
    def get_btn_select_tag(self):
        return self.find_Element(self._btn_select_tag)

    # 裂变海报
    # 添加海报按钮
    def get_btn_add_poster(self):
        return self.find_Element(self._btn_add_poster)
    # 选择员工按钮
    def get_btn_select_client(self):
        return self.find_Element(self._btn_select_client)

    # 活动奖励
    # 兑奖码输入框
    def get_input_redeem_code(self):
        return self.find_Element(self._input_redeem_code)
    # 兑奖链接输入框
    def get_input_redeem_link(self):
        return self.find_Element(self._input_redeem_link)
    # 兑奖图片按钮
    def get_btn_redeem_pic(self):
        return self.find_Element(self._btn_redeem_pic)
    # 兑奖规则输入框
    def get_input_redeem_rule(self):
        return self.find_Element(self._input_redeem_rule)

    # 新客欢迎语
    # 欢迎语选择按钮
    def get_btn_welcoming_select(self):
        return self.find_Element(self._btn_welcoming_select)
    # 图片选择按钮
    def get_btn_select_pic(self):
        return self.find_Element(self._btn_select_pic)
    # 网页选择按钮
    def get_btn_select_web(self):
        return self.find_Element(self._btn_select_web)
    # 小程序选择按钮
    def get_btn_select_mini(self):
        return self.find_Element(self._btn_select_mini)
    # 欢迎语输入框
    def get_input_welcoming(self):
        return self.find_Element(self._input_welcoming)

    # 下发途径
    # 个人群发按钮
    def get_btn_personal_sender(self):
        return self.find_Element(self._btn_personal_sender)
    # 管理员统一群发按钮
    def get_btn_admin_sender(self):
        return self.find_Element(self._btn_admin_sender)
    # 阅读勾选按钮
    def get_btn_have_read(self):
        return self.find_Element(self._btn_have_read)
    # 保存按钮
    def get_btn_save(self):
        return self.find_Element(self._btn_save)

    # 组织架构
    # 员工输入框
    def get_input_staff(self):
        return self.find_Element(self._input_staff)
    # 员工节点
    def get_btn_node_staff(self):
        return self.find_Element(self._btn_node_staff)
    # 确定按钮
    def get_btn_confirm_staff(self):
        return self.find_Element(self._btn_confirm_staff)

    # 标签选择
    # 标签1
    def get_btn_tag1(self):
        return self.find_Element(self._btn_tag1)
    # 标签2
    def get_btn_tag2(self):
        return self.find_Element(self._btn_tag2)
    # 确定按钮
    def get_btn_confirm_tag(self):
        return self.find_Element(self._btn_confirm_tag)

    # 海报素材选择
    # 素材输入框
    def get_input_poster_search(self):
        return self.find_Element(self._input_poster_search)
    # 海报选择
    def get_btn_poster_select(self):
        return self.find_Element(self._btn_poster_select)
    # 确定按钮
    def get_btn_confirm_poster(self):
        return self.find_Element(self._btn_confirm_poster)

    # 添加网页消息
    # 搜索输入框
    def get_input_web_search(self):
        return self.find_Element(self._input_web_search)
    # 网页选择
    def get_btn_web_select(self):
        return self.find_Element(self._btn_web_select)
    # 确定按钮
    def get_btn_confirm_web(self):
        return self.find_Element(self._btn_confirm_web)

    # 添加小程序消息
    # 搜索输入框
    def get_input_mini_search(self):
        return self.find_Element(self._input_mini_search)
    # 小程序选择
    def get_btn_mini_select(self):
        return self.find_Element(self._btn_mini_select)
    # 确定按钮
    def get_btn_confirm_mini(self):
        return self.find_Element(self._btn_confirm_mini)

    # 详情页面
    # 活动名称
    def get_text_mission_name(self):
        return self.find_Element(self._text_mission_name)
    # 引导语
    def get_text_guide(self):
        return self.find_Element(self._text_guide)
    # 客户数
    def get_text_client_num(self):
        return self.find_Element(self._text_client_num)
    # 活动时间
    def get_text_act_time(self):
        return self.find_Element(self._text_act_time)
    # 标签
    def get_text_tag(self):
        return self.find_Element(self._text_tag)
    # 员工
    def get_text_staff(self):
        return self.find_Element(self._text_staff)
    # 兑奖码
    def get_text_redeem_code(self):
        return self.find_Element(self._text_redeem_code)
    # 兑奖链接
    def get_text_redeem_link(self):
        return self.find_Element(self._text_redeem_link)
    # 兑奖规则
    def get_text_redeem_rule(self):
        return self.find_Element(self._text_redeem_rule)
    # 欢迎语
    def get_text_welcome(self):
        return self.find_Element(self._text_welcome)
    # 下发途径
    def get_text_distribute_way(self):
        return self.find_Element(self._text_distribute_way)

    """元素操作层"""
    # 任务宝页面
    def click_btn_mission_treasure(self):
        return self.click_element(self.get_btn_mission_treasure())
    # 任务宝名称搜索输入框
    def sendkeys_input_mission_name_search(self, value):
        return self.send_keys(self.get_input_mission_name_search(), value)
    # 开始时间
    def sendkeys_input_start_time_search(self, value):
        return self.send_keys(self.get_input_start_time_search(), value)
    # 结束时间
    def sendkeys_input_end_time_search(self, value):
        return self.send_keys(self.get_input_end_time_search(), value)
    # 查询按钮
    def click_btn_search(self):
        return self.click_element(self.get_btn_search())
    # 重置按钮
    def click_btn_reset(self):
        return self.click_element(self.get_btn_reset())
    # 新建任务按钮
    def click_btn_create_mission(self):
        return self.click_element(self.get_btn_create_mission())
    # 任务活动名称
    def gettexts_texts_mission_names(self):
        return self.get_elements_values(self.get_texts_mission_names())
    # 裂变客户数量
    def gettexts_texts_clients_num(self):
        return self.get_elements_values(self.get_texts_clients_num())
    # 活动状态
    def gettexts_texts_mission_status(self):
        return self.get_elements_values(self.get_texts_mission_status())
    # 活动时间
    def gettexts_texts_mission_times(self):
        return self.get_elements_values(self.get_texts_mission_times())
    # 详情
    def click_btn_mission_details(self, index):
        return self.click_element(self.get_btn_mission_details(index))
    # 编辑
    def click_btn_mission_edit(self, index):
        return self.click_element(self.get_btn_mission_edit(index))
    # 页面数
    def gettexts_text_page(self):
        return self.get_element_value(self.get_text_page())
    # 翻页按钮
    def click_btn_next_page(self):
        return self.click_element(self.get_btn_next_page())
    # 任务总数
    def gettexts_text_mission_num(self):
        return self.get_element_value(self.get_text_mission_num())

    # 活动名称输入框
    def sendkeys_input_mission_name(self, value):
        return self.send_keys(self.get_input_mission_name(), value)
    # 引导语输入框
    def sendkeys_input_guide_words(self, value):
        return self.send_keys(self.get_input_guide_words(), value)
    # 人数输入框
    def sendkeys_input_clients_amount(self, value):
        return self.send_keys(self.get_input_clients_amount(), value)
    # 活动开始时间
    def sendkeys_input_start_time(self, value):
        return self.send_keys(self.get_input_start_time(), value)
    # 结束时间
    def sendkeys_input_end_time(self, value):
        return self.send_keys(self.get_input_end_time(), value)
    # 确定时间
    def click_btn_confirm_date(self):
        return self.click_element(self.get_btn_confirm_date())

    # 活动发起成员
    # 发起成员选择按钮
    def click_btn_member_partical_selected(self):
        return self.click_element(self.get_btn_member_partical_selected())
    # 全部按钮
    def click_btn_member_all_selected(self):
        return self.click_element(self.get_btn_member_all_selected())
    # 选择成员按钮
    def click_btn_select_member(self):
        return self.click_element(self.get_btn_select_member())
    # 全部按钮
    def click_btn_tag_all_selected(self):
        return self.click_element(self.get_btn_tag_all_selected())
    # 客户标签选择按钮
    def click_btn_tag_partical_selected(self):
        return self.click_element(self.get_btn_tag_partical_selected())
    # 选择标签按钮
    def click_btn_select_tag(self):
        return self.click_element(self.get_btn_select_tag())

    # 裂变海报
    # 添加海报按钮
    def click_btn_add_poster(self):
        return self.click_element(self.get_btn_add_poster())
    # 选择员工按钮
    def click_btn_select_client(self):
        return self.click_element(self.get_btn_select_client())

    # 活动奖励
    # 兑奖码输入框
    def sendkeys_input_redeem_code(self, value):
        return self.send_keys(self.get_input_redeem_code(), value)
    # 兑奖链接输入框
    def sendkeys_input_redeem_link(self, value):
        return self.send_keys(self.get_input_redeem_link(), value)
    # 兑奖图片按钮
    def click_btn_redeem_pic(self):
        return self.click_element(self.get_btn_redeem_pic())
    # 兑奖规则输入框
    def sendkeys_input_redeem_rule(self, value):
        return self.send_keys(self.get_input_redeem_rule(), value)

    # 新客欢迎语
    # 欢迎语选择按钮
    def click_btn_welcoming_select(self):
        return self.click_element(self.get_btn_welcoming_select())
    # 图片选择按钮
    def click_btn_select_pic(self):
        return self.click_element(self.get_btn_select_pic())
    # 网页选择按钮
    def click_btn_select_web(self):
        return self.click_element(self.get_btn_select_web())
    # 小程序选择按钮
    def click_btn_select_mini(self):
        return self.click_element(self.get_btn_select_mini())
    # 欢迎语输入框
    def sendkeys_input_welcoming(self, value):
        return self.send_keys(self.get_input_welcoming(), value)

    # 下发途径
    # 个人群发按钮
    def click_btn_personal_sender(self):
        return self.click_element(self.get_btn_personal_sender())
    # 管理员统一群发按钮
    def click_btn_admin_sender(self):
        return self.click_element(self.get_btn_admin_sender())
    # 阅读勾选按钮
    def click_btn_have_read(self):
        return self.click_element(self.get_btn_have_read())
    # 保存按钮
    def click_btn_save(self):
        return self.click_element(self.get_btn_save())

    # 组织架构
    # 员工输入框
    def sendkeys_input_staff(self, value):
        return self.send_keys(self.get_input_staff(), value)
    # 员工节点
    def click_btn_node_staff(self):
        return self.click_element(self.get_btn_node_staff())
    # 确定按钮
    def click_btn_confirm_staff(self):
        return self.click_element(self.get_btn_confirm_staff())

    # 标签选择
    # 标签1
    def click_btn_tag1(self):
        return self.click_element(self.get_btn_tag1())
    # 标签2
    def click_btn_tag2(self):
        return self.click_element(self.get_btn_tag2())
    # 确定按钮
    def click_btn_confirm_tag(self):
        return self.click_element(self.get_btn_confirm_tag())

    # 海报素材选择
    # 素材输入框
    def sendkeys_input_poster_search(self, value):
        return self.send_keys(self.get_input_poster_search(), value)
    # 海报选择
    def click_btn_poster_select(self):
        return self.click_element(self.get_btn_poster_select())
    # 确定按钮
    def click_btn_confirm_poster(self):
        return self.click_element(self.get_btn_confirm_poster())

    # 添加网页消息
    # 搜索输入框
    def sendkeys_input_web_search(self, value):
        return self.send_keys(self.get_input_web_search(), value)
    # 网页选择
    def click_btn_web_select(self):
        return self.click_element(self.get_btn_web_select())
    # 确定按钮
    def click_btn_confirm_web(self):
        return self.click_element(self.get_btn_confirm_web())

    # 添加小程序消息
    # 搜索输入框
    def sendkeys_input_mini_search(self, value):
        return self.send_keys(self.get_input_mini_search(), value)
    # 小程序选择
    def click_btn_mini_select(self):
        return self.click_element(self.get_btn_mini_select())
    # 确定按钮
    def click_btn_confirm_mini(self):
        return self.click_element(self.get_btn_confirm_mini())

    # 详情页面
    # 活动名称
    def gettexts_text_mission_name(self):
        return self.get_element_value(self.get_text_mission_name())
    # 引导语
    def gettexts_text_guide(self):
        return self.get_element_value(self.get_text_guide())
    # 客户数
    def gettexts_text_client_num(self):
        return self.get_element_value(self.get_text_client_num())
    # 活动时间
    def gettexts_text_act_time(self):
        return self.get_element_value(self.get_text_act_time())
    # 标签
    def gettexts_text_tag(self):
        return self.get_element_value(self.get_text_tag())
    # 员工
    def gettexts_text_staff(self):
        return self.get_element_value(self.get_text_staff())
    # 兑奖码
    def gettexts_text_redeem_code(self):
        return self.get_element_value(self.get_text_redeem_code())
    # 兑奖链接
    def gettexts_text_redeem_link(self):
        return self.get_element_value(self.get_text_redeem_link())
    # 兑奖规则
    def gettexts_text_redeem_rule(self):
        return self.get_element_value(self.get_text_redeem_rule())
    # 欢迎语
    def gettexts_text_welcome(self):
        return self.get_element_value(self.get_text_welcome())
    # 下发途径
    def gettexts_text_distribute_way(self):
        return self.get_element_value(self.get_text_distribute_way())

    """业务层"""
    def switch_to_current(self):
        self.click_btn_mission_treasure()
        sleep(3)

    def select_member(self, user):
        self.sendkeys_input_staff(user)
        sleep(1)
        self.tap_keyboard('enter')
        sleep(2)
        self.click_btn_node_staff()
        sleep(1)
        self.click_btn_confirm_staff()

    def select_poster(self, msg):
        self.sendkeys_input_poster_search(msg)
        sleep(1)
        self.tap_keyboard('enter')
        sleep(2)
        self.click_btn_poster_select()
        sleep(1)
        self.click_btn_confirm_poster()

    def search_by_name(self, name):
        self.sendkeys_input_mission_name_search(name)
        sleep(1)
        self.click_btn_search()
        sleep(2)
        pages = int(self.gettexts_text_page())
        count = 1
        while pages > 0 and count <= 3:
            try:
                namelist = self.gettexts_texts_mission_names()
            except Exception:
                print('12321')
                try:
                    self.check_exist_in_page('暂无数据')
                except Exception as e:
                    raise e
                else:
                    ele = self.find_Element((By.XPATH, '//span[text()="暂无数据"]'))
                    rect = self.locate_element(ele)
                    self.GetScreen('按姓名搜索，无数据', rect=rect)
                    self.printout('搜索条件下无数据')
            # except Exception as e:
            #     raise e
            else:
                for i in namelist:
                    try:
                        self.check_exist_in_lists(name, i)
                    except AssertionError as e:
                        ele = self.find_Element(By.XPATH, '//div[text()="{}"]'.format(i))
                        rect = self.locate_element(ele)
                        self.GetScreen('按姓名搜索，错误', rect=rect)
                        self.printout('搜索条件与数据不匹配')
                        raise e
            self.click_btn_next_page()
            pages -= 1
            count += 1

    def search_by_date(self, stime, etime):
        self.sendkeys_input_start_time_search(stime)
        sleep(1)
        self.sendkeys_input_end_time_search(etime)
        sleep(1)
        self.click_btn_search()
        sleep(2)
        pages = int(self.gettexts_text_page())
        count = 1
        while pages > 0 and count <= 3:
            try:
                timelist = self.gettexts_texts_mission_times()
            except TimeoutException:
                try:
                    self.check_exist_in_page('暂无数据')
                except Exception as e:
                    raise e
                else:
                    ele = self.find_Element((By.XPATH, '//span[text()="暂无数据"]'))
                    rect = self.locate_element(ele)
                    self.GetScreen('按时间搜索，无数据', rect=rect)
                    self.printout('搜索条件下无数据')
            except Exception as e:
                raise e
            else:
                for i in timelist:
                    start = (i.split(' '))[0]
                    end = ((i.split(' '))[1])[9:]
                    st = datetime.datetime.strptime(start, '%Y-%m-%d')
                    et = datetime.datetime.strptime(end, '%Y-%m-%d')
                    sa = datetime.datetime.strptime(stime, '%Y-%m-%d')
                    ea = datetime.datetime.strptime(etime, '%Y-%m-%d')
                    try:
                        self.assert_True(st >= sa, '验证{} >= {}'.format(st, sa))
                        self.assert_True(et <= ea, '验证{} <= {}'.format(st, sa))
                    except AssertionError as e:
                        ele = self.find_Element(By.XPATH, '//div[text()="{}"]'.format(i))
                        rect = self.locate_element(ele)
                        self.GetScreen('按日期搜索，错误', rect=rect)
                        self.printout('搜索条件与数据不匹配')
                        raise e
            self.click_btn_next_page()
            pages -= 1
            count += 1

    def reset(self, name):
        f_pagenum = self.gettexts_text_mission_num()
        self.sendkeys_input_mission_name_search(name)
        sleep(1)
        self.click_btn_search()
        sleep(2)
        m_pagenum = self.gettexts_text_mission_num()
        self.assert_Not_Equal(f_pagenum, m_pagenum)
        self.click_btn_reset()
        sleep(2)
        self.assert_Equal(self.gettexts_text_mission_num(), f_pagenum)


    def create_mission(self, cname, guide, people, user, msg, code, link, path, rule, welcome):
        """
        :param cname: str 任务宝名称
        :param guide: str 引导语
        :param people: str 人数
        :param user: str 发起成员
        :param msg: str 海报名称
        :param code: str 兑奖码
        :param link: str 兑奖链接
        :param path: str 图片路径
        :param rule: str 兑奖规则
        :param welcome: str 欢迎语
        :return:
        """
        self.click_btn_create_mission()
        sleep(2)
        self.sendkeys_input_mission_name(cname)
        sleep(1)
        self.sendkeys_input_guide_words(guide)
        sleep(1)
        self.sendkeys_input_clients_amount(people)
        sleep(1)
        now = datetime.datetime.now()
        delta = datetime.timedelta(days=1)
        startime = now + delta
        endtime = now + 2 * delta
        self.sendkeys_input_start_time(startime.strftime('%Y-%m-%d %H:%M:%S'))
        sleep(1)
        self.sendkeys_input_end_time(endtime.strftime('%Y-%m-%d %H:%M:%S'))
        sleep(1)
        self.click_btn_confirm_date()
        sleep(2)
        self.click_btn_member_partical_selected()
        sleep(2)
        self.click_btn_select_member()
        sleep(2)
        self.select_member(user)
        sleep(2)
        self.click_btn_add_poster()
        sleep(2)
        self.select_poster(msg)
        sleep(2)
        self.sendkeys_input_redeem_code(code)
        sleep(2)
        self.sendkeys_input_redeem_link(link)
        sleep(2)
        self.click_btn_redeem_pic()
        sleep(2)
        self.tap_keyboard('shift')
        pat = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + path
        print(pat)
        self.control_keyboard(pat)
        sleep(1)
        self.tap_keyboard('enter')
        sleep(2)
        self.sendkeys_input_redeem_rule(rule)
        sleep(2)
        self.sendkeys_input_welcoming(welcome)
        sleep(2)
        self.click_btn_have_read()
        sleep(2)
        self.click_btn_save()
        sleep(4)
        self.check_exist_in_page('%s-%s' % (startime.strftime('%Y-%m-%d %H:%M:%S'), endtime.strftime('%Y-%m-%d %H:%M:%S')))



