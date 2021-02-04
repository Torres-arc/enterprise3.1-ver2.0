from selenium.webdriver.common.by import By
from commons.base_page import BasePage
from time import sleep
from pykeyboard import PyKeyboard

'''红包记录查询'''
class Redrecord(BasePage):
    # 元素定位信息
    # 基础页面
    # 左侧红包记录查询按键获取
    _btn_red_record = (By.XPATH,'//li[text()="红包记录查询"]')
    #发红包人获取全部
    _select_send_man = (By.XPATH,'//*[@id="app"]/section/section/section/main/div/div[1]/div/div/form/div[1]/div/div/div/div/div/input')
    #发红包人选择云晗
    _select_yunhan = (By.XPATH,'//li[@class="el-select-dropdown__item hover"]/div/span')
    #点击查询
    _btn_search = (By.XPATH,'//*[@id="app"]/section/section/section/main/div/div[1]/div/div/form/div[3]/div/button/span')

    '''元素定位层'''
    # 基础页面
    # 获取红包记录查询按钮
    def get_btn_red_record(self):
        return self.find_Element(self._btn_red_record)

    # 获取根据发包人选择下拉框
    def get_select_send_man(self):
        return self.find_Element(self._select_send_man)

    # 发红包人选择云晗
    def get_select_yunhan(self):
        return self.find_Element(self._select_yunhan)

    # 点击查询
    def get_btn_search(self):
        return self.find_Element(self._btn_search)

    '''元素操作层'''
    # 基础页面
    # 点击红包记录查询按钮
    def click_btn_red_record(self):
        return self.click_element(self.get_btn_red_record())

    # 点击取根据发包人选择下拉框
    def click_select_yunhan(self):
        return self.click_element(self.get_select_yunhan())

    # 发红包人选择云晗
    def click_select_send_man(self):
        return self.click_element(self.get_select_send_man())

    # 点击查询
    def click_btn_search(self):
        return self.click_element(self.get_btn_search())

    # '''元素操作并进行封装'''
    # # 获取红包记录查询按钮
    # def click_btn_red_record(self):
    #     self.find_element(self._btn_red_record).click()
    #
    # # 获取根据发包人选择下拉框
    # def click_select_send_man(self):
    #     self.find_element(self._select_send_man).click()
    #
    # # 发红包人选择云晗
    # def click_select_yunhan(self):
    #     self.find_element(self._select_yunhan).click()
    #
    # # 点击查询
    # def click_btn_search(self):
    #     self.find_element(self._btn_search).click()


    '''业务层'''
    def search_send_man(self):
        # sleep(2)
        # #拖动滚动条至底部
        # self.scroll_screen(self.get_btn_red_record(), 5)
        # self.click_btn_red_record()
        # sleep(3)
        self.click_select_send_man()
        sleep(3)
        self.click_select_yunhan()
        sleep(3)
        self.click_btn_search()
        sleep(3)