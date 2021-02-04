import os
import xlwings as xw
import datetime
import time


class SwitchToExcel:
    def read_file(self, path, sheetname, ranges, type=None):
        app = xw.App(visible=False, add_book=False)
        app.display_alerts = False
        app.screen_updating = False
        wb = app.books.open(path)
        if type is None:
            value = wb.sheets[sheetname].range(ranges).value
            wb.close()
            app.quit()
            return value
        elif type == 'down':
            value = wb.sheets[sheetname].range(ranges).expand('down').value
            wb.close()
            app.quit()
            return value

    def new_file(self, testdir):
        list = os.listdir(testdir)
        list.sort(key=lambda fn: os.path.getmtime(testdir + '\\' + fn))
        filetime = datetime.datetime.fromtimestamp(os.path.getmtime(testdir + '\\' + list[-1]))
        filepath = os.path.join(testdir, list[-1])
        print("最新修改的文件(夹)：" + list[-1])
        print("时间：" + filetime.strftime('%Y-%m-%d %H-%M-%S'))
        return filepath

    def createExcel(self):
        path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)) + '\\Log')
        path1 =self.new_file(path)
        app = xw.App(visible=False, add_book=False)
        app.display_alerts = False
        app.screen_updating = False
        filepath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        wb = app.books.add()
        wb.sheets['Sheet1'].name = 'log'
        wb.sheets['log'].range('A1').value = '运行时间'
        # wb.sheets['log'].range('a1:a5').merge()
        wb.sheets['log'].range('b1').value = '测试页面'
        wb.sheets['log'].range('c1').value = '测试用例'
        wb.sheets['log'].range('d1').value = '调用函数'
        wb.sheets['log'].range('e1').value = '日志等级'
        wb.sheets['log'].range('f1').value = '用例运行信息'
        wb.sheets['log'].autofit()
        wb.sheets['log'].range('f1').column_width = 77
        f = open(path1, encoding='utf-8')
        line = f.readline()
        count = 2
        while line:
            if line.startswith('2020'):
                msg = line.split(' ')
                wb.sheets['log'].range('a' + str(count)).value = msg[0]
                wb.sheets['log'].range('e' + str(count)).value = msg[2]
                if msg[2] == 'INFO':
                    wb.sheets['log'].range('e' + str(count)).color = (255, 255, 0)
                if msg[2] == 'ERROR':
                    wb.sheets['log'].range('e' + str(count)).color = (255, 0, 0)
                if msg[1].startswith('base'):
                    a = msg[3].split('\\')
                    # wb.sheets['log'].range('b' + str(count)).value = a[-1]
                    string1 = "".join(msg[6:])
                    wb.sheets['log'].range('f' + str(count)).value = string1[:-1]
                    wb.sheets['log'].range('d' + str(count)).value = a[-1]+ ':' +msg[5] + '[line:' + msg[4] + ']'
                else:
                    wb.sheets['log'].range('b' + str(count)).value = (msg[1].split('['))[0]
                    wb.sheets['log'].range('f' + str(count)).value = msg[3]
                    if msg[3].startswith('开始执行:用例') or msg[3].startswith('开始执行 用例'):
                        curstart = count
                        wb.sheets['log'].range('c' + str(count)).value = (msg[3].split('-'))[1:]
                    if msg[3].startswith('执行结束:用例') or msg[3].startswith('执行结束 用例'):
                        curend = count
                        wb.sheets['log'].range('c'+str(curstart)+":"+'c'+str(curend)).merge()
                    if msg[3].endswith('自动化测试') and msg[3].startswith('开始执行'):
                        curstart1 = count
                        # wb.sheets['log'].range('b' + str(count)).value = (msg[3].split('-'))[-1]
                    if msg[3].endswith('自动化测试') and msg[3].startswith('执行结束'):
                        curend1 = count
                        wb.sheets['log'].range('b' + str(curstart1) + ":" + 'b' + str(curend1)).merge()
                wb.sheets['log'].autofit()
                # print(line, end='')
                if msg[3].startswith('Finish'):
                    break
                line = f.readline()
                count += 1
            else:
                wb.sheets['log'].range('f' + str(count)).value = line
                line = f.readline()

        time.sleep(5)
        wb.save()
        wb.close()
        app.quit()
        f.close()
