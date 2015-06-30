from main.activity.activity_login import *
from main.activity.activity_myshop_order import *
from main.activity.activity_logout import *
from main.function.setup import *
from main.lib.user_data import *
from random import randint
import unittest


date_list = ["Today", "Tomorrow", "2 Days", "3 Days", "4 Days", "5 Days", "6 Days", "7 Days"]
courier_list = ["JNE", "TIKI", "RPX", "Pos Indonesia", "Wahana", "Cahaya", "Pandu", "First"]


class TestShippingConfirmation(unittest.TestCase):

    _site = "live"

    def setUp(self):
        self.driver = tsetup()
        print("Checking Shipping Confirmation Page")

    def test_1_check_all_filter(self):
        print ("TEST #1 : Check Filter")
        print ("==========================================")
        driver = self.driver

        email = user2['email']
        pwd = user2['pwd']

        #Object activity
        loginValidate = loginActivity()
        myshop_order = myshopOrderActivity()
        logoutValidate = logoutActivity()

        #Action
        loginValidate.do_login(driver, email, pwd, self._site)
        myshop_order.goto_myshop_order_process(driver, self._site)
        for each_date in date_list:
            myshop_order.choose_due_date(driver, each_date)
            time.sleep(2)
            for each_courier in courier_list:
                    myshop_order.choose_shipment(driver, each_courier)
                    time.sleep(2)
                    print ("Filter due date(%s) with courier (%s) has been checked" %(each_date,each_courier))
                    myshop_order.do_search(driver)
                    time.sleep(2)


        logoutValidate.do_logout(driver,self._site)

    def test_2_check_search_function(self):
        print ("TEST #2 : Check Search Function")
        print ("==========================================")
        driver = self.driver

        email = user2['email']
        pwd = user2['pwd']

        #Object activity
        loginValidate = loginActivity()
        myshop_order = myshopOrderActivity()
        logoutValidate = logoutActivity()
        loginValidate.do_login(driver, email, pwd, self._site)
        myshop_order.goto_myshop_order_process(driver, self._site)


        random_numb = randint(1,100000000)

        myshop_order.input_search_for_invoice(driver, random_numb)
        time.sleep(2)
        myshop_order.do_search(driver)
        time.sleep(3)

        logoutValidate.do_logout(driver, self._site)

    def tearDown(self):
        print("Testing akan selesai dalam beberapa saat..")
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(warnings='ignore')