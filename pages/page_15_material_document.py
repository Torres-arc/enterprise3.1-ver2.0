from selenium.webdriver.common.by import By
from commons.base_page import BasePage
from time import sleep
import os
from pykeyboard import PyKeyboard



# 素材中心——文件
class DocumentMaterialPage(BasePage):
    # 元素定位信息
    # 添加文件
    _document_material_page = (By.XPATH, '//li[text()="文件"]')
    _add_document = (By.XPATH, '//span[text()="添加文件"]')
    _update_docoment_button = (By.XPATH, '//div[@class="el-upload__text"]')
    _sure_add_docement = (By.XPATH, '(//span[@class="dialog-footer"]/button)[2]')
    _confirm_sure_add_docement = (By.XPATH, '//button[@class="el-button el-button--default el-button--small el-button--primary "]')
    # 编辑
    _edit_document = (By.XPATH, '(//span[text()="编辑"])[1]')
    _edit_document_name = (By.XPATH, '//input[@placeholder="请输入分类名称"]')
    _sure_edit_document = (By.XPATH, '//button[@class="el-button el-button--default el-button--small el-button--primary "]')
    _assert_edit_document_name = (By.XPATH, '(//td[@class="el-table_1_column_2  "])[1]')
    # 删除
    _delete_document = (By.XPATH, '(//button[@class="el-button el-button--text el-button--medium"])[3]')
    _sure_delete_document = (By.XPATH, '//button[@class="el-button el-button--default el-button--small el-button--primary "]')

# 元素操作并进行封装
    # 点击跳转文件素材页面
    def click_document_material_page(self):
        # self.scroll_screen(self._document_material_page, 5)
        self.find_Element(self._document_material_page).click()
    # 添加文件封装
    def add_document(self):
        self.find_Element(self._add_document).click()
        self.find_Element(self._update_docoment_button).click()
        sleep(3)
        path1 = os.path.abspath(os.path.dirname(os.path.dirname(__file__)) + '//materials//pic//document.docx')
        k = PyKeyboard()
        k.tap_key(k.shift_key)
        k.type_string(path1)
        sleep(1)
        k.tap_key(k.enter_key)
        sleep(2)
        # os.system('D:\\huhuijun\\updateinfo\\uddocument.exe')
        sleep(2)
        self.find_Element(self._sure_add_docement).click()
        sleep(1)
        self.find_Element(self._confirm_sure_add_docement).click()
        sleep(1)
        self.check_exist_in_page('添加文件成功')

    # 编辑操作封装
    def edit_document(self):
        self.find_Element(self._edit_document).click()
        self.find_Element(self._edit_document_name).clear()
        self.find_Element(self._edit_document_name).send_keys('云夏的测试文件素材')
        sleep(1)
        self.find_Element(self._sure_edit_document).click()
        sleep(1)
        self.check_exist_in_page('修改名称成功')
        sleep(1)


    # 删除操作封装
    def delete_document(self):
        self.move_click_element(self.find_Element(self._delete_document))
        self.find_Element(self._sure_delete_document).click()



    '''业务层'''
    def addDocument(self):
        sleep(3)
        self.click_document_material_page()
        sleep(2)
        self.add_document()
        sleep(2)


    def editDocument(self):
        sleep(3)
        self.driver.refresh()
        sleep(1)
        self.edit_document()
        sleep(2)
        text = self.get_element_value(self.find_Element(self._assert_edit_document_name))
        if text == '云夏的测试文件素材':
            print('编辑成功')
        else:
            print('编辑失败')
        sleep(1)



    def deleteDocument(self):
        sleep(3)
        self.delete_document()
        sleep(1)
        self.check_exist_in_page('删除成功')
        sleep(1)
