from main.page.base import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class HeaderPage(BasePage):
    # LOCATOR
    _logo_tokopedia_loc = (By.CSS_SELECTOR, 'div.container-fluid div.topbar-logo-wrapper a')
    _category_list_loc = (By.CSS_SELECTOR, 'ul.topbar-nav li.dropdown-topbar-category a.dropdown-toggle')
    _search_bar_loc = (By.CSS_SELECTOR, 'div.search-parent-older div.search-parent input#search-keyword')
    _search_bar_select_category_loc = (By.CSS_SELECTOR, 'div.search-parent div.cat-wrapper select.cat-select')
    _search_button_loc = (
        By.CSS_SELECTOR, 'div.search-parent div.cat-wrapper span.btn-search-wrapper button.btn-search')
    _help_loc = (By.XPATH, '/html/body/header/div/div/div[2]/ul/li[1]/a')

    _guest_header = {
        'help_loc': (By.CSS_SELECTOR, 'div.pull-right ul.topbar-nav li.dropdown a'),
        'register_loc': (By.CSS_SELECTOR, 'div.pull-right ul.topbar-nav li.dropdown-single a'),
        'login_loc': (By.CSS_SELECTOR, 'div.pull-right ul.topbar-nav li.dropdown-right a')
    }

    _guest_login_header = {
        'email_loc': (By.ID, 'inputEmail'),
        'pwd_loc': (By.ID, 'inputPassword'),
        'submit_loc': (By.CLASS_NAME, 'btn-action'),
        'reset_pwd_loc': (By.CSS_SELECTOR, 'form#header-frm-login div.row-fluid div.span5 small a'),
        'checkbox_remember_loc': (By.CSS_SELECTOR, 'div.span7 div.pull-right label.checkbox input')
    }
    #--

    #NOTIFICATION LOCATOR
    _notification_loc = (By.CSS_SELECTOR, 'li.dropdown-right a.dropdown-toggle div.relative i.icon-new-message')
    #--

    #Notification Locator - Inbox
    _notification_header = {
        'inbox_message_notification_loc': (By.XPATH, '/html/body/header/div/div/div[2]/ul/li[2]/ul/li[1]/a'),
        'inbox_talk_notification_loc': (By.XPATH, '/html/body/header/div/div/div[2]/ul/li[2]/ul/li[2]/a'),
        'inbox_review_notification_loc': (By.XPATH, '/html/body/header/div/div/div[2]/ul/li[2]/ul/li[3]/a'),
        'inbox_price_alert_notification_loc': (By.XPATH, '/html/body/header/div/div/div[2]/ul/li[2]/ul/li[4]/a'),
        'inbox_ticket_notification_loc': (By.XPATH, '/html/body/header/div/div/div[2]/ul/li[2]/ul/li[5]/a'),
        'inbox_resolution_center_notification_loc': (By.XPATH, '/html/body/header/div/div/div[2]/ul/li[2]/ul/li[6]/a'),
        'myshop_order_notification_loc': (By.XPATH, '/html/body/header/div/div/div[2]/ul/li[2]/ul/li[8]/a'),
        'myshop_order_status_notification_loc': (By.XPATH, '/html/body/header/div/div/div[2]/ul/li[2]/ul/li[9]/a'),
        'cancelled_order_notification_loc': (By.XPATH, '/html/body/header/div/div/div[2]/ul/li[2]/ul/li[10]/a'),
        'tx_delivery_confirm_notification_loc': (By.XPATH, '/html/body/header/div/div/div[2]/ul/li[2]/ul/li[11]/a'),

        'all_notification_loc': (By.XPATH, '/html/body/header/div/div/div[2]/ul/li[2]/ul/li/a')
    }
    #--

    #Notification Locator - Sales
    #_myshop_order_notification_loc = (By.XPATH, '/html/body/header/div/div/div[2]/ul/li[2]/ul/li[8]/a')
    #_myshop_order_status_notification_loc = (By.XPATH, '/html/body/header/div/div/div[2]/ul/li[2]/ul/li[9]/a')

    #Notification Locator - Purchase
    #_cancelled_order_notification_loc = (By.XPATH, '/html/body/header/div/div/div[2]/ul/li[2]/ul/li[10]/a')
    #_tx_delivery_confirm_notification_loc = (By.XPATH, '/html/body/header/div/div/div[2]/ul/li[2]/ul/li[11]/a')


    #MYSHOP LOCATOR
    _myshop_loc = (By.CSS_SELECTOR, 'li#shop-tab a.dropdown-toggle img.imgshop')

    _myshop_header = {
        'myshop_domain_loc': (By.XPATH, '/html/body/header/div/div/div[2]/ul/li[3]/ul/li[1]/a'),
        'sales_loc': (By.XPATH, '/html/body/header/div/div/div[2]/ul/li[3]/ul/li[3]/a'),
        'add_product_loc': (By.XPATH, '/html/body/header/div/div/div[2]/ul/li[3]/ul/li[4]/a'),
        'product_list_loc': (By.XPATH, '/html/body/header/div/div/div[2]/ul/li[3]/ul/li[5]/a'),
        'topads_loc': (By.XPATH, '/html/body/header/div/div/div[2]/ul/li[3]/ul/li[6]/a'),
        'manage_shop_loc': (By.XPATH, '/html/body/header/div/div/div[2]/ul/li[3]/ul/li[7]/a'),
        'manage_admin_loc': (By.XPATH, '/html/body/header/div/div/div[2]/ul/li[3]/ul/li[8]/a'),

        'all_myshop_loc': (By.XPATH, '/html/body/header/div/div/div[2]/ul/li[3]/ul/li/a')
    }
    #--

    #USER LOCATOR
    _user_loc = (By.CSS_SELECTOR, 'li#user-tab')
    _user_loc_open = (By.CSS_SELECTOR, 'li#user-tab.open')
    #--

    _myprofile_menu = {
        'my_profile_loc': (By.XPATH, '/html/body/header/div/div/div[2]/ul/li[4]/ul/li[1]/a'),
        'my_deposit_loc': (By.XPATH, '/html/body/header/div/div/div[2]/ul/li[4]/ul/li[2]/a'),
        'purchase_loc': (By.XPATH, '/html/body/header/div/div/div[2]/ul/li[4]/ul/li[4]/a'),
        'my_settings_loc': (By.XPATH, '/html/body/header/div/div/div[2]/ul/li[4]/ul/li[5]/a'),
        'logout_loc': (By.XPATH, '/html/body/header/div/div/div[2]/ul/li[4]/ul/li[7]/a'),

        'all_myprofile_loc': (By.XPATH, '/html/body/header/div/div/div[2]/ul/li[4]/ul/li/a')
    }

    #CART LOCATOR
    _shopping_cart_loc = (By.CSS_SELECTOR, 'div.pull-right ul#b-nav li.dropdown-last')
    #--

    #[LOGIN] Action-List
    def check_header_elements(self, flag):
        count_notification_menu = 0
        count_myshop_menu = 0
        count_myprofile_menu = 0

        print("Checking Header elements Title!")
        print("======================")
        if flag == 1:
            print("Checking Tokopedia Logo at Header...")
            try:
                if self.find_element(*self._logo_tokopedia_loc).is_displayed():
                    print("Logo Tokopedia found!")
            except:
                print("Logo Tokopedia is not found! Please check!")

            print("Checking Category lists at Header...")
            try:
                if self.find_element(*self._category_list_loc).is_displayed():
                    print("Category List found!")
            except:
                print("List of category is not found! Please check!")

            print("Checking Search Bar at Header...")
            try:
                if self.find_element(*self._search_bar_loc).is_displayed():
                    print("Search Bar found!")
            except:
                print("Search bar is not found! Please check!")

            print("Checking Notification Menu at Header...")
            for each_notification_header_bar in self.find_elements(*self._notification_header['all_notification_loc']):
                #self.check_visible_element(*self._notification_header[each_notification])
                #print ("Notification Title found : " + "'" + each_notification.get_attribute('innerHTML').strip() + "'")
                count_notification_menu += 1
            print("Total Notification Menu : %d" % (count_notification_menu))

            print("Checking Myshop Menu at Header...")
            for each_myshop_header_bar in self.find_elements(*self._myshop_header['all_myshop_loc']):
                count_myshop_menu += 1
            print("Total Myshop Menu : %d" % (count_myshop_menu))

            print("Checking Myprofile Menu at Header...")
            for each_myprofile_header_bar in self.find_elements(*self._myprofile_menu['all_myprofile_loc']):
                count_myprofile_menu += 1
            print("Total Myprofile Menu : %d" % (count_myprofile_menu))

            print("Checking Shopping Cart at Header...")
            try:
                if self.find_element(*self._shopping_cart_loc).is_displayed():
                    print("Shopping cart is found!")
            except:
                print("Shopping Cart is not found! Please check!")

            print("===========================")
            print("All header has been checked! DONE")

        elif flag == 0:
            for each_header_bar in self._guest_header:
                self.check_visible_element(*self._guest_header[each_header_bar])
                print(
                    "Header Title found : " + "'" + self.find_element(*self._guest_header[each_header_bar]).text + "'")


    def mouse_hover_to_notification_bar(self):
        return self.mouse_hover_to(*self._notification_loc)

    def mouse_hover_to_myshop_bar(self):
        return self.mouse_hover_to(*self._myshop_loc)

    def mouse_hover_to_user_bar(self):
        retry = 0
        while(retry < 3):
            try:
                self.mouse_hover_to(*self._user_loc)
                element_open = self.find_element(*self._user_loc_open)
                return element_open
            except:
                time.sleep(1)
                self.mouse_hover_to(*self._shopping_cart_loc)
                retry+=1


    #MENU INBOX NOTIFICATIONS
    def mouse_hover_to_inbox_message_notification(self):
        return self.mouse_hover_to(*self._notification_header['inbox_message_notification_loc'])

    def mouse_hover_and_go_to_inbox_message_notification(self):
        notif_inbox_message = self.mouse_hover_to(*self._notification_header['inbox_message_notification_loc'])
        self._click(notif_inbox_message)

    def mouse_hover_to_inbox_talk_notification(self):
        return self.mouse_hover_to(*self._notification_header['inbox_talk_notification_loc'])

    def mouse_hover_and_go_to_inbox_talk_notification(self):
        notif_inbox_talk = self.mouse_hover_to(*self._notification_header['inbox_talk_notification_loc'])
        self._click(notif_inbox_talk)

    def mouse_hover_to_inbox_review_notification(self):
        return self.mouse_hover_to(*self._notification_header['inbox_review_notification_loc'])

    def mouse_hover_and_go_to_inbox_review_notification(self):
        notif_inbox_review = self.mouse_hover_to(*self._notification_header['inbox_review_notification_loc'])
        self._click(notif_inbox_review)

    def mouse_hover_to_inbox_price_alert_notification(self):
        return self.mouse_hover_to(*self._notification_header['inbox_price_alert_notification_loc'])

    def mouse_hover_and_go_to_inbox_price_alert_notification(self):
        notif_inbox_price_alert = self.mouse_hover_to(*self._notification_header['inbox_price_alert_notification_loc'])
        self._click(notif_inbox_price_alert)

    def mouse_hover_to_inbox_resolution_center_notification(self):
        return self.mouse_hover_to(*self._notification_header['inbox_resolution_center_notification_loc'])

    def mouse_hover_and_go_to_inbox_resolution_center_notification(self):
        notif_inbox_resolution_center = self.mouse_hover_to(
            *self._notification_header['inbox_resolution_center_notification_loc'])
        self._click(notif_inbox_resolution_center)

    #MYSHOP NOTIFICATIONS
    def mouse_hover_to_myshop_order_notification(self):
        return self.mouse_hover_to(*self._notification_header['myshop_order_notification_loc'])

    def mouse_hover_and_go_to_myshop_order_notification(self):
        notif_myshop_order = self.mouse_hover_to(*self._notification_header['myshop_order_notification_loc'])
        self._click(notif_myshop_order)

    def mouse_hover_to_myshop_order_status_notification(self):
        return self.mouse_hover_to(*self._notification_header['myshop_order_status_notification_loc'])

    def mouse_hover_and_go_to_myshop_order_status_notification(self):
        notif_myshop_order_status = self.mouse_hover_to(
            *self._notification_header['myshop_order_status_notification_loc'])
        self._click(notif_myshop_order_status)


    #SALES NOTIFICATIONS
    def mouse_hover_to_cancelled_order_notification(self):
        return self.mouse_hover_to(*self._notification_header['cancelled_order_notification_loc'])

    def mouse_hover_and_go_to_cancelled_order_notification(self):
        notif_cancelled_order = self.mouse_hover_to(*self._notification_header['cancelled_order_notification_loc'])
        self._click(notif_cancelled_order)

    def mouse_hover_to_delivery_confirm_notification(self):
        return self.mouse_hover_to(*self._notification_header['tx_delivery_confirm_notification_loc'])

    def mouse_hover_and_go_to_delivery_confirm_notification(self):
        notif_delivery_confirm = self.mouse_hover_to(*self._notification_header['tx_delivery_confirm_notification_loc'])
        self._click(notif_delivery_confirm)

    #--


    #EDIT PROFILE
    def mouse_hover_to_setting(self):
        self.check_visible_element(*self._myprofile_menu['my_settings_loc'])
        user_setting = self.mouse_hover_to(*self._myprofile_menu['my_settings_loc'])
        time.sleep(1)
        self._click(user_setting)
    #--

    #MENU USER
    def mouse_hover_to_logout(self):
        return self.mouse_hover_to(*self._myprofile_menu['logout_loc'])

    def mouse_hover_and_go_to_logout(self):
        do_logout = self.mouse_hover_to(*self._myprofile_menu['logout_loc'])
        self._click(do_logout)

    #--

    def check_header_status(self, flag):
        if flag == 1:
            print("user logged in!")
            self.check_header_elements(flag)
        elif flag == 0:
            print("user not logged in!")
            self.check_header_elements(flag)

    #[NON-LOGIN] Action List
    def do_login(self, email, pwd):
        self.find_element(*self._guest_header['login_loc']).click()

        def input_email():
            self.find_element(*self._guest_login_header['email_loc']).send_keys(email)

        def input_pwd():
            self.find_element(*self._guest_login_header['pwd_loc']).send_keys(pwd)

        def submit():
            self.find_element(*self._guest_login_header['submit_loc']).click()

        return input_email(), input_pwd(), submit()

