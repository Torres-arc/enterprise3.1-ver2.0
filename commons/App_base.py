from airtest.core.android import Android
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from PIL import Image
from airtest.core.api import *


class AppBase(object):
    def poco_screenshots(self, bound, save_as_path):
        a, b, c, d = bound
        # 元素截图
        img = self.pic_screen()
        xy = img.size
        x = xy[0]
        y = xy[1]
        print(x, y)
        x1 = d
        y1 = a
        x2 = b
        y2 = c
        print(x1, y1, x2, y2)
        print(int(x * x1), int(y * y1), int(x * x2), int(y * y2))
        cropped = img.crop((int(x * x1), int(y * y1), int(x * x2), int(y * y2)))  # (left, upper, right, lower)
        if '.png' not in save_as_path:
            save_as_path = os.path.join(save_as_path, '%s.png' % time.strftime("%H_%M_%S", time.localtime(time.time())))
            print(save_as_path)
        cropped.save(save_as_path)
        # os.remove(image_path)  # 删除原图
        return save_as_path

    def pic_screen(self):
        image_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)) + '\\img\\test.png')
        print(image_path)
        if not os.path.isfile(image_path):
            os.mkdir(os.path.dirname(image_path))
        snapshot(image_path)  # 将当前截图保存到image_path
        img = Image.open(image_path)  # 打开图片：image_path
        return img

    def touch_click_xy(self, pos):
        # 获取手机屏幕尺寸
        xy = self.pic_screen().size
        x = xy[0]
        y = xy[1]
        print(x, y)
        return pos[0] * x * 2, pos[1] * y * 2

    def app_restart(self, package):  # APP重启
        connect_device("Android:///?cap_method=JAVACAP&&touch_method=ADBTOUCH&&ori_method=ADBORI")
        stop_app(package)
        start_app(package)

    def switch_other_work(self, work_string):  # 切换到企业,返回当前页面的活动，
        poco = self.get_poco()
        poco(text="其他企业").wait_for_appearance(20)
        poco(text="其他企业").click()
        poco(text=work_string).wait_for_appearance(20)
        if not poco(text=work_string).parent().sibling('com.tencent.wework:id/bim').exists():
            poco(text=work_string).click()
        else:
            poco("com.tencent.wework:id/hxb").click()
        return Android().get_top_activity()[1]

    def get_poco(self):
        return AndroidUiautomationPoco(
            use_airtest_input=True,
            screenshot_each_action=False)

    def process_flashback(self, top_activity):  # 处理首页闪退
        while not top_activity == '.launch.WwMainActivity':
            start_app("com.tencent.wework")
            sleep(3)

    def del_wc_customer(self, name):
        connect_device("Android:///?cap_method=JAVACAP&&touch_method=ADBTOUCH&&ori_method=ADBORI")
        poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        stop_app("com.tencent.mm")
        start_app("com.tencent.mm")
        poco('com.tencent.mm:id/f8y').click()
        poco('com.tencent.mm:id/bhn').set_text(name)
        sleep(3)
        poco(text='江苏微盛网络科技有限公司').click()
        poco('android.support.v7.widget.LinearLayoutCompat').click()
        poco('com.tencent.mm:id/f3y').click()
        poco('android.support.v7.widget.LinearLayoutCompat').click()
        poco(text='删除').click()
        poco(text="删除").click()

    def del_wwc(self, target):
        connect_device("Android:///?cap_method=JAVACAP&&touch_method=ADBTOUCH&&ori_method=ADBORI")
        poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        stop_app("com.tencent.wework")
        start_app('com.tencent.wework')
        sleep(5)
        while not poco(text=target):
            poco().swipe('up')
        poco(text=target).click()
        poco('com.tencent.wework:id/hxm').click()
        poco('com.tencent.wework:id/ehs').click()
        poco('com.tencent.wework:id/hxm').click()
        poco(text='删除').click()
        poco(text='确认删除').click()
        stop_app('com.tencent.wework')