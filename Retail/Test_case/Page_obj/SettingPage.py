'''
@File  : SettingPage.py
@Author: Piepis
@Date  : 2020/2/10 19:30
@Desc  : 
'''

from Retail.Test_case.Page_obj.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Retail.Report.Log.log import Logger
import logging,time
from Retail.Test_case.models.Doyaml import DealYaml

log = Logger(__name__,CmdLevel=logging.INFO,FileLevel=logging.INFO)
key_word = DealYaml().yaml_to_str()['SettingPage']
# ProLang =(By.ID,'cate_item_2')
# PyItem = (By.XPATH,'//*[@id="cate_content_block_2"]/div[2]/ul/li[5]/a')
# settingButton = (By.XPATH,'//*[@id="span_userinfo"]/a[4]')
# profileBtn = (By.XPATH,'/html/body/app-root/div/mat-sidenav-container/mat-sidenav/div/app-drawer/mat-nav-list/a[2]/div')
# param = {'name': [(By.ID,'txt_name'),'test',(By.ID,'ddl_name'),'任何人',(By.ID,'chk_name'),'Y'],
#          'gender': [(By.XPATH, '//*[@id="Gender" and @value="0"]'),(By.ID, 'ddl_gender'), '任何人', (By.ID, 'chk_gender'), 'Y'],
#          'birthday':[(By.ID,'year'),'1984',(By.ID,'month'),'9',(By.ID,'day'),'14',(By.ID,'ddl_birth'),'仅好友',(By.ID,'chk_birth'),'Y'],
#          'hometown':[(By.ID,'s1'),'河北省',(By.ID,'s2'),'邯郸市',(By.ID,'ddl_home'),'仅好友',(By.ID,'chk_home'),'Y'],
#          'reside':[(By.ID,'reside1'),'北京市',(By.ID,'reside2'),'西城区',(By.ID,'ddl_reside'),'仅好友',(By.ID,'chk_reside'),'N'],
#          'marriage':[(By.ID,'ddl_block_marriage'),'已婚',(By.ID,'ddl_marriage'),'仅好友',(By.ID,'chk_marry'),'N'],
#          'position':[(By.ID,'txt_position'),'test',(By.ID,'ddl_position'),'保密',(By.ID,'chk_marry'),'N'],
#          'company':[(By.ID,'txt_company'),'test',(By.ID,'ddl_company'),'保密',(By.ID,'chk_company'),'N'],
#          'status':[(By.ID,'ddl_block_status'),'待业中',(By.ID,'ddl_status'),'保密',(By.ID,'chk_status'),'N']
#
#          }
# updateDone = (By.ID,'lit_tip')
# saveBtn = (By.ID,'btn_submit')
# upFilePage = (By.XPATH, '//mat-nav-list/a[3]/div')
# uploadBtn = (By.NAME, 'file')


class SetPage(BasePage):


    def mPage(self):
        self.onOver(key_word['ProLang'])
        self.click_loc(key_word['PyItem'])

    def basicSetPage(self):

        self.click_loc(key_word['settingButton'])
        self.click_loc(key_word['profileBtn'])



    def select(self, value,*loc ):
        ele = self.findElement(*loc)
        try:
            Select(ele).select_by_visible_text(value)
            time.sleep(2)
        except Exception:
            log.excep('下拉菜单选择失败，请检查')
        else:
            log.info('下拉选择%s' % value)






    def save_profile(self):
        # self.click_loc(profileBtn)
        #姓名
        self.inputValue(key_word['param']['name'][1],key_word['param']['name'][0])
        self.select(key_word['param']['name'][3],key_word['param']['name'][2])
        self.checkOnOff(key_word['param']['name'][5],key_word['param']['name'][4])
        #性别
        self.click_loc(key_word['param']['gender'][0])
        self.select(key_word['param']['gender'][2],key_word['param']['gender'][1])
        self.checkOnOff(key_word['param']['gender'][4],key_word['param']['gender'][3])
        #出生日期
        self.select(key_word['param']['birthday'][1],key_word['param']['birthday'][0])
        self.select(key_word['param']['birthday'][3],key_word['param']['birthday'][2])
        self.select(key_word['param']['birthday'][5], key_word['param']['birthday'][4])
        self.select(key_word['param']['birthday'][7],key_word['param']['birthday'][6])
        self.checkOnOff(key_word['param']['birthday'][9],key_word['param']['birthday'][8])
        #家乡
        self.select(key_word['param']['hometown'][1],key_word['param']['hometown'][0])
        self.select(key_word['param']['hometown'][3], key_word['param']['hometown'][2])
        self.select(key_word['param']['hometown'][5], key_word['param']['hometown'][4])
        self.checkOnOff(key_word['param']['birthday'][7],key_word['param']['birthday'][6])
        #现居住地
        self.select(key_word['param']['reside'][1],key_word['param']['reside'][0])
        self.select(key_word['param']['reside'][3],key_word['param']['reside'][2])
        self.select(key_word['param']['reside'][5],key_word['param']['reside'][4])
        self.checkOnOff(key_word['param']['reside'][7],key_word['param']['reside'][6])
        #婚姻
        self.select(key_word['param']['marriage'][1],key_word['param']['marriage'][0])
        self.select(key_word['param']['marriage'][3],key_word['param']['marriage'][2])
        self.checkOnOff(key_word['param']['marriage'][5],key_word['param']['marriage'][4])
        #职位
        self.inputValue(key_word['param']['position'][1],key_word['param']['position'][0])
        self.select(key_word['param']['position'][3],key_word['param']['position'][2])
        self.checkOnOff(key_word['param']['position'][5],key_word['param']['position'][4])
        #单位
        self.inputValue(key_word['param']['company'][1],key_word['param']['company'][0])
        self.select(key_word['param']['company'][3],key_word['param']['company'][2])
        self.checkOnOff(key_word['param']['company'][5],key_word['param']['company'][4])
        #工作状况
        self.select(key_word['param']['status'][1],key_word['param']['status'][0])
        self.select(key_word['param']['status'][3],key_word['param']['status'][2])
        self.checkOnOff(key_word['param']['status'][5],key_word['param']['status'][4])

        #保存
        self.click_loc(key_word['saveBtn'])
        info = self.getValue(key_word['updateDone'])
        return info


    # def upload_file(self):
    #     self.click_loc(settingButton)
    #     self.findElement(uploadBtn).send_keys(r'D:\JekinsProject\Retail\Report\Image\fail\test_prolang_fail.png')




















if __name__ == '__main__':
    pass