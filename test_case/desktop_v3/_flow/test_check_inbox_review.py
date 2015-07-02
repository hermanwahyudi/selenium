from main.activity.desktop_v3.activity_login import *
from main.activity.desktop_v3.activity_logout import *
from main.activity.desktop_v3.activity_inbox_review import *
from utils.lib.user_data import *
from utils.function.setup import *
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium import webdriver
from pyvirtualdisplay import Display
import unittest

# display = Display(visible=0, size=(1024, 768))
# display.start()


class TestCheckInboxReview(unittest.TestCase):

    _site = "live"

    def setUp(self):
        self.driver = tsetup("phantomjs")

        # ff_profile = FirefoxProfile()
        # ff_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so','false')  #--Disable Flashplayer
        # ff_profile.set_preference('permissions.default.stylesheet', 2)
        # ff_profile.set_preference('permissions.default.image',2)  #--Disable Image
        #self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(300)



    def test_1_check_counter(self):
        print ("TEST #1 : Check Counter at Inbox Review")
        print ("========================================")
        driver = self.driver
        total_test_user = 0

        for each_user in user:

            email = user[total_test_user]['email']
            pwd = user[total_test_user]['pwd']
            print ("use = firefox")

            login = loginActivity()
            inbox_review = inboxReviewActivity()
            inbox_review.setObject(driver)
            logout = logoutActivity()

            login.do_login(driver, each_user, email, pwd, self._site)
            inbox_review.goto_inbox_review(self._site)
            inbox_review.check_counter_review()
            logout.do_logout(driver, self._site)
            total_test_user +=1

    def tearDown(self):
        print("Testing akan selesai dalam beberapa saat..")
        self.driver.quit()
        # display.stop()

if __name__ == '__main__':
    unittest.main(warnings='ignore')