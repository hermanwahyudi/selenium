__author__ = 'QC1'
from main.page.base import BasePage
import time
from selenium.webdriver.common.by import By
from utils.lib.user import *

class PriceAlertPage(BasePage):
    _pl = ""

    # LOCATORS
    # PANEL LEFT
    _username_loc = (By.CSS_SELECTOR, 'div#side-profile div.clear-b div.span8 small.pull-left a')
    _deposit_amount_loc = (By.CSS_SELECTOR, 'div.ellipsis a.deposit-link strong#include-deposit')
    _shop_name_loc = (By.CSS_SELECTOR, 'div.top-admin div.clear-b div.span8 small.pull-left a')
    _shop_status_loc = (By.CSS_SELECTOR, 'div.top-admin div.clear-b div.span8 div.ellipsis a')

    #Panel Left -- INBOX
    _panel_my_inbox_loc = {
        '_inbox_message_loc': (By.XPATH, '//*[@id="accordion-inbox"]/div/ul/li[1]/a'),
        '_inbox_talk_loc': (By.XPATH, '//*[@id="accordion-inbox"]/div/ul/li[2]/a'),
        '_inbox_review_loc': (By.XPATH, '//*[@id="accordion-inbox"]/div/ul/li[3]/a'),
        '_inbox_price_alert_loc': (By.XPATH, '//*[@id="accordion-inbox"]/div/ul/li[4]/a'),
        '_inbox_ticket_loc': (By.XPATH, '//*[@id="accordion-inbox"]/div/ul/li[5]/a'),
        '_inbox_resolution_center_loc': (By.XPATH, '//*[@id="accordion-inbox"]/div/ul/li[6]/a')
    }

    #Panel Left -- MY PROFILE
    _panel_my_profile_loc = {
        '_tx_payment_confirm_loc': (By.XPATH, '//*[@id="accordion-profile"]/div/ul/li[1]/a'),
        '_my_favorite_shop_loc': (By.XPATH, '//*[@id="accordion-profile"]/div/ul/li[2]/a'),
        '_my_profile_setting_loc': (By.XPATH, '//*[@id="accordion-profile"]/div/ul/li[3]/a')
    }

    #Panel Top
    _top_notification = (By.XPATH, '/html/body/header/div/div/div[2]/ul/li[2]')
    _top_price_notification = (By.XPATH, '//*[@id="notification-ul"]/li[4]/a')

    #Price Alert Row Locator
    _panel_price_alert={
        '_price_alert_row_loc': (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[2]/div[1]/div/table/tbody/tr[1]'),
        '_found_price_alert_icon_loc': (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[2]/div[1]/div/table/tbody/tr/td[2]/div/div'),
        '_price_alert_click_loc' : (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[2]/div[1]/div/table/tbody/tr/td[2]/div/img'),
        '_shop_inside_price_alert' : (By.XPATH, '/html/body/div[1]/div[5]/div/div[3]/div[3]/div[1]/div/ul')
    }

    def open(self, site=""):
        self._open(site, self._pl)

    def check_price_alert(self):
        self.mouse_hover_to(*self._top_notification)
        time.sleep(3)
        self.find_element(*self._top_price_notification).click()
        time.sleep(2)
        self.mouse_hover_to(*self._panel_price_alert['_price_alert_row_loc'])
        print("Price alert element has been found! Price alert update succeeded!!")
        time.sleep(3)

    def search_inbox_price_alert(self):
        self.mouse_hover_to(*self._top_notification)
        time.sleep(3)
        self.find_element(*self._top_price_notification).click()
        time.sleep(2)
        self.mouse_hover_to(*self._panel_price_alert['_price_alert_row_loc'])
        print("Price alert element has been found! Looking for any price alert notification..")
        self.find_element(*self._panel_price_alert['_found_price_alert_icon_loc'])
        print("Found a shop with the desired price or lower! Opening the alert list..")
        self.find_element(*self._panel_price_alert['_price_alert_click_loc']).click()
        self.check_visible_element(*self._panel_price_alert['_shop_inside_price_alert'])
        print("A shop with the desired price or lower is found! Price alert notification succeeded!")
        time.sleep(3)

