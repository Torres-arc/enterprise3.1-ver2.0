from selenium.webdriver.common.by import By
from commons.base_page import BasePage
from time import sleep
import os
from pykeyboard import PyKeyboard


# 素材中心——文件
class SmallRoutineMaterialPage(BasePage):
    # 元素定位信息
    # 添加小程序
    _small_routine_material_page = (By.XPATH, '//li[text()="小程序"]')
    _add_small_routine = (By.XPATH, '//span[text()="添加小程序"]')
    _input_small_routine_name = (By.XPATH, '//input[@placeholder="请输入小程序标题"]')
    _input_small_routine_appid = (By.XPATH, '//input[@placeholder="请输入小程序appid"]')
    _input_small_routine_page_address = (By.XPATH, '//input[@placeholder="请输入小程序page路径"]')
    _update_small_routine_image = (By.XPATH, '//div[@class="el-upload__text"]')
    _sure_add_small_routine_page = (By.XPATH, '//span[@class="dialog-footer"]/button[2]')
    _confirm_sure_add_small_routine = (By.XPATH, '//button[@class="el-button el-button--default el-button--small el-button--primary "]')
    # 编辑
    _edit_small_routine = (By.XPATH, '(//i[@class="el-tooltip el-icon-edit item"])[1]')
    _input_edit_small_routine_name = (By.XPATH, '//input[@placeholder="请输入小程序标题"]')
    _finish_edit_small_routine_page = (By.XPATH, '//span[text()="完 成"]')
    _confirm_finish_edit_small_routine_page = (By.XPATH, '//button[@class="el-button el-button--default el-button--small el-button--primary "]')
    _assert_edit_small_routine = (By.XPATH, '(//div[@class="text-limit"])[1]')
    # 删除
    _delete_small_routine = (By.XPATH, '(//i[@class="el-tooltip el-icon-delete item"])[1]')
    _sure_delete_small_routine = (By.XPATH, '//button[@class="el-button el-button--default el-button--small el-button--primary "]')


# 元素操作并进行封装
    # 点击跳转小程序素材页面
    def click_small_routine_material_page(self):
        self.find_Element(self._small_routine_material_page).click()

    # 添加小程序封装
    def add_small_routine(self):
        self.click_element(self.find_Element(self._add_small_routine))
        self.send_keys(self.find_Element(self._input_small_routine_name), '云夏的测试小程序素材')
        self.send_keys(self.find_Element(self._input_small_routine_appid), 'wx81190b2c32e2c2d3')
        self.send_keys(self.find_Element(self._input_small_routine_page_address), 'pages/missionList.htm')
        self.click_element(self.find_Element(self._update_small_routine_image))
        sleep(2)
        path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)) + '//materials//pic//photo.png')
        k = PyKeyboard()
        k.tap_key(k.shift_key)
        k.type_string(path)
        sleep(1)
        k.tap_key(k.enter_key)
        sleep(2)
        # os.system('D:\\huhuijun\\updateinfo\\udphoto.exe')
        self.scroll_screen(self.find_Element(self._sure_add_small_routine_page), -10)
        sleep(1)
        self.click_element(self.find_Element(self._sure_add_small_routine_page))
        sleep(2)
        self.click_element(self.find_Element(self._confirm_sure_add_small_routine))


    # 编辑操作封装
    def edit_small_routine(self):
        self.click_element(self.find_Element(self._edit_small_routine))
        sleep(1)
        self.find_Element(self._input_edit_small_routine_name).clear()
        self.send_keys(self.find_Element(self._input_edit_small_routine_name), '编辑后云夏的测试小程序素材')
        self.click_element(self.find_Element(self._finish_edit_small_routine_page))
        sleep(1)
        self.click_element(self.find_Element(self._confirm_finish_edit_small_routine_page))




    # 删除操作封装
    def delete_small_routine(self):
        self.click_element(self.find_Element(self._delete_small_routine))
        sleep(1)
        self.click_element(self.find_Element(self._sure_delete_small_routine))




    '''业务层'''
    def addSmallroutine(self):
        sleep(3)
        self.add_small_routine()
        sleep(1)
        print('成功添加小程序素材')



    def editSmallroutine(self):
        sleep(3)
        self.edit_small_routine()
        sleep(1)
        text = self.get_element_value(self.find_Element(self._assert_edit_small_routine))
        if text == '编辑后云夏的测试小程序素材':
            print('编辑成功')
        else:
            print('编辑失败')
        sleep(1)



    def deleteSmallroutine(self):
        sleep(3)
        self.delete_small_routine()
        sleep(1)
        self.check_exist_in_page('删除成功')
