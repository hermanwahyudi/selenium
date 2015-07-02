__author__ = 'QC1'


import unittest
from main.activity.android.andr_activity_login import *
from main.activity.android.andr_activity_logout import *
from time import sleep
from utils.function.setup import *
from utils.lib.user_data import *
from appium import webdriver

class TestTokopediaLoginAndroid(unittest.TestCase):
    # Class to run tests for Tokopedia android application


    def setUp(self):
        # # Setup for the test
        # desired_caps = {}
        # desired_caps['platformName'] = 'Android'
        # # platformVersion can be used to select desired emulator
        # desired_caps['platformVersion'] = '4.4.4'
        # desired_caps['deviceName'] = 'Google Nexus 5'
        # # Returns abs path relative to this file and not cwd
        # # desired_caps['app'] will reinstall the app. comment it if you already installed Tokopedia application
        # # desired_caps['app'] = os.path.abspath('D:\AndroidApps\Tokopedia.apk')
        # desired_caps['appPackage'] = 'com.tokopedia.tkpd'
        # desired_caps['appActivity'] = '.SplashScreen'
        # self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        #
        # # reset is used to erase previous session in the application
        # self.driver.reset()
        self.driver = tsetup_andr()

    def test_1_login_seller(self):
        print("Tokopedia Account Test #1 : Testing for seller login")
        sleep(2)

        #Object Activity
        login_activity = ActivityLogin()
        logout_activity = ActivityLogout()

        login_activity.do_login(self.driver, AndroidSeller["email"], AndroidSeller["password"])
        login_activity.seller_login_validation(self.driver)

        self.driver.keyevent(4)
        sleep(1)
        logout_activity.do_logout(self.driver)

    def test_2_login_empty(self):
        print("Tokopedia Account Test #2 : Testing login without email and password")
        sleep(2)

        login_activity = ActivityLogin()

        login_activity.do_login_input_empty(self.driver)

    def tearDown(self):
        print("Testing done. The test environment will be closed in a few moment. . . .")
        sleep(5)
        self.driver.quit()

#---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTokopediaLoginAndroid)
    unittest.TextTestRunner(verbosity=2).run(suite)