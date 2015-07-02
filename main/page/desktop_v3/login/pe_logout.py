import time,os,sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/'))
from main.page.base import BasePage
from selenium.webdriver.common.by import By

class LogoutPage(BasePage):

    _pl= "logout.pl"

    def check_current_url(self):
        #print(self.driver.current_url)
        if self.driver.current_url == 'https://www.tokopedia.com/':
            print("Saat ini berada di %s , dan bersiap Logout.." %self.driver.current_url)
            time.sleep(3)

    def open(self, site=""):
        self._open(site, self._pl)