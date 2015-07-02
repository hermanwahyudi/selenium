__author__ = 'QC1'

from main.page.android.andr_base import *

class PageShop(PageBaseMobile):

    #add new product locator
    loc_widget_pic = {"pic1" : "//android.widget.ImageView[@resource-id='com.tokopedia.tkpd:id/imageborder1']",
                      "pic2" : "//android.widget.ImageView[@resource-id='com.tokopedia.tkpd:id/imageborder2']",
                      "pic3" : "//android.widget.ImageView[@resource-id='com.tokopedia.tkpd:id/imageborder3']",
                      "pic4" : "//android.widget.ImageView[@resource-id='com.tokopedia.tkpd:id/imageborder4']",
                      "pic5" : "//android.widget.ImageView[@resource-id='com.tokopedia.tkpd:id/imageborder5']"
                      }

    loc_widget_album_download = "//android.widget.TextView[@resource-id='com.tokopedia.tkpd:id/picture_gallery_album_name'][@text='Download']"
    loc_widget_image_select = "//android.widget.ImageView[@resource-id='com.tokopedia.tkpd:id/picture_gallery_imageview']"

    loc_widget_uploaded_action = {"description" : "//android.widget.TextView[@index='0']",
                                  "main_picture" : "//android.widget.TextView[@index='1']",
                                  "delete" : "//android.widget.TextView[@index='2']"}

    loc_input_product_name = "//android.widget.EditText[@resource-id='com.tokopedia.tkpd:id/product_name']"
    loc_widget_1st_category = "//android.widget.Spinner[@resource-id='com.tokopedia.tkpd:id/categories']"
    loc_widget_2nd_category = "//android.widget.Spinner[@resource-id='com.tokopedia.tkpd:id/categories2']"
    loc_widget_3rd_category = "//android.widget.Spinner[@resource-id='com.tokopedia.tkpd:id/categories3']"

    loc_select_1st_category = "//android.widget.CheckedTextView[@resource-id='android:id/text1'][@index='1']"
    loc_select_2nd_category = "//android.widget.CheckedTextView[@resource-id='android:id/text1'][@index='1']"
    loc_select_3rd_category = "//android.widget.CheckedTextView[@resource-id='android:id/text1'][@index='1']"

    loc_widget_currency = "//android.widget.Spinner[@resource-id='com.tokopedia.tkpd:id/currency']"
    loc_select_currency_dollar = "//android.widget.CheckedTextView[@resource-id='android:id/text1'][@index='1']"
    loc_input_price = "//android.widget.EditText[@resource-id='com.tokopedia.tkpd:id/price']"

    loc_input_weight = "//android.widget.EditText[@resource-id='com.tokopedia.tkpd:id/weight']"
    loc_widget_weight_unit = "//android.widget.Spinner[@resource-id='com.tokopedia.tkpd:id/weight_unit']"
    loc_select_weight_unit_kg = "//android.widget.CheckedTextView[@resource-id='android:id/text1'][@index='1']"

    loc_widget_minimum_order = "//android.widget.EditText[@resource-id='com.tokopedia.tkpd:id/minimum_order']"

    loc_assert_prod_name = "//android.widget.TextView[@resource-id='com.tokopedia.tkpd:id/prod_name'][@text='test product']"

    #skipping wholesale price

    loc_widget_add_to = "//android.widget.Spinner[@resource-id='com.tokopedia.tkpd:id/add_to']"
    loc_widget_add_to_warehouse = "//android.widget.CheckedTextView[@text='Gudang']"

    loc_widget_prod_desc = "//android.widget.EditText[@resource-id='com.tokopedia.tkpd:id/desc']"
    loc_widget_save_product = "//android.widget.TextView[@resource-id='com.tokopedia.tkpd:id/submit']"
    loc_widget_save_product_add_new = "//android.widget.TextView[@resource-id='com.tokopedia.tkpd:id/submit_2']"




    #etalase locator
    loc_widget_add_new = "//android.widget.TextView[@resource-id='com.tokopedia.tkpd:id/action_add_new']"
    loc_widget_edit = "//android.widget.ImageView[@resource-id='com.tokopedia.tkpd:id/edit_but']"
    loc_widget_delete = "//android.widget.ImageView[@resource-id='com.tokopedia.tkpd:id/delete_but']"

    loc_widget_etalase_input = "//android.widget.EditText[@resource-id='com.tokopedia.tkpd:id/message_talk']"
    loc_widget_save = loc_widget_pic_gallery = "//android.widget.Button[@resource-id='android:id/button1']"
    loc_widget_cancel = loc_widget_pic_camera =  "//android.widget.Button[@resource-id='android:id/button2']"

    def add_new_etalase(self, etalase_name):
        self.driver.find_element_by_xpath(self.loc_widget_add_new).click()
        print("Etalase name: ", etalase_name)
        self.driver.find_element_by_xpath(self.loc_widget_etalase_input).send_keys(etalase_name)
        self.driver.find_element_by_xpath(self.loc_widget_save).click()
        self.snooze()

    def delete_etalase(self):
        self.driver.find_element_by_xpath(self.loc_widget_delete).click()
        self.driver.find_element_by_xpath(self.loc_widget_save).click()
        self.snooze()

    def upload_picture(self):
        self.snooze()
        self.driver.find_element_by_xpath(self.loc_widget_pic["pic1"]).click()
        self.driver.find_element_by_xpath(self.loc_widget_pic_gallery).click()
        self.driver.find_element_by_xpath(self.loc_widget_album_download).click()
        self.driver.find_element_by_xpath(self.loc_widget_image_select).click()
        self.snooze()

    def insert_product_detail(self):
        self.driver.find_element_by_xpath(self.loc_input_product_name).send_keys("test product")
        self.driver.find_element_by_xpath(self.loc_widget_1st_category).click()
        self.snooze(1)
        self.driver.find_element_by_xpath(self.loc_select_1st_category).click()
        self.snooze(1)
        self.driver.find_element_by_xpath(self.loc_widget_2nd_category).click()
        self.snooze(1)
        self.driver.find_element_by_xpath(self.loc_select_2nd_category).click()
        self.snooze(1)
        self.driver.find_element_by_xpath(self.loc_widget_3rd_category).click()
        self.snooze(1)
        self.driver.find_element_by_xpath(self.loc_select_3rd_category).click()
        self.swipeDown(250, 800, 250, 550, 300)
        self.driver.find_element_by_xpath(self.loc_input_price).send_keys('1111')
        self.driver.find_element_by_xpath(self.loc_input_weight).send_keys('1')
        self.swipeDown(250, 800, 250, 550, 300)
        self.snooze(1)
        print("Adding minimum order. . .")
        self.driver.find_element_by_xpath(self.loc_widget_minimum_order).send_keys('1')
        self.swipeDown(250, 800, 250, 550, 300)
        self.snooze(1)
        print("Adding add to. . .")
        self.driver.find_element_by_xpath(self.loc_widget_add_to).click()
        self.snooze(1)
        self.driver.find_element_by_xpath(self.loc_widget_add_to_warehouse).click()
        self.swipeDown()
        self.explicit_wait(self.loc_widget_prod_desc)
        self.driver.find_element_by_xpath(self.loc_widget_prod_desc).send_keys('testing product description by inputing this text')
        self.driver.find_element_by_xpath(self.loc_widget_save_product).click()
        self.snooze(5)
        assert self.driver.find_element_by_xpath(self.loc_assert_prod_name)
        print("Product upload succeeded")
