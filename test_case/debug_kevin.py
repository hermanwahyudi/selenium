from main.activity.activity_login import *
from main.activity.activity_logout import *
from main.activity.activity_myshop_editor import *
from main.lib.user_data import *
from main.function.setup import *
import unittest


class TestDebug(unittest.TestCase):

    _site = "live"

    def setUp(self):
        print ('TEST "Myshop-Editor"')
        self.driver = tsetup("phantomjs")


    def test_debug1(self):
        print ("TEST #1 : Change Shop Editor")
        print ("============================")
        driver = self.driver

        email = user1['email']
        pwd = user1['pwd']

        login = loginActivity()
        myshopEdit = myshopEditorActivity()
        logout = logoutActivity()

        login.do_login(driver, email, pwd, self._site)

        myshopEdit.setObject(driver)
        myshopEdit.goto_myshop_editor(self._site)
        myshopEdit.edit_slogan_shop()
        myshopEdit.edit_shop_description()
        myshopEdit.change_shop_status_to("close")
        time.sleep(3)

        myshopEdit.save_changes()
        time.sleep(2)

        logout.do_logout(driver, self._site)


    def tearDown(self):
        print("Testing akan selesai dalam beberapa saat..")
        self.driver.close()

if __name__ == '__main__':
    unittest.main(warnings='ignore')

# list_due_date = {
#         'Choose' : (By.XPATH, "/html/body/ul[1]/li[1]"),
#         'Today' : (By.XPATH, "/html/body/ul[1]/li[2]"),
#         'Tomorrow' : (By.XPATH, "/html/body/ul[1]/li[3]"),
#         '2 Days' : (By.XPATH, "/html/body/ul[1]/li[4]"),
#         '3 Days' : (By.XPATH, "/html/body/ul[1]/li[5]"),
#         '4 Days' : (By.XPATH, "/html/body/ul[1]/li[6]"),
#         '5 Days' : (By.XPATH, "/html/body/ul[1]/li[7]"),
#         '6 Days' : (By.XPATH, "/html/body/ul[1]/li[8]"),
#         '7 Days' : (By.XPATH, "/html/body/ul[1]/li[9]")
#     }
#
# keys = list(list_due_date)
# print (keys)
# print (list_due_date[random.choice(keys)])
#
# # for key in list_due_date:
# #     print (random.choice(list(list_due_date.items())))
#
# for a in range(len(list_due_date)):
#     # print (random.choice(list(list_due_date[a+1])))
#     # if a <1:
#     #     break
#     print (a)
#
# #print (list_due_date[a])
# # for a in list_due_date:
# #     print (random.choice(list_due_date[a]))