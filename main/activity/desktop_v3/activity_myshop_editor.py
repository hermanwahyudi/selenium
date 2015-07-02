from main.page.desktop_v3.myshop.pe_myshop_info import *
from main.page.desktop_v3.myshop.pe_myshop_etalase import *


class myshopEditorActivity():

    def setObject(self, driver):
        self.myshop_editor_page = MyshopInfoPage(driver)
        self.myshop_etalase_page = MyshopEtalasePage(driver)



    #---------------------------------------------
    # TAB : SHOP INFORMATION
    #---------------------------------------------
    def goto_myshop_editor(self,site=""):
        self.myshop_editor_page.open(site)

    def click_tab_shop_information(self):
        MyshopSettingsBasePage.select_tab_shop_information()

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


    #------------------------------------------
    #TAB : ETALASE
    #------------------------------------------
    def goto_myshop_etalase(self, site=""):
        self.myshop_etalase_page.open(site)

    def click_tab_etalase(self, driver):
        MyshopSettingsBasePage(driver).select_tab_etalase()

    def add_new_etalase(self, etal_name):
        temp = self.myshop_etalase_page.click_add_etalase()
        if temp ==1:
            self.myshop_etalase_page.input_etalase_name(etal_name)
        else:
            return 0

    def delete_last_etalase(self):
        self.myshop_etalase_page.delete_etalase()

    def add_then_edit_etalase(self, driver):
        for i in range(2):
            for x in self.myshop_etalase_page.list_in:
                if i == 0:
                    #self.myshop_etalase_page.add_etalase(x)
                    self.myshop_etalase_page.click_add_etalase()
                    self.myshop_etalase_page.input_etalase_name(x)
                elif i == 1:
                    #self.myshop_etalase_page.add_etalase(x)
                    self.myshop_etalase_page.click_edit_etalase()
                    self.myshop_etalase_page.input_etalase_name(x)
                time.sleep(1)
                driver.refresh()


    def act_n_times(self, driver, flag, N):
        print("Action " + str(flag) + " " + str(N) + " kali.")
        i = 0
        while (i < N):
            r = self.myshop_etalase_page.list_in[randint(0, len(self.myshop_etalase_page.list_in) - 1)]
            if (flag == "add"):
                self.myshop_etalase_page.click_add_etalase()
                self.myshop_etalase_page.input_etalase_name(r)
                print("Add Etalase ke-%s kali" %(str(i + 1)))
            if (flag == "edit"):
                #self.edit_etalase(r)
                self.myshop_etalase_page.click_edit_etalase()
                self.myshop_etalase_page.input_etalase_name(r)
                print("Edit Etalase ke-%s kali"  %(str(i + 1)))
            if (flag == "delete"):
                self.myshop_etalase_page.delete_etalase()
                print("Delete Etalase ke-%s kali"  %(str(i + 1)))
            driver.refresh()
            i += 1