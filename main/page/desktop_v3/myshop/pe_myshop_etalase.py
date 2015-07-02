from main.page.desktop_v3.myshop.pe_myshop_base import *
from utils.function.general import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
import time


class MyshopEtalasePage(MyshopSettingsBasePage):
    # instance variable
    _page = "myshop-etalase.pl"
    _btn_add_loc = (By.CSS_SELECTOR, 'a#btn-add')
    _ename_loc = (By.CSS_SELECTOR, "div.control-group div.controls input#e-name")
    _submit_loc = (By.CSS_SELECTOR, "button.btn-action")
    _link_edit_loc = (By.CSS_SELECTOR, "a.edit-etalase")
    _link_delete_loc = (By.CSS_SELECTOR, "a.delete-etalase")
    _src_drag_loc = (By.CSS_SELECTOR, "i.icon-move")
    _dst_drag_loc = (By.CSS_SELECTOR, "li.li-711848")
    _submit_del_loc = (By.XPATH, "//button[@name='submit']")
    _link_edit_latest_loc = (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[2]/div/ol/li[last()]/div/div[3]/small/a[1]')

    # test case input
    list_in = ['', 'a', 'ما تم تؤكل', '什么被吃掉', 'វបានគេបរិភោគ', '131231']

    def open(self, site=""):
        self._open(site, self._page)


    def drag_etalase(self):
        try:
            print("Drag and Drop")
            time.sleep(2)
            src = self.driver.find_element(*self._src_drag_loc)
            dst = self.driver.find_element(*self._dst_drag_loc)
            ActionChains(self.driver).drag_and_drop(src, dst).perform()
        except Exception as inst:
            print(inst)


    def click_add_etalase(self):
        self.check_visible_element(*self._btn_add_loc)
        #self.check_clickable_element(*self._btn_add_loc)
        #wait_visible_element(self.driver,*self._btn_add_loc)
        #self.driver.refresh()
        target_element = self.find_element(*self._btn_add_loc)
        self.click_on_javascript(target_element)
        #self.check_visible_element(By.CSS_SELECTOR, 'div.container-fluid div#rf div.dialog-footer button.jqmClose')
        #self.driver.implicitly_wait(30)
        time.sleep(2)
        print ("asdwe")
        try:
            if "Anda hanya bisa menambah sampai 150 etalase." in self.driver.find_element_by_tag_name('body').text:
                print ("Etalase already reached maximum.")
                return 0
            elif "Anda hanya bisa menambah sampai 150 etalase." not in self.driver.find_element_by_tag_name('body').text:
                return 1
        except:
            print("Error before defining element of : Etalase")
            return 1

        #btn_add_etalase = self.find_element(*self._btn_add_loc)
        #self._click(btn_add_etalase)
        #print ("Button 'Add Etalase' not found!")



    def input_etalase_name(self, input1=""):
        self.check_visible_element(*self._ename_loc)
        self.find_element(*self._ename_loc).clear()
        self.find_element(*self._ename_loc).send_keys(input1)
        btn_submit = self.find_element(*self._submit_loc)
        self._click(btn_submit)
        time.sleep(2)
        assert "Maaf, Permohonan Anda tidak dapat diproses saat ini. Mohon dicoba kembali." not in self.driver.find_element_by_tag_name('body').text
        assert "Sorry, your request failed to be processed. Please try again." not in self.driver.find_element_by_tag_name('body').text
        print ("Etalase has been added successfully!")


    def click_edit_etalase(self):
        self.check_visible_element(*self._link_edit_latest_loc)
        self.driver.find_element(*self._link_edit_latest_loc).click()


    def delete_etalase(self, N=""):
        self.check_visible_element(*self._link_delete_loc)
        time.sleep(3)
        self.find_element(*self._link_delete_loc).click()
        time.sleep(3)
        self.find_element(*self._submit_del_loc).click()
        time.sleep(3)
        print ("Etalase[Top] has been deleted successfully!")


    def __str__(self):
        return "Page " + self.driver.title