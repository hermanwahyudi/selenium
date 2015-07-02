from main.page.base import BasePage
from selenium.webdriver.common.by import By

class UserSetting(BasePage):
    #tabs locator
    _tab_personal_profile_loc = (By.XPATH, "//*[@id='content-container']/div[5]/div/div[2]/ul/li[1]/a")
    _tab_address_list_loc = (By.XPATH, "//*[@id='content-container']/div[5]/div/div[2]/ul/li[2]/a")
    _tab_bank_accounts_loc = (By.XPATH, "//*[@id='content-container']/div[5]/div/div[2]/ul/li[3]/a")
    _tab_notification_loc = (By.XPATH, "//*[@id='content-container']/div[5]/div/div[2]/ul/li[4]/a")
   #--

    def select_user_profile_tab(self):
        self.driver.find_element(*self._tab_personal_profile_loc).click()

    def select_address_list_tab(self):
        self.driver.find_element(*self._tab_address_list_loc).click()

    def select_bank_accounts_tab(self):
        self.driver.find_element(*self._tab_bank_accounts_loc).click()

    def select_notif_tab(self):
        self.driver.find_element(*self._tab_notification_loc).click()
