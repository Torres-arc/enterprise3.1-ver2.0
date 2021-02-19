from selenium.webdriver.common.by import By
from commons.base_page import BasePage
from unittest import TestCase
from time import sleep
from pykeyboard import PyKeyboard

'''群发记录页面'''


class sendRecord_page(BasePage):
    """元素定位信息"""

    # 客户营销tab
    _btn_client_marketing_tab = (By.XPATH, '//span[text()="客户营销"]/..')
    # 企业群发页面
    _btn_addmessage = (By.XPATH, '//li[text()=" 企业群发 "]')
    # 内容消息列表
    _texts_msg = (By.CSS_SELECTOR, "tbody>tr>td:nth-child(1)>div")
    # 创建开始日期搜索
    _input_search_creat_start_time = (By.CSS_SELECTOR, 'input[placeholder="开始时间"]')
    # 创建结束日期搜索
    _input_search_creat_end_time = (By.CSS_SELECTOR, 'input[placeholder="结束时间"]')
    # 内容搜索
    _input_search_msg = (By.CSS_SELECTOR, 'input[placeholder="请输入"]')
    # 查询
    _btn_serach = (By.XPATH, "//span[text()='查询']/..")
    # 创建日期列表
    _texts_create_time = (By.CSS_SELECTOR, "tbody>tr>td:nth-child(4)>div")
    # 页面数
    _text_page_num = (By.CSS_SELECTOR, '.el-pager li:last-child')
    # 翻页按钮
    _btn_next_page = (By.CSS_SELECTOR, '.btn-next')

    '''元素定位层'''

    # 群发记录
    def get_sendRecord(self):
        return self.find_Element(self._sendRecord)

    # 内容消息
    def get_text(self):
        return self.find_Element(self._text)

    # 群发类型
    def get_tpye(self):
        return self.find_Element(self._type)

    # 发送客户
    def get_sendcus(self):
        return self.find_Element(self._sendcus)

    # 查询按钮
    def get_searchBtn(self):
        return self.find_Element(self._serachBtn)

    # 查询后的列表
    def get_tr(self):
        return self.find_Elements(self._tr)

    # 查询后的内容
    def get_text1(self):
        return self.find_Elements(self._text1)

    # 开始时间
    def get_startTime(self):
        return self.find_Element(self._startTime)

    # 结束时间
    def get_endTime(self):
        return self.find_Element(self._endTime)

    # 查询后的时间
    def get_time1(self):
        return self.find_Element(self._time1)

    # 重置按钮
    def get_reset(self):
        return self.find_Element(self._reset)

    def get_totalnum(self):
        return self.find_Element(self._totalnum)

    '''元素操作层'''

    # 点击群发记录界面
    def click_sendRecord(self):
        return self.click_element(self.get_sendRecord())

    # 输入内容
    def sendkeys_text1(self, value):
        return self.send_keys(self.get_text(), value)

    # 选择群发类型
    def click_type(self):
        return self.click_element(self.get_tpye())

    # 选择发送客户
    def click_sendcus(self):
        return self.click_element(self.get_sendcus())

    def sendkeys_st(self, value):
        return self.send_keys(self.get_startTime(), value)

    def sendkeys_et(self, value):
        return self.send_keys(self.get_endTime(), value)

    # 点击查询
    def click_serachBtn(self):
        return self.click_element(self.get_searchBtn())

    # 点击重置
    def click_reset(self):
        return self.click_element(self.get_reset())

    # 获取数量
    def get_totalnum1(self):
        return self.get_element_value(self.get_totalnum())

    '''业务层'''

    # 通过消息内容查询，断言消息内容
    def searchBytext(self, info):
        self.click_sendRecord()
        sleep(2)
        self.sendkeys_text1(info)
        sleep(1)
        self.click_serachBtn()
        sleep(3)
        for e in self.get_text1():
            self.check_exist_in_lists(info, self.get_element_value(e))

    # 通过群发类型查询，断言群发类型
    def searchBytype(self):
        self.click_sendRecord()
        sleep(2)
        self.click_type()
        sleep(1)
        self.click_sendcus()
        sleep(2)
        self.click_serachBtn()
        sleep(4)
        for e in self.get_tr():
            self.check_exist_in_lists("发送客户", self.get_element_value(e))

    # 通过创建时间查询，断言创建时间
    def searchBytime(self, stime, etime):
        self.click_sendRecord()
        sleep(2)
        self.sendkeys_st(stime)
        self.sendkeys_et(etime)
        sleep(1)
        k = PyKeyboard()
        k.tap_key(k.enter_key)
        self.click_serachBtn()
        sleep(4)
        self.assert_Equal(stime, self.get_element_value(self.get_time1()).split(' ')[0])

    # 重置功能
    def reset(self, info):
        self.click_sendRecord()
        sleep(4)
        a = self.get_totalnum1()
        # print(a)
        self.sendkeys_text1(info)
        sleep(1)
        self.click_serachBtn()
        sleep(3)
        self.click_reset()
        sleep(4)
        b = self.get_totalnum1()
        # print(b)
        self.assert_Equal(a, b)
        sleep(1)
