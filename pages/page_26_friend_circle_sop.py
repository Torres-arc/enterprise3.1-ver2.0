# -*- coding: utf-8 -*-
# @Time    : 2020/12/26 11:07
# @Author  : Torres
# @File    : page_26_friend_circle_sop.py

from selenium.webdriver.common.by import By
from commons.base_page import BasePage


class FriendCircleSOP(BasePage):
    """元素定位信息"""
    # 朋友圈SOP页面
    _btn_friend_circle_sop_page = (By.XPATH, '//li[text()="朋友圈SOP"]')
    # 规则名称列表
    _texts_rule_names = (By.CSS_SELECTOR, 'tbody tr td:nth-child(1) div')
    # 创建人列表
    _texts_key_words = 'tbody tr td:nth-child(2) ww-open-data"]'
    # 详情
    _btn_download = (By.XPATH, '//span[text()="详情"]/..')
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
    # 选择发送成员
    _btn_add_keys = (By.XPATH, '//span[text()="选择发送成员"]/..')
    # 添加人输入框
    _input_key_words = (By.CSS_SELECTOR, 'input[placeholder="请输入关键词"]')
    # 员工节点按钮
    _btn_confirm_keys = (By.CSS_SELECTOR, '.custom-tree-node')
    # 员工选择确认按钮
    _btn_confirm_staff = (By.CSS_SELECTOR, 'div[aria-label="选择添加人"] .el-dialog__footer button+button')
    # 添加推送按钮
    _btn_add_msg = (By.XPATH, '//span[text()="添加推送"]/..')
    # 推送内容输入框
    _input_send_name = (By.XPATH, '//label[text()="内容名称"]/following-sibling::div/div/input')
    # 起始时间输入框
    _input_start_time = (By.CSS_SELECTOR, 'input[placeholder="起始时间"]')
    # 结束时间输入框
    _input_end_time = (By.CSS_SELECTOR, 'input[placeholder="结束时间"]')
    # 消息输入框
    _input_msg = (By.CSS_SELECTOR, 'input[placeholder="直接开始输入"]')
    # 素材确认按钮
    _btn_confirm_msg = (By.CSS_SELECTOR, 'div[class="el-form-item el-form-item--small"] button')
    # 新建确定按钮
    _btn_confirm = (By.XPATH, '//span[text()=" 确定 "]/..')
    """元素定位层"""

    """元素操作层"""

    """业务层"""



