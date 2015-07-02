from utils.function.setup import *
from utils.lib.user_data import *
from main.activity.desktop_v3.activity_login import *
from main.activity.desktop_v3.activity_logout import *
from main.activity.desktop_v3.activity_user_settings import *
import unittest

class TestProfile(unittest.TestCase):
    #Instance
    _site = "beta"

    def setUp(self):
        test_driver = ""
        self.driver = tsetup("chrome")
        self.flag = 0
        
    def test_edit_profile(self):
        print("> ::TEST EDIT PROFILE::")
        print("=======================")
        driver = self.driver
        self.user= user8

        email = self.user['email']
        pwd = self.user['password']
        
        #Object Activity
        loginValidate = loginActivity()
        logoutValidate = logoutActivity()
        editProfile = settingProfileActivity()
        #--
        
        loginValidate.do_login(driver, self.user, email, pwd, self._site)
        editProfile.profile_data(driver, "input hobby here", "input messenger here", pwd)
        logoutValidate.do_logout(driver, self._site)

    def test_edit_password(self):
        print("> ::TEST EDIT PASSWORD::")
        print("========================")
        driver = self.driver
        self.user= user8

        email = self.user['email']
        pwd = self.user['password']

        #Object Activity
        loginValidate = loginActivity()
        logoutValidate = logoutActivity()
        editPassword = settingProfileActivity()
        #--

        loginValidate.do_login(driver, self.user, email, pwd, self._site)
        editPassword.profile_password(driver, pwd, "123456789")
        logoutValidate.do_logout(driver, self._site)
        
    def test_edit_picture(self):
        print("> ::TEST EDIT PICTURE::")
        print("=======================")
        driver = self.driver
        self.user= user8

        email = self.user['email']
        pwd = self.user['password']

        #Object Activity
        loginValidate = loginActivity()
        logoutValidate = logoutActivity()
        editPicture = settingProfileActivity()
        #--

        loginValidate.do_login(driver, self.user, email, pwd, self._site)
        editPicture.profile_picture(driver)
        logoutValidate.do_logout(driver, self._site)

    def tearDown(self):
        print("> ::Testing has done, the browser window will be closed soon::")
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(warnings='ignore')