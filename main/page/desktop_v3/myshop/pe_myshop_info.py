from main.page.desktop_v3.myshop.pe_myshop_base import *
import time

list_myshop_info_validation = {
    'v_slogan' : "Slogan harus diisi.",
    'v_shop_description' : "Deskripsi harus diisi.",
    'v_shop_close_note' : "Catatan harus diisi.",
    'v_shop_close_date' : "Tanggal penutupan tidak benar."
}

class MyshopInfoPage(MyshopSettingsBasePage):
    _page = "myshop-editor.pl"

    # Locators
    #'Membership' Section
    _extend_membership_btn = (By.CSS_SELECTOR, 'div.row-fluid div.span12 div.mt-10 a.btn-action')


    #'Shop Info' Section
    _slogan_text_area = (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[3]/form/div[2]/div[2]/input')
    _slogan_max_char = (By.CSS_SELECTOR, 'div.controls-row small.pull-right div#counter-tagline strong')
    _description_text_area = (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[3]/form/div[3]/div[2]/textarea[2]')
    _description_max_char = (By.CSS_SELECTOR, 'div.controls-row small.pull-right div#counter-desc strong')
    _select_shop_status = (By.CSS_SELECTOR, 'div.controls a.selectBox-dropdown span.selectBox-label')
    _shop_open_status = (By.XPATH, '/html/body/ul/li[2]/a')
    _shop_closed_status = (By.XPATH, '/html/body/ul/li[1]/a')
    _submit_save_btn = (By.CSS_SELECTOR, 'div.mb-20 div.controls div.span8 button.btn-action')

    #'Shop Image' Section
    _browse_image_btn = (By.CSS_SELECTOR, 'div.clear-b div.ellipsis a#pickfiles_shop')

    #'Shop Cover' Section
    _change_cover_btn = (By.CSS_SELECTOR, 'div.pull-right button#change-cover')
    _view_my_shop_loc = (By.XPATH, '/html/body/div[1]/div[5 ]/div/div[2]/div[4]/div/div/div[1]/ul/li[2]/a')

    #Conditional Loc
    _shop_closed_notes = (By.CSS_SELECTOR, 'div#close-detail div.controls input.span9')
    _shop_closed_date = (By.CSS_SELECTOR, 'div#close-detail div.controls-row div.controls input#closed_until')

    def open(self, site=""):
        self._open(site, self._page)

    def input_slogan(self, slogan=""):
        self.clear_slogan()
        self.find_element(*self._slogan_text_area).send_keys(slogan)

    def clear_slogan(self):
        self.check_visible_element(*self._slogan_text_area)
        self.find_element(*self._slogan_text_area).clear()

    def input_shop_description(self, description=""):
        self.clear_shop_description()
        self.find_element(*self._description_text_area).send_keys(description)

    def clear_shop_description(self):
        self.check_visible_element(*self._description_text_area)
        self.find_element(*self._description_text_area).clear()

    def input_shop_close_note(self, note=""):
        self.clear_shop_close_note()
        #self.check_visible_element(*self._shop_closed_notes)
        self.find_element(*self._shop_closed_notes).send_keys(note)

    def clear_shop_close_note(self):
        self.check_visible_element(*self._shop_closed_notes)
        self.find_element(*self._shop_closed_notes).clear()

    def input_shop_close_date(self, date=""):
        self.clear_shop_close_date()
        self.find_element(*self._shop_closed_date).send_keys(date)

    def click_shop_close_note_text_area(self):
        self.find_element(*self._shop_closed_date).click()

    def clear_shop_close_date(self):
        self.check_visible_element(*self._shop_closed_date)
        self.find_element(*self._shop_closed_date).clear()

    def click_view_my_shop(self):
        self.check_visible_element(*self._view_my_shop_loc)
        view_my_shop = self.find_element(*self._view_my_shop_loc)
        self._click(view_my_shop)

    def click_save_button(self):
        self.check_visible_element(*self._submit_save_btn)
        #self.find_element(*self._submit_save_btn).click()
        target = self.find_element(*self._submit_save_btn)
        self.click_on_javascript(target)

    def edit_slogan(self, input=""):
        print ("Check : Edit Shop Slogan")
        print ("======================")
        shop_slogan = "Fertile Ozone pleaseee!?"
        self.clear_slogan()
        if input != None:
            self.input_slogan(shop_slogan)
        else:
            self.input_slogan(input)
        print ("Shop Slogan: %s" %(shop_slogan))

    def check_max_slogan_char(self):
        slogan_max_char = self.find_element(*self._slogan_max_char).text
        print("Slogan Maximum Character : %s character" % (slogan_max_char))

        #CHECK Max Character Validation
        #print("Now checking Maximum character validation...")
        #time.sleep(2)
        #self.find_element(*self._slogan_text_area).clear()
        #self.find_element(*self._slogan_text_area).send_keys("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1")

    def edit_shop_description(self, input=""):
        print ("Check : Edit Shop Description")
        print ("=====================")
        shop_description = "Haloooooooooooooo haloooooooo"
        self.clear_shop_description()
        if input != None:
            self.input_shop_description(shop_description)
        else:
            self.input_shop_description(input)
        print ("Shop Description : %s" %(shop_description))

    def check_max_description_char(self):
        shop_description_max_char = self.find_element(*self._description_max_char)
        print ("Shop Description Maximum : %s character" %(shop_description_max_char))
        print ("Now checking Maximum character validation...")

    def set_shop_status_to_open(self):
        print ("Set Shop Status to : Open")
        self.check_visible_element(*self._select_shop_status)
        self.find_element(*self._select_shop_status).click()
        self.check_visible_element(*self._shop_open_status)
        self.find_element(*self._shop_open_status).click()

    def set_shop_status_to_closed(self):
        print ("Set Shop Status to : Closed")
        self.check_visible_element(*self._select_shop_status)
        self.find_element(*self._select_shop_status).click()
        self.check_visible_element(*self._shop_closed_status)
        self.find_element(*self._shop_closed_status).click()


    def edit_shop_closed_notes(self):
        shop_notes = "Mau Berlibur dulu yahhhhhhhhhhhhh"

        self.clear_shop_close_note()
        self.input_shop_close_note(shop_notes)
        print ("Input Shop Notes : %s" %(shop_notes))


    def save_changes(self):
        self.click_save_button()
        print("The changes you made has been saved!")






