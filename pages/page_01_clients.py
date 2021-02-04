from selenium.webdriver.common.by import By
from commons.base_page import BasePage
from time import sleep
# from pykeyboard import PyKeyboard
# from airtest.core.api import *
# from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from commons.readfile import *
from commons.log import log
from config.readConfig import *


class ClientPage(BasePage):
    """元素定位信息"""
    # 本页面元素
    # 客户管理tab
    _btn_client_manage_tab = (By.XPATH, '//span[text()="客户管理"]/..')
    # 客户页面
    _btn_client_page = (By.XPATH, '//li[text()=" 客户 "]')
    # 暂无数据显示
    _text_ele_empty_data = (By.CSS_SELECTOR, '.el-table__empty-text')
    # 姓名输入框
    _input_name = (By.CSS_SELECTOR, 'input[placeholder="请输入"]')
    # 更多筛选按钮
    _btn_more_filter = (By.CSS_SELECTOR, '.more_btn')
    # 添加人输入框
    _btn_select_adder = (By.XPATH, '//p[text()="添加人"]/following-sibling::div')
    # 标签输入框
    _btn_select_tag = (By.XPATH, '//p[text()="标签"]/following-sibling::div')
    # 查询按钮
    _btn_search = (By.XPATH, '//span[text()="查 询"]/..')
    # 提醒打标签按钮
    _btn_remind = (By.XPATH, '//span[text()="批量提醒打标签"]')
    # 指定客户
    _btn_specify_custom = 'tbody tr:nth-child({}) td:first-child div'
    # 客户姓名表
    _texts_clients_name = (By.CSS_SELECTOR, 'tbody tr td:first-child div')
    # 客户添加人表
    _texts_clients_adders = (By.CSS_SELECTOR, 'td ww-open-data')
    # 下一页按钮
    _btn_next = (By.CLASS_NAME, 'btn-next')
    # 页面数
    _text_pages_number = (By.CSS_SELECTOR, '.el-pager li:last-child')
    # 客户标签组
    _texts_customs_tags = 'tbody tr:nth-child({}) td:nth-child(3) div span[class*="tag"]'

    # 标签页元素
    _btn_tag_group = '//div[@class="tagName" and text()="{}"]'
    _btn_tags = '//li[@class="tag" and text()=" {} "]'

    # 组织架构弹窗
    _input_addname = (By.XPATH, '//input[@placeholder="请输入关键词"]')
    _btn_adder = (By.CLASS_NAME, 'custom-tree-node')
    _btn_confirm = (By.XPATH, '//div[@class="el-dialog"]/div[3]/div/button[2]')

    # 客户详情页面
    # 所有标签
    _texts_full_tags = (By.XPATH, '//span[@class="el-tag el-tag--info el-tag--light"]')

    '''元素定位层'''
    # 本页面元素
    # 客户管理tab
    def get_btn_client_manage_tab(self):
        return self.find_Element(self._btn_client_manage_tab)
    # 客户页面
    def get_btn_client_page(self):
        return self.find_Element(self._btn_client_page)
    # 暂无数据显示
    def get_text_ele_empty_data(self):
        return self.find_Element(self._text_ele_empty_data)
    # 姓名输入框
    def get_input_name(self):
        return self.find_Element(self._input_name)
    # 更多筛选按钮
    def get_btn_more_filter(self):
        return self.find_Element(self._btn_more_filter)
    # 添加人输入框
    def get_btn_select_adder(self):
        return self.find_Element(self._btn_select_adder)
    # 标签输入框
    def get_btn_select_tag(self):
        return self.find_Element(self._btn_select_tag)
    # 查询按钮
    def get_btn_search(self):
        return self.find_Element(self._btn_search)
    # 提醒打标签按钮
    def get_btn_remind(self):
        return self.find_Element(self._btn_remind)
    # 指定客户
    def get_btn_specify_custom(self, index):
        return self.find_Element((By.CSS_SELECTOR, self._btn_specify_custom.format(index)))
    # 客户姓名表
    def get_texts_clients_name(self):
        return self.find_Elements(self._texts_clients_name)
    # 客户添加人表
    def get_texts_clients_adders(self):
        return self.find_Elements(self._texts_clients_adders)
    # 下一页按钮
    def get_btn_next(self):
        return self.find_Element(self._btn_next)
    # 页面数
    def get_text_pages_number(self):
        return self.find_Element(self._text_pages_number)
    # 客户标签组
    def get_texts_customs_tags(self, index):
        return self.find_Elements((By.CSS_SELECTOR, self._texts_customs_tags.format(index)))

    # 标签页元素
    def get_btn_tag_group(self, text):
        return self.find_Element((By.XPATH, self._btn_tag_group.format(text)))
    def get_btn_tags(self, text):
        return self.find_Element((By.XPATH, self._btn_tags.format(text)))

    # 组织架构弹窗
    def get_input_addname(self):
        return self.find_Element(self._input_addname)
    def get_btn_adder(self):
        return self.find_Element(self._btn_adder)
    def get_btn_confirm(self):
        return self.find_Element(self._btn_confirm)

    # 客户详情页面
    # 所有标签
    def get_texts_full_tags(self):
        return self.find_Element(self._texts_full_tags)

    '''元素操作层'''

    # 本页面元素
    # 客户管理tab
    def click_btn_client_manage_tab(self):
        return self.click_element(self.get_btn_client_manage_tab())
    # 客户页面
    def click_btn_client_page(self):
        return self.click_element(self.get_btn_client_page())
    # 暂无数据显示
    def gettexts_text_ele_empty_data(self):
        return self.get_element_value(self.get_text_ele_empty_data())
    # 姓名输入框
    def sendkeys_input_name(self, value):
        return self.send_keys(self.get_input_name(), value)
    # 更多筛选按钮
    def click_btn_more_filter(self):
        return self.click_element(self.get_btn_more_filter())
    # 添加人输入框
    def click_btn_select_adder(self):
        return self.click_element(self.get_btn_select_adder())
    # 标签输入框
    def click_btn_select_tag(self):
        return self.click_element(self.get_btn_select_tag())
    # 查询按钮
    def click_btn_search(self):
        return self.click_element(self.get_btn_search())
    # 提醒打标签按钮
    def click_btn_remind(self):
        return self.click_element(self.get_btn_remind())
    # 指定客户
    def click_btn_specify_custom(self, index):
        return self.click_element(self.get_btn_specify_custom(index))
    # 客户姓名表
    def gettexts_texts_clients_name(self):
        return self.get_elements_values(self.get_texts_clients_name())
    # 客户添加人表
    def gettexts_texts_clients_adders(self):
        """由于员工数据是调用企微组件，无法直接获取；因此通过给到的openid，调用企微接口并进行数据匹配，获取姓名"""
        list = []
        for i in self.get_texts_clients_adders():
            list.append(i.get_attribute('openid'))
        return list
    # 下一页按钮
    def click_btn_next(self):
        return self.click_element(self.get_btn_next())
    # 页面数
    def gettexts_text_pages_number(self):
        return self.get_element_value(self.get_text_pages_number())
    # 客户标签组
    def gettexts_texts_customs_tags(self, index):
        return self.get_elements_values(self.get_texts_customs_tags(index))

    # 标签页元素
    def click_btn_tag_group(self, text):
        return self.click_element(self.get_btn_tag_group(text))
    def click_btn_tags(self, text):
        return self.click_element(self.get_btn_tags(text))

    # 组织架构弹窗
    def sendkeys_input_addname(self, value):
        return self.send_keys(self.get_input_addname(), value)
    def click_btn_adder(self):
        return self.click_element(self.get_btn_adder())
    def click_btn_confirm(self):
        return self.click_element(self.get_btn_confirm())

    # 客户详情页面
    # 所有标签
    def gettexts_texts_full_tags(self):
        return self.get_elements_values(self.get_texts_full_tags())

    '''业务层'''
    # 跳转至客户页面
    def switch_to_current(self):
        self.click_btn_client_manage_tab()  # 跳转至客户管理tab
        sleep(1)
        self.click_btn_client_page()  # 进入客户页面
        sleep(3)

    def search_by_name(self, name):
        self.sendkeys_input_name(name)  # 输入要搜索的客户姓名
        sleep(2)
        self.click_btn_search()
        sleep(2)
        number = self.gettexts_text_pages_number()
        n = 1

        # 这里是对查找页面数做了一个限制，如果搜索结果多于3页，则只验证前3页的数据符合要求
        if int(number) <= 3:
            # 进行逐页验证
            while n <= int(number):
                sleep(2)

                # 进行一个异常判断，接口数据是否正常获取
                try:
                    # 获取客户列表接口数据
                    res = self.get_response_data('{}/v3/customer-center/customer/getPageList'.format(base_page))
                    reslist = self.dict_get(res, 'name')
                except Exception as e:
                    log().error('未成功获取接口数据')
                    n += 1
                # 接口数据正常，验证ui层面
                else:
                    # 获取ui数据，并与接口数据进行比对
                    list = self.gettexts_texts_clients_name()
                    newlist = []
                    for i in list:
                        newlist.append((i.split(' @微')[0]))
                    if isinstance(reslist, str):
                        reslist = [reslist]
                    reslist.sort()
                    newlist.sort()
                    self.assert_Equal(reslist, newlist)

                    # 数据正确后，对数据是否符合搜索要求进行验证
                    for text in list:
                        stext = text.split("@")
                        try:
                            self.check_exist_in_lists(name, stext[0])
                        except Exception as e:
                            # ele = self.find_Element((By.XPATH, "//div[contains(text(), '{}')]".format(stext[0])))
                            # rect = self.locate_element(ele, zoom=1.25)
                            # self.GetScreen('客户列表', rect=rect)
                            raise e
                    sleep(2)
                    self.click_btn_next()
                    n = n + 1
        else:
            while n <= 3:
                sleep(5)
                try:
                    res = self.get_response_data(
                        '{}/v3/customer-center/customer/getPageList'.format(base_page))
                    reslist = self.dict_get(res, 'name')
                except Exception as e:
                    log().error('未成功获取接口数据')
                    n += 1
                else:
                    list = self.gettexts_texts_clients_name()
                    newlist = []
                    for i in list:
                        newlist.append((i.split(' @微')[0]))
                    reslist.sort()
                    newlist.sort()
                    self.assert_Equal(reslist, newlist)
                    for text in list:
                        stext = text.split("@")
                        try:
                            self.check_exist_in_lists(name, stext[0])
                        except:
                            ele = self.find_Element((By.XPATH, "//div[contains(text(), '{}')]".format(stext[0])))
                            rect = self.locate_element(ele, zoom=1.25)
                            self.GetScreen('客户列表', rect=rect)
                    sleep(2)
                    self.click_btn_next()
                    n = n + 1
        sleep(2)

    def search_by_adder(self, name):
        # 点击更多筛选
        self.click_btn_more_filter()
        sleep(1)
        # 打开组织机构弹窗
        self.click_btn_select_adder()
        sleep(2)
        self.sendkeys_input_addname(name)
        sleep(1)
        self.tap_keyboard('enter')
        sleep(2)
        self.click_btn_adder()
        sleep(2)
        self.click_btn_confirm()
        sleep(2)
        self.click_btn_search()
        sleep(2)
        number = self.gettexts_text_pages_number()
        n = 1
        m = 1
        list=[]

        # 搜索逻辑与之前类似
        if int(number) <= 3:
            while n <= int(number):
                alist = self.gettexts_texts_clients_adders()
                print(alist)
                for i in alist:
                    print(i)
                    list.append(self.get_userid_info(i))
                print(list)
                for text in list:
                    if not (text == name):
                        self.click_btn_specify_custom(m)
                        sleep(3)
                        t = self.gettexts_texts_clients_adders()
                        sleep(1)
                        self.check_exist_in_lists(name, t)
                        self.GetScreen('查看添加人列表')
                        sleep(1)
                        self._back()
                        sleep(2)
                    m += 1
                    sleep(1)
                self.click_btn_next()
                sleep(1)
                n = n + 1
        else:
            while n <= 3:
                alist = self.gettexts_texts_clients_adders()
                for i in alist:
                    list.append(self.get_userid_info(i))
                print(list)
                for text in list:
                    if not (text == name):
                        self.click_btn_specify_custom(m)
                        sleep(3)
                        t = self.gettexts_texts_clients_adders()
                        sleep(1)
                        try:
                            self.check_exist_in_lists(name, t)
                        except Exception:
                            self.GetScreen('查看添加人列表')
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
        self.click_btn_select_tag()
        sleep(3)
        self.scroll_screen(self.get_btn_tag_group(taggroup), -10)
        sleep(2)
        self.click_btn_tags(tag)
        sleep(2)
        self.click_btn_confirm()
        sleep(2)
        self.click_btn_search()
        sleep(2)
        number = self.gettexts_text_pages_number()
        n = 1
        if int(number) <= 3:
            while n <= int(number):
                num = len(self.gettexts_texts_clients_name())
                count = 1
                while count <= num:
                    lists = self.gettexts_texts_customs_tags(count)
                    if not(tag in lists):
                        self.click_btn_specify_custom(count)
                        sleep(3)
                        t = self.gettexts_texts_full_tags()
                        try:
                            self.check_exist_in_lists(tag, t)
                        except:
                            self.GetScreen('查看标签')
                        sleep(2)
                        self._back()
                        sleep(2)
                    count += 1
                self.click_btn_next()
                sleep(2)
                n += 1
        else:
            while n <= 3:
                num = len(self.gettexts_texts_clients_name())
                count = 1
                # lists = self.gettext_clients_tags(count)
                while count <= num:
                    lists = self.gettexts_texts_customs_tags(count)
                    if not(tag in lists):
                        self.click_btn_specify_custom(count)
                        sleep(3)
                        t = self.gettexts_texts_full_tags()
                        try:
                            self.check_exist_in_lists(tag, t)
                        except:
                            print('目标标签{}不在{}内'.format(tag, t))
                            self.GetScreen('查看标签')
                        sleep(2)
                        self._back()
                        sleep(2)
                    count += 1
                self.click_btn_next()
                sleep(2)
                n += 1
        sleep(2)

    # 搜索重置功能
    # def reset(self, name):
    #     sleep(5)
    #     a = self.gettext_total_clients_num()
    #     self.sendkey_name(name)
    #     self.click_search()
    #     sleep(6)
    #     # b = self.gettext_total_clients_num()
    #     self.click_reset()
    #     sleep(3)
    #     c = self.gettext_total_clients_num()
    #     self.assert_Equal(a, c)
    #     sleep(1)

    # 批量提醒打标签功能
    # def remind_tags(self, adder):
    #     sleep(5)
    #     self.click_adder()
    #     sleep(2)
    #     self.sendkey_addname(adder)
    #     k = PyKeyboard()
    #     k.tap_key(k.enter_key)
    #     sleep(3)
    #     self.click_addername()
    #     sleep(1)
    #     self.click_confirm()
    #     sleep(2)
    #     self.click_search()
    #     sleep(5)
    #     num = self.get_clients_num()
    #     name_list = self.gettexts_clients_names()
    #     nlist = []
    #     for i in name_list:
    #         nlist.append((i.split(' @'))[0])
    #     self.click_check_box()
    #     self.click_remind()
    #     sleep(2)
    #     # self.click_chat_app()
    #     # sleep(1)
    #     # self.click_btn_sure()
    #     # sleep(1.5)
    #     self.check_exist_in_page("提醒成功")
    #     sleep(3)
    #     text = self.get_app_msg(num)
    #     print(text)
    #     text.sort()
    #     nlist.sort()
    #     self.assert_Equal(nlist, text)

    # def get_app_msg(self, num):
    #     connect_device("Android:///?cap_method=ADBCAP&&touch_method=ADBTOUCH&&ori_method=ADBORI")
    #     poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    #     stop_app('com.tencent.wework')
    #     start_app('com.tencent.wework')
    #     # poco(text="其他企业").click()
    #     # if not poco(text="微盛企微管家").parent().sibling('com.tencent.wework:id/bim').exists():
    #     #     poco(text="江苏微盛网络科技有限公司").click()
    #     # else:
    #     #     poco('com.tencent.wework:id/hxb').click()
    #     sleep(8)
    #     while not poco(text='客户运营'):
    #         poco().swipe('up')
    #     if poco(text="客户运营").parent().parent().offspring('com.tencent.wework:id/g2q').exists():
    #         poco(text="客户运营").click()
    #     else:
    #         print('未收到提醒')
    #         log().warning('未收到打标签提醒')
    #         return []
    #     lists = poco('com.tencent.wework:id/ejd')
    #     tlist = []
    #     for i in lists:
    #         tlist.append((i.get_text())[7:-4])
    #     # for i in chatlist[-1][1:]:
    #     #     texst.append(i[7:-4])
    #     return tlist[-num:]
    #
    # 导出列表
    # def export_clients_list(self):
    #     plist = os.path.abspath(os.path.dirname(os.path.dirname(__file__)) + '\\materials')
    #     print(plist)
    #     file_list = os.listdir(plist)
    #     print(file_list)
    #     for file in file_list:
    #         if file.startswith('客户列表.xlsx'):
    #             os.remove((plist+'\\客户列表.xlsx'))
    #     self.click_btn_export_list()
    #     sleep(10)
    #     fpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)) + '\\materials\\客户列表.xlsx')
    #     lists = SwitchToExcel().read_file(path=fpath, sheetname='0', ranges='a2', type='down')
    #     list1 = list(set(lists))
    #     num = self.gettext_total_clients_num()
    #     self.assert_Equal(int(num), len(list1))










