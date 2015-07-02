from utils.function.setup import *
from utils.lib.user_data import *
from main.activity.desktop_v3.activity_login import *
from main.activity.desktop_v3.activity_logout import *
from main.activity.desktop_v3.activity_user_settings import *
import unittest

class TestNotification(unittest.TestCase):
    #Instance
    _site = "live"

    def setUp(self):
        test_driver = ""
        self.driver = tsetup("firefox")
        self.flag = 0

    def test_edit_notification(self):
        print("> ::TEST EDIT NOTIFICATION::")
        print("============================")
        driver = self.driver
        self.user= user8

        email = self.user['email']
        pwd = self.user['password']

        #Object Activity
        loginValidate = loginActivity()
        logoutValidate = logoutActivity()
        editNotification = settingNotificationActivity()
        #--

        loginValidate.do_login(driver, self.user, email, pwd, self._site)
        editNotification.notif_setting(driver)
        logoutValidate.do_logout(driver, self._site)

    def tearDown(self):
        print("> ::Testing has done, the browser window will be closed soon::")
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(warnings = 'ignore')