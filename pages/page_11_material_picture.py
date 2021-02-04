from selenium.webdriver.common.by import By
from commons.base_page import BasePage
from time import sleep
import os

'''图片页面！！！'''


class PicPage(BasePage):
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
    _btn_group_move_start_more = (By.XPATH, "//span[text()='自动化测试勿删_新建分组']/../../div")
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

    # 图片
    _btn_pic_label = (By.XPATH, "//li[text()='图片']")
    # 添加图片
    _btn_add_pic = (By.XPATH, "//span[text()='添加图片']")
    # 编辑图片 图片名称
    _input_add_pic_add_name = (By.XPATH, "(//label[text()='图片名称']/following::input)[1]")
    # 编辑图片 确认
    _btn_add_pic_add_name_ok = (By.XPATH, "(//label[text()='图片名称']/following::button)[2]")
    # 添加图片 图片分类
    _btn_add_pic_style_choose = (By.XPATH, "(//label[text()='图片分类']/following::input)[1]")
    # 添加图片 图片分类按钮 选项
    _btn_add_pic_style_choose_x = (By.XPATH, "(//span[text()='自动化测试勿删_新建分组'])[3]/../label[1]")
    # 添加图片 选择图片
    _btn_add_pic_choose_pic = (By.XPATH, "//div[text()='上传图片']")
    # 添加图片 保存
    _btn_add_pic_save = (By.XPATH, "(//label[text()='图片分类']/following::button)[2]")
    # 搜索图片素材
    _input_search_pic = (By.XPATH, "//input[@placeholder='搜索图片素材']")
    # 第一张图片素材 勾选项
    _btn_first_pic_select = (By.XPATH, "(//span[@class='el-checkbox__input']//span)[2]")
    # 第一张图片素材 移动位置
    _btn_first_pic_move_ele = (By.XPATH, "(//div[@class='el-image']//img)[1]")
    # 第一张图片素材 移动位置-编辑
    _btn_first_pic_edit = (By.XPATH, "(//div[@class='poster-card-opertion']//i)[1]")
    # 第一张图片素材 删除
    _btn_pic_del = (By.XPATH, "//span[text()='删除']")
    # 第一张图片素材 删除-确认删除
    _btn_pic_del_ok = (By.XPATH, "//span[text()='删除图片']/../../../div[3]/button[2]")

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

    # 图片
    def get_btn_pic_label(self):
        return self.find_Element(self._btn_pic_label)

    # 添加图片
    def get_btn_add_pic(self):
        return self.find_Element(self._btn_add_pic)

    # 编辑图片 图片名称
    def get_input_add_pic_add_name(self):
        return self.find_Element(self._input_add_pic_add_name)

    # 编辑图片 确认
    def get_btn_add_pic_add_name_ok(self):
        return self.find_Element(self._btn_add_pic_add_name_ok)

    # 添加图片 图片分类
    def get_btn_add_pic_style_choose(self):
        return self.find_Element(self._btn_add_pic_style_choose)

    # 添加图片 图片分类按钮 选项
    def get_btn_add_pic_style_choose_x(self):
        return self.find_Element(self._btn_add_pic_style_choose_x)

    # 添加图片 选择图片
    def get_btn_add_pic_choose_pic(self):
        return self.find_Element(self._btn_add_pic_choose_pic)

    # 添加图片 保存
    def get_btn_add_pic_save(self):
        return self.find_Element(self._btn_add_pic_save)

    # 搜索图片素材
    def get_btn_search_pic(self):
        return self.find_Element(self._input_search_pic)

    # 第一张图片素材 勾选项
    def get_btn_first_pic_select(self):
        return self.find_Element(self._btn_first_pic_select)

    # 第一张图片素材 移动位置
    def get_btn_first_pic_move_ele(self):
        return self.find_Element(self._btn_first_pic_move_ele)

    # 第一张图片素材 移动位置-编辑
    def get_btn_first_pic_edit(self):
        return self.find_Element(self._btn_first_pic_edit)

    # 第一张图片素材 删除
    def get_btn_pic_del(self):
        return self.find_Element(self._btn_pic_del)

    # 第一张图片素材 删除-确认删除
    def get_btn_pic_del_ok(self):
        return self.find_Element(self._btn_pic_del_ok)

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
        return self.click_element(self.get_btn_group_move_start())

    # 一级分类 移动分组测试
    def click_btn_group_move_end(self):
        return self.click_element(self.get_btn_group_move_end())

    # 一级分类 更多
    def click_btn_group_move_start_more(self):
        return self.move_click_element(self.get_btn_group_move_start_more())

    # 一级分类 更多 添加子分类
    def click_btn_group_move_start_more_add_child(self):
        return self.click_element(self.get_btn_group_move_start_more_add_child())

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

    # 选择分组 二次确定
    def click_btn_choose_group_ok_twice(self):
        return self.click_element(self.get_btn_choose_group_ok_twice())

    # 图片
    def click_btn_pic_label(self):
        return self.click_element(self.get_btn_pic_label())

    # 添加图片
    def click_btn_add_pic(self):
        return self.click_element(self.get_btn_add_pic())

    # 编辑图片 图片名称
    def sendkeys_input_add_pic_add_name(self, value):
        return self.send_keys(self.get_input_add_pic_add_name(), value)

    # 编辑图片 确认
    def click_btn_add_pic_add_name_ok(self):
        return self.click_element(self.get_btn_add_pic_add_name_ok())

    # 添加图片 图片分类
    def click_btn_add_pic_style_choose(self):
        return self.click_element(self.get_btn_add_pic_style_choose())

    # 添加图片 图片分类按钮 选项
    def click_btn_add_pic_style_choose_x(self):
        return self.move_click_element(self.get_btn_add_pic_style_choose_x())

    # 添加图片 选择图片
    def click_btn_add_pic_choose_pic(self):
        return self.click_element(self.get_btn_add_pic_choose_pic())

    # 添加图片 保存
    def click_btn_add_pic_save(self):
        return self.click_element(self.get_btn_add_pic_save())

    # 搜索图片素材
    def sendkeys_input_search_pic(self, value):
        return self.send_keys(self.get_btn_search_pic(), value)

    # 第一张图片素材 勾选项
    def click_btn_first_pic_select(self):
        return self.click_element(self.get_btn_first_pic_select())

    # 第一张图片素材 移动位置
    def move_btn_first_pic_move_ele(self):
        return self.move_to_element(self.get_btn_first_pic_move_ele())

    # 第一张图片素材 移动位置-编辑
    def click_btn_first_pic_edit(self):
        return self.click_element(self.get_btn_first_pic_edit())

    # 第一张图片素材 删除
    def click_btn_pic_del(self):
        return self.click_element(self.get_btn_pic_del())

    # 第一张图片素材 删除-确认删除
    def click_btn_pic_del_ok(self):
        return self.click_element(self.get_btn_pic_del_ok())

    '''业务层'''

    def switch_to_current(self):
        sleep(2)
        self.click_btn_pic_label()
        sleep(3)

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

    # 添加图片
    def add_pic(self):
        _pic = '\\materials\\pic\\test2.png'
        path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)) + _pic)
        self.click_btn_add_pic()
        sleep(1)
        self.click_btn_add_pic_style_choose()
        sleep(1)
        self.click_btn_add_pic_style_choose_x()
        sleep(2)
        self.click_btn_add_pic_style_choose()
        sleep(2)
        self.click_btn_add_pic_choose_pic()
        sleep(2)
        self.tap_keyboard("shift")
        self.control_keyboard(path)
        self.tap_keyboard("enter")
        sleep(2)
        self.click_btn_add_pic_save()
        sleep(2)

    def check_add_pic(self):
        sleep(2)
        self.click_btn_group_move_start()
        sleep(2)
        self.check_exist_in_page("test2.png")

    # 搜索图片
    def search_pic(self):
        self.sendkeys_input_search_pic("test2.png")
        self.tap_keyboard("enter")
        sleep(2)

    def check_search_pic(self):
        sleep(2)
        self.check_exist_in_page("test2.png")

    # 移动分组
    def move_group(self):
        self.sendkeys_input_search_pic("test2.png")
        self.tap_keyboard("enter")
        sleep(2)
        self.click_btn_first_pic_select()
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
        self.check_exist_in_page("test2.png")

    def edit_pic(self):
        self.sendkeys_input_search_pic("test2.png")
        self.tap_keyboard("enter")
        sleep(2)
        self.move_btn_first_pic_move_ele()
        self.click_btn_first_pic_edit()
        sleep(2)
        self.sendkeys_input_add_pic_add_name("test2_edit.png")
        self.click_btn_add_pic_add_name_ok()
        sleep(2)

    def check_edit_pic(self):
        sleep(2)
        self.click_btn_group_move_end()
        sleep(2)
        self.check_exist_in_page("test2_edit.png")

    def del_pic(self):
        self.sendkeys_input_search_pic("test2_edit.png")
        self.tap_keyboard("enter")
        sleep(2)
        self.click_btn_first_pic_select()
        sleep(2)
        self.click_btn_pic_del()
        sleep(2)
        self.click_btn_pic_del_ok()
        sleep(2)

    def check_del_pic(self):
        sleep(2)
        self.sendkeys_input_search_pic("test2_edit.png")
        self.tap_keyboard("enter")
        sleep(2)
        self.check_not_exist_in_page("test2_edit.png")

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
        sleep(1)

    def check_del_new_group(self):
        sleep(4)
        self.check_not_exist_in_page("自动化测试勿删_新建分组")
