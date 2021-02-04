from selenium.webdriver.common.by import By
from commons.base_page import BasePage
from time import sleep
from pykeyboard import PyKeyboard
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from PIL import Image
from airtest.core.android import Android
from airtest.core.api import *
from commons.log import log
from commons.App_base import AppBase


'''云晗编写'''
'''流失提醒'''
class LossRemind(BasePage):
    '''元素定位信息'''
    # 左侧流失提醒按键获取
    _btn_loss_remind = (By.XPATH,'//li[text()="流失提醒"]')
    # 客户名称输入框元素
    _input_customer_name = (By.XPATH,'//input[@placeholder="请输入"]')
    # 添加人的元素
    _btn_adder = (By.XPATH,'//label[text()="添加人"]/../div/div')
    # 添加标签的元素
    _btn_label = (By.XPATH,'//label[text()="标签"]/../div/div')
    # 查询按键的元素
    _btn_search = (By.XPATH,'//span[text()="查询"]')
    # 重置按键的元素
    _btn_reset = (By.XPATH,'//span[text()="重置"]')
    # 指定客户
    _specify_custom = '//table[@class="el-table__body"]/tbody/tr[%s]/td[4]'
    # 客户姓名表
    _clients_name = (By.XPATH, '//table[@class="el-table__body"]/tbody/tr/td[1]/div')
    # 客户添加人表
    _clients_adders = (By.XPATH, '//table[@class="el-table__body"]/tbody/tr/td[3]/div/div/span')
    # 下一页按钮的元素
    _btn_next = (By.XPATH, '//i[@class="el-icon el-icon-arrow-right"]')
    # 页面数的元素
    _pages_number = (By.XPATH, '//*[@class="el-pager"]/li')
    # 客户标签组
    _customs_tags = '//table[@class="el-table__body"]/tbody/tr[%s]/td[6]/div/span'
    # 获取客户数的元素
    _client_num = (By.XPATH, 'el-pagination__total')

    # 标签页元素
    _tag_group = '//div[@class="tagName" and text()="%s"]'
    _tags = '//li[@class="tag" and text()="%s"]'

    # 点击添加人后显示的元素
    _input_addname = (By.XPATH, '//input[@placeholder="请输入关键词"]')
    _adder = (By.CLASS_NAME, 'custom-tree-node')
    _btn_confirm = (By.XPATH, '//div[@class="el-dialog"]/div[3]/div/button[2]')

    # 客户详情页面
    _full_adders = (By.XPATH, '//div[@class="water-fall-item"]/div[5]/div[2]/div/span')
    _full_tags = (By.XPATH, '//span[@class="el-tag el-tag--info el-tag--small el-tag--light"]')

    '''元素定位层'''
    # 获取左侧流失提醒按键
    def get_btn_loss_remind(self):
        return self.find_Element(self._btn_loss_remind)
    # 获取客户名称输入框
    def get_input_customer_name(self):
        return self.find_Element(self._input_customer_name)
    # 获取添加人
    def get_btn_adder(self):
        return self.find_Element(self._btn_adder)
    # 获取标签
    def get_btn_lable(self):
        return self.find_Element(self._btn_label)
    # 获取查询
    def get_btn_search(self):
        return self.find_Element(self._btn_search)
    # 获取重置
    def get_btn_reset(self):
        return self.find_Element(self._btn_reset)
    # 获取客户列表名称
    def get_clients_names(self):
        return self.find_Elements(self._clients_name)
    # 获取客户添加人列表名称
    def get_clients_adders(self):
        return self.find_Elements(self._clients_adders)
    # 获取翻页按钮
    def get_btn_next(self):
        return self.find_Element(self._btn_next)
    # 获取页面数
    def get_pages_number(self):
        return self.find_Elements(self._pages_number)
    # 获取指定添加人
    def get_specify_client(self, num):
        pat = self._specify_custom.replace('%s', str(num))
        path = (By.XPATH, pat)
        return self.find_Element(path)
    # 获取客户标签组元素
    def get_clients_tags(self, n):
        path = self._customs_tags.replace('%s', str(n))
        a = (By.XPATH, path)
        return self.find_Elements(a)
    # 获取总客户数
    def get_total_clients_num(self):
        return self.find_Element(self._client_num)

    # 组织架构窗口
    # 获取客户名称输入框
    def get_input_addname(self):
        return self.find_Element(self._input_addname)
    # 获取添加人
    def get_adder(self):
        return self.find_Element(self._adder)
    # 获取确定按钮
    def get_btn_confirm(self):
        return self.find_Element(self._btn_confirm)

    # 客户详情页
    # 获取所有添加人
    def get_full_adders(self):
        return self.find_Elements(self._full_adders)
    # 获取所有标签
    def get_full_tags(self):
        return self.find_Elements(self._full_tags)

    '''元素操作层'''
    # 点击流失提醒按键
    def click_btn_loss_remind(self):
        return self.click_element(self.get_btn_loss_remind())
    # 点击客户名称输入框
    def sendkey_name(self,name):
        return self.send_keys(self.get_input_customer_name(),name)
    # 点击添加人
    def click_btn_adder(self):
        return self.click_element(self.get_btn_adder())
    # 点击标签
    def click_btn_label(self):
        return self.click_element(self.get_btn_lable())
    # 点击查询
    def click_btn_search(self):
        return self.click_element(self.get_btn_search())
    # 点击重置
    def click_btn_reset(self):
        return self.click_element(self.get_btn_reset())
    # 点击翻页按钮
    def click_btn_next(self):
        return self.click_element(self.get_btn_next())
    # 跳转至指定用户详情页
    def click_specify_client(self, num):
        return self.move_click_element(self.get_specify_client(num))
    # 获取客户总数量
    def gettext_total_clients_num(self):
        return self.get_element_value(self.get_total_clients_num())
        # 获取客户名称列表

    def gettexts_clients_names(self):
        return self.get_elements_values(self.get_clients_names())
        # 获取客户添加人列表

    def gettexts_clients_adders(self):
        return self.get_elements_values(self.get_clients_adders())
        # 获取特定标签组

    def get_specify_tag_group(self, tag):
        path = self._tag_group.replace('%s', str(tag))
        a = (By.XPATH, path)
        return self.find_Element(a)

    # 点击特定标签
    def get_specify_tag(self, tag):
        path = self._tags.replace('%s', str(tag))
        a = (By.XPATH, path)
        return self.find_Element(a)

    # 组织架构页面
    # 输入添加人
    def sendkey_addname(self, name):
        return self.send_keys(self.get_input_addname(), name)
    # 选择添加人
    def click_addername(self):
        return self.move_click_element(self.get_adder())
    # 点击确定
    def click_confirm(self):
        return self.click_element(self.get_btn_confirm())
    # 标签页面
    # 点击特定元素
    def click_specify_tag(self, tag):
        return self.move_click_element(self.get_specify_tag(tag))
    # 客户详情页
    # 获取所有添加人名称
    def gettext_full_adders(self):
        return self.get_elements_values(self.get_full_adders())
    # 获取所有标签内容
    def gettext_full_tags(self):
        return self.get_elements_values(self.get_full_tags())

    # 获取客户标签组数据
    def gettext_clients_tags(self, n):
        if not self.get_clients_tags(n) == 0:
            tag_groups = self.get_clients_tags(n)
            text = []
            for group in tag_groups:
                text.append(self.get_element_value(group))
            return text
        else:
            return ['']


    '''业务层'''
    def get_numbers(self):
        list = self.get_pages_number()
        return list[-1].text

    def get_clients_num(self):
        list = self.gettexts_clients_names()
        return len(list)

    def search_by_name(self, name):
        sleep(5)
        self.sendkey_name(name)
        self.click_btn_search()
        sleep(6)
        number = self.get_numbers()
        n = 1
        while n <= int(number):
            list = self.gettexts_clients_names()
            for text in list:
                stext = text.split("@")
                self.check_exist_in_lists(name, stext[0])
            sleep(2)
            self.click_btn_next()
            n = n + 1
        sleep(2)
        # self.click_reset()
        # self._back()
        sleep(5)

    def search_by_adder(self, name):
        sleep(4)
        self.click_btn_adder()
        sleep(2)
        self.sendkey_addname(name)
        k = PyKeyboard()
        k.tap_key(k.enter_key)
        sleep(3)
        self.click_addername()
        sleep(1)
        self.click_confirm()
        sleep(2)
        self.click_btn_search()
        sleep(5)
        number = self.get_numbers()
        n = 1
        m = 1
        while n <= int(number):
            list = self.gettexts_clients_adders()
            for text in list:
                if not (text == name):
                    self.click_specify_client(m)
                    sleep(3)
                    t = self.gettext_full_adders()
                    sleep(1)
                    self.check_exist_in_lists(name, t)
                    sleep(1)
                    self._back()
                    sleep(2)
                m += 1
                sleep(1)
            self.click_btn_next()
            sleep(1)
            n = n + 1
        sleep(2)
        # self.click_reset()
        # self._back()
        sleep(2)

    def search_by_tag(self, taggroup, tag):
        sleep(5)
        self.click_btn_label()
        sleep(3)
        self.scroll_screen(self.get_specify_tag_group(taggroup), -10)
        sleep(2)
        self.click_specify_tag(tag)
        sleep(2)
        self.click_confirm()
        sleep(2)
        self.click_btn_search()
        sleep(4)
        number = self.get_numbers()
        n = 1
        while n <= int(number):
            num = self.get_clients_num()
            count = 1
            # lists = self.gettext_clients_tags(count)
            while count <= num:
                lists = self.gettext_clients_tags(count)
                if not (tag in lists):
                    self.click_specify_client(count)
                    sleep(3)
                    t = self.gettext_full_tags()
                    self.check_exist_in_lists(tag, t)
                    sleep(2)
                    self._back()
                    sleep(2)
                count += 1
            self.click_btn_next()
            sleep(2)
            n += 1
        sleep(2)

    def reset(self, name):
        sleep(5)
        a = self.gettext_total_clients_num()
        self.sendkey_name(name)
        self.click_btn_search()
        sleep(6)
        # b = self.gettext_total_clients_num()
        self.click_btn_reset()
        sleep(3)
        c = self.gettext_total_clients_num()
        self.assert_Equal(a, c)
        sleep(1)

    def check_app_info(self, customer, staff):
        connect_device("Android:///?cap_method=JAVACAP&&touch_method=ADBTOUCH&&ori_method=ADBORI")
        poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        AppBase().del_wc_customer(staff)
        sleep(4)
        stop_app("com.tencent.wework")
        start_app('com.tencent.wework')
        sleep(5)
        while not poco(text=customer):
            poco().swipe('up')
        if not poco(text=customer).offspring('com.tencent.wework:id/g2q').exists():
            log().error('未收到流失提醒')
        poco(text=customer).click()
        if poco('com.tencent.wework:id/ejd')[-1].get_text() == '客户 「Torres」将您删除了，查看客户详情':
            log().info('经验证，流失提醒成功')
        else:
            tet = poco('com.tencent.wework:id/ejd')[-1].get_text()
            log().error('没有收到对应的流失提醒，最后一条为：', tet)
