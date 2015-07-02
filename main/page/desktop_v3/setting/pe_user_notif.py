from main.page.desktop_v3.setting.pe_user import *
import time

class UserNotif(UserSetting):
    #tab instance for notification
    _notice_newsletter_loc = (By.ID, 'f-notice-news-letter')
    _notice_review_loc = (By.ID, 'f-notice-review')
    _notice_talk_loc = (By.ID, 'f-notice-talk-product')
    _notice_pm_loc = (By.ID, 'f-notice-pm')
    _notice_pm_admin_loc = (By.ID, 'f-notice-pm-from-admin')
    _button_save_notification_loc = (By.XPATH, '//*[@id="frm_notification"]/button')
    #--

    def set_notification(self):
        try:
            time.sleep(2)
            i = 1
            while (i < 2):
                self.driver.find_element(*self._notice_newsletter_loc).click()
                self.driver.find_element(*self._notice_review_loc).click()
                self.driver.find_element(*self._notice_talk_loc).click()
                self.driver.find_element(*self._notice_pm_loc).click()
                self.driver.find_element(*self._notice_pm_admin_loc).click()
                i += 1
                time.sleep(2)
                self.driver.find_element(*self._button_save_notification_loc).click()

                time.sleep(2)
        except Exception as inst:
            print(inst)