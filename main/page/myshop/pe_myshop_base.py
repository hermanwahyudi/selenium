from main.page.base import BasePage
from selenium.webdriver.common.by import By

class MyshopSettingsBasePage(BasePage):

    #Tab Locators
    _tab_shop_info = (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/ul/li[1]/a')
    _tab_shipping = (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/ul/li[2]/a')
    _tab_payment = (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/ul/li[3]/a')
    _tab_etalase = (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/ul/li[4]/a')
    _tab_notes = (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/ul/li[5]/a')
    _tab_location = (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/ul/li[6]/a')

    #Global Action
    def select_tab_shop_info(self):
        tab_shop_info = self.find_element(*self._tab_shop_info)
        self._click(tab_shop_info)
        if (self.driver.current_url == "https://www.tokopedia.com/myshop-editor.pl"):
            print ("saat ini berada di %s" %(self.driver.current_url))
        else:
            print (self.driver.current_url + " is a wrong accessed page")

    def select_tab_shipping(self):
        tab_shipping = self.find_element(*self._tab_shipping)
        self._click(tab_shipping)
        if (self.driver.current_url == "https://www.tokopedia.com/myshop-editor.pl?tab=shipping"):
            print ("saat ini berada di %s" %(self.driver.current_url))
        else:
            print (self.driver.current_url + " is a wrong accessed page")

    def select_tab_payment(self):
        tab_payment = self.find_element(*self._tab_payment)
        self._click(tab_payment)
        if (self.driver.current_url == "https://www.tokopedia.com/myshop-editor.pl?tab=shipping"):
            print ("saat ini berada di %s" %(self.driver.current_url))
        else:
            print (self.driver.current_url + " is a wrong accessed page")

    def select_tab_etalase(self):
        tab_etalase = self.find_element(*self._tab_etalase)
        self._click(tab_etalase)
        if (self.driver.current_url == "https://www.tokopedia.com/myshop-etalase.pl"):
            print ("saat ini berada di %s" %(self.driver.current_url))
        else:
            print (self.driver.current_url + " is a wrong accessed page")

    def select_tab_notes(self):
        tab_notes = self.find_element(*self._tab_notes)
        self._click(tab_notes)
        if (self.driver.current_url == "https://www.tokopedia.com/myshop-note.pl"):
            print ("saat ini berada di %s" %(self.driver.current_url))
        else:
            print (self.driver.current_url + " is a wrong accessed page")

    def select_tab_offline_store_location(self):
        tab_offline_store_location = self.find_element(*self._tab_location)
        self._click(tab_offline_store_location)
        if (self.driver.current_url == "https://www.tokopedia.com/myshop-address.pl"):
            print ("saat ini berada di %s" %(self.driver.current_url))
        else:
            print (self.driver.current_url + " is a wrong accessed page")




