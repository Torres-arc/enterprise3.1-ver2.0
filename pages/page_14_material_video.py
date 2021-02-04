from selenium.webdriver.common.by import By
from commons.base_page import BasePage
from time import sleep
from pykeyboard import PyKeyboard
from commons.log import log
import os


class MaterialVideoPage(BasePage):
    """元素定位信息"""
    # 基础页面
    # 跳转页面
    _btn_video = (By.XPATH, '//li[text()="视频"]')
    # 添加视频按钮
    _btn_add_audio = (By.XPATH, '//span[text()="添加视频"]/..')
    # 视频素材模块
    _video_water_fall_title = (By.CSS_SELECTOR, '.picture-text-title')
    _video_water_fall_sum = (By.CSS_SELECTOR, '.picture-text-desc')
    _video_btn_edit = (By.CSS_SELECTOR, '[class="el-tooltip el-icon-edit item"]')
    _video_btn_delete = (By.CSS_SELECTOR, '[class="el-tooltip el-icon-delete item"]')
    _video_module = (By.CSS_SELECTOR, '.el-checkbox-group')
    # 新增分组按钮
    _btn_add_group = (By.CSS_SELECTOR, 'div.left-menu-box i.el-icon-plus')
    # 分组名输入框
    _input_group = (By.CSS_SELECTOR, '.el-dialog__body input')
    # 确定按钮
    _btn_confirm = (By.XPATH, '//div[@class="dialog-footer"]/button[2]')
    # 分组名字列表
    _list_group_name = (By.XPATH, '//span[@class="department-name"]')

    # 编辑素材输入框
    _input_edit_audio = (By.CSS_SELECTOR, 'div[class="el-input el-input--small"]>input')
    # 特定分组
    _specify_group = ('xpath', '//span[text()="%s"]')
    # 特定分组编辑按钮
    _btn_specify_group_edit = ('xpath', '//span[text()="%s"]/../../div')

    # 分组编辑弹窗
    # 添加子分组按钮
    _btn_add_child_group = (By.CSS_SELECTOR, 'ul[x-placement] :nth-child(2)')
    # 修改名称按钮
    _btn_change_group_name = (By.CSS_SELECTOR, 'ul[x-placement] :nth-child(3)')
    # 删除分组按钮
    _btn_delete_group = (By.CSS_SELECTOR, 'ul[x-placement] :nth-child(4)')
    # 删除分组确定按钮
    _btn_delete_group_confirm = (By.CSS_SELECTOR, 'div[aria-label="删除分类"] div[class$="btns"] button:last-child')

    # 添加视频页面
    # 视频分类下拉框
    _btn_video_classify = (By.CSS_SELECTOR, 'div.el-form-item__content input[placeholder]')
    # 视频分类选择
    _btn_select_group1 = ('xpath', '//span[text()="%s"]')
    _btn_select_group2 = '../label'
    # 上传视频按钮
    _btn_upload_video = (By.XPATH, '//div[text()="点击上传"]')
    # 封面上传按钮
    _btn_upload_pic = (By.XPATH, '//div[text()="点击上传"]')
    # 添加完成按钮
    _btn_complete = (By.XPATH, '//span[text()="完 成"]/..')
    # 摘要输入框
    _input_summary = (By.CSS_SELECTOR, 'input[placeholder="请输入视频摘要"]')
    # 确认提交按钮
    _btn_confirm_commit = (By.CSS_SELECTOR, 'div.el-message-box__btns :nth-child(2)')


    """元素定位层"""
    # 获取跳转按钮
    def get_btn_video(self):
        return self.find_Element(self._btn_video)
    # 添加视频按钮
    def get_btn_add_audio(self):
        return self.find_Element(self._btn_add_audio)
    # 获取特定网页标题
    def get_text_title_video(self):
        return self.find_Elements(self._video_water_fall_title)
    # 获取特定网页摘要
    def get_text_sum_video(self):
        return self.find_Elements(self._video_water_fall_sum)
    # 获取编辑网页按钮
    def get_btn_edit(self):
        return self.find_Elements(self._video_btn_edit)
    # 获取删除网页按钮
    def get_btn_delete(self):
        return self.find_Elements(self._video_btn_delete)
    # 获取网页模块列表数量
    def get_video_module_dic(self):
        list = self.find_Elements(self._video_module)
        return len(list)
    # 新增分组按钮
    def get_btn_add_group(self):
        return self.find_Element(self._btn_add_group)
    # 分组名输入框
    def get_input_group(self):
        return self.find_Element(self._input_group)
    # 确定按钮
    def get_btn_confirm(self):
        return self.find_Element(self._btn_confirm)
    # 获取分组名字列表
    def get_list_group_name(self):
        return self.find_Elements(self._list_group_name)
    # 获取特定分组
    def get_specify_group(self, group):
        return self.find_ele_replace(self._specify_group[0], self._specify_group[1], group)
    # 获取特定分组的编辑按钮
    def get_btn_specify_group_edit(self, group):
        return self.find_ele_replace(self._btn_specify_group_edit[0], self._btn_specify_group_edit[1], group)

    # 分组编辑弹窗
    # 添加子分组按钮
    def get_btn_add_child_group(self):
        return self.find_Element(self._btn_add_child_group)
    # 修改名称按钮
    def get_btn_change_group_name(self):
        return self.find_Element(self._btn_change_group_name)
    # 删除分组按钮
    def get_btn_delete_group(self):
        return self.find_Element(self._btn_delete_group)
    # 删除分组确定按钮
    def get_btn_delete_group_confirm(self):
        return self.find_Element(self._btn_delete_group_confirm)

    # 添加视频页面
    # 视频分类下拉框
    def get_btn_video_classify(self):
        return self.find_Element(self._btn_video_classify)
    # 获取下拉框分组选择
    def get_btn_select_group1(self, group):
        return self.find_eles_replace(self._btn_select_group1[0], self._btn_select_group1[1], group)
    def get_btn_select_group2(self, group):
        ele = self.get_btn_select_group1(group)
        return ele[-1].find_element(By.XPATH, self._btn_select_group2)
    # 上传视频按钮
    def get_btn_upload_video(self):
        return self.find_Element(self._btn_upload_video)
    # 封面上传按钮
    def get_btn_upload_pic(self):
        return self.find_Element(self._btn_upload_pic)
    # 添加完成按钮
    def get_btn_complete(self):
        return self.find_Element(self._btn_complete)
    # 摘要输入框
    def get_input_summary(self):
        return self.find_Element(self._input_summary)
    # 确认提交按钮
    def get_btn_confirm_commit(self):
        return self.find_Element(self._btn_confirm_commit)


    """元素操作层"""
    # 点击跳转页面
    def click_btn_video(self):
        return self.click_element(self.get_btn_video())
    # 添加视频按钮
    def click_btn_add_video(self):
        return self.click_element(self.get_btn_add_audio())
    # 点击编辑按钮
    def click_btn_edit(self, index):
        return self.click_element(self.get_btn_edit()[index])
    # 点击删除按钮
    def click_btn_delete(self, index):
        return self.click_element(self.get_btn_delete()[index])
    # 获取文本视频标题
    def gettext_video_title(self, index):
        return self.get_element_value(self.get_text_title_video()[index])
    # 获取文本视频摘要
    def gettext_video_sum(self, index):
        return self.get_element_value(self.get_text_sum_video()[index])
    # 新增分组按钮
    def click_btn_add_group(self):
        return self.click_element(self.get_btn_add_group())
    # 分组名输入框
    def sendkeys_input_group(self, value):
        return self.send_keys(self.get_input_group(), value)
    # 确定按钮
    def click_btn_confirm(self):
        return self.click_element(self.get_btn_confirm())
    # 获取文本分组名字列表
    def gettext_list_group_name(self):
        return self.get_elements_values(self.get_list_group_name())
    # 点击特定分组
    def click_specify_group(self, group):
        return self.move_click_element(self.get_specify_group(group))
        # 点击特定分组的编辑按钮
    def click_btn_specify_group_edit(self, group):
        return self.move_click_element(self.get_btn_specify_group_edit(group))

    # 分组编辑弹窗
    # 添加子分组按钮
    def click_btn_add_child_group(self):
        return self.click_element(self.get_btn_add_child_group())
    # 修改名称按钮
    def click_btn_change_group_name(self):
        return self.click_element(self.get_btn_change_group_name())
    # 删除分组按钮
    def click_btn_delete_group(self):
        return self.click_element(self.get_btn_delete_group())
    # 删除分组确定按钮
    def click_btn_delete_group_confirm(self):
        return self.click_element(self.get_btn_delete_group_confirm())

    # 点击网页分类下拉框
    def click_select_video_classify(self):
        return self.click_element(self.get_btn_video_classify())
     # 点击下拉框分组选择
    def click_btn_select_group(self, group):
        return self.click_element(self.get_btn_select_group2(group))
    # 上传视频按钮
    def click_btn_upload_video(self):
        return self.click_element(self.get_btn_upload_video())
    # 封面上传按钮
    def click_btn_upload_pic(self):
        return self.click_element(self.get_btn_upload_pic())
    # 添加完成按钮
    def click_btn_complete(self):
        return self.click_element(self.get_btn_complete())
    # 摘要输入框
    def sendkey_input_summary(self, value):
        return self.send_keys(self.get_input_summary(), value)
    # 确认提交按钮
    def click_btn_confirm_commit(self):
        return self.click_element(self.get_btn_confirm_commit())

    """业务层"""
    def switch_to_current(self):
        sleep(2)
        self.click_btn_video()
        sleep(3)

    # 将网页信息列表录入列表
    def get_list_video(self):
        n = 0
        count = self.get_video_module_dic()
        lists = [[] for i in range(count)]
        while n < count:
            lists[n].append(self.gettext_video_title(n))
            lists[n].append(self.gettext_video_sum(n))
            n += 1
        return lists

    def add_video(self, path, ppath, group, sum, name):
        k = PyKeyboard()
        path1 = os.path.abspath(os.path.dirname(os.path.dirname(__file__)) + path)
        path2 = os.path.abspath(os.path.dirname(os.path.dirname(__file__)) + ppath)
        self.click_btn_add_video()
        sleep(2)
        self.click_select_video_classify()
        sleep(1)
        self.click_btn_select_group(group)
        sleep(1)
        self.click_select_video_classify()
        sleep(1)
        self.click_btn_upload_video()
        sleep(3)
        k.tap_key(k.shift_key)
        k.type_string(path1)
        sleep(1)
        k.tap_key(k.enter_key)
        sleep(3)
        self.click_btn_upload_pic()
        sleep(3)
        k.tap_key(k.shift_key)
        k.type_string(path2)
        sleep(1)
        k.tap_key(k.enter_key)
        sleep(3)
        self.sendkey_input_summary(sum)
        sleep(1)
        self.click_btn_complete()
        sleep(1)
        self.click_btn_confirm_commit()
        sleep(1.5)
        self.check_exist_in_page('添加成功')
        self.check_exist_in_page(name)

    def edit_video(self, name, sum2):
        list = self.get_list_video()
        index = 0
        for n in list:
            if name == n[0]:
                self.click_btn_edit(index)
                break
            index += 1
        sleep(2)
        self.sendkey_input_summary(sum2)
        sleep(1)
        self.click_btn_complete()
        sleep(2)
        self.click_btn_confirm_commit()
        sleep(1.5)
        self.assert_Equal(self.gettext_video_sum(index), (' '+sum2+" "))

    def delete_video(self, name):
        list = self.get_list_video()
        index = 0
        for n in list:
            if name == n[0]:
                self.click_btn_delete(index)
                break
            index += 1
            sleep(2)
        self.click_btn_confirm_commit()
        sleep(2)
        self.check_not_exist_in_page(name)
        self.check_exist_in_page('删除成功')

    def add_group(self, group_name):
        self.click_btn_add_group()
        sleep(2)
        self.sendkeys_input_group(group_name)
        sleep(1)
        self.click_btn_confirm()
        sleep(2)
        lists = self.gettext_list_group_name()
        self.check_exist_in_lists(group_name, lists)

    def delete_group(self, group):
        self.click_specify_group(group)
        sleep(1.5)
        self.click_btn_specify_group_edit(group)
        sleep(3)
        self.click_btn_delete_group()
        sleep(2)
        self.click_btn_delete_group_confirm()
        sleep(2)
        self.check_not_exist_in_page(group)
