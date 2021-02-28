from configparser import ConfigParser
import os
import json

conf = ConfigParser()
parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 读取文件
path = parentDirPath + '/config/config.ini'
conf.read(path, encoding='utf-8')


corpid = conf.get("control", "corpid")
corpsecret = conf.get("control", "corpsecret")

set_env = conf.get("control", "env")  # 参数有两个1: 'test' 2: 'www'
version = conf.get("control", "version")

if set_env == 'www':
    base_page = conf.get("control", "base_page_www")
elif set_env == 'test':
    base_page = conf.get("control", "base_page_test")

class WWWEnv:
    # 账号、密码
    username = conf.get("website", "username")
    password = conf.get("website", "password")
    # url
    url = conf.get("website", "url")


class ver_31_www:
    # 账号、密码
    username = conf.get("3.1_www", "username")
    password = conf.get("3.1_www", "password")
    # url
    url = conf.get("3.1_www", "url")


class ver_31_test:
    username = conf.get("3.1_test", "username")
    password = conf.get("3.1_test", "password")
    # url
    url = conf.get("3.1_test", "url")


class TestEnv:
    # 账号、密码
    username = conf.get("test_env", "username")
    password = conf.get("test_env", "password")
    # url
    url = conf.get("test_env", "url")


caps = {
    'browserName': 'chrome',
    'goog:loggingPrefs': {
        'browser': 'ALL',
        'driver': 'ALL',
        'performance': 'ALL',
    },
    'goog:chromeOptions': {
        'perfLoggingPrefs': {
            'enableNetwork': True,
        },
        'w3c': False,
    },
}


class clientpage:
    # 客户姓名
    name = conf.get('client_page', 'name')
    # 添加人姓名
    adder = conf.get('client_page', 'adder')
    # 标签及标签组
    tag_group31 = conf.get('client_page', 'tag_group31')
    tag31 = conf.get('client_page', 'tag31')


class lossremindpage:
    # 客户姓名
    name = conf.get('loss_remind_page', 'name')
    # 添加人姓名
    adder = conf.get('loss_remind_page', 'adder')
    # 标签及标签组
    tag_group = conf.get('loss_remind_page', 'tag_group')
    tag = conf.get('loss_remind_page', 'tag')


class clientcodepage:
    user = conf.get('client_code_page', 'user')
    user2 = conf.get('client_code_page', 'user2')
    actscene = conf.get('client_code_page', 'actscene')
    actscene2 = conf.get('client_code_page', 'actscene2')
    welcome = conf.get('client_code_page', 'welcome')
    welcome2 = conf.get('client_code_page', 'welcome2')
    picpath = conf.get('client_code_page', 'picpath')
    taglist = conf.get('client_code_page', 'taglist').split(" ")
    tel = conf.get('client_code_page', 'tel')
    web_msg = conf.get('client_code_page', 'web_msg')
    creator = conf.get('client_code_page', 'creator')
    stime = conf.get('client_code_page', 'stime')
    etime = conf.get('client_code_page', 'etime')


class addmessagepage:
    msg = conf.get('add_message_page', 'msg')
    sender = conf.get('add_message_page', 'sender')


class clientgroupcodepage:
    actname = conf.get('client_group_code_page', 'actname')
    actname1 = conf.get('client_group_code_page', 'actname1')
    actscene1 = conf.get('client_group_code_page', 'actscene1')
    actscene = conf.get('client_group_code_page', 'actscene')
    groupname = conf.get('client_group_code_page', 'groupname')
    groupname2 = conf.get('client_group_code_page', 'groupname2')
    editgname = conf.get('client_group_code_page', 'editgname')
    guide = conf.get('client_group_code_page', 'guide')
    date = conf.get('client_group_code_page', 'date')
    date2 = conf.get('client_group_code_page', 'date2')
    limit = conf.get('client_group_code_page', 'limit')
    limit2 = conf.get('client_group_code_page', 'limit2')
    search_key = conf.get('client_group_code_page', 'search_key')


class welcomingmsgpage:
    msg = conf.get('welcoming_msg_page', 'msg')
    staff = conf.get('welcoming_msg_page', 'staff')
    key = conf.get('welcoming_msg_page', 'key')
    edited_msg = conf.get('welcoming_msg_page', 'edited_msg')

class clientgrouppage:
    name = conf.get('client_group_page', 'name')
    master_name = conf.get('client_group_page', 'master_name')
    start_time = conf.get('client_group_page', 'start_time')
    end_time = conf.get('client_group_page', 'end_time')


class clienttagpage:
    tag_group = conf.get('client_tag_page', 'tag_group')
    tag1 = conf.get('client_tag_page', 'tag1')
    tag = json.loads(tag1)
    tag2 = conf.get('client_tag_page', 'tag2')
    tagn = json.loads(tag2)
    delete = conf.get('client_tag_page', 'delete')
    add = conf.get('client_tag_page', 'add')


class materialwebpage:
    title1 = conf.get('material_web_page', 'title1')
    pattitle = conf.get('material_web_page', 'parti_title')
    summary1 = conf.get('material_web_page', 'summary1')
    summary_changed = conf.get('material_web_page', 'summary_changed')
    title2 = conf.get('material_web_page', 'title2')
    summary2 = conf.get('material_web_page', 'summary2')
    main = conf.get('material_web_page', 'main')
    group = conf.get('material_web_page', 'group')
    path1 = conf.get('material_web_page', 'path1')
    path2 = conf.get('material_web_page', 'path2')
    link = conf.get('material_web_page', 'link')
    cgroup = conf.get('material_web_page', 'cgroup')


class materialaudiopage:
    group = conf.get('material_audio_page', 'group')
    path = conf.get('material_audio_page', 'path')
    name1 = conf.get('material_audio_page', 'name1')
    name2 = conf.get('material_audio_page', 'name2')


class materialvideopage:
    group = conf.get('material_video_page', 'group')
    path = conf.get('material_video_page', 'path')
    name = conf.get('material_video_page', 'name')
    sum = conf.get('material_video_page', 'sum')
    sum2 = conf.get('material_video_page', 'sum2')


class organizationpage:
    name = conf.get('organization_page', 'name')


class circleoffriends:
    key = conf.get('circle_of_friends', 'keys')
    start_time = conf.get('circle_of_friends', 'start_time')
    end_time = conf.get('circle_of_friends', 'end_time')
    staff = conf.get('circle_of_friends', 'staff')
    msg = conf.get('circle_of_friends', 'msg')
    msg2 = conf.get('circle_of_friends', 'msg2')


class MassHair:
    search_name = conf.get('mass_hair', 'search_name')
    test_material = conf.get('mass_hair', 'test_material')
    search_input = conf.get('mass_hair', 'search_input')


class missiontreasure:
    name = conf.get('mission_treasure', 'name')
    stime = conf.get('mission_treasure', 'stime')
    etime = conf.get('mission_treasure', 'etime')
    mname = conf.get('mission_treasure', 'mname')
    gname = conf.get('mission_treasure', 'gname')
    guide2 = conf.get('mission_treasure', 'guide2')
    guide = conf.get('mission_treasure', 'guide')
    people = conf.get('mission_treasure', 'people')
    user = conf.get('mission_treasure', 'user')
    msg = conf.get('mission_treasure', 'msg')
    code = conf.get('mission_treasure', 'code')
    link = conf.get('mission_treasure', 'link')
    path = conf.get('mission_treasure', 'path')
    rule = conf.get('mission_treasure', 'rule')
    welcome = conf.get('mission_treasure', 'welcome')


class pullnewclient:
    search_name = conf.get('pull_new_client', 'search_name')
    name = conf.get('pull_new_client', 'name')
    user = conf.get('pull_new_client', 'user')
    guide = conf.get('pull_new_client', 'guide')
    code = conf.get('pull_new_client', 'code')
    group_name = conf.get('pull_new_client', 'group_name')
    taglist = conf.get('pull_new_client', 'taglist').split(" ")
    ename = conf.get('pull_new_client', 'ename')
    euser = conf.get('pull_new_client', 'euser')
    eguide = conf.get('pull_new_client', 'eguide')
    egroup_name = conf.get('pull_new_client', 'egroup_name')

class keystogroup:
    search_name = conf.get('keys_to_group', 'search_name')
    name = conf.get('keys_to_group', 'name')
    guide = conf.get('keys_to_group', 'guide')
    code = conf.get('keys_to_group', 'code')
    keys = conf.get('keys_to_group', 'keys').split(" ")
    keys2 = conf.get('keys_to_group', 'keys2').split(" ")
    group_name = conf.get('keys_to_group', 'group_name')
    ename = conf.get('keys_to_group', 'ename')
    eguide = conf.get('keys_to_group', 'eguide')
    egroup_name = conf.get('keys_to_group', 'egroup_name')


class creatgroupbytags:
    name = conf.get('creat_group_by_tags', 'name')
    task_name = conf.get('creat_group_by_tags', 'task_name')
    staff = conf.get('creat_group_by_tags', 'staff')
    guide = conf.get('creat_group_by_tags', 'guide')
    code = conf.get('creat_group_by_tags', 'code')
    stime = conf.get('creat_group_by_tags', 'stime')
    etime = conf.get('creat_group_by_tags', 'etime')

class groupsop:
    search_name = conf.get('group_sop', 'search_name')
    name = conf.get('group_sop', 'name')
    group = conf.get('group_sop', 'group')
    msg_name = conf.get('group_sop', 'msg_name')
    stime = conf.get('group_sop', 'stime')
    etime = conf.get('group_sop', 'etime')
    msg = conf.get('group_sop', 'msg')
    ename = conf.get('group_sop', 'ename')
    egroup = conf.get('group_sop', 'egroup')
    emsg_name = conf.get('group_sop', 'emsg_name')
    estime = conf.get('group_sop', 'estime')
    eetime = conf.get('group_sop', 'eetime')
    emsg = conf.get('group_sop', 'emsg')