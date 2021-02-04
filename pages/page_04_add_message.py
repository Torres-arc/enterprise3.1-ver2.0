from selenium.webdriver.common.by import By
from commons.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from time import sleep
from commons.App_base import *
from config.readConfig import MassHair

'''新增群发页面！！！'''


class AddmessagePage(BasePage):
    # 元素定位信息
    _btn_addmessage = (By.XPATH, '//li[text()="新增群发"]/..')
    # 发送范围
    _btn_select_target_client = (By.XPATH, '//span[text()="选择发送客户"]')
    # 全部客户
    _btn_all_clients = (By.XPATH, '//span[text]')
    # 按照条件筛选
    _btn_fliter = (By.XPATH, '//span[text()="按照条件筛选客户"]/preceding-sibling::span')
    # 筛选条件-添加人
    _btn_select_adder = (By.CSS_SELECTOR, '.select-user-box > div')
    # 添加人输入框
    _input_adder = (By.CSS_SELECTOR, '.el-col .el-input__inner')
    # 选择添加人
    _btn_adder_node = (By.CSS_SELECTOR, '.custom-tree-node')    # 选择添加人窗口的确认按钮
    _btn_sure_adder = (By.CSS_SELECTOR,
                       '.el-dialog__wrapper:nth-child(3) .el-dialog__footer:nth-child(3) button:last-child')
    # 选择发送客户的确认按钮
    _btn_select_sure = (By.CSS_SELECTOR, 'div[aria-label="选择发送客户"] .el-dialog__footer button:last-child')
    # 文本
    _btn_add_select_text = (By.CSS_SELECTOR, '#pane-text > .material-add-btn')
    _input_search_text = (By.CSS_SELECTOR, '#pane-text .filter-left > .el-input > .el-input__inner')
    _btn_select_text = (By.CSS_SELECTOR, ".radio .el-radio__inner")
    _btn_sure_text = (By.CSS_SELECTOR, ".material-dialog .el-button--primary")
    # 网页
    _btn_web_tab = (By.CSS_SELECTOR, "#tab-web > span")
    _btn_add_select_web = (By.CSS_SELECTOR, '#pane-web > .material-add-btn > div')
    _input_search_web = (By.CSS_SELECTOR, '#pane-web .filter-left > .el-input > .el-input__inner')
    _btn_select_web = (By.CSS_SELECTOR, 'div[aria-label="选取网页素材"] #pane-web .water-fall-item')
    _btn_sure_web = (By.CSS_SELECTOR, ".el-dialog__footer:nth-child(3) .el-button--primary")
    # 图片
    _btn_pic_tab = (By.CSS_SELECTOR, "#tab-picture > span")
    _btn_add_select_pic = (By.CSS_SELECTOR, '#pane-picture > .material-add-btn')
    _input_search_pic = (By.CSS_SELECTOR, '#pane-picture .filter-left > .el-input > .el-input__inner')
    _btn_select_pic = (By.CSS_SELECTOR, 'div[aria-label="选取图片素材"] #pane-picture div[class*="picture"] .water-fall-item')
    _btn_sure_pic = (By.CSS_SELECTOR, ".el-dialog__footer:nth-child(3) .el-button--primary")
    # 海报
    _btn_poster_tab = (By.CSS_SELECTOR, ".el-icon-picture-outline-round")
    _btn_add_select_poster = (By.CSS_SELECTOR, '#pane-poster > .material-add-btn > div')
    _input_search_poster = (By.CSS_SELECTOR, '#pane-poster .filter-left > .el-input > .el-input__inner')
    _btn_select_poster = (By.CSS_SELECTOR,
                          'div[aria-label="选取海报素材"] #pane-poster div[class*="picture-c"]:nth-child(4) .water-fall-item')
    _btn_sure_poster = (By.CSS_SELECTOR, ".el-dialog__footer:nth-child(3) .el-button--primary")
    # 小程序
    _btn_mini_tab = (By.CSS_SELECTOR, "#tab-miniprogram > span")
    _btn_add_select_mini = (By.CSS_SELECTOR, '#pane-miniprogram > .material-add-btn > div')
    _input_search_mini = (By.CSS_SELECTOR, '#pane-miniprogram .filter-left > .el-input > .el-input__inner')
    _btn_select_mini = (By.CSS_SELECTOR, 'div[aria-label="选取小程序素材"] #pane-miniprogram'
                                         ' div[class*="picture-c"]:nth-child(5) .water-fall-item')
    _btn_sure_mini = (By.CSS_SELECTOR, ".el-dialog__footer:nth-child(3) .el-button--primary")
    # 发送
    _btn_send = (By.CSS_SELECTOR, ".el-button--primary:nth-child(1)")
    # 发送客户群
    _btn_send_to_group = (By.CSS_SELECTOR, ".el-radio:nth-child(2) .el-radio__inner")
    # 发送范围--按群主选择客户群
    _btn_send_range = (By.CSS_SELECTOR, ".el-link--primary > .el-link--inner")

    '''元素定位层'''
    def get_btn_addmessage(self):
        return self.find_Element(self._btn_addmessage)
    # 发送范围
    def get_btn_select_target_client(self):
        return self.find_Element(self._btn_select_target_client)
    # 全部客户
    def get_btn_all_clients(self):
        return self.find_Element(self._btn_all_clients)
    # 按照条件筛选
    def get_btn_fliter(self):
        return self.find_Element(self._btn_fliter)
    # 筛选条件-添加人
    def get_btn_select_adder(self):
        return self.find_Element(self._btn_select_adder)
    # 添加人输入框
    def get_input_adder(self):
        return self.find_Element(self._input_adder)
    # 选择添加人
    def get_btn_adder_node(self):
        return self.find_Element(self._btn_adder_node)
    def get_btn_sure_adder(self):
        return self.find_Element(self._btn_sure_adder)
    # 选择发送客户的确认按钮
    def get_btn_select_sure(self):
        return self.find_Element(self._btn_select_sure)
    # 文本
    def get_btn_add_select_text(self):
        return self.find_Element(self._btn_add_select_text)
    def get_input_search_text(self):
        return self.find_Element(self._input_search_text)
    def get_btn_select_text(self):
        return self.find_Element(self._btn_select_text)
    def get_btn_sure_text(self):
        return self.find_Element(self._btn_sure_text)
    # 网页
    def get_btn_web_tab(self):
        return self.find_Element(self._btn_web_tab)
    def get_btn_add_select_web(self):
        return self.find_Element(self._btn_add_select_web)
    def get_input_search_web(self):
        return self.find_Element(self._input_search_web)
    def get_btn_select_web(self):
        return self.find_Element(self._btn_select_web)
    def get_btn_sure_web(self):
        return self.find_Element(self._btn_sure_web)
    # 图片
    def get_btn_pic_tab(self):
        return self.find_Element(self._btn_pic_tab)
    def get_btn_add_select_pic(self):
        return self.find_Element(self._btn_add_select_pic)
    def get_input_search_pic(self):
        return self.find_Element(self._input_search_pic)
    def get_btn_select_pic(self):
        return self.find_Element(self._btn_select_pic)
    def get_btn_sure_pic(self):
        return self.find_Element(self._btn_sure_pic)
    # 海报
    def get_btn_poster_tab(self):
        return self.find_Element(self._btn_poster_tab)
    def get_btn_add_select_poster(self):
        return self.find_Element(self._btn_add_select_poster)
    def get_input_search_poster(self):
        return self.find_Element(self._input_search_poster)
    def get_btn_select_poster(self):
        return self.find_Element(self._btn_select_poster)
    def get_btn_sure_poster(self):
        return self.find_Element(self._btn_sure_poster)
    # 小程序
    def get_btn_mini_tab(self):
        return self.find_Element(self._btn_mini_tab)
    def get_btn_add_select_mini(self):
        return self.find_Element(self._btn_add_select_mini)
    def get_input_search_mini(self):
        return self.find_Element(self._input_search_mini)
    def get_btn_select_mini(self):
        return self.find_Element(self._btn_select_mini)
    def get_btn_sure_mini(self):
        return self.find_Element(self._btn_sure_mini)
    # 发送
    def get_btn_send(self):
        return self.find_Element(self._btn_send)
    # 发送客户群
    def get_btn_send_to_group(self):
        return self.find_Element(self._btn_send_to_group)
    # 发送范围--按群主选择客户群
    def get_btn_send_range(self):
        return self.find_Element(self._btn_send_range)

    '''元素操作层'''

    # 元素定位信息
    def click_btn_addmessage(self):
        return self.move_click_element(self.get_btn_addmessage())
    # 发送范围
    def click_btn_select_target_client(self):
        return self.click_element(self.get_btn_select_target_client())
    # 全部客户
    def click_btn_all_clients(self):
        return self.click_element(self.get_btn_all_clients())
    # 按照条件筛选
    def click_btn_fliter(self):
        return self.click_element(self.get_btn_fliter())
    # 筛选条件-添加人
    def click_btn_select_adder(self):
        return self.click_element(self.get_btn_select_adder())
    # 添加人输入框
    def sendkeys_input_adder(self, value):
        return self.send_keys(self.get_input_adder(), value)
    # 选择添加人
    def click_btn_adder_node(self):
        return self.move_click_element(self.get_btn_adder_node())
    def click_btn_sure_adder(self):
        return self.click_element(self.get_btn_sure_adder())
    # 选择发送客户的确认按钮
    def click_btn_select_sure(self):
        return self.move_click_element(self.get_btn_select_sure())
    # 文本
    def click_btn_add_select_text(self):
        return self.click_element(self.get_btn_add_select_text())
    def sendkeys_input_search_text(self, value):
        return self.send_keys(self.get_input_search_text(), value)
    def click_btn_select_text(self):
        return self.click_element(self.get_btn_select_text())
    def click_btn_sure_text(self):
        return self.click_element(self.get_btn_sure_text())
    # 网页
    def click_btn_web_tab(self):
        return self.click_element(self.get_btn_web_tab())
    def click_btn_add_select_web(self):
        return self.click_element(self.get_btn_add_select_web())
    def sendkeys_input_search_web(self, value):
        return self.send_keys(self.get_input_search_web(), value)
    def click_btn_select_web(self):
        return self.click_element(self.get_btn_select_web())
    def click_btn_sure_web(self):
        return self.click_element(self.get_btn_sure_web())
    # 图片
    def click_btn_pic_tab(self):
        return self.click_element(self.get_btn_pic_tab())
    def click_btn_add_select_pic(self):
        return self.click_element(self.get_btn_add_select_pic())
    def sendkeys_input_search_pic(self, value):
        return self.send_keys(self.get_input_search_pic(), value)
    def click_btn_select_pic(self):
        return self.click_element(self.get_btn_select_pic())
    def click_btn_sure_pic(self):
        return self.click_element(self.get_btn_sure_pic())
    # 海报
    def click_btn_poster_tab(self):
        return self.click_element(self.get_btn_poster_tab())
    def click_btn_add_select_poster(self):
        return self.click_element(self.get_btn_add_select_poster())
    def sendkeys_input_search_poster(self, value):
        return self.send_keys(self.get_input_search_poster(), value)
    def click_btn_select_poster(self):
        return self.click_element(self.get_btn_select_poster())
    def click_btn_sure_poster(self):
        return self.click_element(self.get_btn_sure_poster())
    # 小程序
    def click_btn_mini_tab(self):
        return self.click_element(self.get_btn_mini_tab())
    def click_btn_add_select_mini(self):
        return self.click_element(self.get_btn_add_select_mini())
    def sendkeys_input_search_mini(self, value):
        return self.send_keys(self.get_input_search_mini(), value)
    def click_btn_select_mini(self):
        return self.click_element(self.get_btn_select_mini())
    def click_btn_sure_mini(self):
        return self.click_element(self.get_btn_sure_mini())
    # 发送
    def click_btn_send(self):
        return self.click_element(self.get_btn_send())
    # 发送客户群
    def click_btn_send_to_group(self):
        return self.click_element(self.get_btn_send_to_group())
    # 发送范围--按群主选择客户群
    def click_btn_send_range(self):
        return self.click_element(self.get_btn_send_range())

    '''业务层'''
    def switch_to_current(self):
        self.click_btn_addmessage()
        sleep(2)

    def send_message(self, ktype, mtype, msg, sender):
        sleep(2)
        if ktype == 'client':
            self.click_btn_select_target_client()
            sleep(2)
            self.click_btn_fliter()
            sleep(2)
            self.click_btn_select_adder()
        elif ktype == 'group':
            self.click_btn_send_to_group()
            sleep(2)
            self.click_btn_send_range()
        sleep(2)
        self.sendkeys_input_adder(sender)
        sleep(1)
        self.tap_keyboard('enter')
        self.tap_keyboard('enter')
        sleep(1)
        self.click_btn_adder_node()
        sleep(2)
        self.click_btn_sure_adder()
        sleep(2)
        self.click_btn_select_sure()
        sleep(2)
        if mtype == 'text':
            self.click_btn_add_select_text()
            sleep(2)
            self.sendkeys_input_search_text(msg)
            sleep(1)
            self.tap_keyboard('enter')
            sleep(2)
            self.click_btn_select_text()
            sleep(2)
            self.click_btn_sure_text()
        elif mtype == 'web':
            self.click_btn_web_tab()
            sleep(2)
            self.click_btn_add_select_web()
            sleep(2)
            self.sendkeys_input_search_web(msg)
            sleep(1)
            self.tap_keyboard('enter')
            sleep(2)
            self.click_btn_select_web()
            sleep(2)
            self.click_btn_sure_web()
        elif mtype == 'pic':
            self.click_btn_pic_tab()
            sleep(2)
            self.click_btn_add_select_pic()
            sleep(2)
            self.sendkeys_input_search_pic(msg)
            sleep(1)
            self.tap_keyboard('enter')
            sleep(2)
            self.click_btn_select_pic()
            sleep(2)
            self.click_btn_sure_pic()
        elif mtype == 'poster':
            self.click_btn_poster_tab()
            sleep(2)
            self.click_btn_add_select_poster()
            sleep(2)
            self.sendkeys_input_search_poster(msg)
            sleep(1)
            self.tap_keyboard('enter')
            sleep(2)
            self.click_btn_select_poster()
            sleep(2)
            self.click_btn_sure_poster()
        elif mtype == 'mini':
            self.click_btn_mini_tab()
            sleep(2)
            self.click_btn_add_select_mini()
            sleep(2)
            self.sendkeys_input_search_mini(msg)
            sleep(1)
            self.tap_keyboard('enter')
            sleep(2)
            self.click_btn_select_mini()
            sleep(2)
            self.click_btn_sure_mini()
        sleep(2)
        self.click_btn_send()
        sleep(3)
        self.switch_to_current()