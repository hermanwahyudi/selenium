from main.activity.activity_resolution_center import *
from selenium import webdriver
import time
import unittest


inv = "INV/20141209/XIV/XII/7536235"

class TestResolutionCenter (unittest.TestCase):


    dict = {
        "email_buyer" : "tkpd.qc+10@gmail.com",
        "psw_email_buyer" : "edy123#"
    }


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.RC = Activity_Resolution_Center(self.driver)
        self.RC.set_parameter(self.dict)

    def test_validate_resolution_ticket(self):
        print("-Validate Resolution Ticket-")
        driver = self.driver
        print ( "\n\nWhat problem occur in the order ? \n"
                "1. Product not same as description\n"
                "2. Product is broken\n"
                "Solution of 1 and 2:\n"
                        "1. Refund Money / Please fill total refund money\n"
                        "2. Return product as order\n"
                        "3. Return product and refund / Please fill total refund money\n"

                "\n3. The Quantity is different\n"
                "Solution:\n"
                        "1. Refund Money / Please fill total refund money\n"
                        "4. Send remaining product\n"
                        "3. Return product and refund / Please fill total refund money\n"
                "\n4. Shipping agency is different\n"
                        "[Please fill total shipping fee]\n"
                "\nEnter number of problem, solution, refund money(if needed) \n"
                "and total shipping fee(if needed)\n\n")

        while True:
            self.reply_comment = input('Fill discussion message : ')
            try:
                self.choose_problem = int(input('Enter the problem [1-4] : '))
                pass
                if (self.choose_problem == 4):
                    self.total_shipping_fee = int(input('Enter a mount of Total Shipping : '))
                    self.fill_refund_money = []
                    break

                elif (self.choose_problem > 0 and self.choose_problem < 4):
                    while True:
                        try:
                            self.choose_solution = int(input('Enter the solution [1-3] : '))
                            pass
                            if (self.choose_solution == 1 or self.choose_solution == 3):
                                self.fill_refund_money = int(input('Enter fill refund money : '))
                                self.total_shipping_fee = []
                                break
                            elif (self.choose_solution == 2 or self.choose_solution == 4):
                                self.total_shipping_fee, self.fill_refund_money = [], []
                                break
                            else:
                                print ("The range must be set between 1 to 4")
                        except ValueError:
                            print('Input must be numeric')
                    break
                else:
                    print ("The range must be set between 1 to 4")

            except ValueError:
                print('Input must be numeric')

        if (self.choose_problem == 1 or self.choose_problem ==2):
            if (self.choose_solution == 4):
                print ("\nProblem or solution option that you filled is not available")
                os._exit(1)
            else:
                pass

        if (self.choose_problem == 3):
            if(self.choose_solution == 2):
                print ("\nProblem or solution option that you filled is not available")
                os._exit(1)
            else:
                pass

        print("\nProcessing ... \n")
        self.RC.goto_resolution_center(driver, inv)
        self.RC.reply_comment_with_choose_problem(driver, self.reply_comment, self.choose_problem, self.total_shipping_fee)
        self.RC.choose_solution(driver, self.choose_solution, self.fill_refund_money)

    def tearDown(self):
        print("Testing akan selesai dalam beberapa saat..")
        time.sleep(5)
        #self.driver.close()

if __name__ == '__main__':
    unittest.main()