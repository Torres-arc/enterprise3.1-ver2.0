# coding=utf-8
import unittest
from imp import reload
import time

import requests
from commons.APIRequest import *
from commons.HTMLTestRunner_cn import HTMLTestRunner
from generate import generate
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from commons.log import log
from commons.base_page import BasePage
import config.readConfig as rc
from commons.readfile import SwitchToExcel
from tkinter import *
import tkinter.messagebox

os.chdir(sys.path[0])


class MainPage:
    paths = os.path.dirname(os.path.abspath(__file__)) + '\\test_case'
    lists = os.listdir(paths)
    for i in lists:
        path = os.path.join(paths, i)
        if os.path.isdir(path):
            lists.remove(i)
        if not i.startswith("test"):
            lists.remove(i)
    v = []
    w = []
    origin_dict = {}
    example_dict = {}
    current_dict = {}
    root = Tk()
    version = ""
    env = ""
    var = IntVar()
    var2 = IntVar()
    var4 = IntVar()
    var3 = IntVar()
    btn = []

    def suitsget(self):
        dict = {}
        paths = os.path.dirname(os.path.abspath(__file__)) + '\\test_case'
        discover = unittest.defaultTestLoader.discover(paths, pattern="test*", top_level_dir=None)
        for test_cases in discover:
            for cases in test_cases:
                name = re.findall(r'<test[\S]+', str(cases))
                casea = re.findall(r'=[a-z][\S]+?>', str(cases))
                for i in casea:
                    namess = (name[0])[1:]
                    dict.setdefault((namess.split('.'))[0], []).append(i[1:-1])
        self.origin_dict = dict
        self.example_dict = dict
        return dict

    def select_version(self):
        if self.var.get() == 1:
            self.version = "3.0"
        elif self.var.get() == 2:
            self.version = "3.1"

    def select_env(self):
        if self.var2.get() == 1:
            self.env = "www"
        elif self.var2.get() == 2:
            self.env = "test"

    def getselect(self, test):
        index = self.lists.index(test)
        if test[:-3] in self.current_dict:
            del self.current_dict[test[:-3]]
            # print(self.current_dict)
        else:
            # print(self.current_dict)
            self.current_dict[test[:-3]] = self.example_dict[test[:-3]]
            # print(self.current_dict)
        if self.btn[index]['state'] == 'normal':
            self.btn[index]['state'] = 'disabled'
        if self.btn[index]['state'] == 'disabled':
            self.btn[index]['state'] = 'normal'

    def unselectall(self):
        for index, item in enumerate((self.lists[:-1])):
            self.v[index].set('')
            self.btn[index]['state'] = 'disabled'
        self.current_dict = {}
        # print(self.example_dict)

    def selectall(self):
        for index, item in enumerate((self.lists[:-1])):
            self.v[index].set(item)
            self.btn[index]['state'] = 'normal'
        self.current_dict = self.example_dict
        # print(self.example_dict)

    def unselectall1(self, lists):
        for index, item in enumerate(lists):
            self.w[index].set('')

    def selectall1(self, lists):
        for index, item in enumerate(lists):
            self.w[index].set(item)

    def showselect(self):
        # print(self.version)
        # print(self.env)
        self.version = '3.1'
        # if self.version == "3.1" and self.env == "test":
        #     tkinter.messagebox.showerror('错误', '目前3.1不支持测试环境运行自动化！')
        #     return
        self.root.destroy()
        print(self.env)
        start(self.version, self.env, self.current_dict, 0)

    def getcases(self, page, ttk):
        selected = [i.get() for i in self.w if i.get()]
        # print(selected)
        if selected:
            self.example_dict[page] = selected
            self.current_dict[page] = selected
            # print(self.current_dict)
        if not selected:
            index = self.lists.index((page + '.py'))
            # print(index)
            self.v[index].set('')
            self.btn[index]['state'] = 'disabled'
        ttk.destroy()

    def creat(self):
        self.root.title('客户运营自动化测试')
        Label(self.root, text="请选择测试版本:").grid(row=0, column=0)
        self.current_dict = self.suitsget()
        self.example_dict = self.suitsget()
        Radiobutton(self.root, text='企微3.0',
                    variable=self.var, value=1, command=self.select_version, state=DISABLED).grid(row=0, column=1)
        Radiobutton(self.root, text='企微3.1',
                    variable=self.var, value=2, command=self.select_version, state=DISABLED).grid(row=0, column=2)
        self.var.set(2)
        Label(self.root, text="请选择测试环境:").grid(row=1, column=0)
        Radiobutton(self.root, text='正式环境',
                    variable=self.var2, value=1, command=self.select_env).grid(row=1, column=1)
        Radiobutton(self.root, text='测试环境',
                    variable=self.var2, value=2, command=self.select_env).grid(row=1, column=2)
        # self.var2.set(1)
        Label(self.root, text="请选择需要进行测试的页面:").grid(row=2, column=0)
        Radiobutton(self.root, text='全选',
                    variable=self.var4, value=1, command=self.selectall).grid(row=2, column=1)
        Radiobutton(self.root, text='清空',
                    variable=self.var4, value=2, command=self.unselectall).grid(row=2, column=2)
        for i, item in enumerate(self.lists[:-1]):
            self.v.append(StringVar())
            Checkbutton(self.root, variable=self.v[-1], text=item, onvalue=item, offvalue='',
                        command=lambda a=item: self.getselect(a)).grid(row=i // 2 + 3, column=((i % 2) * 2), sticky=W)
            asa = Button(self.root, text='详细', command=lambda items=item: self.create_son(items))
            asa.grid(row=i // 2 + 3, column=(((i % 2) * 2) + 1))
            self.v[-1].set(item)
            self.btn.append(asa)
        Button(self.root, text="开始测试", command=self.showselect).grid(row=len(self.lists) - 5, column=1)
        self.root.mainloop()

    def create_son(self, page):
        ttk = Toplevel()
        ttk.title('客户运营自动化测试')
        lists = (self.suitsget())[page[:-3]]
        Label(ttk, text="请选择具体测试用例:").grid(row=1, column=2, sticky=W)
        Radiobutton(ttk, text='全选', variable=self.var3,
                    value=2, command=lambda lis=lists: self.selectall1(lis)).grid(row=2, column=1)
        Radiobutton(ttk, text='反选', variable=self.var3,
                    value=1, command=lambda lis=lists: self.unselectall1(lis)).grid(row=2, column=2)
        self.w.clear()
        # print(self.current_dict[page[:-3]])
        for i, info in enumerate(lists):
            self.w.append(StringVar())
            Checkbutton(ttk, variable=self.w[-1], text=info, onvalue=info,
                        offvalue='').grid(row=(i // 3) + 3, column=(i % 3) + 1, sticky=W)

            if info in self.current_dict[page[:-3]]:
                self.w[-1].set(info)
        Button(ttk, text="选择完成", command=lambda curpage=page[:-3]: self.getcases(curpage, ttk)) \
            .grid(row=len(lists) // 3 + 4, column=2)


# 发送测试邮件报告
def send_email(test_report, connect, sender, password, receiver, receiver2, receiver3, title, main, test_log):
    # 获取报告文件：'related'43行
    f = open(test_report, 'rb')
    f1 = open(test_log, 'rb')
    test_msg = f.read()
    test_msg1 = f1.read()
    subject = title
    body = '<p>' + main + '<p>'
    msgRoot = MIMEMultipart('related')
    # 邮件标题
    msgRoot['Subject'] = subject
    msgRoot['From'] = sender
    msgRoot['To'] = receiver
    # 邮件内容
    body = MIMEText(body, 'html', 'utf-8')  # 正文
    att = MIMEText(test_msg, 'base64', 'utf-8')  # 附件
    att1 = MIMEText(test_msg1, 'base64', 'utf-8')
    att['Content-Type'] = 'application/octet-stream'
    att.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', "企微测试报告.html.html"))
    att1['Content-Type'] = 'application/octet-stream'
    att1.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', "企微测试报告日志.xlsx"))
    msgRoot.attach(att)
    msgRoot.attach(att1)
    msgRoot.attach(body)

    smtp = smtplib.SMTP()
    smtp.connect(connect)
    smtp.login(sender, password)
    smtp.sendmail(sender, receiver, msgRoot.as_string())
    smtp.sendmail(sender, receiver2, msgRoot.as_string())
    smtp.sendmail(sender, receiver3, msgRoot.as_string())


# 收集测试用例
def create_my_suit(dicts):
    my_suit = unittest.TestSuite()
    paths = os.path.dirname(os.path.abspath(__file__)) + '\\test_case'
    for i in dicts.keys():
        discover = unittest.defaultTestLoader.discover(paths, pattern=(i + '.py'), top_level_dir=None)
        for test_suit in discover:
            for test_cases in test_suit:
                for a in test_cases:
                    if (str(a).split(' '))[0] in dicts[i]:
                        module = ((re.findall(r'\(\S+\.', str(a)))[0])[1:-1]
                        Class = ((re.findall(r'\.\S+', str(a)))[0])[1:-1]
                        # print(module)
                        # print(Class)
                        # print((str(a).split(' '))[0])
                        my_suit.addTest(unittest.TestLoader().loadTestsFromName(
                            '{}.{}.{}'.format(module, Class, (str(a).split(' '))[0])))
    return my_suit


def robotMsgSender(result):
    passed = result.success_count
    error = result.error_count
    fail = result.failure_count
    skip = result.skip_count
    total = int(passed) + int(error) + int(fail) + int(skip)
    percent = '{:.2%}'.format(int(passed) / int(total))
    send_url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=6b262540-2bd6-4d99-aa7b-0ad3b47a6534'
    headers = {"Content-Type": "text/plain"}
    text1 = "企微自动化测试结果摘要如下"
    text0 = ">运行版本:<font color=\"comment\"> {}</font> 目标环境:<font color=\"comment\"> {}</font>".format(rc.version,
                                                                                                      rc.set_env)
    text2 = ">时间:<font color=\"comment\"> {}</font>".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    text3 = ">总测试用例数:<font color=\"comment\"> {}例</font>".format(total)
    text4 = ">用例通过数:<font color=\"comment\"> {}例</font>".format(passed)
    text5 = ">用例错误数:<font color=\"comment\"> {}例</font>".format(error)
    text6 = ">用例失败数:<font color=\"comment\"> {}例</font>".format(fail)
    text7 = ">用例跳过数:<font color=\"comment\"> {}例</font>".format(skip)
    text8 = ">用例通过率:<font color=\"comment\"> {}</font>".format(percent)
    tlist = [text1, text0, text2, text3, text4, text5, text6, text7, text8]
    content = '\n'.join(tlist)
    content1 = "企微自动化测试已完成，请前往邮箱查看结果"
    send_values1 = {
        "msgtype": "text",
        "text": {
            "content": content1,
            "mentioned_mobile_list": ["18951576962", "17135107435", "18068267173"]
        },
    }
    send_values = {
        "msgtype": "markdown",
        "markdown": {
            "content": content
        },
    }
    requests.post(url=send_url, headers=headers, json=send_values1)
    requests.post(url=send_url, headers=headers, json=send_values)


def start(version, env, dicts, status):
    if status == 0:
        BasePage(object).set_ini('control', 'version', version)
        BasePage(object).set_ini('control', 'env', env)
        reload(rc)
        refreshInfo()
        log().info('Start')
        mysuit = create_my_suit(dicts)
    else:
        BasePage(object).set_ini('control', 'version', '3.1')
        BasePage(object).set_ini('control', 'env', 'www')
        reload(rc)
        refreshInfo()
        log().info('Start')
        mysuit = dicts
    runer = HTMLTestRunner(title="企微3.1测试报告", stream=open("企微测试报告.html", "wb"),
                           verbosity=2, retry=2, save_last_try=True)
    result = runer.run(mysuit)
    # BeautifulReport(mysuit).report(filename='测试报告', description='企微3.0web测试', report_dir='')
    log().info('Finish')
    robotMsgSender(result)
    path = os.path.dirname(os.path.abspath('企微测试报告.html') + '\\企微测试报告.html')
    SwitchToExcel().createExcel()
    dir = os.path.abspath(__file__) + '\\Log'
    file_list = os.listdir('.')
    for file in file_list:
        if file.startswith('企微自动化测试日志'):
            os.remove('企微自动化测试日志.xlsx')
        if file.startswith('工作簿'):
            src = os.path.join(os.path.abspath(os.path.dirname(__file__)), file)
            os.rename(src, '企微自动化测试日志.xlsx')
    path1 = (os.path.dirname(os.path.abspath(__file__)) + '\\企微自动化测试日志.xlsx')
    print(path1)
    send_email(test_report=path,
               connect='smtp.yunyou.top',
               sender='yunye@wshoto.com',
               password='WS123321',
               receiver='yunshu@wshoto.com',
               receiver2='yunhan@wshoto.com',
               receiver3='yunan@wshoto.com',
               title='企微测试报告.html',
               main='发送测试邮件，报告查收附件',
               test_log=path1)
    generate()


if __name__ == "__main__":
    MainPage().creat()
