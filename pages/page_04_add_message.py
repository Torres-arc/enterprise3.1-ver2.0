from selenium.webdriver.common.by import By
from commons.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from time import sleep
from commons.App_base import *
from config.readConfig import MassHair

'''新增群发页面！！！'''


class AddmessagePage(BasePage):
    """"元素定位信息"""
    # 客户营销tab
    _btn_client_marketing_tab = (By.XPATH, '//span[text()="客户营销"]/..')
    # 企业群发页面
    _btn_addmessage = (By.XPATH, '//li[text()=" 企业群发 "]')
    # 新建群发按钮
    _btn_create_msg = (By.XPATH, '//span[text()="新建企业群发"]/..')
    # 发送范围
    _btn_send_range = (By.XPATH, '//span[text()="发送给客户群"]/preceding-sibling::span')
    # 按群主选择客户群
    _btn_select_client_group = (By.XPATH, '//span[text()="按群主选择客户群"]/..')
    # 按照条件筛选
    _btn_filter = (By.XPATH, '//span[text()="按条件筛选客户"]/preceding-sibling::span')
    # 筛选条件-添加人
    _btn_select_adder = (By.CSS_SELECTOR, '.filter-pop>div button')
    # 添加人输入框
    _input_adder = (By.CSS_SELECTOR, '.el-col .el-input__inner')
    # 选择添加人
    _btn_adder_node = (By.CSS_SELECTOR, '.custom-tree-node')
    # 选择添加人窗口的确认按钮
    _btn_sure_adder = (By.CSS_SELECTOR, 'div[aria-label="选择添加人"] .el-dialog__footer button+button')
    # 从素材中心选取按钮
    _btn_select_from_material_center = (By.XPATH, '//span[text()="从素材中心选取"]/..')
    # 文本
    # 搜索
    _input_search_text = (By.CSS_SELECTOR, '#pane-text .filter-left > .el-input > .el-input__inner')
    # 单选框
    _btn_select_text = (By.CSS_SELECTOR, ".radio .el-radio__inner")
    # 确认按钮
    _btn_sure_text = (By.CSS_SELECTOR, ".material-dialog .el-button--primary")
    # 网页
    _btn_web_tab = (By.CSS_SELECTOR, '#tab-web')
    _input_search_web = (By.CSS_SELECTOR, '#pane-web .filter-left > .el-input > .el-input__inner')
    _btn_select_web = (By.CSS_SELECTOR, 'div[aria-label="选取网页素材"] #pane-web .water-fall-item')
    _btn_sure_web = (By.CSS_SELECTOR, ".el-dialog__footer:nth-child(3) .el-button--primary")
    # 图片
    _btn_pic_tab = (By.CSS_SELECTOR, "#tab-picture")
    _input_search_pic = (By.CSS_SELECTOR, '#pane-picture .filter-left > .el-input > .el-input__inner')
    _btn_select_pic = (By.CSS_SELECTOR, 'div[aria-label="选取图片素材"] #pane-picture div[class*="picture"] .water-fall-item')
    _btn_sure_pic = (By.CSS_SELECTOR, ".el-dialog__footer:nth-child(3) .el-button--primary")
    # 海报
    _btn_poster_tab = (By.CSS_SELECTOR, "#tab-poster")
    _input_search_poster = (By.CSS_SELECTOR, '#pane-poster .filter-left > .el-input > .el-input__inner')
    _btn_select_poster = (By.CSS_SELECTOR, 'div[aria-label="选取海报素材"] #pane-poster div[class*="picture-c"]:nth-child(4) .el-checkbox')
    _btn_sure_poster = (By.CSS_SELECTOR, ".el-dialog__footer:nth-child(3) .el-button--primary")
    # 小程序
    _btn_mini_tab = (By.CSS_SELECTOR, "#tab-miniprogram")
    _input_search_mini = (By.CSS_SELECTOR, '#pane-miniprogram .filter-left > .el-input > .el-input__inner')
    _btn_select_mini = (By.CSS_SELECTOR, 'div[aria-label="选取小程序素材"] #pane-miniprogram div[class*="picture-c"]:nth-child(5) .water-fall-item')
    _btn_sure_mini = (By.CSS_SELECTOR, ".el-dialog__footer:nth-child(3) .el-button--primary")
    # 发送
    _btn_send = (By.XPATH, '//span[text()="通知成员发送"]/..')

    '''元素定位层'''
    # 客户营销tab
    def get_btn_client_marketing_tab(self):
        return self.find_Element(self._btn_client_marketing_tab)
    # 企业群发页面
    def get_btn_addmessage(self):
        return self.find_Element(self._btn_addmessage)
    # 新建群发按钮
    def get_btn_create_msg(self):
        return self.find_Element(self._btn_create_msg)
    # 发送范围
    def get_btn_send_range(self):
        return self.find_Element(self._btn_send_range)
    # 按群主选择客户群
    def get_btn_select_client_group(self):
        return self.find_Element(self._btn_select_client_group)
    # 按照条件筛选
    def get_btn_filter(self):
        return self.find_Element(self._btn_filter)
    # 筛选条件-添加人
    def get_btn_select_adder(self):
        return self.find_Element(self._btn_select_adder)
    # 添加人输入框
    def get_input_adder(self):
        return self.find_Element(self._input_adder)
    # 选择添加人
    def get_btn_adder_node(self):
        return self.find_Element(self._btn_adder_node)
    # 选择添加人窗口的确认按钮
    def get_btn_sure_adder(self):
        return self.find_Element(self._btn_sure_adder)
    # 从素材中心选取按钮
    def get_btn_select_from_material_center(self):
        return self.find_Element(self._btn_select_from_material_center)

    # 文本
    # 搜索
    def get_input_search_text(self):
        return self.find_Element(self._input_search_text)
    # 单选框
    def get_btn_select_text(self):
        return self.find_Element(self._btn_select_text)
    # 确认按钮
    def get_btn_sure_text(self):
        return self.find_Element(self._btn_sure_text)

    # 网页
    def get_btn_web_tab(self):
        return self.find_Element(self._btn_web_tab)
    def get_input_search_web(self):
        return self.find_Element(self._input_search_web)
    def get_btn_select_web(self):
        return self.find_Element(self._btn_select_web)
    def get_btn_sure_web(self):
        return self.find_Element(self._btn_sure_web)

    # 图片
    def get_btn_pic_tab(self):
        return self.find_Element(self._btn_pic_tab)
    def get_input_search_pic(self):
        return self.find_Element(self._input_search_pic)
    def get_btn_select_pic(self):
        return self.find_Element(self._btn_select_pic)
    def get_btn_sure_pic(self):
        return self.find_Element(self._btn_sure_pic)

    # 海报
    def get_btn_poster_tab(self):
        return self.find_Element(self._btn_poster_tab)
    def get_input_search_poster(self):
        return self.find_Element(self._input_search_poster)
    def get_btn_select_poster(self):
        return self.find_Element(self._btn_select_poster)
    def get_btn_sure_poster(self):
        return self.find_Element(self._btn_sure_poster)

    # 小程序
    def get_btn_mini_tab(self):
        return self.find_Element(self._btn_mini_tab)
    def get_input_search_mini(self):
        return self.find_Element(self._input_search_mini)
    def get_btn_select_mini(self):
        return self.find_Element(self._btn_select_mini)
    def get_btn_sure_mini(self):
        return self.find_Element(self._btn_sure_mini)

    # 发送
    def get_btn_send(self):
        return self.find_Element(self._btn_send)

    '''元素操作层'''
    # 客户营销tab
    def click_btn_client_marketing_tab(self):
        return self.click_element(self.get_btn_client_marketing_tab())
    # 企业群发页面
    def click_btn_addmessage(self):
        return self.click_element(self.get_btn_addmessage())
    # 新建群发按钮
    def click_btn_create_msg(self):
        return self.click_element(self.get_btn_create_msg())
    # 发送范围
    def click_btn_send_range(self):
        return self.click_element(self.get_btn_send_range())
    # 按群主选择客户群
    def click_btn_select_client_group(self):
        return self.click_element(self.get_btn_select_client_group())
    # 按照条件筛选
    def click_btn_filter(self):
        return self.click_element(self.get_btn_filter())
    # 筛选条件-添加人
    def click_btn_select_adder(self):
        return self.click_element(self.get_btn_select_adder())
    # 添加人输入框
    def sendkeys_input_adder(self, value):
        return self.send_keys(self.get_input_adder(), value)
    # 选择添加人
    def click_btn_adder_node(self):
        return self.click_element(self.get_btn_adder_node())
    # 选择添加人窗口的确认按钮
    def click_btn_sure_adder(self):
        return self.click_element(self.get_btn_sure_adder())
    # 从素材中心选取按钮
    def click_btn_select_from_material_center(self):
        return self.click_element(self.get_btn_select_from_material_center())

    # 文本
    # 搜索
    def sendkeys_input_search_text(self, value):
        return self.send_keys(self.get_input_search_text(), value)
    # 单选框
    def click_btn_select_text(self):
        return self.click_element(self.get_btn_select_text())
    # 确认按钮
    def click_btn_sure_text(self):
        return self.click_element(self.get_btn_sure_text())

    # 网页
    def click_btn_web_tab(self):
        return self.click_element(self.get_btn_web_tab())
    def sendkeys_input_search_web(self, value):
        return self.send_keys(self.get_input_search_web(), value)
    def click_btn_select_web(self):
        return self.click_element(self.get_btn_select_web())
    def click_btn_sure_web(self):
        return self.click_element(self.get_btn_sure_web())

    # 图片
    def click_btn_pic_tab(self):
        return self.click_element(self.get_btn_pic_tab())
    def sendkeys_input_search_pic(self, value):
        return self.send_keys(self.get_input_search_pic(), value)
    def click_btn_select_pic(self):
        return self.click_element(self.get_btn_select_pic())
    def click_btn_sure_pic(self):
        return self.click_element(self.get_btn_sure_pic())

    # 海报
    def click_btn_poster_tab(self):
        return self.click_element(self.get_btn_poster_tab())
    def sendkeys_input_search_poster(self, value):
        return self.send_keys(self.get_input_search_poster(), value)
    def click_btn_select_poster(self):
        return self.click_element(self.get_btn_select_poster())
    def click_btn_sure_poster(self):
        return self.click_element(self.get_btn_sure_poster())

    # 小程序
    def click_btn_mini_tab(self):
        return self.click_element(self.get_btn_mini_tab())
    def sendkeys_input_search_mini(self, value):
        return self.send_keys(self.get_input_search_mini(), value)
    def click_btn_select_mini(self):
        return self.click_element(self.get_btn_select_mini())
    def click_btn_sure_mini(self):
        return self.click_element(self.get_btn_sure_mini())

    # 发送
    def click_btn_send(self):
        return self.click_element(self.get_btn_send())

    '''业务层'''
    def switch_to_current(self):
        self.click_btn_client_marketing_tab()
        sleep(2)
        self.click_btn_addmessage()
        sleep(2)

    def send_message(self, ktype, mtype, msg, sender):
        sleep(2)
        self.click_btn_create_msg()
        sleep(2)
        if ktype == 'client':
            self.click_btn_filter()
            sleep(2)
            self.click_btn_select_adder()
        elif ktype == 'group':
            self.click_btn_send_range()
            sleep(2)
            self.click_btn_select_client_group()
        sleep(2)
        self.sendkeys_input_adder(sender)
        sleep(1)
        self.tap_keyboard('enter')
        sleep(2)
        self.click_btn_adder_node()
        sleep(2)
        self.click_btn_sure_adder()
        sleep(2)
        self.click_btn_select_from_material_center()
        sleep(2)
        if mtype == 'text':
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