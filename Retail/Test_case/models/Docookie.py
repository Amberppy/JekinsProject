from Retail.Test_case.models.Driver import WDriver
import time,json
from Retail.Test_case.Page_obj.base_page import BasePage
from Retail.Report.Log.log import Logger
import logging,os
from Retail.Config import Conf
from selenium.webdriver.common.by import By

log = Logger(__name__,CmdLevel=logging.INFO,FileLevel=logging.INFO)


account_text = (By.XPATH,'//span[@id ="span_userinfo"]/a[1]')
class DealCookie(BasePage):
    def getCookie(self):
        self.open()
        try:
            self.jScript('alert("请在30s内自行登陆！")')
            time.sleep(30)
        except Exception:
            log.excep('自行登录失败，无法获得登陆cookie')
        else:
            log.info('自行登陆成功，开始获取cookie...')

        try:
            cookies = self.driver.get_cookies()
            print('cookies',cookies)
            with open(os.path.join(Conf.dataPath,'cookie.txt'),'w') as f:
                f.write(json.dumps(cookies))
        except Exception:
            log.excep(('获取cookie失败，请查看%scookie文件')%Conf.dataPath)
        else:
            log.info('获取cookie成功，请查看cookie文件')

    def addCookie(self):
        self.driver.delete_all_cookies()
        self.open()
        try:
            with open(os.path.join(Conf.dataPath,'cookie.txt')) as f:
                cookie = json.loads(f.read())
            for c in cookie:
                self.driver.add_cookie(c)
            self.driver.refresh()
            accounts = self.getValue(account_text)

        except Exception:
            log.excep(('cookie自动登陆失败..%s')%cookie)
        else:
            log.info('cookie加载登陆成功！')
            if accounts == 'ppybear':
                log.info('用户登录成功')
            else:
                log.excep('用户登录不成功，请check[%s]'%accounts)










if __name__=='__main__':
    coo = DealCookie(driver=WDriver().fireFoxDriver(),url='https://www.cnblogs.com/')
    #coo.getCookie()
    coo.addCookie()








