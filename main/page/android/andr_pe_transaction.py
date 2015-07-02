__author__ = 'QC1'

from main.page.android.andr_base import *
import random

class PageTransaction(PageBaseMobile):

    #locator  for purchasing product process
    loc_widget_favshop_1 = "//android.widget.TextView[@resource-id='com.tokopedia.tkpd:id/shop_name'][@text='YS Electronics']"
    loc_widget_product_1 = "//android.widget.ImageView[@resource-id='com.tokopedia.tkpd:id/product_image_1']"
    loc_widget_buy_button = "//android.widget.TextView[@resource-id='com.tokopedia.tkpd:id/buy_but'][@text='BELI']"
    loc_widget_agency = "//android.widget.Spinner[@resource-id='com.tokopedia.tkpd:id/agency']"
    loc_agency_selection = {"JNE" : "//android.widget.CheckedTextView[@text='JNE']"}
    loc_widget_buy_2 = "//android.widget.TextView[@resource-id='com.tokopedia.tkpd:id/buy_button']"
    loc_widget_select_payment_method = "//android.widget.TextView[@resource-id='com.tokopedia.tkpd:id/spinner_payment'][@text='Pilih metode pembayaran dulu']"
    loc_payment_method_selection = {"Saldo_tokopedia" : "//android.widget.TextView[@resource-id='com.tokopedia.tkpd:id/name'][@text='Saldo Tokopedia']"}
    loc_widget_pay = "//android.widget.Button[@resource-id='android:id/button1'][@text='Bayar']"
    loc_widget_browse = "//android.widget.Button[@resource-id='android:id/button2'][@text='Lanjutkan belanja']"
    loc_widget_checkout = "//android.widget.TextView[@resource-id='com.tokopedia.tkpd:id/checkout_but']"
    loc_checkout_pass = "//android.widget.EditText[@resource-id='com.tokopedia.tkpd:id/password']"
    loc_confirm_pay = "//android.widget.TextView[@resource-id='com.tokopedia.tkpd:id/pay_but'][@text='Bayar']"
    loc_order_status = "//android.widget.TextView[@resource-id='com.tokopedia.tkpd:id/order_stats_but'][@text='Status Pemesanan']"

    #seller route - new order process
    loc_notification_tray_icon = "//android.widget.ImageView[@resource-id='com.tokopedia.tkpd:id/search_but_ab']"
    loc_notification_latest = "//android.widget.TextView[@resource-id='com.tokopedia.tkpd:id/title_notif'][@index='0']"
    loc_latest_list_order = "//android.widget.LinearLayout[@resource-id='com.tokopedia.tkpd:id/main_view'][@index='0']"
    loc_notification_new_order = "//android.widget.TextView[@resource-id='com.tokopedia.tkpd:id/title_notif'][@text='Order Baru']"
    loc_notification_shipment_confirmation = "//android.widget.TextView[@resource-id='com.tokopedia.tkpd:id/title_notif'][@text='Konfirmasi Pengiriman']"
    loc_accept_order = "//android.widget.TextView[@resource-id='com.tokopedia.tkpd:id/accept'][@text='Terima Pesanan']"
    loc_reject_order = "//android.widget.TextView[@resource-id='com.tokopedia.tkpd:id/reject'][@text='Tolak']"
    loc_receipt_number = "//android.widget.EditText[@resource-id='com.tokopedia.tkpd:id/ref_number']"
    loc_confirm_shipping = "//android.widget.TextView[@resource-id='com.tokopedia.tkpd:id/confirm_button']"
    loc_cancel_shipping = "//android.widget.TextView[@resource-id='com.tokopedia.tkpd:id/cancel_button']"
    loc_detail_shipping = "//android.widget.TextView[@resource-id='com.tokopedia.tkpd:id/detail_button']"
    loc_order_shipped = "//android.widget.TextView[@resource-id='com.tokopedia.tkpd:id/confirm_button'][@text='Order telah diproses']"

    #buyer route - confirm product has been received
    loc_shipment_number = "//android.widget.TextView[@text='Nomor Resi'][@index='0']"
    loc_widget_package_received = "//android.widget.TextView[@resource-id='com.tokopedia.tkpd:id/receive_btn'][@text='PAKET DITERIMA']"
    loc_review_top_item = "//android.widget.LinearLayout[@resource-id='com.tokopedia.tkpd:id/main_view'][@index='0']"
    loc_review_detail = {"review_text" : "//android.widget.EditText[@resource-id='com.tokopedia.tkpd:id/write_message']", "review_quality" : "//android.widget.Spinner[@resource-id='com.tokopedia.tkpd:id/prod_quality_rat_spin']",
                         "review_speed":"//android.widget.Spinner[@resource-id='com.tokopedia.tkpd:id/ship_speed_rat_spin']", "review_accuracy":"//android.widget.Spinner[@resource-id='com.tokopedia.tkpd:id/prod_acc_rat_spin']",
                         "review_service":"//android.widget.Spinner[@resource-id='com.tokopedia.tkpd:id/shop_service_rat_spin']", "review_submit":"//android.widget.TextView[@resource-id='com.tokopedia.tkpd:id/submit_but']",
                         "resource_cancel":"//android.widget.TextView[@resource-id='com.tokopedia.tkpd:id/cancel_but']"}
    dummy_text = "Integer maximus risus tempus tempus dignissim. Vivamus ut pretium lectus, sit amet egestas justo. Morbi non dui tellus. Praesent in massa id lectus sagittis dignissim non et nisl. Aenean sollicitudin."

    #yes/no button
    loc_button_yes = loc_button_ok = "//android.widget.Button[@resource-id='android:id/button1']"
    loc_button_no = "//android.widget.Button[@resource-id='android:id/button2']"
    loc_button_complaint = "//android.widget.Button[@resource-id='android:id/button3']"

    #random number for review rating
    def randomstar(self):
        return random.randint(1,5)

    # Purchase product functions
    def tap_favshop(self):
        self.driver.find_element_by_xpath(self.loc_widget_favshop_1).click()

    def tap_product(self):
        self.driver.find_element_by_xpath(self.loc_widget_product_1).click()

    def tap_buy_product(self):
        self.swipeDown()
        self.snooze()
        self.driver.find_element_by_xpath(self.loc_widget_buy_button).click()

    def tap_buy_detail(self):
        self.swipeDown()
        self.snooze()
        print("select agency...")
        self.driver.find_element_by_xpath(self.loc_widget_agency).click()
        self.snooze()
        self.driver.find_element_by_xpath(self.loc_agency_selection["JNE"]).click()
        self.snooze()
        print("click buy button...")
        self.driver.find_element_by_xpath(self.loc_widget_buy_2).click()

    def tap_buy_payment_method(self):
        print("selecting payment method...")
        self.driver.find_element_by_xpath(self.loc_widget_pay).click()
        self.snooze()
        self.driver.find_element_by_xpath(self.loc_widget_select_payment_method).click()
        self.snooze()
        self.driver.find_element_by_xpath(self.loc_payment_method_selection["Saldo_tokopedia"]).click()
        print("Saldo Tokopedia selected")
        self.snooze()
        self.driver.find_element_by_xpath(self.loc_widget_checkout).click()

    def tap_buy_final_confirmation(self, password):
        print("Entering user password")
        self.driver.find_element_by_xpath(self.loc_checkout_pass).send_keys(password)
        self.snooze()
        self.driver.find_element_by_xpath(self.loc_confirm_pay).click()
        self.snooze()
        self.driver.find_element_by_xpath(self.loc_order_status).click()
        self.snooze()

    #order process functions
    def tap_order(self):
        print("Entering order list. . .")
        self.driver.find_element_by_xpath(self.loc_notification_tray_icon).click()
        self.explicit_wait(self.loc_notification_new_order)
        self.driver.find_element_by_xpath(self.loc_notification_new_order).click()
        self.explicit_wait(self.loc_latest_list_order)
        self.driver.find_element_by_xpath(self.loc_latest_list_order).click()
        self.snooze()
        self.swipeDown()
        self.snooze()
        self.driver.find_element_by_xpath(self.loc_accept_order).click()
        self.driver.find_element_by_xpath(self.loc_button_yes).click()
        self.snooze()
        self.driver.keyevent(4)
        self.explicit_wait(self.loc_notification_tray_icon)
        self.driver.find_element_by_xpath(self.loc_notification_tray_icon).click()
        self.explicit_wait(self.loc_notification_shipment_confirmation)
        self.driver.find_element_by_xpath(self.loc_notification_shipment_confirmation).click()
        self.driver.find_element_by_xpath(self.loc_latest_list_order).click()
        self.explicit_wait(self.loc_receipt_number)
        self.driver.find_element_by_xpath(self.loc_receipt_number).send_keys(str(random.randint(100000000000,999999999999)))
        self.swipeDown()
        self.driver.find_element_by_xpath(self.loc_confirm_shipping).click()
        self.snooze()
        order_success_text = self.driver.find_element_by_xpath(self.loc_order_shipped)
        return order_success_text.text

    #buyer confirmation that product has been received function
    def tap_buyer_confirm(self):
        self.driver.find_element_by_xpath(self.loc_notification_tray_icon).click()
        self.explicit_wait(self.loc_notification_latest)
        self.driver.find_element_by_xpath(self.loc_notification_latest).click()
        self.driver.find_element_by_xpath(self.loc_shipment_number).click()
        self.snooze()
        self.swipeDown()
        self.swipeDown()
        self.snooze()
        self.driver.find_element_by_xpath(self.loc_widget_package_received).click()
        self.explicit_wait(self.loc_button_yes)
        self.driver.find_element_by_xpath(self.loc_button_yes).click()
        self.explicit_wait(self.loc_button_yes)
        self.driver.find_element_by_xpath(self.loc_button_yes).click()
        self.explicit_wait(self.loc_review_top_item)
        self.driver.find_element_by_xpath(self.loc_review_top_item).click()

        print("Typing review. . .")
        self.driver.find_element_by_xpath(self.loc_review_detail["review_text"]).send_keys(self.dummy_text)

        print("Rating satisfaction. . .")
        self.driver.find_element_by_xpath(self.loc_review_detail["review_quality"]).click()
        self.driver.find_element_by_xpath("//android.widget.ImageView[@index='"+str(self.randomstar())+"']").click()

        self.driver.find_element_by_xpath(self.loc_review_detail["review_speed"]).click()
        self.driver.find_element_by_xpath("//android.widget.ImageView[@index='"+str(self.randomstar())+"']").click()

        self.driver.find_element_by_xpath(self.loc_review_detail["review_accuracy"]).click()
        self.driver.find_element_by_xpath("//android.widget.ImageView[@index='"+str(self.randomstar())+"']").click()

        self.driver.find_element_by_xpath(self.loc_review_detail["review_service"]).click()
        self.driver.find_element_by_xpath("//android.widget.ImageView[@index='"+str(self.randomstar())+"']").click()

        self.driver.find_element_by_xpath(self.loc_review_detail["review_submit"]).click()
        print("Review succeeded. Now logging out...")
        self.snooze(3)
