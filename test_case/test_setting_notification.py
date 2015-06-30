from main.function.setup import *
from main.activity.activity_login import *
from main.activity.activity_logout import *
from main.activity.activity_user_settings import *
import unittest

class TestNotification(unittest.TestCase):
    #Instance
    _site = "live"

    #dictionary user
    dict_user = {
        "email_1" : "tkpd.qc+35@gmail.com",
        "pass_1" : "123456789",
        "email_2" : "tkpd.qc+36@gmail.com",
        "pass_2" : "123456789"
    }

    def setUp(self):
        test_driver = ""
        self.driver = tsetup("firefox")
        self.flag = 0

    def test_edit_notification(self):
        print("> ::TEST EDIT NOTIFICATION::")
        print("============================")
        driver = self.driver

        #Object Activity
        loginValidate = loginActivity()
        logoutValidate = logoutActivity()
        editNotification = settingNotificationActivity()
        #--

        loginValidate.do_login(driver, self.dict_user['email_1'], self.dict_user['pass_1'], self._site)
        editNotification.notif_setting(driver)
        logoutValidate.do_logout(driver, self._site)

    def tearDown(self):
        print("> ::Testing has done, the browser window will be closed soon::")
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(warnings = 'ignore')