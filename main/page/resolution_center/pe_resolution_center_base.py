from main.page.base import BasePage
from selenium.webdriver.common.by import By

class ResolutionCenterBasePage(BasePage):
    #locators level
    _tab_p_my_complaint = (By.ID, "as-buyer-link")
    _tab_p_complaint_from_buyer = (By.XPATH, ".//*[@id='as-seller-link']")

    def select_tab_my_complaints(self):
        tab_my_complaint = self.find_element(*self._tab_p_my_complaint)
        self._click(tab_my_complaint)
        if (self.driver.current_url == "https://www.tokopedia.com/resolution-center.pl"):
            print("Your current page is https://www.tokopedia.com/resolution-center.pl")
        else:
            print("Your current page is https://www.tokopedia.com/resolution-center.pl?as=1")

    def select_tab_complaint_from_buyer(self):
        _tab_complaint_from_buyer = self.find_element(*self._tab_p_complaint_from_buyer)
        self._click(_tab_complaint_from_buyer)
        if (self.driver.current_url == "https://www.tokopedia.com/resolution-center.pl"):
            print("Your current page is https://www.tokopedia.com/resolution-center.pl")
        else:
            print("Your current page is https://www.tokopedia.com/resolution-center.pl?as=1")
