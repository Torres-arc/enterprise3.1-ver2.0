import datetime
from time import sleep

from airtest.core.android import Android
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from selenium.webdriver.common.by import By

from commons.App_base import AppBase
from commons.base_page import BasePage
from commons.log import log
from config.readConfig import *
from commons.readfile import SwitchToExcel


class ClientCodePage(BasePage):
    # 元素定位信息
    # 员工活码页面
    _btn_employee_code_page = (By.XPATH, '//li[text()="员工活码"]')
    # 新建员工活码
    _btn_add_employee_code = (By.XPATH, '//span[text()="新建员工活码"]/..')
    # 批量新建
    _btn_batch_create = (By.XPATH, '//span[text()="批量新建"]/..')
    # 删除
    _btn_delete = (By.XPATH, '//span[text()="删除"]/..')
    # 删除确认按钮
    _btn_delete_confirm = (By.XPATH, '//span[text()="确 认"]')
    # 下载
    _btn_download = (By.XPATH, '//span[text()="下载"]/..')
    # 批量下载
    _btn_batch_download = (By.XPATH, '//span[text()="批量下载"]/..')
    # 使用员工输入框
    _btn_user = (By.XPATH, '//label[text()="使用员工"]/following-sibling::div')
    # 姓名输入框
    _input_name = (By.XPATH, '//label[text()="姓名"]/following-sibling::div/div/input')
    # 手机号输入框
    _input_phone_number = (By.XPATH, '//label[text()="手机号"]/following-sibling::div/div/input')
    # 活动场景输入框
    _input_act_scene = (By.XPATH, '//label[text()="活动场景"]/following-sibling::div/div/input')
    # 创建人输入框
    _input_creator = (By.XPATH, '//label[text()="创建人"]/following-sibling::div/div/input')
    # 创建时间输入框
    _input_creat_time1 = (By.CSS_SELECTOR, 'input[placeholder="开始日期"]')
    _input_creat_time2 = (By.CSS_SELECTOR, 'input[placeholder="结束日期"]')
    # 查询按钮
    _btn_search = (By.XPATH, '//span[text()="查询"]/..')
    # 重置按钮
    _btn_reset = (By.XPATH, '//span[text()="重置"]/..')
    # 导出按钮
    _btn_export = (By.XPATH, '//span[text()="导出"]/..')
    # 更多按钮
    _btn_more = (By.XPATH, '//span[text()="更多"]/..')
    # 查看详情按钮
    _btn_check_detail = (By.CSS_SELECTOR, 'ul[x-placement] li:nth-child(1)')
    # 编辑按钮
    _btn_edit = (By.CSS_SELECTOR, 'ul[x-placement] li:nth-child(2)')
    # 删除按钮
    _btn_delete_code = (By.CSS_SELECTOR, 'ul[x-placement] li:nth-child(3)')
    # 删除确定按钮
    _btn_delete_code_sure = (By.CSS_SELECTOR, '.el-message-box button[class$="ary "]')
    # 使用员工文本
    _texts_user = (By.CSS_SELECTOR, 'tbody td:nth-child(3)>div>span>svg[class$="icon"]+div>ww-open-data')
    # 显示额外文本按钮
    _show_more = '//tr[%s]/td[3]/div/span[2]/i'
    # 额外员工文本
    _texts_addition_user = (By.CSS_SELECTOR, 'div[role]>span[class$="plain" ] ww-open-data')
    # 姓名文本
    _texts_name = (By.CSS_SELECTOR, 'tbody td:nth-child(4) span')
    # 手机号文本
    _texts_telnum = (By.CSS_SELECTOR, 'tbody td:nth-child(5) div')
    # 活动场景文本
    _texts_actscene = (By.CSS_SELECTOR, 'tbody td:nth-child(6) div')
    # 创建时间文本
    _texts_ctetime = (By.CSS_SELECTOR, 'tbody td:nth-child(8) div')
    # 创建人文本
    _texts_creator = (By.CSS_SELECTOR, 'tbody td:nth-child(7) span')
    # 总数量
    _text_total_num = (By.CSS_SELECTOR, 'span.promise:nth-child(2)')
    # 页数
    _text_page_num = (By.CSS_SELECTOR, '.el-pager>li:last-child')
    # 翻页按钮
    _btn_next_page = (By.CSS_SELECTOR, '.btn-next')
    # 全选框
    _btn_check_box = (By.CSS_SELECTOR, '.el-checkbox>span>span')
    # 复制链接
    _btn_copy_link = (By.XPATH, '//span[text()="复制链接"]/..')
    # 页面容量
    _btn_page_size = (By.CSS_SELECTOR, 'input[placeholder="请选择"]')
    # 15条
    _btn_15_size = (By.XPATH, '//span[text()="15条/页"]/..')

    # 新建界面
    # 批量单人活码
    _btn_type_batch_single = (By.XPATH, '//span[text()="批量单人"]/../span')
    # 单人活码
    _btn_type_single = (By.XPATH, '//span[text()="单人"]/../span')
    # 多人活码
    _btn_type_multi = (By.XPATH, '//span[text()="多人"]/../span')
    # 使用员工
    _btn_add_employer = (By.XPATH, '//span[text()="添加"]/..')
    # 活动场景输入框
    _input_activity_scene = (By.XPATH, '//*[@placeholder="输入活动场景"]')
    # 高级设置
    _btn_advanced_design = (By.XPATH, '//span[text()="高级设置"]/..')
    # 添加标签
    _btn_add_tags = (By.XPATH, '//span[text()="添加标签"]/..')
    # 选择前三个标签
    _btn_tags = (By.XPATH, '(//*[@class="tag"])[1]')
    _btn_tags2 = (By.XPATH, '(//*[@class="tag"])[2]')
    _btn_tags3 = (By.XPATH, '(//*[@class="tag"])[3]')
    # 确定标签按钮
    _btn_confirm = (By.XPATH, '(//span[text()="确 定"]/..)[2]')
    # 添加欢迎语
    _btn_welcoming_speech_button = (By.XPATH, '//span[text()="添加图片/网页/小程序消息"]')
    # 欢迎语图片按钮
    _btn_wel_pic = (By.XPATH, '//p[text()="图 片"]/../..')
    # 欢迎语网页按钮
    _btn_wel_web = (By.XPATH, '//p[text()="网 页"]/../..')
    # 欢迎语小程序按钮
    _btn_wel_mini = (By.XPATH, '//p[text()="小程序"]/../..')
    # 网页搜索输入框
    _input_search_web = (By.CSS_SELECTOR, '[placeholder="搜索素材"]')
    # 网页选择按钮
    _btn_select_web = (By.CSS_SELECTOR, '.waterFall .water-fall-item')
    # 网页选择按钮
    _btn_select_mini = (By.CSS_SELECTOR, 'div[aria-label="添加小程序消息"] div[class*="pic"] .waterFall>.water-fall-item')
    # 网页选择确定按钮
    _btn_web_sure = (By.CSS_SELECTOR, 'div[aria-label="添加网页消息"] div[class$="footer"] button:last-child')
    # 网页选择确定按钮
    _btn_mini_sure = (By.CSS_SELECTOR, 'div[aria-label="添加小程序消息"] div[class$="footer"] button:last-child')
    # 欢迎语输入框
    _input_welcomg = (By.CSS_SELECTOR, 'textarea')
    # 保存按钮
    _btn_save = (By.XPATH, '//span[text()="保存"]/..')

    # 组织架构
    # 输入框
    _input_client = (By.CSS_SELECTOR, 'input[placeholder$="关键词"]')
    # 结点
    _btn_client_node = (By.CSS_SELECTOR, '.custom-tree-node')
    # 外部确定
    _btn_confirm_outer = (By.XPATH, '(//span[text()="确 定"]/..)[3]')
    # 确定
    _btn_comfirm = (By.XPATH, '(//span[text()="确 定"]/..)[2]')

    # 活码详情页面
    # 网页名文本
    _text_web_info = (By.CSS_SELECTOR, '.webpage-info .title')
    # 图片元素
    _ele_pic_info = (By.CSS_SELECTOR, '.greetingImg')
    # 标签文本
    _texts_tag_list = (By.CSS_SELECTOR, 'span[class*="tag--info"]')
    # 欢迎语文本
    _text_wel_speech = (By.XPATH, '//div[text()="欢迎语："]/following-sibling::div')

    """元素定位层"""
    # 员工活码页面
    def get_btn_employee_code_page(self):
        return self.find_Element(self._btn_employee_code_page)
    # 新建员工活码
    def get_btn_add_employee_code(self):
        return self.find_Element(self._btn_add_employee_code)
    # 批量新建
    def get_btn_batch_create(self):
        return self.find_Element(self._btn_batch_create)
    # 删除
    def get_btn_delete(self):
        return self.find_Element(self._btn_delete)
    # 删除确认按钮
    def get_btn_delete_confirm(self):
        return self.find_Element(self._btn_delete_confirm)
    # 下载
    def get_btn_download(self):
        return self.find_Element(self._btn_download)
    # 批量下载
    def get_btn_batch_download(self):
        return self.find_Element(self._btn_batch_download)
    # 使用员工输入框
    def get_btn_user(self):
        return self.find_Element(self._btn_user)
    # 姓名输入框
    def get_input_name(self):
        return self.find_Element(self._input_name)
    # 手机号输入框
    def get_input_phone_number(self):
        return self.find_Element(self._input_phone_number)
    # 活动场景输入框
    def get_input_act_scene(self):
        return self.find_Element(self._input_act_scene)
    # 创建人输入框
    def get_input_creator(self):
        return self.find_Element(self._input_creator)
    # 创建时间输入框
    def get_input_creat_time1(self):
        return self.find_Element(self._input_creat_time1)
    def get_input_creat_time2(self):
        return self.find_Element(self._input_creat_time2)
    # 查询按钮
    def get_btn_search(self):
        return self.find_Element(self._btn_search)
    # 重置按钮
    def get_btn_reset(self):
        return self.find_Element(self._btn_reset)
    # 导出按钮
    def get_btn_export(self):
        return self.find_Element(self._btn_export)
    # 更多按钮
    def get_btn_more(self):
        return self.find_Element(self._btn_more)
    # 查看详情按钮
    def get_btn_check_detail(self):
        return self.find_Element(self._btn_check_detail)
    # 编辑按钮
    def get_btn_edit(self):
        return self.find_Element(self._btn_edit)
    # 删除按钮
    def get_btn_delete_code(self):
        return self.find_Element(self._btn_delete_code)
    # 删除确定按钮
    def get_btn_delete_code_sure(self):
        return self.find_Element(self._btn_delete_code_sure)
    # 使用员工文本
    def get_texts_user(self):
        return self.find_Elements(self._texts_user)
    # 显示额外文本按钮
    def get_show_more(self, index):
        return self.find_ele_replace('xpath', self._show_more, str(index+1))
    # 额外员工文本
    def get_texts_addition_user(self):
        return self.find_Elements(self._texts_addition_user)
    # 姓名文本
    def get_texts_name(self):
        return self.find_Elements(self._texts_name)
    # 手机号文本
    def get_texts_telnum(self):
        return self.find_Elements(self._texts_telnum)
    # 活动场景文本
    def get_texts_actscene(self):
        return self.find_Elements(self._texts_actscene)
    # 创建时间文本
    def get_texts_ctetime(self):
        return self.find_Elements(self._texts_ctetime)
    # 创建人文本
    def get_texts_creator(self):
        return self.find_Elements(self._texts_creator)
    # 总数量
    def get_text_total_num(self):
        return self.find_Element(self._text_total_num)
    # 页数
    def get_text_page_num(self):
        return self.find_Element(self._text_page_num)
    # 全选框
    def get_btn_check_box(self):
        return self.find_Element(self._btn_check_box)
    # 复制链接
    def get_btn_copy_link(self):
        return self.find_Element(self._btn_copy_link)
    # 页面容量
    def get_btn_page_size(self):
        return self.find_Element(self._btn_page_size)
    # 15条
    def get_btn_15_size(self):
        return self.find_Element(self._btn_15_size)

    # 新建界面
    # 批量单人活码
    def get_btn_type_batch_single(self):
        return self.find_Element(self._btn_type_batch_single)
    # 单人活码
    def get_btn_type_single(self):
        return self.find_Element(self._btn_type_single)
    # 多人活码
    def get_btn_type_multi(self):
        return self.find_Element(self._btn_type_multi)
    # 使用员工
    def get_btn_add_employer(self):
        return self.find_Element(self._btn_add_employer)
    # 活动场景输入框
    def get_input_activity_scene(self):
        return self.find_Element(self._input_activity_scene)
    # 高级设置
    def get_btn_advanced_design(self):
        return self.find_Element(self._btn_advanced_design)
    # 添加标签
    def get_btn_add_tags(self):
        return self.find_Element(self._btn_add_tags)
    # 选择前三个标签
    def get_btn_tags(self):
        return self.find_Element(self._btn_tags)
    def get_btn_tags2(self):
        return self.find_Element(self._btn_tags2)
    def get_btn_tags3(self):
        return self.find_Element(self._btn_tags3)
    # 确定标签按钮
    def get_btn_confirm(self):
        return self.find_Element(self._btn_confirm)
    # 添加欢迎语
    def get_btn_welcoming_speech_button(self):
        return self.find_Element(self._btn_welcoming_speech_button)
    # 欢迎语图片按钮
    def get_btn_wel_pic(self):
        return self.find_Element(self._btn_wel_pic)
    # 欢迎语网页按钮
    def get_btn_wel_web(self):
        return self.find_Element(self._btn_wel_web)
    # 欢迎语网页按钮
    def get_btn_wel_mini(self):
        return self.find_Element(self._btn_wel_mini)
    # 网页搜索输入框
    def get_input_search_web(self):
        return self.find_Element(self._input_search_web)
    # 网页选择按钮
    def get_btn_select_web(self):
        return self.find_Element(self._btn_select_web)
    # 小程序选择按钮
    def get_btn_select_mini(self):
        return self.find_Element(self._btn_select_mini)
    # 网页选择确定按钮
    def get_btn_mini_sure(self):
        return self.find_Element(self._btn_mini_sure)
    # 网页选择确定按钮
    def get_btn_web_sure(self):
        return self.find_Element(self._btn_web_sure)
    # 欢迎语输入框
    def get_input_welcomg(self):
        return self.find_Element(self._input_welcomg)
    # 保存按钮
    def get_btn_save(self):
        return self.find_Element(self._btn_save)
    # 翻页按钮
    def get_btn_next_page(self):
        return self.find_Element(self._btn_next_page)

    # 组织架构
    # 输入框
    def get_input_client(self):
        return self.find_Element(self._input_client)
    # 结点
    def get_btn_client_node(self):
        return self.find_Element(self._btn_client_node)
    def get_btn_confirm_outer(self):
        return self.find_Element(self._btn_confirm_outer)
    # 确定
    def get_btn_comfirm(self):
        return self.find_Element(self._btn_comfirm)

    # 活码详情页面
    # 网页名文本
    def get_text_web_info(self):
        return self.find_Element(self._text_web_info)
    # 图片元素
    def get_ele_pic_info(self):
        return self.find_Element(self._ele_pic_info)
    # 标签文本
    def get_texts_tag_list(self):
        return self.find_Elements(self._texts_tag_list)
    # 欢迎语文本
    def get_text_wel_speech(self):
        return self.find_Element(self._text_wel_speech)

    """元素操作层"""
    # 员工活码页面
    def click_btn_employee_code_page(self):
        return self.click_element(self.get_btn_employee_code_page())
    # 新建员工活码
    def click_btn_add_employee_code(self):
        return self.click_element(self.get_btn_add_employee_code())
    # 批量新建
    def click_btn_batch_create(self):
        return self.click_element(self.get_btn_batch_create())
    # 删除
    def click_btn_delete(self):
        return self.click_element(self.get_btn_delete())
    # 删除确认按钮
    def click_btn_delete_confirm(self):
        return self.click_element(self.get_btn_delete_confirm())
    # 下载
    def click_btn_download(self):
        return self.click_element(self.get_btn_download())
    # 批量下载
    def click_btn_batch_download(self):
        return self.click_element(self.get_btn_batch_download())
    # 使用员工输入框
    def click_btn_user(self):
        return self.click_element(self.get_btn_user())
    # 姓名输入框
    def sendkeys_input_name(self, value):
        return self.send_keys(self.get_input_name(), value)
    # 手机号输入框
    def sendkeys_input_phone_number(self, value):
        return self.send_keys(self.get_input_phone_number(), value)
    # 活动场景输入框
    def sendkeys_input_act_scene(self, value):
        return self.send_keys(self.get_input_act_scene(), value)
    # 创建人输入框
    def sendkeys_input_creator(self, value):
        return self.send_keys(self.get_input_creator(), value)
    # 创建时间输入框
    def sendkeys_input_creat_time1(self, value):
        return self.send_keys(self.get_input_creat_time1(), value)
    def sendkeys_input_creat_time2(self, value):
        return self.send_keys(self.get_input_creat_time2(), value)
    # 查询按钮
    def click_btn_search(self):
        return self.click_element(self.get_btn_search())
    # 重置按钮
    def click_btn_reset(self):
        return self.click_element(self.get_btn_reset())
    # 导出按钮
    def click_btn_export(self):
        return self.click_element(self.get_btn_export())
    # 更多按钮
    def click_btn_more(self):
        return self.click_element(self.get_btn_more())
    # 查看详情按钮
    def click_btn_check_detail(self):
        return self.click_element(self.get_btn_check_detail())
    # 编辑按钮
    def click_btn_edit(self):
        return self.click_element(self.get_btn_edit())
    # 删除按钮
    def click_btn_delete_code(self):
        return self.click_element(self.get_btn_delete_code())
    # 删除确定按钮
    def click_btn_delete_code_sure(self):
        return self.move_click_element(self.get_btn_delete_code_sure())
    # 使用员工文本
    def gettexts_texts_user(self):
        list = []
        for i in self.get_texts_user():
            list.append(i.get_attribute('openid'))
        return list
    # 显示额外文本按钮
    def move_to_show_more(self, index):
        return self.move_to_element(self.get_show_more(index))
    # 额外员工文本
    def gettexts_texts_addition_user(self):
        list = []
        for i in self.get_texts_addition_user():
            list.append(i.get_attribute('openid'))
        return list
    # 姓名文本
    def gettexts_texts_name(self):
        return self.get_elements_values(self.get_texts_name())
    # 手机号文本
    def gettexts_texts_telnum(self):
        return self.get_elements_values(self.get_texts_telnum())
    # 活动场景文本
    def gettexts_texts_actscene(self):
        return self.get_elements_values(self.get_texts_actscene())
    # 创建时间文本
    def gettexts_texts_ctetime(self):
        return self.get_elements_values(self.get_texts_ctetime())
    # 创建人文本
    def gettexts_texts_creator(self):
        return self.get_elements_values(self.get_texts_creator())
    # 总数量
    def gettexts_text_total_num(self):
        return self.get_element_value(self.get_text_total_num())
    # 页数
    def gettexts_text_page_num(self):
        return self.get_element_value(self.get_text_page_num())
    # 翻页按钮
    def click_btn_next_page(self):
        return self.click_element(self.get_btn_next_page())
    # 全选框
    def click_btn_check_box(self):
        return self.click_element(self.get_btn_check_box())
    # 复制链接
    def click_btn_copy_link(self):
        return self.click_element(self.get_btn_copy_link())
    # 页面容量
    def click_btn_page_size(self):
        return self.click_element(self.get_btn_page_size())
    # 15条
    def click_btn_15_size(self):
        return self.click_element(self.get_btn_15_size())

    # 新建界面
    # 批量单人活码
    def click_btn_type_batch_single(self):
        return self.click_element(self.get_btn_type_batch_single())
    # 单人活码
    def click_btn_type_single(self):
        return self.click_element(self.get_btn_type_single())
    # 多人活码
    def click_btn_type_multi(self):
        return self.click_element(self.get_btn_type_multi())
    # 使用员工
    def click_btn_add_employer(self):
        return self.click_element(self.get_btn_add_employer())
    # 活动场景输入框
    def sendkeys_input_activity_scene(self, value):
        return self.send_keys(self.get_input_activity_scene(), value)
    # 高级设置
    def click_btn_advanced_design(self):
        return self.click_element(self.get_btn_advanced_design())
    # 添加标签
    def click_btn_add_tags(self):
        return self.click_element(self.get_btn_add_tags())
    # 选择前三个标签
    def click_btn_tags(self):
        return self.click_element(self.get_btn_tags())
    def gettext_btn_tags(self):
        return self.get_element_value(self.get_btn_tags())
    def click_btn_tags2(self):
        return self.click_element(self.get_btn_tags2())
    def gettext_btn_tags2(self):
        return self.get_element_value(self.get_btn_tags2())
    def click_btn_tags3(self):
        return self.click_element(self.get_btn_tags3())
    # 确定标签按钮
    def click_btn_confirm(self):
        return self.click_element(self.get_btn_confirm())
    # 添加欢迎语
    def click_btn_welcoming_speech_button(self):
        return self.move_to_element(self.get_btn_welcoming_speech_button())
    # 欢迎语图片按钮
    def click_btn_wel_pic(self):
        return self.click_element(self.get_btn_wel_pic())
    # 欢迎语网页按钮
    def click_btn_wel_web(self):
        return self.click_element(self.get_btn_wel_web())
    # 欢迎语网页按钮
    def click_btn_wel_mini(self):
        return self.click_element(self.get_btn_wel_mini())
    # 网页搜索输入框
    def sendkeys_input_search_web(self, value):
        return self.send_keys(self.get_input_search_web(), value)
    # 网页选择按钮
    def click_btn_select_web(self):
        return self.move_click_element(self.get_btn_select_web())
    # 小程序选择按钮
    def click_btn_select_mini(self):
        return self.click_element(self.get_btn_select_mini())
    # 网页选择确定按钮
    def click_btn_mini_sure(self):
        return self.click_element(self.get_btn_mini_sure())
    # 网页选择确定按钮
    def click_btn_web_sure(self):
        return self.click_element(self.get_btn_web_sure())
    # 欢迎语输入框
    def sendkeys_input_welcomg(self, value):
        return self.send_keys(self.get_input_welcomg(), value)
    # 保存按钮
    def click_btn_save(self):
        return self.click_element(self.get_btn_save())

    # 组织架构
    # 输入框
    def sendkeys_input_client(self, value):
        return self.send_keys(self.get_input_client(), value)
    # 结点
    def click_btn_client_node(self):
        return self.click_element(self.get_btn_client_node())
    def click_btn_confirm_outer(self):
        return self.click_element(self.get_btn_confirm_outer())
    # 确定
    def click_btn_comfirm(self):
        return self.click_element(self.get_btn_comfirm())

    # 活码详情页面
    # 网页名文本
    def gettexts_text_web_info(self):
        return self.get_element_value(self.get_text_web_info())
    # 标签文本
    def gettexts_texts_tag_list(self):
        return self.get_elements_values(self.get_texts_tag_list())
    # 欢迎语文本
    def gettexts_text_wel_speech(self):
        return self.get_element_value(self.get_text_wel_speech())

    """业务层"""
    def switch_to_current(self):
        self.click_btn_employee_code_page()
        sleep(3)

    # 检查页面元素正常
    def check_page_data(self):
        sleep(4)
        response = self.get_response_data(
            '{}/v3/api-qrcode/guide_qr_code/staff/list'.format(base_page))
        totalnum = self.gettexts_text_total_num()
        pagenum = self.gettexts_text_page_num()
        try:
            self.assert_Equal(self.dict_get(response, 'total'), int(totalnum))
        except AssertionError as e:
            log().error('显示活码总数与接口数据不一致')
        try:
            self.assert_Equal(self.dict_get(response, 'totalPage'), int(pagenum))
        except AssertionError as e:
            log().error('总页数与接口数据不一致')
        names = self.gettexts_texts_name()
        if self.dict_get(response, 'total') > 10:
            try:
                self.assert_True(len(names) == 10, '验证{}==10'.format(len(names)))
            except AssertionError as e:
                log().error('页面展示的数量不足10条')
        else:
            try:
                self.assert_True(len(names) == self.dict_get(response, 'total'))
            except AssertionError as e:
                log().error('页面展示的数量与接口数据不一致')

    # 获取活码信息
    def get_msg(self, index):
        userlist = self.gettexts_texts_user()
        namelist = self.gettexts_texts_name()
        tellist = self.gettexts_texts_telnum()
        actlist = self.gettexts_texts_actscene()
        msg_list = []
        for i in range(len(userlist)):
            msg_list.append([userlist[i], namelist[i], tellist[i], actlist[i]])
        return msg_list[index-1]

    def search_by_user(self, user):
        self.click_btn_user()
        sleep(2)
        self.sendkeys_input_client(user)
        sleep(2)
        self.tap_keyboard('enter')
        self.tap_keyboard('enter')
        sleep(2)
        self.click_btn_client_node()
        sleep(2)
        self.click_btn_confirm_outer()
        sleep(2)
        self.click_btn_search()
        sleep(2)
        pagenum = self.gettexts_text_page_num()
        user_list = []
        for i in range(int(pagenum)):
            alist = self.gettexts_texts_user()
            print(alist)
            for i in alist:
                print(i)
                user_list.append(self.get_userid_info(i))
            print(user_list)
            for x in user_list:
                if x == user:
                    self.assert_Equal(x, user)
                else:
                    try:
                        self.get_show_more(user_list.index(x))
                    except TimeoutError:
                        self.assert_Equal(x, user)
                    else:
                        self.move_to_show_more(user_list.index(x))
                    sleep(2)
                    addi_list = []
                    alist = self.gettexts_texts_addition_user()
                    print(alist)
                    for i in alist:
                        print(i)
                        addi_list.append(self.get_userid_info(i))
                    print(addi_list)
                    self.check_exist_in_lists(user, addi_list)
            self.click_btn_next_page()
            sleep(3)

    def search_by_type(self, type, msg):
        if type == 'name':
            self.sendkeys_input_name(msg)
        elif type == 'tel':
            self.sendkeys_input_phone_number(msg)
        elif type == 'scene':
            self.sendkeys_input_act_scene(msg)
        elif type == 'creator':
            self.sendkeys_input_creator(msg)
        sleep(1)
        self.click_btn_search()
        sleep(2)
        pagenum = self.gettexts_text_page_num()
        for i in range(int(pagenum)):
            if type == 'name':
                name_list = self.gettexts_texts_name()
            elif type == 'tel':
                name_list = self.gettexts_texts_telnum()
            elif type == 'scene':
                name_list = self.gettexts_texts_actscene()
            elif type == 'creator':
                name_list = self.gettexts_texts_creator()
            else:
                log().error('未知搜索类型！')
                break
            for x in name_list:
                self.check_exist_in_lists(msg, x)
            self.click_btn_next_page()
            sleep(2)

    def search_by_create_time(self, ctime, etime):
        self.sendkeys_input_creat_time1(ctime)
        sleep(1)
        self.sendkeys_input_creat_time2(etime)
        sleep(1)
        self.click_btn_search()
        sleep(2)
        pagenum = self.gettexts_text_page_num()
        for i in range(int(pagenum)):
            time_list = self.gettexts_texts_ctetime()
            for date in time_list:
                times = (date.split(' '))[0]
                st = datetime.datetime.strptime(ctime, '%Y-%m-%d')
                et = datetime.datetime.strptime(etime, '%Y-%m-%d')
                nt = datetime.datetime.strptime(times, '%Y-%m-%d')
                self.assert_True(st <= nt <= et, '判断{} <= {} <= {}'.format(st, nt, et))
            self.click_btn_next_page()
            sleep(2)

    # 重置
    def reset_search(self, ctime, etime):
        sleep(2)
        total = self.gettexts_text_total_num()
        self.search_by_create_time(ctime, etime)
        sleep(2)
        curtotal = self.gettexts_text_total_num()
        self.assert_Not_Equal(total, curtotal,)
        self.click_btn_reset()
        sleep(2)
        self.assert_Equal(total, self.gettexts_text_total_num())

    # 批量新建
    def create_in_batch(self, *user):
        self.click_btn_batch_create()
        sleep(3)
        for i in user:
            self.sendkeys_input_client(i)
            sleep(1)
            self.tap_keyboard('enter')
            self.tap_keyboard('enter')
            sleep(2)
            self.click_btn_client_node()
            sleep(2)
        self.click_btn_confirm()
        sleep(6)
        # msg1 = self.get_msg(1)
        # msg2 = self.get_msg(2)
        # print('msg1' + str(msg1))
        # print('msg2' + str(msg2))
        # list1 = [msg2[0], msg1[0]]
        # list1.sort()
        # list2 = list(user)
        # list2.sort()
        # try:
        #     self.assert_Equal(list1, list2)
        #     self.assert_True(msg1[-1] == msg2[-1] == '批量生成的单人码',
        #                      '{} 与 {} 相等，为"批量生成的单人码"'.format(msg1[-1], msg2[-1]))
        # except Exception as e:
        #     try:
        #         self.check_exist_in_page('该员工已经创建')
        #     except AssertionError:
        #         log().error('发生错误，新建失败')
        #     else:
        #         log().error('员工活码已存在，创建失败')
        try:
            self.check_exist_in_page('批量新建成功')
        except:
            log().error('新建失败')
        else:
            self.delete_code()
            self.delete_code()

    # 选择单人
    def single_code(self, user):
        self.click_btn_type_single()
        sleep(2)
        self.click_btn_add_employer()
        sleep(2)
        self.sendkeys_input_client(user)
        sleep(1)
        self.tap_keyboard('enter')
        self.tap_keyboard('enter')
        sleep(2)
        self.click_btn_client_node()
        sleep(2)
        self.click_btn_comfirm()

    # 按type添加活码
    def add_code_type(self, stype, *user):
        if stype == 'batch':
            self.click_btn_type_batch_single()
        elif stype == 'multi':
            self.click_btn_type_multi()
        sleep(2)
        self.click_btn_add_employer()
        for i in user[0]:
            sleep(2)
            self.sendkeys_input_client(i)
            sleep(1)
            self.tap_keyboard('enter')
            self.tap_keyboard('enter')
            sleep(2)
            self.click_btn_client_node()
            sleep(1)
        sleep(2)
        self.click_btn_comfirm()

    # 单个删除
    def delete_code(self):
        self.click_btn_more()
        sleep(2)
        self.click_btn_delete_code()
        sleep(2)
        self.click_btn_delete_code_sure()
        sleep(1.5)
        self.check_exist_in_page('删除成功')

    # 批量删除
    def delete_code_in_batch(self, scene='自动化'):
        self.search_by_type('scene', scene)
        sleep(2)
        self.click_btn_page_size()
        sleep(2)
        self.click_btn_15_size()
        sleep(2)
        self.click_btn_check_box()
        sleep(1)
        self.click_btn_delete()
        sleep(2)
        self.click_btn_delete_confirm()
        sleep(2)
        self.check_exist_in_page('批量删除成功')

    # 添加活码
    def add_code(self, act_scene, welcome, msg_type, msg, code_type, *user):
        self.click_btn_add_employee_code()
        sleep(2)
        if len(user) == 1:
            self.single_code(user)
        if len(user) >= 2:
            self.add_code_type(code_type, user)
        sleep(2)
        self.sendkeys_input_activity_scene(act_scene)
        sleep(2)
        self.click_btn_advanced_design()
        sleep(2)
        self.click_btn_add_tags()
        sleep(2)
        a = self.gettext_btn_tags()
        self.click_btn_tags()
        b = self.gettext_btn_tags2()
        self.click_btn_tags2()
        taglist = [a, b]
        self.set_ini('client_code_page', 'taglist', ' '.join(taglist))
        sleep(2)
        self.click_btn_comfirm()
        sleep(2)
        self.sendkeys_input_welcomg(welcome)
        sleep(2)
        self.click_btn_welcoming_speech_button()
        sleep(1)
        if msg_type == 'pic':
            self.click_btn_wel_pic()
            sleep(2)
            mte_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)) + msg)
            self.tap_keyboard('shift')
            self.control_keyboard(mte_path)
            sleep(1)
            self.tap_keyboard('enter')
        elif msg_type == 'web':
            self.click_btn_wel_web()
            sleep(2)
            self.sendkeys_input_search_web(msg)
            sleep(2)
            self.tap_keyboard('enter')
            sleep(3)
            self.click_btn_select_web()
            sleep(1)
            self.click_btn_web_sure()
        elif msg_type == 'mini':
            self.click_btn_wel_mini()
            sleep(2)
            self.sendkeys_input_search_web(msg)
            sleep(2)
            self.tap_keyboard('enter')
            sleep(3)
            self.click_btn_select_mini()
            sleep(1)
            self.click_btn_mini_sure()
        sleep(3)
        self.click_btn_save()
        if code_type == "batch":
            sleep(4)
        else:
            sleep(1.5)
        sleep(1.5)
        try:
            self.assert_Equal(self.get_cur_url(), '{}/co/code/employee'.format(base_page))
        except AssertionError as e:
            log().error('未成功回退至员工活码页面，新建失败或未跳转')
            self.switch_to_current()
        except Exception as e:
            log().error('网址跳转判断出现了预料外的错误')
            self.switch_to_current()
        try:
            self.check_exist_in_page(act_scene)
        except AssertionError:
            log().error('未成功新建活码')
        except Exception:
            log().error('出现预料外的错误')

    # 查看详情
    def check_code_info(self, msglist):
        sleep(2)
        self.click_btn_more()
        sleep(2)
        self.click_btn_check_detail()
        sleep(3)
        data = self.get_response_data('{}/v3/api-qrcode/guide_qr_code/staff/detail?id='.format(base_page))
        lists = ['activeScenario', 'customGreeting', 'tagName', 'webTitle']
        x = 0
        for i in lists:
            a = self.dict_get(data, i)
            if type(a).__name__ == 'list':
                a.sort()
                msglist[x].sort()
            try:
                self.assert_Equal(a, msglist[x])
            except Exception as e:
                self.switch_to_current()
                sleep(2)
                raise e
            x += 1
            # print(info)
        # msglist[4].sort()
        # info[4].sort()
        # for i in range(6):
        #     self.assert_Equal(info[i], msglist[i])
        self.switch_to_current()
        try:
            self.assert_Equal(self.get_cur_url(), '{}/co/code/employee'.format(base_page))
        except AssertionError as e:
            log().error('未成功回退至员工活码页面')
            self.switch_to_current()
        except Exception as e:
            log().error('网址跳转判断出现了预料外的错误')
            self.switch_to_current()
        sleep(2)

    # 编辑活码
    def edit_code(self, scene, wel):
        sleep(2)
        self.click_btn_more()
        sleep(2)
        self.click_btn_edit()
        sleep(2)
        self.sendkeys_input_activity_scene(scene)
        sleep(1)
        self.sendkeys_input_welcomg(wel)
        sleep(2)
        self.click_btn_save()
        sleep(2)
        try:
            self.assert_Equal(self.get_cur_url(), '{}/co/code/employee'.format(base_page))
        except AssertionError as e:
            log().error('未成功回退至员工活码页面，新建失败或未跳转')
            self.switch_to_current()
        except Exception as e:
            log().error('网址跳转判断出现了预料外的错误')
            self.switch_to_current()
        self.check_exist_in_page('保存成功')
        lists = self.gettexts_texts_actscene()
        self.assert_Equal(lists[0], scene)

    # 复制链接
    def copy_link(self):
        sleep(2)
        self.click_btn_copy_link()
        sleep(2)
        # self.check_exist_in_page('复制成功')
        sleep(1.5)
        data = self.get_response_data('{}/v3/api-qrcode/guide_qr_code/common/get_url?id'.format(base_page))
        self.assert_Equal(self.dict_get(data, 'message'), 'success')
        self.assert_Equal(self.dict_get(data, 'success'), True)

    # 导出功能
    def export(self):
        fpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)) + '\\materials')
        directory_list = os.listdir(fpath)
        print(directory_list)
        for filename in directory_list:
            if filename.startswith('员工活码') and filename.endswith('.xlsx'):
                a = filename
                print(a)
                os.remove((fpath + '\\' + a))
            else:
               pass
        self.click_btn_export()
        sleep(10)
        a = []
        directory_list = os.listdir(fpath)
        print(directory_list)
        for filename in directory_list:
            print(filename)
            if filename.startswith('员工活码'):
                a = filename
            else:
                continue
        if not a:
            return
        lists = SwitchToExcel().read_file(path=(fpath + '\\' + a), sheetname='0', ranges='a2', type='down')
        # print(lists)
        num = self.gettexts_text_total_num()
        self.assert_Equal(int(num), len(lists))

    # 前后端集成
    def integrated_test(self):
        # msg = self.get_msg(1)
        # if msg[3] == actscene and msg[0] == user:
        #     self.click_btn_more()
        # else:
        #     self.search_by_type('scene', actscene)
        #     msg = self.get_msg(1)
        #     try:
        #         self.assert_Equal(msg[3], actscene, '经验证，{} 与 {} 相等'.format(msg[3], actscene))
        #     except AssertionError:
        #         log().error('未找到目标活码')
        #         return
        self.click_btn_more()
        sleep(2)
        self.click_btn_check_detail()
        sleep(3)
        wellist = []
        wellist.append(self.gettexts_text_web_info())
        wellist.append(self.gettexts_text_wel_speech())
        taglist = self.gettexts_texts_tag_list()
        dict1 = self.get_response_data('{}/v3/api-qrcode/guide_qr_code/common/get_url?id='.format(base_page))
        string1 = self.dict_get(dict1, 'data')
        str4 = "".join(string1)
        print(str4)
        print(wellist)
        print(taglist)
        self.test(link=str4,
                  msg=wellist,
                  tags=taglist)

    def test(self, link, msg, tags, receiver='Torres', sender='马越月'):
        wel = self.add_client(repr(link)[1:-1], len(msg))
        wel.sort()
        msg.sort()
        self.assert_Equal(wel, msg)
        chatlist, taglist = self.check_wwc_msg(receiver)
        chat = chatlist[-len(msg):]
        chat.sort()
        tags.sort()
        taglist.sort()
        self.assert_Equal(taglist, tags)
        AppBase().del_wwc(receiver)
        AppBase().del_wc_customer(sender)

    def check_wwc_msg(self, target):
        connect_device("Android:///?cap_method=JAVACAP&&touch_method=ADBTOUCH&&ori_method=ADBORI")
        poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        stop_app("com.tencent.wework")
        start_app('com.tencent.wework')
        sleep(5)
        while not poco(text=target):
            poco().swipe('up')
        poco(text=target).click()
        list1 = poco('com.tencent.wework:id/er2').children()
        chatlist = []
        for i in list1:
            if i.offspring('com.tencent.wework:id/ejx').exists():
                for x in i.offspring('com.tencent.wework:id/ejx'):
                    chatlist.append(x.get_text())
            if i.offspring('com.tencent.wework:id/ejd').exists():
                chatlist.append(i.offspring('com.tencent.wework:id/ejd').get_text())
            if i.offspring('com.tencent.wework:id/hss').exists():
                chatlist.append(i.offspring('com.tencent.wework:id/hss').get_text())
            else:
                continue
        poco('com.tencent.wework:id/hxm').click()
        poco('com.tencent.wework:id/ehs').click()
        list12 = poco('com.tencent.wework:id/bkn').children()
        taglist = []
        for i in list12:
            taglist.append(''.join(i.get_text()))
        stop_app('com.tencent.wework')
        return chatlist, taglist

    def add_client(self, site, count):
        connect_device("Android:///?cap_method=JAVACAP&&touch_method=ADBTOUCH&&ori_method=ADBORI")
        poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        android_info = Android().get_display_info()
        android_px = (android_info['width'], android_info['height'])
        stop_app("com.tencent.mm")
        start_app("com.tencent.mm")
        sleep(3)
        poco(textMatches='^微信.*$').wait_for_appearance()
        sleep(5)
        while not poco(text="文件传输助手"):
            poco.scroll(direction='vertical', percent=0.3, duration=1.0)
        poco(text="文件传输助手").click()
        poco("com.tencent.mm:id/al_").set_text(site)
        poco(text="发送").click()
        sleep(2)
        xx = AppBase().touch_click_xy(poco("com.tencent.mm:id/ala")[-1].get_position())
        touch([xx[0], xx[1]])
        sleep(3)
        poco.long_click(pos=(0.5, 0.5))
        sleep(5)
        path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)) + '\\materials\\pic\\try.png')
        touch(Template(path, target_pos=8, resolution=android_px))
        sleep(2)
        if poco(text="添加到通讯录").exists():
            poco(text="添加到通讯录").click()
        sleep(4)
        poco(text="发消息").click()
        sleep(10)
        welcome_text = []
        for i in range(-count, 0):
            if poco("com.tencent.mm:id/al4").offspring("com.tencent.mm:id/an3").child(
                    "android.widget.RelativeLayout")[i].offspring('com.tencent.mm:id/ala').exists():
                poco("com.tencent.mm:id/al4").offspring("com.tencent.mm:id/an3").child("android.widget.RelativeLayout")[
                i].offspring('com.tencent.mm:id/ala').long_click()
            elif poco("com.tencent.mm:id/al4").offspring("com.tencent.mm:id/an3").child("android.widget.RelativeLayout")[
                i].offspring('com.tencent.mm:id/pp').exists():
                poco("com.tencent.mm:id/al4").offspring("com.tencent.mm:id/an3").child("android.widget.RelativeLayout")[
                    i].offspring('com.tencent.mm:id/pp').long_click()
            path1 = os.path.abspath(os.path.dirname(os.path.dirname(__file__)) + '\\materials\\pic\\icon1.png')
            touch(Template(path1, resolution=android_px))
            welcome_text.append(poco("com.tencent.mm:id/dv0").get_text())  # 欢迎语引用
        text = []
        text1 = []
        for i in welcome_text:
            text.append((i.split('：'))[1:])
        for i in text:
            a = ''.join(i)
            if a.startswith('[链接]'):
                a = a.split('[链接]')
            text1.append(''.join(a))
        stop_app('com.tencent.mm')
        return text1
