import os,sys, time
from main.page.base import *
from main.function.general import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from random import randint
import time
import re
import math

class ResolutionCenter(BasePage):

    _pl = "resolution-center.pl"

     #locator path
    _menu_reso_center = (By.XPATH, "/html/body/div[1]/div[5]/div/div[1]/ul/li[1]/div[2]/div/ul/li[6]/a")
    _list_reso_log = (By.XPATH, "/html/body/div[1]/div[5]/div/div[2]/div/div[3]/div[1]/div/table")
    _shop_name = (By.XPATH, ".//*[@id='resolution-23918']/div[2]/div/p/span[3]/a")
    _status_reso2 = (By.XPATH, ".//*[@id='all-dispute-list']")

    _counter_complain_from_buyer = (By.XPATH, ".//*[@id='as-seller-link']/span/span")
    _counter_all_page = (By.XPATH, ".//*[@id='all-dispute-list']/div[2]/div[1]/div/small/b[2]")
    _inv_reso_detail = (By.XPATH, "/html/body/div[1]/div[5]/div/div[2]/div[2]/div[2]/div/p/a")

    _next_page = (By.XPATH, "/html/body/div[1]/div[5]/div/div[2]/div/div[3]/div[2]/div[2]/div/div/ul/li[4]/a/strong")

    _detail_textarea_loc = (By.XPATH, "//textarea[@id='reply-textarea']")
    _detail_button_submit = (By.XPATH, ".//*[@id='submit-comment']")
    _detail_upload_files = (By.XPATH, ".//*[@id='pickfiles']")
    _detail_edit_solution = (By.ID, "edit-solution")
    _detail_confirm_solution = (By.ID, "confirm-solution")
    _button_confirm_solution = (By.XPATH, ".//*[@id='rf']/div/button[2]")

    ### What problem occur in the order ?
    # The Quantity is different
    _detail_checkbox_1_of_3 = (By.XPATH, "/html/body/div[1]/div[5]/div/div[2]/div[2]/form/div/div[6]/div[2]/div/div/div[3]/label[1]/input")
    # Send remaining product
    _detail_checkbox_2_of_3 = (By.XPATH, "/html/body/div[1]/div[5]/div/div[2]/div/form/div/div[6]/div[4]/div/ul/li[3]/label/input")

    _change_other_checkbox_up = (By.XPATH, ".//*[@id='trouble-box']/div/div[3]/label[1]/input")

    ### What solution you want ?
    _change_other_checkbox_down = (By.XPATH, ".//*[@id='trouble-box']/div/div[3]/label[1]/input")
    _complaint_time = (By.XPATH, "/html/body/div[1]/div[5]/div/div[2]/div[2]/div[2]/div/p/span[1]")


    _response_checkbox_up = (By.XPATH, ".//*[@id='trouble-box']/div/div/label")
    _response_checkbox_up_2 = (By.XPATH, ".//*[@id='trouble-box']/div/div/label/input")
    _response_checkbox_down = (By.XPATH, ".//*[@id='solution-choice-div']/div[4]/div/ul/li/label")

    _problem_1_loc = (By.XPATH, ".//*[@id='trouble-box']/div/div[2]/label[1]/input")
    _problem_2_loc = (By.XPATH, ".//*[@id='trouble-box']/div/div[2]/label[2]/input")
    _problem_3_loc = (By.XPATH, ".//*[@id='trouble-box']/div/div[3]/label[1]/input")
    _problem_4_loc = (By.XPATH, ".//*[@id='trouble-box']/div/div[3]/label[2]/input")



    _total_invoice_s1 = (By.XPATH, ".//*[@id='solution-choice-div']/div[4]/div/ul/li[1]/div/span")
    _total_invoice_s3 = (By.XPATH, ".//*[@id='solution-choice-div']/div[4]/div/ul/li[4]/div/span")
    _total_invoice_s4 = (By.XPATH, ".//*[@id='ship_fee_span']")


    _fill_amount_refund_money_s1 = (By.XPATH, "/html/body/div[1]/div[5]/div/div[2]/div/form/div/div[6]/div[4]/div/ul/li[1]/div/input")
    _fill_amount_refund_money_s3 = (By.XPATH, "/html/body/div[1]/div[5]/div/div[2]/div/form/div/div[6]/div[4]/div/ul/li[4]/div/input")
    _fill_amount_refund_money_s4 = (By.XPATH, "/html/body/div[1]/div[5]/div/div[2]/div/form/div/div[6]/div[3]/input")


    #_total_invoice = (By.XPATH, "/html/body/div[1]/div[5]/div/div[2]/div/form/div/div[6]/div[4]/div/ul/li[1]/div/span/strong")
    _solution_1_loc = (By.XPATH, ".//*[@id='refund-sol']")
    _solution_2_loc = (By.XPATH, ".//*[@id='retur-good']")
    _solution_3_loc = (By.XPATH, ".//*[@id='retur-refund']")
    _solution_4_loc = (By.XPATH, ".//*[@id='send-remain']")
    _solution_5_loc = (By.XPATH, ".//*[@id='solution-choice-div']/div[3]/input")


    _dict_problem = {
        'problem_1_Text' : 'Product not same as description',
        'problem_2_Text' : 'Product is broken',
        'problem_3_Text' : 'The Quantity is different',
        'problem_4_Text' : 'Shipping agency is different'
    }

    _dict_solution_ = {
        'solution_1_Text' : 'Refund Money',
        'solution_2_Text' : 'Return product as order',
        'solution_3_Text' : 'Return product and refund',
        'solution_4_Text' : 'Send remaining product'
    }


    def open(self, site=""):
        self._open(site, self._pl)

    def view_complaint(self, driver, inv):
        cond = False
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(self._status_reso2))
            #self.check_visible_element(*self._status_reso2)
            status_temp = self.driver.find_element(*self._status_reso2)
            if status_temp.is_displayed():
                if ("Tidak ada data resolusi" in status_temp.text or "No Resolution Data" in status_temp.text):
                    print("No Resolution Data")
                else:
                    counter = int(self.driver.find_element(*self._counter_complain_from_buyer).text)
                    sum_page = int(self.driver.find_element(*self._counter_all_page).text)
                    total_page = math.ceil(sum_page/10)
                    x, y, z = 0, int(counter/10), int(counter%10)
                    if(z > 0):
                        y += 1
                    while x < y and not cond:
                        print("\n")
                        print("You are in Resolution Center page, in My Complaint tab section")
                        print("Page", [int(x+1)], "of", [total_page])
                        list_reso = self.find_elements(*self._list_reso_log)
                        for i in list_reso:
                            if inv in i.text:
                                time.sleep(2)
                                id_reso = i.find_element(By.TAG_NAME, "tr").get_attribute("id")
                                ticket_reso = self.find_element(By.XPATH, "//*[@id='"+id_reso+"']")
                                ticket_reso.click()
                                time.sleep(2)
                                shop_name_reso = self.driver.find_element(By.XPATH, ".//*[@id='resolution-"+id_reso+"']/div[2]/div/p/span[3]/a").text
                                inv_number = self.driver.find_element(*self._inv_reso_detail).text
                                time_complain = self.driver.find_element(*self._complaint_time).text
                                if (inv_number == inv):
                                    print ("The ticket resolution is valid in detail page")
                                print("Shop name : ", shop_name_reso," | ", inv_number )
                                print("Complaint Create Time : ", time_complain)
                                cond = True
                                break
                            time.sleep(1)
                        x += 1
                        if(x < y and not cond):
                            self.next_page()
                            print("Next page Resolution Center")
                            time.sleep(2)

                    if(not cond):
                        print("Resolution ticket like ", inv , "is Not Found!\n")

        except Exception as inst:
            print(inst)


    def fill_message_and_choose_problem(self, driver, reply_comment, choose_problem, total_shipping_fee):

        print ("Trying to choose Problem...")
        #WebDriverWait(driver, 10).until(EC.presence_of_element_located(self._detail_textarea_loc))
        input_comment = self.driver.find_element(*self._detail_textarea_loc)
        input_comment.clear()
        input_comment.send_keys(reply_comment)
        self.driver.find_element(*self._detail_edit_solution).click()
        time.sleep(2)
        self.desc_problem = choose_problem
        while switch(choose_problem):

            if case(1):
                responsiblity_checkbox_1 = self.find_elements(*self._response_checkbox_up)
                for i in responsiblity_checkbox_1:
                    cond1 = self._dict_problem['problem_1_Text']
                    if cond1 in i.text:
                        time.sleep(1)
                        self.driver.find_element(*self._problem_1_loc).click()
                        time.sleep(4)
                        check_validate_p1 = self.find_element(*self._problem_1_loc).get_attribute("checked")
                        if check_validate_p1 == "true":
                            print ("Other checkbox option of solution like - Product not same as description- is Checked")
                        else:
                            print ("**** Other checkbox option of solution like - Product not same as description- is NOT Checked !!!")
                break

            if case(2):
                responsiblity_checkbox_2 = self.find_elements(*self._response_checkbox_up)
                for i in responsiblity_checkbox_2:
                    cond2 = self._dict_problem['problem_2_Text']
                    if cond2 in i.text:
                        time.sleep(4)
                        self.driver.find_element(*self._problem_2_loc).click()
                        time.sleep(4)
                        check_validate_p2 = self.find_element(*self._problem_2_loc).get_attribute("checked")
                        if check_validate_p2 == "true":
                            print ("Other checkbox option of solution like -Product is broken- is Checked")
                        else:
                            print ("**** Other checkbox option of solution like -Product is broken- is NOT Checked !!!")
                break

            if case(3):
                responsiblity_checkbox_3 = self.find_elements(*self._response_checkbox_up)
                for i in responsiblity_checkbox_3:
                    cond3 = self._dict_problem['problem_3_Text']
                    if cond3 in i.text:
                        time.sleep(1)
                        self.driver.find_element(*self._problem_3_loc).click()
                        time.sleep(4)
                        check_validate_p3 = self.find_element(*self._problem_3_loc).get_attribute("checked")
                        if check_validate_p3 == "true":
                            print ("Other checkbox option of solution like -The Quantity is different- is Checked")
                        else:
                            print ("**** Other checkbox option of solution like -The Quantity is different- is NOT Checked !!!")
                break

            if case(4):
                responsiblity_checkbox_4 = self.find_elements(*self._response_checkbox_up)
                for i in responsiblity_checkbox_4:
                    self.cond4 = self._dict_problem['problem_4_Text']
                    if self.cond4 in i.text:
                        time.sleep(1)
                        self.driver.find_element(*self._problem_4_loc).click()
                        time.sleep(2)
                        check_validate_p4 = self.find_element(*self._problem_4_loc).get_attribute("checked")
                        if check_validate_p4 == "true":
                            print ("Other checkbox option of solution like -Shipping agency is different- is Checked")
                        else:
                            print ("**** Other checkbox option of solution like -Shipping agency is different- is NOT Checked !!! \n Please Check It")

                        print ("\nTrying to insert Total Shiping Fee...\n")
                        time.sleep(1)
                        getnum= self.driver.find_element(*self._total_invoice_s4)
                        enum = getnum.find_element(By.TAG_NAME, "strong").text
                        splitnum = enum.split(".")
                        join = "".join(splitnum)
                        current_amount = int(re.search(r'\d+', join).group())

                        self.driver.find_element(*self._fill_amount_refund_money_s4).clear()
                        self.driver.find_element(*self._fill_amount_refund_money_s4).send_keys(total_shipping_fee)
                        time.sleep(1)
                        if current_amount < int(total_shipping_fee):
                            print ("Error, Current amount that you filled out is greater than Rp "+str(current_amount)+",-")
                            print ("Your current emount is Rp "+total_shipping_fee+",-")
                            os._exit(1)
                        else:

                            self.driver.find_element(*self._detail_confirm_solution).click()
                            self.driver.find_element(*self._button_confirm_solution).click()
                            time.sleep(4)
                            self.driver.find_element(*self._detail_edit_solution).click()
                            time.sleep(1)
                            result_amount = self.driver.find_element(*self._fill_amount_refund_money_s4).get_attribute("value")

                            if (total_shipping_fee != result_amount):
                                print("Refund money and actual refund money is not same")
                            else:
                                print ("Checkbox option of solution as input shipping fee has been succesfully inserted")
                                print ("================================")
                                self.validate_problem()
                                print ("Attempt amount is Rp "+total_shipping_fee+",-")
                                print ("Result amount is Rp " +result_amount+",-")
                                print ("================================")
                                print ("Solution succesfully changed")
                                print ("All process finished")
                                os._exit(1)
                break



    def choose_solution(self, driver, choose_solution, fill_refund_money):

        print ("\nTrying to choose Solution...\n")
        self.solution = choose_solution
        while switch(choose_solution):
            if case(1):
                responsiblity_checkbox_1 = self.find_elements(*self._response_checkbox_down)
                for i in responsiblity_checkbox_1:
                    cond = self._dict_solution_['solution_1_Text']
                    if cond in i.text:
                        time.sleep(1)
                        self.driver.find_element(*self._solution_1_loc).click()
                        time.sleep(1)
                        getnum= self.driver.find_element(*self._total_invoice_s1)
                        enum = getnum.find_element(By.TAG_NAME, "strong").text
                        splitnum = enum.split(".")
                        join = "".join(splitnum)
                        current_amount = int(re.search(r'\d+', join).group())

                        self.driver.find_element(*self._fill_amount_refund_money_s1).clear()
                        self.driver.find_element(*self._fill_amount_refund_money_s1).send_keys(fill_refund_money)
                        time.sleep(2)
                        if current_amount < int(fill_refund_money):
                            print ("Error, Current amount that you filled out is greater than Rp "+str(current_amount)+",-")
                            print ("Your current emount is Rp "+fill_refund_money+",-")
                            os._exit(1)
                        else:
                            self.driver.find_element(*self._detail_confirm_solution).click()
                            self.driver.find_element(*self._button_confirm_solution).click()
                            time.sleep(4)
                            self.driver.find_element(*self._detail_edit_solution).click()
                            time.sleep(1)
                            result_amount = self.driver.find_element(*self._fill_amount_refund_money_s1).get_attribute("value")
                            check_validate_s1 = self.find_element(*self._solution_1_loc).get_attribute("checked")
                            if check_validate_s1 == "true":
                                if (fill_refund_money != result_amount):
                                    print("Refund money and actual refund money is not same")
                                else:
                                    print ("Checkbox option of solution like -Shipping agency is different- is Checked")
                                    print ("================================")
                                    self.validate_problem()
                                    print ("The solution is "+ cond)
                                    print ("Attempt amount is Rp "+fill_refund_money+",-")
                                    print ("Result amount is Rp " +result_amount+",-")
                                    print ("================================")
                                    print ("Solution succesfully changed")
                                    print ("All process finished")
                            else:
                                print ("**** Other checkbox option of solution like -Shipping agency is different- is NOT Checked !!!")
                break

            if case(2):
                responsiblity_checkbox_2 = self.find_elements(*self._response_checkbox_down)
                for i in responsiblity_checkbox_2:
                    cond = self._dict_solution_['solution_2_Text']
                    if cond in i.text:
                        time.sleep(1)
                        self.driver.find_element(*self._solution_2_loc).click()
                        time.sleep(1)
                        self.driver.find_element(*self._detail_confirm_solution).click()
                        self.driver.find_element(*self._button_confirm_solution).click()
                        time.sleep(4)
                        self.driver.find_element(*self._detail_edit_solution).click()
                        check_validate_s2 = self.find_element(*self._solution_2_loc).get_attribute("checked")
                        if check_validate_s2 == "true":
                            print ("Checkbox option of solution like -Return product as order- is Checked")
                            print ("================================")
                            self.validate_problem()
                            print ("The solution is "+ cond)
                            print ("================================")
                            print ("Solution succesfully changed")
                            print ("All process finished")

                        else:
                            print ("**** Checkbox option of solution like -Return product as order- is NOT Checked !!!")
                break

            if case(3):
                responsiblity_checkbox_3 = self.find_elements(*self._response_checkbox_down)
                for i in responsiblity_checkbox_3:
                    cond = self._dict_solution_['solution_3_Text']
                    if cond in i.text:
                        time.sleep(1)
                        self.driver.find_element(*self._solution_3_loc).click()
                        time.sleep(1)
                        getnum= self.driver.find_element(*self._total_invoice_s3)
                        enum = getnum.find_element(By.TAG_NAME, "strong").text
                        splitnum = enum.split(".")
                        join = "".join(splitnum)
                        current_amount = int(re.search(r'\d+', join).group())

                        self.driver.find_element(*self._fill_amount_refund_money_s3).clear()
                        self.driver.find_element(*self._fill_amount_refund_money_s3).send_keys(fill_refund_money)
                        time.sleep(2)
                        if current_amount < int(fill_refund_money):
                            print ("Error, Current amount that you filled out is greater than Rp "+str(current_amount)+",-")
                            print ("Your current emount is Rp "+fill_refund_money+",-")
                            os._exit(1)
                        else:
                            self.driver.find_element(*self._detail_confirm_solution).click()
                            self.driver.find_element(*self._button_confirm_solution).click()
                            time.sleep(4)
                            self.driver.find_element(*self._detail_edit_solution).click()
                            time.sleep(1)
                            result_amount = self.driver.find_element(*self._fill_amount_refund_money_s3).get_attribute("value")
                            check_validate_s1 = self.find_element(*self._solution_3_loc).get_attribute("checked")
                            if check_validate_s1 == "true":
                                if (fill_refund_money != result_amount):
                                    print("Refund money and actual refund money is not same")
                                else:
                                    print ("Checkbox option of solution like -Return product and refund- is Checked")
                                    print ("================================")
                                    self.validate_problem()
                                    print ("The solution is "+ cond)
                                    print ("Attempt amount is Rp "+fill_refund_money+",-")
                                    print ("Result amount is Rp " +result_amount+",-")
                                    print ("================================")
                                    print ("Solution succesfully changed")
                                    print ("All process finished")
                            else:
                                print ("**** Other checkbox option of solution like -Return product and refund- is NOT Checked !!!")
                break

            if case(4):
                responsiblity_checkbox_2 = self.find_elements(*self._response_checkbox_down)
                for i in responsiblity_checkbox_2:
                    cond = self._dict_solution_['solution_4_Text']
                    if cond in i.text:
                        time.sleep(1)
                        self.driver.find_element(*self._solution_4_loc).click()
                        time.sleep(1)
                        self.driver.find_element(*self._detail_confirm_solution).click()
                        self.driver.find_element(*self._button_confirm_solution).click()
                        time.sleep(4)
                        self.driver.find_element(*self._detail_edit_solution).click()
                        check_validate_s2 = self.find_element(*self._solution_4_loc).get_attribute("checked")
                        if check_validate_s2 == "true":
                            print ("Checkbox option of solution like -Send remaining product- is Checked")
                            print ("================================")
                            self.validate_problem()
                            print ("The solution is "+ cond)
                            print ("================================")
                            print ("Solution succesfully changed")
                            print ("All process finished")

                        else:
                            print ("**** Checkbox option of solution like -Return product as order- is NOT Checked !!!")
                break

    def next_page(self):
        try:
            next_other_page = self.driver.find_element(*self._next_page)
            next_other_page.click()
            time.sleep(2)
        except Exception as inst:
            print(inst)


    def validate_problem(self):
        if self.desc_problem == 1:
            print ("The problem is Product not same as description")
        elif self.desc_problem == 2:
            print ("The problem is Product is broken")
        elif self.desc_problem == 3:
            print ("The problem is The Quantity is different")
        elif self.desc_problem == 4:
            print ("The problem is Shipping agency is different")