from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from commons.base_page import BasePage
from time import sleep
from pykeyboard import PyKeyboard


class ChatToolbarPage(BasePage):
    """元素定位信息"""
    # 基础页面
    # 聊天工具栏跳转按钮
    _btn_chat_toolbar = (By.XPATH, '//li[text()="聊天工具栏"]')
    # 抓取素材数量
    _material_num = '//table[@class="el-table__body"]/tbody/tr[%s]/td[3]/div'
    # 抓取素材按钮
    _btn_catch_material = '//table[@class="el-table__body"]/tbody/tr[%s]/td[5]/div/button'
    # 启用按钮
    _btn_open_material = (By.XPATH, '//span[@class="el-switch__core"]')

    # 抓取素材窗口
    # 勾选框（激活）（文本、文件）
    _check_box_isactivate1 = (By.XPATH, '//div[@class="el-checkbox-group"]/label[@class="el-checkbox is-checked"]')
    # 勾选框（激活）（图片）
    _check_box_isactivate2 = (By.XPATH, '//div[@class="bottom clearfix"]/label[@class="el-checkbox is-checked"]')
    # 勾选框（激活）（网页、视频）
    _check_box_isactivate3 = (By.XPATH, '//div[@class="el-checkbox-group"]/div/label[@class="el-checkbox is-checked"]')
    # 翻页箭头
    _switch_page = (By.XPATH, '//i[@class="el-icon-arrow-right"]')
    # 页面数
    _page_num = (By.XPATH, '//div[@class="filter-right"]')
    # 确定按钮
    _btn_confirm = (By.XPATH, '//button/span[text()="确定"]')

    '''元素定位层'''
    # 基础页面
    # 获取聊天工具栏按钮
    def get_btn_chat_toolbar(self):
        return self.find_Element(self._btn_chat_toolbar)
    # 获取特定素材的抓取数量
    def get_material_num(self, index):
        path = self._material_num.replace('%s', str(index))
        way = (By.XPATH, path)
        return self.find_Element(way)
    # 获取抓取素材按钮
    def get_btn_catch_material(self, index):
        path = self._btn_catch_material.replace('%s', str(index))
        way = (By.XPATH, path)
        return self.find_Element(way)
    # 获取素材启用按钮
    def get_btn_open_material(self):
        return self.find_Elements(self._btn_open_material)

    # 抓取素材窗口
    # 获取勾选框（激活）（文本、文件）
    def get_check_box_isactivate1(self):
        try:
            return self.find_Elements(self._check_box_isactivate1)
        except TimeoutException:
            return None
    # 获取勾选框（激活）（图片）
    def get_check_box_isactivate2(self):
        try:
            return self.find_Elements(self._check_box_isactivate2)
        except TimeoutException:
            return None
    # 获取勾选框（激活）（网页、视频）
    def get_check_box_isactivate3(self):
        try:
            return self.find_Elements(self._check_box_isactivate3)
        except TimeoutException:
            return None
    # 获取翻页箭头
    def get_switch_page(self):
        return self.find_Element(self._switch_page)
    # 获取页面数元素
    def get_page_num(self):
        return self.find_Element(self._page_num)
    # 获取确定按钮
    def get_btn_confirm(self):
        return self.find_Element(self._btn_confirm)

    '''元素操作层'''
    # 基础页面
    # 点击跳转至聊天工具栏页面
    def click_btn_chat_toolbar(self):
        return self.click_element(self.get_btn_chat_toolbar())
    # 获取文本特定素材的抓取数量
    def gettext_material_num(self, index):
        return self.get_element_value(self.get_material_num(index))
    # 点击抓取素材按钮
    def click_btn_catch_material(self, index):
        return self.click_element(self.get_btn_catch_material(index))
    # 点击启用素材按钮
    def click_btn_open_material(self, ele):
        return self.move_click_element(ele)

    # 素材页面
    # 点击翻页箭头
    def click_switch_page(self):
        return self.move_click_element(self.get_switch_page())
    # 获取文本页面数量
    def gettext_page_num(self):
        return self.get_element_value(self.get_page_num())
    # 点击确定按钮
    def click_btn_confirm(self):
        return self.click_element(self.get_btn_confirm())

    '''业务层'''
    def switch_to_current(self):
        sleep(2)
        self.click_btn_chat_toolbar()
        sleep(3)

    def check_num(self):
        count = 1
        while count <= 5:
            cot = 0
            num1 = self.gettext_material_num(count)
            if int(num1) == 0:
                count += 1
                continue
            self.click_btn_catch_material(count)
            sleep(3)
            if count == 1 or count == 5:
                text = self.gettext_page_num()
                pagenum = text.split('/')
                num = int(pagenum[0])
                while num <= int(pagenum[1]):
                    if self.get_check_box_isactivate1() is not None:
                        cot += len(self.get_check_box_isactivate1())
                        self.click_switch_page()
                    elif self.get_check_box_isactivate1() is None:
                        self.click_switch_page()
                    sleep(2)
                    num += 1
                self.assert_Equal(str(num1), str(cot))
                self.click_btn_confirm()
            elif count == 2:
                text = self.gettext_page_num()
                pagenum = text.split('/')
                num = int(pagenum[0])
                while num <= int(pagenum[1]):
                    if self.get_check_box_isactivate2() is not None:
                        cot += len(self.get_check_box_isactivate2())
                        self.click_switch_page()
                    elif self.get_check_box_isactivate2() is None:
                        self.click_switch_page()
                    sleep(2)
                    num += 1
                self.assert_Equal(str(num1), str(cot))
                self.click_btn_confirm()
            elif count == 4 or count == 3:
                text = self.gettext_page_num()
                pagenum = text.split('/')
                num = int(pagenum[0])
                while num <= int(pagenum[1]):
                    if self.get_check_box_isactivate3() != 0:
                        cot += len(self.get_check_box_isactivate3())
                        self.click_switch_page()
                    elif self.get_check_box_isactivate3() is None:
                        self.click_switch_page()
                    sleep(2)
                    num += 1
                self.assert_Equal(str(num1), str(cot))
                self.click_btn_confirm()
            sleep(2)
            count += 1
        sleep(3)

    def check_btn_open(self):
        buttons = self.get_btn_open_material()
        sleep(3)
        for btn in buttons:
            self.click_btn_open_material(btn)
            sleep(2)
            self.check_exist_in_page("操作成功")
            sleep(2)
        for btn in buttons:
            self.click_btn_open_material(btn)
            sleep(2)
            self.check_exist_in_page("操作成功")
            sleep(2)

