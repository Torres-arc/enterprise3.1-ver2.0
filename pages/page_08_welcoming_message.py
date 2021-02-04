from selenium.webdriver.common.by import By
from commons.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
from pykeyboard import PyKeyboard

# 员工活码
class WelcomingMessagePage(BasePage):
    # 元素定位信息
    # 欢迎语页面（公共）
    _welcoming_message_page = (By.XPATH, '//li[text()="欢迎语"]')
    _update_photo = (By.XPATH, '(//button[@class="el-button el-button--file el-button--small is-plain"])[1]')
    _update_file = (By.XPATH, '(//button[@class="el-button el-button--file el-button--small is-plain"])[2]')

    # 员工欢迎语
    _em_welcoming_message_page = (By.XPATH, '//div[contains(text(),"员工欢迎语")and(@id="tab-1")]')
    # 新建员工欢迎语元素
    _add_em_welcoming_message = (By.XPATH, '//span[contains(text(),"新建员工欢迎语")]')
    _update_info_button = (By.XPATH, '//span[text()="添加图片/网页/小程序消息"]')
    _save_em_welcoming_message = (By.XPATH, '(//div[@class="el-form-item__content"]/button)[1]')
    # 编辑员工欢迎语元素
    _edit_em_welcoming_message = (By.XPATH, '(//button[@class="el-button el-button--text el-button--medium"])[1]')
    _sava_edit_em_welcoming_message = (By.XPATH, '//span[text()="保存"]')
    # 删除员工欢迎语元素
    _delete_em_welcoming_message = (By.XPATH, '(//button[@class="el-button el-button--text el-button--medium"])[2]')
    _sure_delete_em_welcoming_message = (
        By.XPATH, '//button[@class="el-button el-button--default el-button--small el-button--primary "]')

    # 部门员工欢迎语
    _deptem_welcoming_message_page = (By.CSS_SELECTOR, '#tab-3')
    # 通过员工云夏搜索
    _selete_users = (By.XPATH, '(//input[@placeholder="请输入欢迎语关键词"])[2]')
    _total = (By.XPATH, '(//span[text()="共 1 条"])[2]')
    # 新建部门员工欢迎语元素
    _deptem_welcoming_message = (By.XPATH, '(//i[@class="el-icon-plus"])[2]')
    _add_user = (By.XPATH, '//span[text()="添加"]')
    _select_user = (By.XPATH, '//input[@placeholder="请输入关键词"]')
    _user = (By.XPATH, '//span[@class="custom-tree-node"]')
    _confirm_user_page = (By.XPATH, '((//div[@class="dialog-footer"])[1]/button)[2]')
    _save_deptem_welcoming_message = (By.XPATH, '((//div[@class="el-form-item__content"])[3]/button)[1]')
    # 编辑部门员工欢迎语元素
    _edit_deptem_welcoming_message = (By.XPATH, '(//td[@class="el-table_2_column_9  "]/div/button)[1]')
    _sava_edit_deptem_welcoming_message = (By.XPATH, '//span[text()="保存"]')
    # 删除部门员工欢迎语元素
    _delete_deptem_welcoming_message = (By.XPATH, '(//td[@class="el-table_2_column_9  "]/div/button)[2]')
    _sure_delete_deptem_welcoming_message = (
        By.XPATH, '//button[@class="el-button el-button--default el-button--small el-button--primary "]')

    # 客户群欢迎语
    _cp_welcoming_message_page = (By.XPATH, '//div[contains(text(),"客户群欢迎语")]')
    # 新建客户群欢迎语
    _add_cp_welcoming_message = (By.XPATH, '//span[contains(text(),"新建客户群欢迎语")]')
    _save_cp_welcoming_message = (By.XPATH, '//span[text()="保存"]')
    # 编辑客户群欢迎语
    _edit_cp_welcoming_message = (By.XPATH, '(//td[@class="el-table_3_column_13  "]/div/button)[1]')
    _save_edit_cp_welcoming_message = (By.XPATH, '//span[text()="保存"]')
    # 删除客户群欢迎语
    _delete_cp_welcoming_message = (By.XPATH, '(//td[@class="el-table_3_column_13  "]/div/button)[2]')
    _sure_delete_cp_welcoming_message = (
        By.XPATH, '//button[@class="el-button el-button--default el-button--small el-button--primary "]')

    # 欢迎语输入(公共)
    _welcoming_message = (By.XPATH, '//textarea')

    # 元素操作并进行封装
    # 欢迎语页面
    def click_welcoming_message_page(self):
        self.find_Element(self._welcoming_message_page).click()

    # 员工欢迎语
    # 点击跳转员工欢迎语页面
    def click_em_welcomingmessage(self):
        self.find_Element(self._em_welcoming_message_page).click()

    # 点击新建员工欢迎语按钮
    def click_add_em_welcomingmessage(self):
        self.find_Element(self._add_em_welcoming_message).click()

    # 在新建员工欢迎语页面，输入欢迎语内容
    def input_em_welcomingmessage(self):
        self.find_Element(self._welcoming_message).send_keys('测试员工欢迎语，勿使用')

    # 将鼠标移至到上传图片/网页/小程序按钮
    def moveto__update_info_button(self):
        self.find_Element(self._update_info_button).click()

    # 点击图片进行图片上传
    def input_update_photo(self):
        self.find_Element(self._update_photo).click()
        sleep(2)
        path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)) + '//materials//pic//photo.png')
        k = PyKeyboard()
        k.tap_key(k.shift_key)
        k.type_string(path)
        sleep(1)
        k.tap_key(k.enter_key)
        sleep(2)
        # os.system('D:\\huhuijun\\updateinfo\\udphoto.exe')

    # 点击保存员工欢迎语页面
    def click_save_emwelcomingmessage(self):
        self.find_Element(self._save_em_welcoming_message).click()

    # 点击编辑员工欢迎语按钮
    def click_edit_em_welcoming_message(self):
        self.find_Element(self._edit_em_welcoming_message).click()

    # 在编辑员工欢迎语页面，修改欢迎语内容
    def input_edit_em_welcoming_message(self):
        self.find_Element(self._welcoming_message).clear()
        self.find_Element(self._welcoming_message).send_keys('测试编辑员工欢迎语，勿使用')

    # 点击保存编辑员工欢迎语页面
    def click_sava_edit_em_welcoming_message(self):
        self.find_Element(self._sava_edit_em_welcoming_message).click()

    # 点击删除员工欢迎语按钮
    def click_delete_em_welcoming_message(self):
        self.find_Element(self._delete_em_welcoming_message).click()

    # 在弹出是否确定删除提示框页面，点击确定按钮
    def click_sure_delete_em_welcoming_message(self):
        self.find_Element(self._sure_delete_em_welcoming_message).click()



    # 部门员工欢迎语
    # 点击跳转部门员工欢迎语页面
    def click_deptemwelcomingmessage_page(self):
        self.find_Element(self._deptem_welcoming_message_page).click()

    # 通过输入欢迎语关键字搜索欢迎语
    def input_selete_users(self):
        self.find_Element(self._selete_users).send_keys('勿使用')
        self.find_Element(self._selete_users).send_keys(Keys.ENTER)

    # 稍后处理
    # 若存在欢迎语，则进行删除操作，若没有，则刷新页面
    # def search_by_welcomingmessage(self):
    #     self.find_element(self._selete_users).send_keys('勿使用')

    # 点击新建部门员工欢迎语按钮
    def click_deptemwelcomingmessage(self):
        self.find_Element(self._deptem_welcoming_message).click()

    # 点击添加员工按钮
    def click_add_user(self):
        self.find_Element(self._add_user).click()

    # 在添加员工页面，输入员工名称进行搜索
    def input_select_user(self, value):
        self.find_Element(self._select_user).send_keys(value)
        self.find_Element(self._select_user).send_keys(Keys.ENTER)

    # 勾选所选员工
    def click_user(self):
        self.find_Element(self._user).click()

    # 保存添加员工页面信息
    def click_confirm_user_page(self):
        self.find_Element(self._confirm_user_page).click()

    # 输入欢迎语内容
    def input_deptwelcomingmessage(self):
        self.find_Element(self._welcoming_message).send_keys('测试部门员工欢迎语，勿使用')

    # 点击保存部门员工欢迎语页面
    def click_save_deptemwelcomingmessage(self):
        self.find_Element(self._save_deptem_welcoming_message).click()

    # 点击编辑部门员工欢迎语
    def cilik_edit_deptem_welcoming_message(self):
        self.find_Element(self._edit_deptem_welcoming_message).click()

    # 在编辑部门员工欢迎语页面，修改欢迎语内容
    def input_edit_deptem_welcoming_message(self):
        self.find_Element(self._welcoming_message).clear()
        self.find_Element(self._welcoming_message).send_keys('测试编辑部门员工欢迎语，勿使用')

    # 点击保存部门员工欢迎语页面
    def click_sava_edit_deptem_welcoming_message(self):
        self.find_Element(self._sava_edit_deptem_welcoming_message).click()

    # 点击删除部门员工欢迎语
    def click_delete_deptem_welcoming_message(self):
        self.find_Element(self._delete_deptem_welcoming_message).click()

    # 在弹出是否确定删除提示框页面，点击确定按钮
    def click_sure_delete_deptem_welcoming_message(self):
        self.find_Element(self._sure_delete_deptem_welcoming_message).click()



    # 客户群欢迎语
    # 点击跳转客户群欢迎语页面
    def click_cpwelcomingmessage_page(self):
        self.find_Element(self._cp_welcoming_message_page).click()

    # 点击新建客户群欢迎语按钮
    def click_cp_welcoming_message(self):
        self.find_Element(self._add_cp_welcoming_message).click()

    # 在新建客户群欢迎语页面，输入欢迎语内容
    def input_welcoming_message(self):
        self.find_Element(self._welcoming_message).send_keys('测试客户群欢迎语，勿使用')

    def click_save_cp_welcoming_message(self):
        self.find_Element(self._save_cp_welcoming_message).click()

    # 点击编辑客户群欢迎语按钮
    def click_edit_cp_welcoming_message(self):
        self.find_Element(self._edit_cp_welcoming_message).click()

    # 在编辑客户群欢迎语页面，修改欢迎语内容
    def input_edit_cp_welcoming_message(self):
        self.find_Element(self._welcoming_message).clear()
        self.find_Element(self._welcoming_message).send_keys('测试编辑客户群欢迎语，勿使用')

    # 点击保存客户群欢迎语页面
    def click_save_edit_cp_welcoming_message(self):
        self.find_Element(self._save_edit_cp_welcoming_message).click()

    # 点击删除客户群欢迎语按钮
    def click_delete_cp_welcoming_message(self):
        self.find_Element(self._delete_cp_welcoming_message).click()

    # 在弹出是否确定删除提示框页面，点击确定按钮
    def click_sure_delete_cp_welcoming_message(self):
        self.find_Element(self._sure_delete_cp_welcoming_message).click()

    '''业务层'''

    # 员工欢迎语：新建/编辑/删除
    def addEmmessage(self):
        sleep(3)
        self.click_welcoming_message_page()
        sleep(2)
        self.click_add_em_welcomingmessage()
        sleep(2)
        self.input_em_welcomingmessage()
        sleep(3)
        self.moveto__update_info_button()
        sleep(2)
        self.input_update_photo()
        sleep(5)
        self.click_save_emwelcomingmessage()
        sleep(5)

    def editEmmessage(self):
        sleep(3)
        self.click_welcoming_message_page()
        sleep(2)
        self.click_edit_em_welcoming_message()
        sleep(2)
        self.input_edit_em_welcoming_message()
        sleep(3)
        self.click_sava_edit_em_welcoming_message()
        sleep(5)

    def deleteEmmessage(self):
        sleep(3)
        self.click_welcoming_message_page()
        sleep(2)
        self.click_delete_em_welcoming_message()
        sleep(2)
        self.click_sure_delete_em_welcoming_message()
        sleep(2)

    # 部门员工欢迎语：新建/编辑/删除
    def addDeptemmessage(self, value):
        sleep(3)
        self.click_deptemwelcomingmessage_page()
        sleep(2)
        self.click_deptemwelcomingmessage()
        sleep(2)
        self.click_add_user()
        sleep(5)
        self.input_select_user(value)
        sleep(3)
        self.click_user()
        sleep(1)
        self.click_confirm_user_page()
        sleep(2)
        self.input_deptwelcomingmessage()
        sleep(2)
        self.click_save_deptemwelcomingmessage()
        sleep(5)
        self.driver.refresh()
        sleep(2)

    def editDeptemmessage(self):
        sleep(3)
        self.click_deptemwelcomingmessage_page()
        sleep(2)
        self.cilik_edit_deptem_welcoming_message()
        sleep(2)
        self.input_edit_deptem_welcoming_message()
        sleep(3)
        self.click_sava_edit_deptem_welcoming_message()
        sleep(5)
        self.driver.refresh()
        sleep(2)

    def deleteDeptemmessage(self):
        sleep(3)
        self.click_deptemwelcomingmessage_page()
        sleep(2)
        self.click_delete_deptem_welcoming_message()
        sleep(2)
        self.click_sure_delete_deptem_welcoming_message()
        sleep(2)

    # 客户群欢迎语：新建/编辑/删除
    def addCpmessage(self):
        sleep(3)
        self.click_cpwelcomingmessage_page()
        sleep(2)
        self.click_cp_welcoming_message()
        sleep(2)
        self.input_welcoming_message()
        sleep(2)
        self.click_save_cp_welcoming_message()
        sleep(5)
        self.driver.refresh()
        sleep(2)

    def editCpmessage(self):
        sleep(3)
        self.click_cpwelcomingmessage_page()
        sleep(2)
        self.click_edit_cp_welcoming_message()
        sleep(2)
        self.input_edit_cp_welcoming_message()
        sleep(3)
        self.click_save_edit_cp_welcoming_message()
        sleep(5)
        self.driver.refresh()
        sleep(2)

    def deleteCpmessage(self):
        sleep(3)
        self.click_cpwelcomingmessage_page()
        sleep(2)
        self.click_delete_cp_welcoming_message()
        sleep(2)
        self.click_sure_delete_cp_welcoming_message()
        sleep(2)
