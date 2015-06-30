from main.page.myshop.pe_myshop_info import *

class myshopEditorActivity():

    def setObject(self, driver):
        self.myshop_editor_page = MyshopInfoPage(driver)

    def goto_myshop_editor(self,site=""):
        self.myshop_editor_page.open(site)

    def view_myshop(self):
        self.myshop_editor_page.click_view_my_shop()

    def edit_slogan_shop(self):
        self.myshop_editor_page.edit_slogan()

    def check_maximum_slogan_character(self):
        self.myshop_editor_page.check_max_slogan_char()

    def edit_shop_description(self):
        self.myshop_editor_page.edit_shop_description()

    def change_shop_status_to(self, status=""):
        print ("ACTION : Changing Shop Status..")
        print ("===============================")
        if status=="open":
            self.myshop_editor_page.set_shop_status_to_open()
        elif status=="close":
            self.myshop_editor_page.set_shop_status_to_closed()
            self.myshop_editor_page.edit_shop_closed_notes()
        else:
            self.myshop_editor_page.set_shop_status_to_open()

    #Validation
    def check_validation_input_shop_slogan_empty(self, driver):
        print ("CHECK VALIDATION : Input Slogan Empty")
        print ("=====================================")
        self.myshop_editor_page.input_slogan()
        self.myshop_editor_page.input_shop_description("Haloooooooooooooo haloooooooo")
        self.myshop_editor_page.click_save_button()
        time.sleep(2)
        try:
            assert list_myshop_info_validation['v_slogan'] in driver.find_element_by_tag_name("body").text
            print ("Assert success : %s "%(list_myshop_info_validation['v_slogan']))
        except:
            print ("Fail assert in : %s" %(list_myshop_info_validation['v_slogan']))

        try:
            assert list_myshop_info_validation['v_shop_description'] not in driver.find_element_by_tag_name("body").text
        except:
            print ("Fail assert not in : %s" %(list_myshop_info_validation['v_shop_description']))

        try:
            assert list_myshop_info_validation['v_shop_close_note'] not in driver.find_element_by_tag_name("body").text
        except:
            print ("Fail assert not in : %s" %(list_myshop_info_validation['v_shop_close_note']))

        try:
            assert list_myshop_info_validation['v_shop_close_date'] not in driver.find_element_by_tag_name("body").text
        except:
            print ("Fail assert not in : %s" %(list_myshop_info_validation['v_shop_close_date']))


    def check_validation_input_shop_description_empty(self, driver):
        print ("CHECK VALIDATION : Input Shop Description Empty")
        print ("===============================================")
        self.myshop_editor_page.input_slogan("adswewewq qweqw")
        self.myshop_editor_page.input_shop_description()
        self.myshop_editor_page.click_save_button()
        time.sleep(2)
        try:
            assert list_myshop_info_validation['v_slogan'] not in driver.find_element_by_tag_name("body").text
        except:
            print ("Fail assert not in : %s" %(list_myshop_info_validation['v_slogan']))

        try:
            assert list_myshop_info_validation['v_shop_description'] in driver.find_element_by_tag_name("body").text
            print ("Assert success : %s "%(list_myshop_info_validation['v_shop_description']))
        except:
            print ("Fail assert in : %s" %(list_myshop_info_validation['v_shop_description']))

        try:
            assert list_myshop_info_validation['v_shop_close_note'] not in driver.find_element_by_tag_name("body").text
        except:
            print ("Fail assert not in : %s" %(list_myshop_info_validation['v_shop_close_note']))

        try:
            assert list_myshop_info_validation['v_shop_close_date'] not in driver.find_element_by_tag_name("body").text
        except:
            print ("Fail assert not in : %s" %(list_myshop_info_validation['v_shop_close_date']))


    def check_validation_input_shop_closed_note_empty(self, driver):
        print ("CHECK VALIDATION : Input Shop Close Note Empty")
        print ("===============================================")
        self.myshop_editor_page.input_slogan("adswewewq qweqw")
        self.myshop_editor_page.input_shop_description("cloudy worddsssss")
        self.myshop_editor_page.set_shop_status_to_closed()
        self.myshop_editor_page.input_shop_close_note()
        self.myshop_editor_page.click_save_button()
        time.sleep(2)
        try:
            assert list_myshop_info_validation['v_slogan'] not in driver.find_element_by_tag_name("body").text
        except:
            print ("Fail assert not in : %s" %(list_myshop_info_validation['v_slogan']))

        try:
            assert list_myshop_info_validation['v_shop_description'] not in driver.find_element_by_tag_name("body").text

        except:
            print ("Fail assert in : %s" %(list_myshop_info_validation['v_shop_description']))

        try:
            assert list_myshop_info_validation['v_shop_close_note'] in driver.find_element_by_tag_name("body").text
            print ("Assert success : %s "%(list_myshop_info_validation['v_shop_close_note']))
        except:
            print ("Fail assert not in : %s" %(list_myshop_info_validation['v_shop_close_note']))

        try:
            assert list_myshop_info_validation['v_shop_close_date'] not in driver.find_element_by_tag_name("body").text
        except:
            print ("Fail assert not in : %s" %(list_myshop_info_validation['v_shop_close_date']))

    def check_validation_input_shop_closed_date_empty(self, driver):
        print ("CHECK VALIDATION : Input Shop Close Date Empty")
        print ("===============================================")
        self.myshop_editor_page.input_slogan("adswewewq qweqw")
        self.myshop_editor_page.input_shop_description("cloudy worddsssss")
        self.myshop_editor_page.set_shop_status_to_closed()
        self.myshop_editor_page.input_shop_close_note("Berlibur dulu yahh")
        self.myshop_editor_page.input_shop_close_date()
        self.myshop_editor_page.click_shop_close_note_text_area()
        self.myshop_editor_page.click_save_button()
        time.sleep(2)
        try:
            assert list_myshop_info_validation['v_slogan'] not in driver.find_element_by_tag_name("body").text
        except:
            print ("Fail assert not in : %s" %(list_myshop_info_validation['v_slogan']))

        try:
            assert list_myshop_info_validation['v_shop_description'] not in driver.find_element_by_tag_name("body").text
        except:
            print ("Fail assert in : %s" %(list_myshop_info_validation['v_shop_description']))

        try:
            assert list_myshop_info_validation['v_shop_close_note'] not in driver.find_element_by_tag_name("body").text
        except:
            print ("Fail assert not in : %s" %(list_myshop_info_validation['v_shop_close_note']))

        try:
            assert list_myshop_info_validation['v_shop_close_date'] in driver.find_element_by_tag_name("body").text
            print ("Assert success : %s "%(list_myshop_info_validation['v_shop_close_date']))
        except:
            print ("Fail assert not in : %s" %(list_myshop_info_validation['v_shop_close_date']))

    def check_validation_input_all_empty(self, driver):
        print ("CHECK VALIDATION : All Input Empty")
        print ("===============================================")
        self.myshop_editor_page.input_slogan()
        self.myshop_editor_page.input_shop_description()
        self.myshop_editor_page.set_shop_status_to_closed()
        self.myshop_editor_page.input_shop_close_note()
        self.myshop_editor_page.input_shop_close_date()
        self.myshop_editor_page.click_shop_close_note_text_area()
        self.myshop_editor_page.click_save_button()
        time.sleep(2)
        try:
            assert list_myshop_info_validation['v_slogan'] in driver.find_element_by_tag_name("body").text
            print ("Assert success : %s "%(list_myshop_info_validation['v_slogan']))
        except:
            print ("Fail assert not in : %s" %(list_myshop_info_validation['v_slogan']))

        try:
            assert list_myshop_info_validation['v_shop_description'] in driver.find_element_by_tag_name("body").text
            print ("Assert success : %s "%(list_myshop_info_validation['v_shop_description']))
        except:
            print ("Fail assert in : %s" %(list_myshop_info_validation['v_shop_description']))

        try:
            assert list_myshop_info_validation['v_shop_close_note'] in driver.find_element_by_tag_name("body").text
            print ("Assert success : %s "%(list_myshop_info_validation['v_shop_close_note']))
        except:
            print ("Fail assert not in : %s" %(list_myshop_info_validation['v_shop_close_note']))

        try:
            assert list_myshop_info_validation['v_shop_close_date'] in driver.find_element_by_tag_name("body").text
            print ("Assert success : %s "%(list_myshop_info_validation['v_shop_close_date']))
        except:
            print ("Fail assert not in : %s" %(list_myshop_info_validation['v_shop_close_date']))

    def do_save_changes(self):
        self.myshop_editor_page.save_changes()



