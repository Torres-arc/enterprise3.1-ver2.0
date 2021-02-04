from selenium.webdriver.common.by import By
from commons.base_page import BasePage
from time import sleep
from pykeyboard import PyKeyboard
from commons.log import log
import datetime


class CircleOfFriendsPage(BasePage):
    """元素定位信息"""
    # 朋友圈页面
    _btn_circle_friends = (By.XPATH, '//li[text()="朋友圈"]')
    # 关键词输入框
    _input_key_words = (By.CSS_SELECTOR, 'input[placeholder="请输入关键词"]')
    # 发布时间输入框1
    _input_release_time1 = (By.CSS_SELECTOR, 'input[placeholder="开始时间"]')
    # 发布时间输入框2
    _input_release_time2 = (By.CSS_SELECTOR, 'input[placeholder="结束时间"]')
    # 查询按钮
    _btn_search = (By.XPATH, '//span[text()="查询"]/..')
    # 发布动态按钮
    _btn_release_news = (By.XPATH, '//span[text()="发布动态"]/..')
    # 指定编辑按钮
    _btn_edit = ('xpath', '//table[@class="el-table__body"]/tbody/tr[%s]/td[5]/div/button[1]')
    # 指定删除按钮
    _btn_delete = ('xpath', '//table[@class="el-table__body"]/tbody/tr[%s]/td[5]/div/button[2]')
    # 页码
    _page_num = (By.CSS_SELECTOR, 'ul.el-pager :last-child')
    # 下一页按钮
    _btn_next_page = (By.CSS_SELECTOR, 'button.btn-next')
    # 所选成员列表
    _list_selected_member = (By.CSS_SELECTOR, 'div[class="el-tooltip cell item"]')
    # 发布内容列表
    _list_release_text = (By.CSS_SELECTOR, 'div[class="cell el-tooltip"]')
    # 发布时间列表
    _list_release_time = (By.CSS_SELECTOR, 'tbody tr :nth-child(4)>div.cell')
    # 确认按钮
    _btn_confirm = (By.CSS_SELECTOR, 'div.el-message-box__btns :nth-child(2)')

    # 发布动态页面
    # 选择员工按钮
    _btn_select_staff = (By.XPATH, '//span[text()="选择"]/..')
    # 员工输入框
    _input_staff = (By.CSS_SELECTOR, 'input[placeholder="请输入关键词"]')
    # 员工节点
    _node_staff = (By.CSS_SELECTOR, 'span.custom-tree-node')
    # 员工确定按钮
    _btn_confirm_staff = (By.CSS_SELECTOR, 'div.dialog-footer :nth-child(2)')
    # 添加素材按钮
    _btn_add_material = (By.CSS_SELECTOR, 'div.material-add-btn i')
    # 文本输入框
    _input_text = (By.CSS_SELECTOR, 'textarea[placeholder]')
    # 搜索素材输入框
    _input_search_material = (By.CSS_SELECTOR, 'input[placeholder="搜索素材"]')
    # 素材选择按钮
    _btn_select_material = (By.CSS_SELECTOR, 'span.el-radio__inner')
    # 素材确定按钮
    _btn_confirm_material = (By.CSS_SELECTOR, 'span.dialog-footer :nth-child(2)')
    # 提交按钮
    _btn_commit = (By.XPATH, '//span[text()="提 交"]/..')

    """元素定位层"""
    # 朋友圈页面
    def get_btn_circle_friends(self):
        return self.find_Element(self._btn_circle_friends)
    # 关键词输入框
    def get_input_key_words(self):
        return self.find_Element(self._input_key_words)
    # 发布时间输入框1
    def get_input_release_time1(self):
        return self.find_Element(self._input_release_time1)
    # 发布时间输入框2
    def get_input_release_time2(self):
        return self.find_Element(self._input_release_time2)
    # 查询按钮
    def get_btn_search(self):
        return self.find_Element(self._btn_search)
    # 发布动态按钮
    def get_btn_release_news(self):
        return self.find_Element(self._btn_release_news)
    # 指定编辑按钮
    def get_btn_edit(self, index):
        return self.find_ele_replace(self._btn_edit[0], self._btn_edit[1], str(index))
    # 指定删除按钮
    def get_btn_delete(self, index):
        return self.find_ele_replace(self._btn_delete[0], self._btn_delete[1], str(index))
    # 页码
    def get_page_num(self):
        return self.find_Element(self._page_num)
    # 下一页按钮
    def get_btn_next_page(self):
        return self.find_Element(self._btn_next_page)
    # 所选成员列表
    def get_list_selected_member(self):
        return self.find_Elements(self._list_selected_member)
    # 发布内容列表
    def get_list_release_text(self):
        return self.find_Elements(self._list_release_text)
    # 发布时间列表
    def get_list_release_time(self):
        return self.find_Elements(self._list_release_time)
    # 确认按钮
    def get_btn_confirm(self):
        return self.find_Element(self._btn_confirm)

    # 发布动态页面
    # 选择员工按钮
    def get_btn_select_staff(self):
        return self.find_Element(self._btn_select_staff)
    # 员工输入框
    def get_input_staff(self):
        return self.find_Element(self._input_staff)
    # 员工节点
    def get_node_staff(self):
        return self.find_Element(self._node_staff)
    # 员工确定按钮
    def get_btn_confirm_staff(self):
        return self.find_Element(self._btn_confirm_staff)
    # 添加素材按钮
    def get_btn_add_material(self):
        return self.find_Element(self._btn_add_material)
    # 文本输入框
    def get_input_text(self):
        return self.find_Element(self._input_text)
    # 搜索素材输入框
    def get_input_search_material(self):
        return self.find_Element(self._input_search_material)
    # 素材选择按钮
    def get_btn_select_material(self):
        return self.find_Element(self._btn_select_material)
    # 素材确定按钮
    def get_btn_confirm_material(self):
        return self.find_Element(self._btn_confirm_material)
    # 提交按钮
    def get_btn_commit(self):
        return self.find_Element(self._btn_commit)

    """元素操作层"""
    # 朋友圈页面
    def click_btn_circle_friends(self):
        return self.click_element(self.get_btn_circle_friends())
    # 关键词输入框
    def sendkey_input_key_words(self, value):
        return self.send_keys(self.get_input_key_words(), value)
    # 发布时间输入框1
    def sendkey_input_release_time1(self, value):
        return self.send_keys(self.get_input_release_time1(), value)
    # 发布时间输入框2
    def sendkey_input_release_time2(self, value):
        return self.send_keys(self.get_input_release_time2(), value)
    # 查询按钮
    def click_btn_search(self):
        return self.click_element(self.get_btn_search())
    # 发布动态按钮
    def click_btn_release_news(self):
        return self.click_element(self.get_btn_release_news())
    # 指定编辑按钮
    def click_btn_edit(self, value):
        return self.click_element(self.get_btn_edit(value))
    # 指定删除按钮
    def click_btn_delete(self, value):
        return self.click_element(self.get_btn_delete(value))
    # 页码
    def gettext_page_num(self):
        return self.get_element_value(self.get_page_num())
    # 下一页按钮
    def click_btn_next_page(self):
        return self.click_element(self.get_btn_next_page())
    # 所选成员列表
    def gettext_list_selected_member(self):
        return self.get_elements_values(self.get_list_selected_member())
    # 发布内容列表
    def gettext_list_release_text(self):
        return self.get_elements_values(self.get_list_release_text())
    # 发布时间列表
    def gettext_list_release_time(self):
        return self.get_elements_values(self.get_list_release_time())
    # 确认按钮
    def click_btn_confirm(self):
        return self.click_element(self.get_btn_confirm())

    # 发布动态页面
    # 选择员工按钮
    def click_btn_select_staff(self):
        return self.move_click_element(self.get_btn_select_staff())
    # 员工输入框
    def sendkey_input_staff(self, value):
        return self.send_keys(self.get_input_staff(), value)
    # 员工节点
    def click_node_staff(self):
        return self.click_element(self.get_node_staff())
    # 员工确定按钮
    def click_btn_confirm_staff(self):
        return self.click_element(self.get_btn_confirm_staff())
    # 添加素材按钮
    def click_btn_add_material(self):
        return self.click_element(self.get_btn_add_material())
    # 文本输入框
    def sendkey_input_text(self, value):
        return self.send_keys(self.get_input_text(), value)
    # 搜索素材输入框
    def sendkey_input_search_material(self, value):
        return self.send_keys(self.get_input_search_material(), value)
    # 素材选择按钮
    def click_btn_select_material(self):
        return self.click_element(self.get_btn_select_material())
    # 素材确定按钮
    def click_btn_confirm_material(self):
        return self.click_element(self.get_btn_confirm_material())
    # 提交按钮
    def click_btn_commit(self):
        return self.click_element(self.get_btn_commit())

    """业务层"""
    def switch_to_current(self):
        sleep(2)
        self.click_btn_circle_friends()
        sleep(3)

    def combine_keys(self):
        list1 = self.gettext_list_release_text()
        # list2 = self.gettext_list_selected_member()
        # lists = [[] for i in range(len(list1))]
        # n = 0
        # while n < len(list1):
        #     lists[n].append(list1[n])
        #     lists[n].append(list2[n])
        #     n += 1
        # return lists
        return list1

    def search_by_keys(self, keys):
        self.sendkey_input_key_words(keys)
        sleep(1)
        self.click_btn_search()
        sleep(4)
        pagenum = self.gettext_page_num()
        n = 1
        while n <= int(pagenum):
            lists = self.combine_keys()
            sleep(3)
            lis = self.get_list_release_text()
            m = 0
            while m < len(lis):
                log().debug('验证' + str(lists[m]) + '中，是否存在:' + keys)
                # if keys in lists[m][0] or keys in lists[m][1]:
                #     log().debug('验证成功')
                if keys in lists[m]:
                    log().debug('验证成功')
                else:
                    log().error('验证失败' + keys + '不在列表' + str(lists[m]) + '内')
                m += 1
            n += 1
            self.click_btn_next_page()
            sleep(4)

    def search_by_release_time(self, start_time, end_time):
        self.sendkey_input_key_words('')
        self.sendkey_input_release_time1(start_time)
        sleep(1)
        self.sendkey_input_release_time2(end_time)
        sleep(2)
        self.click_btn_search()
        sleep(3)
        list = self.gettext_list_release_time()
        slist = []
        for n in list:
            slist.append((n.split(' '))[0])
        pages = self.gettext_page_num()
        m = 1
        while m <= int(pages):
            for date in slist:
                st = datetime.datetime.strptime(str(start_time), '%Y-%m-%d')
                et = datetime.datetime.strptime(str(end_time), '%Y-%m-%d')
                nt = datetime.datetime.strptime(str(date), '%Y-%m-%d')
                self.assert_True(et >= nt >= st, '验证 {} >= {} >= {}'.format(et, nt, st))
            self.click_btn_next_page()
            sleep(2)
            m += 1
        sleep(2)

    def add_release_news(self, staff, msg):
        k = PyKeyboard()
        self.click_btn_release_news()
        sleep(4)
        self.click_btn_select_staff()
        sleep(2)
        self.sendkey_input_staff(staff)
        k.tap_key(k.enter_key)
        sleep(2)
        self.click_node_staff()
        sleep(1)
        self.click_btn_confirm_staff()
        sleep(2)
        self.click_btn_add_material()
        sleep(2)
        self.sendkey_input_search_material(msg)
        k.tap_key(k.enter_key)
        sleep(2)
        self.click_btn_select_material()
        sleep(1)
        self.click_btn_confirm_material()
        sleep(2)
        self.click_btn_commit()
        sleep(1.5)
        self.check_exist_in_page('发布成功')
        list = self.combine_keys()
        # self.assert_Equal(staff, list[0][1])
        # self.assert_Equal(msg, list[0][0])
        self.assert_Equal(msg, list[0])

    def edit_release_news(self, staff, msg1, msg2):
        list = self.combine_keys()
        count = 1
        for n in list:
            # if staff == n[1] and msg1 == n[0]:
            if msg1 == n:
                self.click_btn_edit(count)
                sleep(2)
                self.sendkey_input_text(msg2)
                sleep(2)
                self.click_btn_commit()
                sleep(1.5)
                self.check_exist_in_page('操作成功')
                list = self.combine_keys()
                # self.assert_Equal(staff, list[count - 1][1])
                # self.assert_Equal(msg2, list[count - 1][0])
                self.assert_Equal(msg2, list[count - 1])
                break
            count += 1

    def delete_release_news(self, staff, msg):
        list = self.combine_keys()
        count = 1
        for n in list:
            # if staff == n[1] and msg == n[0]:
            if msg == n:
                list = self.gettext_list_release_time()
                timing = list[count-1]
                self.click_btn_delete(count)
                sleep(2)
                self.click_btn_confirm()
                sleep(2)
                self.check_exist_in_page('操作成功')
                self.check_not_exist_in_page(timing)
                break
            count += 1
