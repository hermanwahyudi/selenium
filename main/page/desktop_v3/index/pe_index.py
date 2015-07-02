from main.page.base import BasePage
from selenium.webdriver.common.by import By
from utils.lib.user import *


class IndexPage(BasePage):
    _pl = ""

    # LOCATORS
    #PANEL LEFT
    _username_loc = (By.CSS_SELECTOR, 'div#side-profile div.clear-b div.span8 small.pull-left a')
    _deposit_amount_loc = (By.CSS_SELECTOR, 'div.ellipsis a.deposit-link strong#include-deposit')
    _shop_name_loc = (By.XPATH, '/html/body/div[1]/div[5]/div/div[1]/div/div[2]/div/div[2]/small/a')
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

    #Panel Left -- MY SHOP
    _panel_my_shop_loc = {
        '_myshop_order_loc': (By.XPATH, '//*[@id="accordion-shop"]/div/ul/li[1]/a'),
        '_add_product_loc': (By.XPATH, '//*[@id="accordion-shop"]/div/ul/li[2]/a'),
        '_product_list_loc': (By.XPATH, '//*[@id="accordion-shop"]/div/ul/li[3]/a'),
        '_topads_loc': (By.XPATH, '//*[@id="accordion-shop"]/div/ul/li[4]/a'),
        '_manage_shop_loc': (By.XPATH, '//*[@id="accordion-shop"]/div/ul/li[5]/a'),
        '_manage_admin_loc': (By.XPATH, '//*[@id="accordion-shop"]/div/ul/li[6]/a')
    }

    #Panel Left -- MY PROFILE
    _panel_my_profile_loc = {
        '_tx_payment_confirm_loc': (By.XPATH, '//*[@id="accordion-profile"]/div/ul/li[1]/a'),
        '_my_favorite_shop_loc': (By.XPATH, '//*[@id="accordion-profile"]/div/ul/li[2]/a'),
        '_my_profile_setting_loc': (By.XPATH, '//*[@id="accordion-profile"]/div/ul/li[3]/a')
    }

    #Panel Left -- INSIGHT
    _panel_insight_loc = {
        '_insight_talk_loc': (By.XPATH, '/html/body/div[2]/div[5]/div/div[1]/ul/li[4]/div[2]/div/ul/li[1]/a'),
        '_insight_price_alert_loc': (By.XPATH, '/html/body/div[2]/div[5]/div/div[1]/ul/li[4]/div[2]/div/ul/li[2]/a')
    }

    #Hot List content
    _view_all_hotlist_loc = (By.CSS_SELECTOR, 'div.maincontent-admin a.fs-12')
    _left_hotlist_img_loc = (By.XPATH, '//*[@id="content-container"]/div[5]/div/div[2]/div[1]/div[1]/a/div/div[1]/img')
    _left_hotlist_loc = (By.XPATH, '//*[@id="content-container"]/div[5]/div/div[2]/div[1]/div[1]/a/div/div[2]/div[1]')
    _mid_hotlist_img_loc = (By.XPATH, '//*[@id="content-container"]/div[5]/div/div[2]/div[1]/div[2]/a/div/div[1]/img')
    _mid_hotlist_loc = (By.XPATH, '//*[@id="content-container"]/div[5]/div/div[2]/div[1]/div[2]/a/div/div[2]/div[1]')
    _right_hotlist_img_loc = (By.XPATH, '//*[@id="content-container"]/div[5]/div/div[2]/div[1]/div[3]/a/div/div[1]/img')
    _right_hotlist_loc = (By.XPATH, '//*[@id="content-container"]/div[5]/div/div[2]/div[1]/div[3]/a/div[2]/div[1]')


    #Tab Locator
    _tab_product_feed_loc = (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[2]/div[1]/div[1]/div/ul/li[1]/a')
    _tab_fav_shop_loc = (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[2]/div[1]/div[1]/div/ul/li[2]/a')
    _tab_recently_viewed_loc = (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[2]/div[1]/div[1]/div/ul/li[3]/a')


    #Total Product displayed
    _total_list_product_loc = (By.XPATH, '//*[@id="fav-prod-grid"]/div')
    _total_list_product_img_loc = (By.XPATH, '//*[@id="fav-prod-grid"]/div/a/div/div[1]/img')

    #Total Promote displayed
    _total_list_promo_loc = (By.XPATH, '//*[@id="promo-right-c-0"]/div/div')


    #ACTIONS
    def open(self, site=""):
        self._open(site, self._pl)

    def check_my_username(self):
        print("my username : %s" % (self.find_element(*self._username_loc).text))
        return self.find_element(*self._username_loc).text

    def check_my_deposit(self):
        self.check_visible_element(*self._deposit_amount_loc)
        print("Current deposit : %s" % (self.find_element(*self._deposit_amount_loc).text))
        return self.find_element(*self._deposit_amount_loc).text

    def check_all_product_listed(self):
        total_product = 20
        current_product = 0
        for each_product in self.find_elements(*self._total_list_product_img_loc):
            #print (each_product.get_attribute('src')) #For Debug
            current_product += 1
            if current_product == total_product:
                print("Total listed product checked has reached 20 (Maximum)!")
            elif current_product > total_product:
                print("Total listed product checked has exceeding 20(Maximum)! Please check this now!")


    #[Element] Panel Left
    def check_all_panel_left(self):
        print("Now checking all panel elements..")
        for each_element_at_my_inbox_panel in self._panel_my_inbox_loc:
            self.check_visible_element(*self._panel_my_inbox_loc[each_element_at_my_inbox_panel])
        print ("Panel 'Inbox' checked!")

        for each_element_at_my_shop_panel in self._panel_my_shop_loc:
            self.check_visible_element(*self._panel_my_shop_loc[each_element_at_my_shop_panel])
        print ("Panel 'Shop' checked!")

        for each_element_at_my_profile_panel in self._panel_my_profile_loc:
            self.check_visible_element(*self._panel_my_profile_loc[each_element_at_my_profile_panel])
        print ("Panel 'Profile' checked!")

        for each_element_at_insight_panel in self._panel_insight_loc:
            self.check_visible_element(*self._panel_insight_loc[each_element_at_insight_panel])
        print ("Panel 'Insight' checked!")

        print("All panel elements has been checked and status OK..!")

    def check_all_panel_left_no_shop(self):
        print("Now checking all panel elements..")
        for each_element_at_my_inbox_panel in self._panel_my_inbox_loc:
            self.check_visible_element(*self._panel_my_inbox_loc[each_element_at_my_inbox_panel])
        #print (*self._panel_my_inbox_loc[each_element_at_my_inbox_panel]) #For debug

        for each_element_at_my_profile_panel in self._panel_my_profile_loc:
            self.check_visible_element(*self._panel_my_profile_loc[each_element_at_my_profile_panel])
        #print (*self._panel_my_profile_loc[each_element_at_my_profile_panel]) #For debug

        print("All panel elements has been checked and status OK..!")

    #[Element] Panel Left - User Information
    def click_my_username_at_panel_left(self):
        my_username = self.find_element(*self._username_loc)
        self._click(my_username)

    def click_shop_name_at_panel_left(self):
        my_shop = self.find_element(*self._shop_name_loc)
        self._click(my_shop)

    #[Element] Panel Left - Inbox
    def click_inbox_message_at_panel_left(self):
        panel_inbox_message = self.find_element(*self._panel_my_inbox_loc['_inbox_message_loc'])
        self._click(panel_inbox_message)

    def click_inbox_talk_at_panel_left(self):
        panel_inbox_talk = self.find_element(*self._panel_my_inbox_loc['_inbox_talk_loc'])
        self._click(panel_inbox_talk)

    def click_inbox_review_at_panel_left(self):
        panel_inbox_review = self.find_element(*self._panel_my_inbox_loc['_inbox_review_loc'])
        self._click(panel_inbox_review)

    def click_inbox_price_alert_at_panel_left(self):
        panel_inbox_price_alert = self.find_element(*self._panel_my_inbox_loc['_inbox_price_alert_loc'])
        self._click(panel_inbox_price_alert)

    def click_inbox_ticket_at_panel_left(self):
        panel_inbox_ticket = self.find_element(*self._panel_my_inbox_loc['_inbox_ticket_loc'])
        self._click(panel_inbox_ticket)

    def click_inbox_resolution_center_at_panel_left(self):
        panel_inbox_resolution_center = self.find_element(*self._panel_my_inbox_loc['_inbox_resolution_center_loc'])
        self._click(panel_inbox_resolution_center)

    #[Element] Panel Left - My Shop
    def click_sales_at_panel_left(self):
        panel_myshop_order = self.find_element(*self._panel_my_shop_loc['_myshop_order_loc'])
        self._click(panel_myshop_order)

    def click_add_product_at_panel_left(self):
        panel_add_product = self.find_element(*self._panel_my_shop_loc['_add_product_loc'])
        self._click(panel_add_product)

    def click_product_list_at_panel_left(self):
        panel_product_list = self.find_element(*self._panel_my_shop_loc['_product_list_loc'])
        self._click(panel_product_list)

    def click_topads_at_panel_left(self):
        panel_topads = self.find_element(*self._panel_my_shop_loc['_topads_loc'])
        self._click(panel_topads)

    def click_manage_shop_at_panel_left(self):
        panel_manage_shop = self.find_element(*self._panel_my_shop_loc['_manage_shop_loc'])
        self._click(panel_manage_shop)

    def click_manage_admin_at_panel_left(self):
        panel_manage_admin = self.find_element(*self._panel_my_shop_loc['_manage_admin_loc'])
        self._click(panel_manage_admin)

    #[Element] Panel Left - My Shop
    def click_purchase_at_panel_left(self):
        panel_tx_payment_confirm = self.find_element(*self._panel_my_profile_loc['_tx_payment_confirm_loc'])
        self._click(panel_tx_payment_confirm)

    def click_favorite_shops_at_panel_left(self):
        panel_fav_shop = self.find_element(*self._panel_my_profile_loc['_my_favorite_shop_loc'])
        self._click(panel_fav_shop)

    def click_settings_at_panel_left(self):
        panel_settings = self.find_element(*self._panel_my_profile_loc['_my_profile_setting_loc'])
        self._click(panel_settings)

    #[Element] Panel Left - Insight
    def click_insight_talk(self):
        panel_insight_talk = self.find_element(*self._panel_insight_loc['_insight_talk_loc'])
        self._click(panel_insight_talk)

    def click_insight_price_alert(self):
        panel_insight_price_alert = self.find_element(*self._panel_insight_loc['_insight_price_alert_loc'])
        self._click(panel_insight_price_alert)









