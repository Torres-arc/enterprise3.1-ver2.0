# -*- coding: UTF-8 -*-
# @Time    : 2021/1/8 17:18 
# @Author  : Torres 
# @File    : generate.py
import os
import re
import time

from lxml import etree
from bs4 import BeautifulSoup
import xlwings as xw

dicts = {'test_01_clients': ['test_01_searchByClientName', 'test_02_searchByAdder', 'test_03_searchByTag',
                             'test_04_buttonReset', 'test_05_remindTags'],
         'test_02_client_groups': ['test_01_searchByGroupName', 'test_02_searchByMasterName',
                                   'test_03_searchByCreateTime', 'test_04_buttonReset', 'test_05_exportGroupsList'],
         'test_03_client_tags': ['test_01_addNewTagGroup', 'test_02_editTagGroup', 'test_03_deleteTagGroup'],
         'test_04_add_message': ['test_01_addmessage_wb', 'test_02_addmessage_web', 'test_03_addmessage_pic',
                                 'test_04_addmessage_pos', 'test_05_addmessage_mini', 'test_06_addmessage_text_group',                                 'test_07_addmessage_web_group', 'test_08_addmessage_pic_group',
                                 'test_09_addmessage_pos_group', 'test_10_addmessage_mini_group'],
         'test_05_send_record': ['test_02_serachBytext', 'test_03_serachBytype', 'test_04_serachBytime',
                                 'test_05_reset'],
         'test_06_employee_code': ['test_02_searchByUser', 'test_05_searchByActScene', 'test_07_searchByCreateTime',
                                   'test_08_resetSearch', 'test_09_addSingleClientWebCode', 'test_10_checkCodeInfo',
                                   'test_11_editCode', 'test_12_copyLinkCode', 'test_13_integratedTest',
                                   'test_14_deleteCode', 'test_15_addSingleClientPicCode',
                                   'test_16_addSingleClientMiniCode', 'test_17_addBatchSingleClientMiniCode',
                                   'test_18_addBatchSingleClientPicCode', 'test_19_addBatchSingleClientWebCode',
                                   'test_20_addMultiClientWebCode', 'test_21_addMultiClientMiniCode',
                                   'test_22_addMultiClientPicCode', 'test_23_createCodeInBatch',
                                   'test_24_deleteCodeInBatch', 'test_25_exportCodeInfo'],
         'test_07_client_group_code': ['test_01_addClientgroupcode', 'test_02_manageClientgroupcode',
                                       'test_03_editClientgroupcode', 'test_04_deleteClientgroupcode',
                                       'test_05_selectClientgroupcode'],
         'test_08_welcoming_message': ['test_01_addEmwelcomingmessage', 'test_02_editEmwelcomingmessage',
                                       'test_03_deleteEmwelcomingmessage', 'test_04_addDeptemwelcomingmessage',
                                       'test_05_editDeptemwelcomingmessage', 'test_06_deleteDeptemwelcomingmessage'],
         'test_09_material_poster': ['test_01_add_group', 'test_02_add_poster', 'test_03_search_poster',
                                     'test_04_move_group', 'test_05_edit_poster', 'test_06_del_poster',
                                     'test_07_new_group_add_child', 'test_08_del_new_group'],
         'test_100_red_record': ['test_01_btn_search'],
         'test_10_material_text': ['test_01_add_group', 'test_02_add_text', 'test_03_search_text', 'test_04_move_group',
                                   'test_05_edit_text', 'test_06_del_text', 'test_07_new_group_add_child',
                                   'test_08_del_new_group'],
         'test_11_material_picture': ['test_01_add_group', 'test_02_add_pic', 'test_03_search_pic',
                                      'test_04_move_group', 'test_05_edit_pic', 'test_06_del_pic',
                                      'test_07_new_group_add_child', 'test_08_del_new_group'],
         'test_12_material_web': ['test_01_addGroup', 'test_02_addCustomizeWeb', 'test_03_addExternalLinkWeb',
                                  'test_04_editWeb', 'test_05_searchWeb', 'test_06_deleteWeb', 'test_07_addChildGroup',
                                  'test_08_deleteGroup'],
         'test_13_material_audio': ['test_01_AddGroup', 'test_02_addAudio', 'test_03_editAudio', 'test_04_deleteAudio',
                                    'test_05_deleteGroup'],
         'test_14_material_video': ['test_01_AddGroup', 'test_02_addvideo', 'test_03_editVideo', 'test_04_deleteVideo',
                                    'test_05_deleteGroup'],
         'test_15_material_document': ['test_01_addDocumentmaterial', 'test_02_editDocumentmaterial',
                                       'test_03_deleteDocumentmaterial'],
         'test_16_material_small_routine': ['test_01_addSmallroutinematerial', 'test_02_editSmallroutinematerial',
                                            'test_03_deleteSmallroutinematerial'],
         'test_17_chat_toolbar': ['test_01_getnum', 'test_02_check_button'],
         'test_18_circle_of_friends': ['test_01_searchByKeys', 'test_02_searchByTime', 'test_03_addReleaseNews',
                                       'test_04_editReleaseNews', 'test_05_deleteReleaseNews'],
         'test_19_organization': ['test_01_searchStaff'],
         'test_20_mission_treasure': ['test_01_searchByName', 'test_02_searchByDate', 'test_03_resetSearch',
                                      'test_04_addMission'],
         'test_21_group_fission': ['test_01_searchByName', 'test_02_searchByDate', 'test_03_resetSearch',
                                   'test_04_addMission'],
         'test_22_pull_new_client_into_group': ['test_01_searchByName', 'test_02_createAct', 'test_03_checkDetails',
                                                'test_04_editAct', 'test_05_deleteAct'],
         'test_50_loss_remind': ['test_01_searchByClientName', 'test_03_searchByTag', 'test_04_buttonReset']}


def generate():
    soup = BeautifulSoup(open('企微测试报告.html', encoding='utf-8'), features='html.parser')
    asaa = soup.select('div[style="float: left"] p:first-child')
    curtime = (re.findall(r'\S*\s\S*(?=</p>)', str(asaa)))[0]
    failclasslist = soup.select('tr[id*="ft"]>td>div.testcase')
    fail_list = []
    err_list = []
    for i in failclasslist:
        fail_list.append((i.text.split(':'))[0])
    errclasslist = soup.select('tr[id*="et"]>td>div.testcase')
    for i in errclasslist:
        err_list.append((i.text.split(':'))[0])
    classs = soup.select('tr[class*="Class"]>td:first-child')
    lsits = []
    for i in classs:
        lsits.append((i.text.split('.'))[0])

    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False
    wb = app.books.open('D:/tst/工作簿1.xlsx')
    curs = wb.sheets['测试情况']
    count = 1
    while curs.range(1, count).value is not None:
        print(count, curs.range(1, count).value)
        count += 1
    print(curtime)
    print(count)
    curs.range(1, count).value = curtime
    for i in err_list:
        row = 1
        while True:
            if curs.range(row, 2).value == i:
                curs.range(row, count).color = (255, 255, 0)
                break
            row += 1
    for i in fail_list:
        row = 1
        while True:
            if curs.range(row, 2).value == i:
                curs.range(row, count).color = (255, 0, 0)
                break
            row += 1
    curs.autofit()
    time.sleep(3)
    wb.save()
    wb.close()
    app.kill()

def init_excel():
    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False
    wb=app.books.open('D:/tst/工作簿1.xlsx')
    # wb.sheets['Sheet1'].name = '测试情况'
    curs = wb.sheets['测试情况']
    curs.range('A1').value = '测试页面'
    curs.range('b1').value = '测试用例'
    curs.range('c1').value = '测试时间'
    curs.autofit()
    count = 2
    for i in dicts.keys():
        a_count = str(count)
        curs.range('a' + str(count)).value = i
        for x in dicts[i]:
            curs.range('b' + str(count)).value = x
            count += 1
        b_count = str(count-1)
        curs.range('a'+str(a_count)+":"+'a'+str(b_count)).merge()
    time.sleep(3)
    wb.save()
    wb.close()
    app.kill()


if __name__ == '__main__':
    generate()
