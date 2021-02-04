from selenium.webdriver.common.by import By
from commons.base_page import BasePage
from time import sleep
from pykeyboard import PyKeyboard
import datetime, os
from commons.readfile import SwitchToExcel


class ClientGroupsPage(BasePage):
    """元素定位信息"""
    # 本页面元素
    # 客户管理tab
    _btn_client_manage_tab = (By.XPATH, '//span[text()="客户管理"]/..')
    # 客户群页面
    _btn_client_group_page = (By.XPATH, '//li[text()=" 客户群 "]')
    # 查询按钮
    _btn_search = (By.XPATH, '//span[text()="查 询"]/..')
    # 客户群名输入框
    _input_group_name = (By.XPATH, '//input[@placeholder="请输入"]')
    # 群主输入框
    _btn_select_group_master = (By.XPATH, '//span[text()="请选择"]/..')
    # 创建日期输入框（起始）
    _input_create_start_time = (By.XPATH, '//input[@placeholder="开始时间"]')
    # 更多筛选按钮
    _btn_more_filter = (By.CSS_SELECTOR, '.more_btn')
    # 创建日期输入框（结束）
    _input_create_end_time = (By.XPATH, '//input[@placeholder="结束时间"]')
    # 客户群名列表
    _texts_client_groups_names = (By.CSS_SELECTOR, 'tbody>tr>td:nth-child(2) .cell span')
    # 页面数
    _text_pages_number = (By.CSS_SELECTOR, '.el-pager li:last-child')
    # 下一页按钮
    _btn_next = (By.CLASS_NAME, 'btn-next')
    # 群主名列表
    _texts_master_name = (By.CSS_SELECTOR, 'td ww-open-data')
    # 创建日期列表
    _texts_create_time = (By.CSS_SELECTOR, 'tbody>tr>td:last-child .cell')
    # 导出列表
    _btn_export_groups_list = (By.XPATH, '//span[text()="导出列表"]/..')

    # 点击群主输入框后显示的元素
    # 群主搜索输入框
    _input_client = (By.XPATH, '//input[@placeholder="请输入关键词"]')
    # 员工节点
    _btn_client_node = (By.CLASS_NAME, 'custom-tree-node')
    # 群主选择确认按钮
    _btn_confirm = (By.XPATH, '//div[@class="el-dialog"]/div[3]/div/button[2]')

    '''元素定位层'''
    # 本页面元素
    # 客户管理tab
    def get_btn_client_manage_tab(self):
        return self.find_Element(self._btn_client_manage_tab)
    # 客户群页面
    def get_btn_client_group_page(self):
        return self.find_Element(self._btn_client_group_page)
    # 查询按钮
    def get_btn_search(self):
        return self.find_Element(self._btn_search)
    # 客户群名输入框
    def get_input_group_name(self):
        return self.find_Element(self._input_group_name)
    # 更多筛选按钮
    def get_btn_more_filter(self):
        return self.find_Element(self._btn_more_filter)
    # 群主输入框
    def get_btn_select_group_master(self):
        return self.find_Element(self._btn_select_group_master)
    # 创建日期输入框（起始）
    def get_input_create_start_time(self):
        return self.find_Element(self._input_create_start_time)
    # 创建日期输入框（结束）
    def get_input_create_end_time(self):
        return self.find_Element(self._input_create_end_time)
    # 客户群名列表
    def get_texts_client_groups_names(self):
        return self.find_Elements(self._texts_client_groups_names)
    # 页面数
    def get_text_pages_number(self):
        return self.find_Element(self._text_pages_number)
    # 下一页按钮
    def get_btn_next(self):
        return self.find_Element(self._btn_next)
    # 群主名列表
    def get_texts_master_name(self):
        return self.find_Elements(self._texts_master_name)
    # 创建日期列表
    def get_texts_create_time(self):
        return self.find_Elements(self._texts_create_time)
    # 导出列表
    def get_btn_export_groups_list(self):
        return self.find_Element(self._btn_export_groups_list)

    # 点击群主输入框后显示的元素
    # 群主搜索输入框
    def get_input_client(self):
        return self.find_Element(self._input_client)
    # 员工节点
    def get_btn_client_node(self):
        return self.find_Element(self._btn_client_node)
    # 群主选择确认按钮
    def get_btn_confirm(self):
        return self.find_Element(self._btn_confirm)

    '''元素操作层'''
    # 本页面元素
    # 客户管理tab
    def click_btn_client_manage_tab(self):
        return self.click_element(self.get_btn_client_manage_tab())
    # 客户群页面
    def click_btn_client_group_page(self):
        return self.click_element(self.get_btn_client_group_page())
    # 查询按钮
    def click_btn_search(self):
        return self.click_element(self.get_btn_search())
    # 客户群名输入框
    def sendkeys_input_group_name(self, value):
        return self.send_keys(self.get_input_group_name(), value)
    # 更多筛选按钮
    def click_btn_more_filter(self):
        return self.click_element(self.get_btn_more_filter())
    # 群主输入框
    def click_btn_select_group_master(self):
        return self.click_element(self.get_btn_select_group_master())
    # 创建日期输入框（起始）
    def sendkeys_input_create_start_time(self, value):
        return self.send_keys(self.get_input_create_start_time(), value)
    # 创建日期输入框（结束）
    def sendkeys_input_create_end_time(self, value):
        return self.send_keys(self.get_input_create_end_time(), value)
    # 客户群名列表
    def gettexts_texts_client_groups_names(self):
        return self.get_elements_values(self.get_texts_client_groups_names())
    # 页面数
    def gettexts_text_pages_number(self):
        return self.get_element_value(self.get_text_pages_number())
    # 下一页按钮
    def click_btn_next(self):
        return self.click_element(self.get_btn_next())
    # 群主名列表
    def gettexts_texts_master_name(self):
        lists = []
        for i in self.get_texts_master_name():
            lists.append(i.get_attribute('openid'))
        return lists
    # 创建日期列表
    def gettexts_texts_create_time(self):
        return self.get_elements_values(self.get_texts_create_time())
    # 导出列表
    def click_btn_export_groups_list(self):
        return self.click_element(self.get_btn_export_groups_list())

    # 点击群主输入框后显示的元素
    # 群主搜索输入框
    def sendkeys_input_client(self, value):
        return self.send_keys(self.get_input_client(), value)
    # 员工节点
    def click_btn_client_node(self):
        return self.click_element(self.get_btn_client_node())
    # 群主选择确认按钮
    def click_btn_confirm(self):
        return self.click_element(self.get_btn_confirm())

    '''业务层'''
    # 跳转至客户群页面
    def switch_to_current(self):
        self.click_btn_client_manage_tab()  # 跳转至客户管理tab
        sleep(1)
        self.click_btn_client_group_page()  # 进入客户页面
        sleep(3)

    # 将创建时间切片，只需要年月日
    def get_create_time_list_splited(self):
        list = self.gettexts_texts_create_time()
        time_list = []
        for time in list:
            splited = time.split(' ')
            time_list.append(splited[0])
        return time_list

    def search_by_name(self, group_name):
        self.sendkeys_input_group_name(group_name)
        sleep(2)
        self.click_btn_search()
        sleep(3)
        pages = self.gettexts_text_pages_number()
        m = 1

        if int(pages) <= 3:
            while m <= int(pages):
                name_list = self.gettexts_texts_client_groups_names()
                for name in name_list:
                    self.assert_True(group_name in name, '"{}"存在于"{}"中'.format(group_name, name))
                self.click_btn_next()
                sleep(2)
                m += 1
        else:
            while m <= 3:
                name_list = self.gettexts_texts_client_groups_names()
                for name in name_list:
                    self.assert_True(group_name in name, '"{}"存在于"{}"中'.format(group_name, name))
                self.click_btn_next()
                sleep(2)
                m += 1
        sleep(1)

    def search_by_master(self, master_name):
        self.click_btn_more_filter()
        sleep(1)
        self.click_btn_select_group_master()
        sleep(2)
        self.sendkeys_input_client(master_name)
        sleep(1)
        self.tap_keyboard('enter')
        sleep(2)
        self.click_btn_client_node()
        sleep(1)
        self.click_btn_confirm()
        sleep(2)
        self.click_btn_search()
        sleep(3)
        pages = self.gettexts_text_pages_number()
        m = 1
        list = []

        if int(pages) <= 3:
            while m <= int(pages):
                alist = self.gettexts_texts_master_name()
                print(alist)
                for i in alist:
                    print(i)
                    list.append(self.get_userid_info(i))
                print(list)
                for name in list:
                    self.assert_Equal(master_name, name)
                self.click_btn_next()
                sleep(2)
                m += 1
        else:
            while m <= 3:
                alist = self.gettexts_texts_master_name()
                print(alist)
                for i in alist:
                    print(i)
                    list.append(self.get_userid_info(i))
                print(list)
                for name in list:
                    self.assert_Equal(master_name, name)
                self.click_btn_next()
                sleep(2)
                m += 1
        sleep(1)

    def search_by_create_time(self, start_time, end_time):
        self.sendkeys_input_create_start_time(start_time)
        sleep(1)
        self.sendkeys_input_create_end_time(end_time)
        sleep(1)
        self.click_btn_search()
        sleep(3)
        pages = self.gettexts_text_pages_number()
        m = 1
        if int(pages) <= 3:
            while m <= int(pages):
                list = self.get_create_time_list_splited()
                for date in list:
                    st = datetime.datetime.strptime(start_time, '%Y-%m-%d')
                    et = datetime.datetime.strptime(end_time, '%Y-%m-%d')
                    nt = datetime.datetime.strptime(date, '%Y-%m-%d')
                    self.assert_True(st <= nt <= et)
                self.click_btn_next()
                sleep(2)
                m += 1
        else:
            while m <= 3:
                list = self.get_create_time_list_splited()
                for date in list:
                    st = datetime.datetime.strptime(start_time, '%Y-%m-%d')
                    et = datetime.datetime.strptime(end_time, '%Y-%m-%d')
                    nt = datetime.datetime.strptime(date, '%Y-%m-%d')
                    self.assert_True(st <= nt <= et)
                self.click_btn_next()
                sleep(2)
                m += 1
        sleep(1)

    # def reset(self, name):
    #     sleep(5)
    #     a = self.gettext_client_group_num()
    #     self.sendkeys_group_name_input(name)
    #     self.click_btn_search()
    #     sleep(6)
    #     # b = self.gettext_total_clients_num()
    #     self.click_btn_reset()
    #     sleep(3)
    #     c = self.gettext_client_group_num()
    #     self.assert_Equal(a, c)
    #     sleep(1)

    def export_groups_list(self):
        plist = os.path.abspath(os.path.dirname(os.path.dirname(__file__)) + '\\materials')
        print(plist)
        file_list = os.listdir(plist)
        print(file_list)
        for file in file_list:
            if file.startswith('客户群列表.xlsx'):
                os.remove((plist + '\\客户群列表.xlsx'))
        self.click_btn_export_groups_list()
        sleep(40)
        fpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)) + '\\materials\\客户群列表.xlsx')
        lists = SwitchToExcel().read_file(path=fpath, sheetname='0', ranges='a2', type='down')
        print(len(lists))
        num = self.gettext_client_group_num()
        self.assert_Equal(int(num), len(lists))

