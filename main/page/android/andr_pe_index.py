__author__ = 'QC1'

import random
from main.page.android.andr_base import *

class PageIndex(PageBaseMobile):

    loc_widget_toped = "//android.widget.ImageView[@resource-id='android:id/home']"
    loc_widget_leftSideMenu= "//android.widget.ImageView[@resource-id='android:id/up'][@index='0']"


    loc_widget_cart = "//android.widget.TextView[@resource-id='com.tokopedia.tkpd:id/action_cart']"
    loc_widget_search = "//android.widget.TextView[@resource-id='com.tokopedia.tkpd:id/action_search'"

    pos_view_category = [(88,298)]
    pos_widget_hotList_1 = [(480,590)]
    pos_widget_hotList_2 = [(480,1250)]
    pos_widget_hotList_3 = [(480,1650)]

    widget_menu_dict =  {"loc_widget_login" : "//android.widget.TextView[@resource-id='com.tokopedia.tkpd:id/extra_but']"}


    #left side menu item loc

    loc_widget_logIn = "//android.widget.TextView[@resource-id='com.tokopedia.tkpd:id/extra_but'][@text='MASUK']"
    loc_widget_add_product = "//android.widget.TextView[@resource-id='com.tokopedia.tkpd:id/extra_but']"
    loc_widget_myProfile_Seller = "//android.widget.TextView[@resource-id='com.tokopedia.tkpd:id/title_large'][@text='Sebhastian']"
    loc_widget_myProfile_Buyer = "//android.widget.TextView[@resource-id='com.tokopedia.tkpd:id/title_large'][@text='Yonathan']"
    loc_widget_myStore = "//android.widget.TextView[@resource-id='com.tokopedia.tkpd:id/title_large'][@text='YS Electronics']"
    loc_widget_etalase = "//android.widget.TextView[@resource-id='com.tokopedia.tkpd:id/child_menu'][@text='Etalase']"
    loc_widget_logOut = "//android.widget.TextView[@resource-id='com.tokopedia.tkpd:id/title_large'][@text='Keluar']"

    #yes/no button
    loc_button_yes = loc_button_ok = "//android.widget.Button[@resource-id='android:id/button1']"
    loc_button_no = "//android.widget.Button[@resource-id='android:id/button2']"
    loc_button_complaint = "//android.widget.Button[@resource-id='android:id/button3']"


    def randomnum(self):
        return random.randint(1,5)

    def tap_profile(self, agent="seller"):
        self.explicit_wait(self.loc_widget_leftSideMenu)
        self.driver.find_element_by_xpath(self.loc_widget_leftSideMenu).click()
        if agent=="seller":
            self.explicit_wait(self.loc_widget_myProfile_Seller)
            self.driver.find_element_by_xpath(self.loc_widget_myProfile_Seller).click()
            self.snooze()
        else:
            self.explicit_wait(self.loc_widget_myProfile_Buyer)
            self.driver.find_element_by_xpath(self.loc_widget_myProfile_Buyer).click()
            self.snooze()

    def tap_my_store(self):
        self.driver.find_element_by_xpath(self.loc_widget_leftSideMenu).click()
        self.explicit_wait(self.loc_widget_myStore)
        self.driver.find_element_by_xpath(self.loc_widget_myStore).click()
        self.snooze()

    def tap_etalase(self):
        self.driver.find_element_by_xpath(self.loc_widget_leftSideMenu).click()
        self.explicit_wait(self.loc_widget_etalase)
        self.driver.find_element_by_xpath(self.loc_widget_etalase).click()
        self.snooze()


    def tap_logout(self):
        self.driver.find_element_by_xpath(self.loc_widget_leftSideMenu).click()
        self.snooze()
        print("swipe to the bottom")
        self.swipeDown()
        self.swipeDown()
        self.snooze()
        self.driver.find_element_by_xpath(self.loc_widget_logOut).click()
        self.snooze()
        self.driver.find_element_by_xpath(self.loc_button_yes).click()

    def tap_login(self):
        self.explicit_wait(self.loc_widget_leftSideMenu)
        self.driver.find_element_by_xpath(self.loc_widget_leftSideMenu).click()
        self.explicit_wait(self.loc_widget_logIn)
        self.driver.find_element_by_xpath(self.loc_widget_logIn).click()

    def tap_add_product(self):
        self.driver.find_element_by_xpath(self.loc_widget_leftSideMenu).click()
        self.explicit_wait(self.loc_widget_add_product)
        self.driver.find_element_by_xpath(self.loc_widget_add_product).click()



