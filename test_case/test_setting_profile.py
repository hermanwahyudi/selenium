from main.function.setup import *
from main.activity.activity_login import *
from main.activity.activity_logout import *
from main.activity.activity_user_settings import *
import unittest

class TestProfile(unittest.TestCase):
    #Instance
    _site = "live"
    
    #dictionary user
    dict_user = {
        "email_1" : "tkpd.qc+35@gmail.com",
        "pass_1" : "123456789",
        "email_2" : "tkpd.qc+36@gmail.com",
        "pass_2" : "123456789"
    }

    #dictionary_valid
    
    def setUp(self):
        test_driver = ""
        self.driver = tsetup("firefox")
        self.flag = 0
        
    def test_edit_profile(self):
        print("> ::TEST EDIT PROFILE::")
        print("=======================")
        driver = self.driver
        
        #Object Activity
        loginValidate = loginActivity()
        logoutValidate = logoutActivity()
        editProfile = settingProfileActivity()
        #--
        
        loginValidate.do_login(driver, self.dict_user['email_2'], self.dict_user['pass_2'], self._site)
        editProfile.profile_data(driver, "input hobby here", "input messenger here", self.dict_user['pass_1'])
        logoutValidate.do_logout(driver, self._site)

    def test_edit_password(self):
        print("> ::TEST EDIT PASSWORD::")
        print("========================")
        driver = self.driver

        #Object Activity
        loginValidate = loginActivity()
        logoutValidate = logoutActivity()
        editPassword = settingProfileActivity()
        #--

        loginValidate.do_login(driver, self.dict_user['email_1'], self.dict_user['pass_1'], self._site)
        editPassword.profile_password(driver, self.dict_user['pass_1'], "123456789")
        logoutValidate.do_logout(driver, self._site)
        
    def test_edit_picture(self):
        print("> ::TEST EDIT PICTURE::")
        print("=======================")
        driver = self.driver

        #Object Activity
        loginValidate = loginActivity()
        logoutValidate = logoutActivity()
        editPicture = settingProfileActivity()
        #--

        loginValidate.do_login(driver, self.dict_user['email_2'], self.dict_user['pass_2'], self._site)
        editPicture.profile_picture(driver)
        logoutValidate.do_logout(driver, self._site)

    def tearDown(self):
        print("> ::Testing has done, the browser window will be closed soon::")
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(warnings='ignore')