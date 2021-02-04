from imp import reload

from selenium.webdriver.common.by import By
from commons.base_page import BasePage
from time import sleep
from config.readConfig import *
import config.readConfig as rc


class LoginPage(BasePage):
    """元素定位信息"""
    # _login = (By.LINK_TEXT, '登录')
    _name = (By.NAME, 'username')
    _password = (By.NAME, 'password')
    _login_button = (By.XPATH, '//*[@class="el-form-item__content"]/button')
    _qiwei3 = (By.XPATH, '//span[text()="企微管家3.0体验"]')

    _input_search = (By.XPATH, '//input[@placeholder="搜索关键字"]')
    _btn_search = (By.CSS_SELECTOR, '.el-input-group__append>button')
    _btn_manager = (By.XPATH, '//span[text()="管理"]/..')

    # 3.1uat登录界面
    _input_username = (By.CSS_SELECTOR, 'input[type="text"]')
    _input_pword = (By.CSS_SELECTOR, 'input[type="password"]')
    _btn_login = (By.XPATH, '//span[text()="登入后台 "]/..')
    
    # 切换新版后台
    # 立即体验按钮
    _btn_switch = (By.XPATH, '//span[text()="立即体验"]/..')

    '''元素定位层'''
    # 获取跳转登录界面元素
    # def get_login(self):
    #     return self.find_element(self._login)
    # 获取用户名输入框
    def get_username(self):
        return self.find_Element(self._name)
    # 获取密码输入框
    def get_password(self):
        return self.find_Element(self._password)
    # 获取登录按钮
    def get_loginbtn(self):
        return self.find_Element(self._login_button)
    # 获取企微3.0应用
    def get_app(self):
        return self.find_Element(self._qiwei3)

    # 测试环境登录
    def get_input_search(self):
        return self.find_Element(self._input_search)
    def get_btn_search(self):
        return self.find_Element(self._btn_search)
    def get_btn_manager(self):
        return self.find_Element(self._btn_manager)

    # 3.1uat登录界面
    def get_input_username(self):
        return self.find_Element(self._input_username)
    def get_input_pword(self):
        return self.find_Element(self._input_pword)
    def get_btn_login(self):
        return self.find_Element(self._btn_login)

    # 切换新版后台
    # 立即体验按钮
    def get_btn_switch(self):
        return self.find_Element(self._btn_switch)

    '''元素操作层'''
    # 跳转至登录界面
    # def click_login(self):
    #     return self.click_element(self.get_login())
    # 输入用户名
    def sendkey_username(self, name):
        return self.send_keys(self.get_username(), name)
    # 输入密码
    def sendkey_password(self, password):
        return self.send_keys(self.get_password(), password)
    # 点击登录
    def click_loginbtn(self):
        return self.click_element(self.get_loginbtn())
    # 点击进入企微
    def click_app(self):
        return self.move_click_element(self.get_app())

    def sendkey_input_search(self, value):
        return self.send_keys(self.get_input_search(), value)
    def click_btn_search(self):
        return self.click_element(self.get_btn_search())
    def click_btn_manager(self):
        return self.click_element(self.get_btn_manager())

    # 3.1uat登录界面
    def sendkeys_input_username(self, value):
        return self.send_keys(self.get_input_username(), value)
    def sendkeys_input_pword(self, value):
        return self.send_keys(self.get_input_pword(), value)
    def click_btn_login(self):
        return self.click_element(self.get_btn_login())

    # 切换新版后台
    # 立即体验按钮
    def click_btn_switch(self):
        return self.click_element(self.get_btn_switch())

    '''业务层'''
    # 登录操作
    def login(self, env=set_env, version=version):
        reload(rc)
        if env == 'test' and version == '3.0':
            self.testenv_login(TestEnv.url, TestEnv.username, TestEnv.password)
            self.switch_to_window()
        elif env == 'www' and version == '3.0':
            self.wwwenv_login(WWWEnv.url, WWWEnv.username, WWWEnv.password)
        elif rc.version == '3.1' and rc.set_env == 'test':
            self.version31_login(ver_31_test.url, ver_31_test.username, ver_31_test.password)
        elif rc.version == '3.1' and rc.set_env == 'www':
            self.version31_login(ver_31_www.url, ver_31_www.username, ver_31_www.password)
        try:
            self.check_exist_in_page('管理后台改版')
        except:
            pass
        else:
            print('122')
            self.click_btn_switch()
            sleep(2)
            

    def testenv_login(self, url, name, password):
        self._open(url)
        sleep(2)
        self.sendkey_username(name)
        sleep(2)
        self.sendkey_password(password)
        sleep(2)
        self.click_loginbtn()
        sleep(2)
        self.sendkey_input_search('baozun')
        sleep(1)
        self.click_btn_search()
        sleep(2)
        self.click_btn_manager()
        sleep(5)

    def wwwenv_login(self, url, name, password):
        self._open(url)
        sleep(2)
        self.sendkey_username(name)
        sleep(2)
        self.sendkey_password(password)
        sleep(2)
        self.click_loginbtn()
        sleep(2)
        self.click_app()
        sleep(3)

    def version31_login(self, url, name, password):
        self._open(url)
        sleep(2)
        self.sendkeys_input_username(name)
        sleep(2)
        self.sendkeys_input_pword(password)
        sleep(2)
        self.click_btn_login()
        sleep(3)

    def check_islogin(self):
        lists = ['客户管理', '群发消息', '引流码', '素材中心']
        for text in lists:
            self.check_exist_in_page(text)
        sleep(3)

