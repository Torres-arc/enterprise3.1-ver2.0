from selenium.webdriver.common.by import By
from commons.base_page import BasePage
from time import sleep
from pykeyboard import PyKeyboard

'''文本页面！！！'''


class TextPage(BasePage):
    '''元素定位信息'''
    # 新建分组
    _btn_add_group = (By.XPATH, "(//i[@class='el-icon-plus'])[1]")
    # 一级分类名称 自动化测试勿删_新建分组
    _input_add_group_name = (By.XPATH, "(//span[text()='添加一级分类']/following::input)[1]")
    # 一级分类名称 确认
    _btn_add_group_name_ok = (By.XPATH, "//span[text()='确 定']")
    # 一级分类 自动化测试勿删_新建分组
    _btn_group_move_start = (By.XPATH, "(//span[text()='自动化测试勿删_新建分组'])[1]")
    # 一级分类 移动分组测试
    _btn_group_move_end = (By.XPATH, "(//span[text()='移动分组测试'])[1]")
    # 一级分类 更多
    _btn_group_move_start_more = (By.XPATH, "(//span[text()='自动化测试勿删_新建分组'])/../../div[1]")
    # 一级分类 更多 添加子分类
    _btn_group_move_start_more_add_child = (By.CSS_SELECTOR, "ul[x-placement] :nth-child(2)")
    # 一级分类 更多 添加子分类 输入框
    _input_group_move_start_more_add_child = (By.XPATH, "(//span[text()='添加子分类']/following::input)[1]")
    # 一级分类 更多 添加子分类 确定
    _btn_group_move_start_more_add_child_ok = (By.XPATH, "//span[text()='添加子分类']/../../div[3]/div/button[2]")
    # 二级分类
    _btn_second_group = (By.XPATH, "//span[text()='测试勿删_子分类']")
    # 二级分类 更多
    _btn_second_group_more = (By.XPATH, "//span[text()='测试勿删_子分类']/../../div")
    # 二级分类 更多 删除
    _btn_second_group_more_del = (By.CSS_SELECTOR, "ul[x-placement] :nth-child(3)")
    # 二级分类 更多 删除
    _btn_second_group_more_del_ok = (By.XPATH, "//span[text()='删除分类']/../../../div[3]/button[2]")
    # 一级分类 更多 删除
    _btn_group_move_start_more_del = (By.CSS_SELECTOR, "ul[x-placement] :nth-child(4)")
    # 一级分类 更多 删除 确定
    _btn_group_move_start_more_del_ok = (By.XPATH, "//span[text()='删除分类']/../../../div[3]/button[2]")
    # 移动分组
    _btn_move_group = (By.XPATH, "//span[text()='移动分组']")
    # 选择分组
    _btn_choose_group = (By.XPATH, "//p[text()='选择分组']/../div/div/span")
    # 选择分组 选项
    _btn_choose_group_x = (By.XPATH, "//span[text()='移动分组测试']/../label[1]")
    # 选择分组 确定
    _btn_choose_group_ok = (By.XPATH, "//p[text()='选择分组']/../div[2]/button[2]")
    # 选择分组 二次确认
    _btn_choose_group_ok_twice = (By.XPATH, "//span[text()='提示']/../../../div[3]/button[2]")
    # 文本
    _btn_text_label = (By.XPATH, "//li[text()='文本']")
    # 新建文本
    _btn_add_text = (By.XPATH, "//span[text()='添加文本']")
    # 新建文本 文本分类
    _btn_add_text_style_choose = (By.XPATH, "(//label[text()='文本分类']/following::input)[1]")
    # 新建文本 文本分类按钮 选项
    _btn_add_text_style_choose_x = (By.XPATH, "(//span[text()='自动化测试勿删_新建分组'])[3]/../label[1]")
    # 新建文本 文本内容
    _input_add_text_add_name = (By.XPATH, "//label[text()='文本内容']/following::textarea")
    # 新建文本 确定
    _btn_add_text_ok = (By.XPATH, "//label[text()='文本分类']/../../../../div[3]/span/button[2]")
    # 搜索文本素材
    _input_search_text = (By.XPATH, "//input[@placeholder='搜索文本素材']")
    # 第一张文本素材 勾选项
    _btn_first_text_select = (By.XPATH, "(//span[@class='el-checkbox__input']//span)[2]")
    # 第一张文本素材 移动位置-编辑
    _btn_first_text_edit = (By.XPATH, "(//span[text()='编辑'])[1]")
    # 第一张文本素材 删除
    _btn_text_del = (By.XPATH, "//span[text()='删除']")
    # 第一张文本素材 删除-确认删除
    _btn_text_del_ok = (By.XPATH, "//span[text()='删除文本']/../../../div[3]/button[2]")

    '''元素定位层'''

    # 新建分组
    def get_btn_add_group(self):
        return self.find_Element(self._btn_add_group)

    # 一级分类名称 自动化测试勿删_新建分组
    def get_input_add_group_name(self):
        return self.find_Element(self._input_add_group_name)

    # 一级分类名称 确认
    def get_btn_add_group_name_ok(self):
        return self.find_Element(self._btn_add_group_name_ok)

    # 一级分类 自动化测试勿删_新建分组
    def get_btn_group_move_start(self):
        return self.find_Element(self._btn_group_move_start)

    # 一级分类 移动分组测试
    def get_btn_group_move_end(self):
        return self.find_Element(self._btn_group_move_end)

    # 一级分类 更多
    def get_btn_group_move_start_more(self):
        return self.find_Element(self._btn_group_move_start_more)

    # 一级分类 更多 添加子分类
    def get_btn_group_move_start_more_add_child(self):
        return self.find_Element(self._btn_group_move_start_more_add_child)

    # 一级分类 更多 添加子分类 输入框
    def get_input_group_move_start_more_add_child(self):
        return self.find_Element(self._input_group_move_start_more_add_child)

    # 一级分类 更多 添加子分类 确定
    def get_btn_group_move_start_more_add_child_ok(self):
        return self.find_Element(self._btn_group_move_start_more_add_child_ok)

    # 二级分类
    def get_btn_second_group(self):
        return self.find_Element(self._btn_second_group)

    # 二级分类 更多
    def get_btn_second_group_more(self):
        return self.find_Element(self._btn_second_group_more)

    # 二级分类 更多 删除
    def get_btn_second_group_more_del(self):
        return self.find_Element(self._btn_second_group_more_del)

    # 二级分类 更多 删除
    def get_btn_second_group_more_del_ok(self):
        return self.find_Element(self._btn_second_group_more_del_ok)

    # 一级分类 更多 删除
    def get_btn_group_move_start_more_del(self):
        return self.find_Element(self._btn_group_move_start_more_del)

    # 一级分类 更多 删除 确定
    def get_btn_group_move_start_more_del_ok(self):
        return self.find_Element(self._btn_group_move_start_more_del_ok)

    # 移动分组
    def get_btn_move_group(self):
        return self.find_Element(self._btn_move_group)

    # 选择分组
    def get_btn_choose_group(self):
        return self.find_Element(self._btn_choose_group)

    # 选择分组 选项
    def get_btn_choose_group_x(self):
        return self.find_Element(self._btn_choose_group_x)

    # 选择分组 确定
    def get_btn_choose_group_ok(self):
        return self.find_Element(self._btn_choose_group_ok)

    # 选择分组 二次确认
    def get_btn_choose_group_ok_twice(self):
        return self.find_Element(self._btn_choose_group_ok_twice)

    # 文本
    def get_btn_text_label(self):
        return self.find_Element(self._btn_text_label)

    # 新建文本
    def get_btn_add_text(self):
        return self.find_Element(self._btn_add_text)

    # 新建文本 文本分类
    def get_btn_add_text_style_choose(self):
        return self.find_Element(self._btn_add_text_style_choose)

    # 新建文本 文本分类按钮 选项
    def get_btn_add_text_style_choose_x(self):
        return self.find_Element(self._btn_add_text_style_choose_x)

    # 新建文本 文本内容
    def get_input_add_text_add_name(self):
        return self.find_Element(self._input_add_text_add_name)

    # 新建文本 确定
    def get_btn_add_text_ok(self):
        return self.find_Element(self._btn_add_text_ok)

    # 搜索文本素材
    def get_input_search_text(self):
        return self.find_Element(self._input_search_text)

    # 第一张文本素材 勾选项
    def get_btn_first_text_select(self):
        return self.find_Element(self._btn_first_text_select)

    # 第一张文本素材 移动位置-编辑
    def get_btn_first_text_edit(self):
        return self.find_Element(self._btn_first_text_edit)

    # 第一张文本素材 删除
    def get_btn_text_del(self):
        return self.find_Element(self._btn_text_del)

    # 第一张文本素材 删除-确认删除
    def get_btn_text_del_ok(self):
        return self.find_Element(self._btn_text_del_ok)

    '''元素操作层'''

    # 新建分组
    def click_btn_add_group(self):
        return self.click_element(self.get_btn_add_group())

    # 一级分类名称 自动化测试勿删_新建分组
    def sendkeys_input_add_group_name(self, value):
        return self.send_keys(self.get_input_add_group_name(), value)

    # 一级分类名称 确认
    def click_btn_add_group_name_ok(self):
        return self.click_element(self.get_btn_add_group_name_ok())

    # 一级分类 自动化测试勿删_新建分组
    def click_btn_group_move_start(self):
        return self.move_click_element(self.get_btn_group_move_start())

    # 一级分类 移动分组测试
    def click_btn_group_move_end(self):
        return self.click_element(self.get_btn_group_move_end())

    # 一级分类 更多
    def click_btn_group_move_start_more(self):
        return self.move_click_element(self.get_btn_group_move_start_more())

    # 一级分类 更多 添加子分类
    def click_btn_group_move_start_more_add_child(self):
        return self.move_click_element(self.get_btn_group_move_start_more_add_child())

    # 一级分类 更多 添加子分类 输入框
    def sendkeys_input_group_move_start_more_add_child(self, value):
        return self.send_keys(self.get_input_group_move_start_more_add_child(), value)

    # 一级分类 更多 添加子分类 确定
    def click_btn_group_move_start_more_add_child_ok(self):
        return self.click_element(self.get_btn_group_move_start_more_add_child_ok())

    # 二级分类
    def click_btn_second_group(self):
        return self.click_element(self.get_btn_second_group())

    # 二级分类 更多
    def click_btn_second_group_more(self):
        return self.click_element(self.get_btn_second_group_more())

    # 二级分类 更多 删除
    def click_btn_second_group_more_del(self):
        return self.click_element(self.get_btn_second_group_more_del())

    # 二级分类 更多 删除
    def click_btn_second_group_more_del_ok(self):
        return self.click_element(self.get_btn_second_group_more_del_ok())

    # 一级分类 更多 删除
    def click_btn_group_move_start_more_del(self):
        return self.click_element(self.get_btn_group_move_start_more_del())

    # 一级分类 更多 删除 确定
    def click_btn_group_move_start_more_del_ok(self):
        return self.click_element(self.get_btn_group_move_start_more_del_ok())

    # 移动分组
    def click_btn_move_group(self):
        return self.click_element(self.get_btn_move_group())

    # 选择分组
    def click_btn_choose_group(self):
        return self.click_element(self.get_btn_choose_group())

    # 选择分组 选项
    def click_btn_choose_group_x(self):
        return self.move_click_element(self.get_btn_choose_group_x())

    # 选择分组 确定
    def click_btn_choose_group_ok(self):
        return self.click_element(self.get_btn_choose_group_ok())

    # 选择分组 二次确认
    def click_btn_choose_group_ok_twice(self):
        return self.click_element(self.get_btn_choose_group_ok_twice())

    # 文本
    def click_btn_text_label(self):
        return self.click_element(self.get_btn_text_label())

    # 新建文本
    def click_btn_add_text(self):
        return self.click_element(self.get_btn_add_text())

    # 新建文本 文本分类
    def click_btn_add_text_style_choose(self):
        return self.click_element(self.get_btn_add_text_style_choose())

    # 新建文本 文本分类按钮 选项
    def click_btn_add_text_style_choose_x(self):
        return self.move_click_element(self.get_btn_add_text_style_choose_x())

    # 新建文本 文本内容
    def sendkeys_input_add_text_add_name(self, value):
        return self.send_keys(self.get_input_add_text_add_name(), value)

    # 新建文本 确定
    def click_btn_add_text_ok(self):
        return self.click_element(self.get_btn_add_text_ok())

    # 搜索文本素材
    def sendkeys_input_search_text(self, value):
        return self.send_keys(self.get_input_search_text(), value)

    # 第一张文本素材 勾选项
    def click_btn_first_text_select(self):
        return self.click_element(self.get_btn_first_text_select())

    # 第一张文本素材 移动位置-编辑
    def click_btn_first_text_edit(self):
        return self.click_element(self.get_btn_first_text_edit())

    # 第一张文本素材 删除
    def click_btn_text_del(self):
        return self.click_element(self.get_btn_text_del())

    # 第一张文本素材 删除-确认删除
    def click_btn_text_del_ok(self):
        return self.click_element(self.get_btn_text_del_ok())

    '''业务层'''

    def switch_to_current(self):
        sleep(2)
        self.click_btn_text_label()
        sleep(3)
        # 前置条件 新建移动分组测试一级分类

    def create_moved_group(self):
        try:
            self.get_btn_group_move_end()
        except Exception:
            self.click_btn_add_group()
            sleep(2)
            self.sendkeys_input_add_group_name("移动分组测试")
            self.click_btn_add_group_name_ok()
            sleep(2)

    # 添加自动化测试_新建分组
    def add_group(self):
        self.create_moved_group()
        self.click_btn_add_group()
        sleep(2)
        self.sendkeys_input_add_group_name("自动化测试勿删_新建分组")
        self.click_btn_add_group_name_ok()
        sleep(2)

    def check_add_group(self):
        self.check_exist_in_page("自动化测试勿删_新建分组")

    # 添加海报
    def add_text(self):
        self.click_btn_add_text()
        sleep(1)
        self.click_btn_add_text_style_choose()
        sleep(1)
        self.click_btn_add_text_style_choose_x()
        sleep(2)
        self.sendkeys_input_add_text_add_name("自动化测试勿删_新建")
        sleep(2)
        self.click_btn_add_text_ok()
        sleep(2)

    def check_add_text(self):
        sleep(2)
        self.click_btn_group_move_start()
        sleep(2)
        self.check_exist_in_page("自动化测试勿删_新建")

    # 搜索海报
    def search_text(self):
        self.sendkeys_input_search_text("自动化测试勿删_新建")
        self.tap_keyboard("enter")
        sleep(2)

    def check_search_text(self):
        sleep(2)
        self.check_exist_in_page("自动化测试勿删_新建")

    # 移动分组
    def move_group(self):
        self.sendkeys_input_search_text("自动化测试勿删_新建")
        self.tap_keyboard("enter")
        sleep(2)
        self.click_btn_first_text_select()
        self.click_btn_move_group()
        sleep(2)
        self.click_btn_choose_group()
        sleep(2)
        self.click_btn_choose_group_x()
        sleep(2)
        self.click_btn_choose_group_ok()
        sleep(2)
        self.click_btn_choose_group_ok_twice()
        sleep(2)

    def check_move_group(self):
        sleep(2)
        self.click_btn_group_move_end()
        sleep(2)
        self.check_exist_in_page("自动化测试勿删_新建")

    def edit_text(self):
        self.sendkeys_input_search_text("自动化测试勿删_新建")
        self.tap_keyboard("enter")
        sleep(2)
        self.click_btn_first_text_edit()
        sleep(2)
        self.sendkeys_input_add_text_add_name("自动化测试勿删_编辑")
        self.click_btn_add_text_ok()
        sleep(2)

    def check_edit_text(self):
        sleep(2)
        self.click_btn_group_move_end()
        sleep(2)
        self.check_exist_in_page("自动化测试勿删_编辑")

    def del_text(self):
        self.sendkeys_input_search_text("自动化测试勿删_编辑")
        self.tap_keyboard("enter")
        sleep(2)
        self.click_btn_first_text_select()
        sleep(2)
        self.click_btn_text_del()
        sleep(2)
        self.click_btn_text_del_ok()
        sleep(2)

    def check_del_text(self):
        sleep(2)
        self.sendkeys_input_search_text("自动化测试勿删_编辑")
        self.tap_keyboard("enter")
        sleep(2)
        self.check_not_exist_in_page("自动化测试勿删_编辑")

    def new_group_add_child(self):
        self.click_btn_group_move_start()
        sleep(1)
        self.click_btn_group_move_start_more()
        sleep(1)
        self.click_btn_group_move_start_more_add_child()
        sleep(1)
        self.sendkeys_input_group_move_start_more_add_child("测试勿删_子分类")
        self.click_btn_group_move_start_more_add_child_ok()
        sleep(2)

    def check_new_group_add_child(self):
        sleep(2)
        self.check_exist_in_page("测试勿删_子分类")

    def del_new_group(self):
        self.click_btn_second_group()
        sleep(1)
        self.click_btn_second_group_more()
        sleep(1)
        self.click_btn_second_group_more_del()
        sleep(1)
        self.click_btn_group_move_start_more_del_ok()
        sleep(3)
        self.click_btn_group_move_start()
        sleep(1)
        self.click_btn_group_move_start_more()
        sleep(1)
        self.click_btn_group_move_start_more_del()
        sleep(1)
        self.click_btn_group_move_start_more_del_ok()
        sleep(2)

    def check_del_new_group(self):
        sleep(2)
        self.check_not_exist_in_page("自动化测试勿删_新建分组")
