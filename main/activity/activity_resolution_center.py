from main.page.resolution_center.pe_resolution_center import *
from main.page.login.pe_login import *

class Activity_Resolution_Center():

    _site = "live"

    def __init__(self, driver):
        self.login = LoginPage(driver)
        self.reso_center = ResolutionCenter (driver)

    def set_parameter(self, global_parameter):
        self.dict = global_parameter

    def goto_resolution_center(self, driver, inv):
        self.login.open(self._site)
        self.login.do_login(self.dict['email_buyer'], self.dict['psw_email_buyer'])
        self.reso_center.open(self._site)
        self.reso_center.view_complaint(driver, inv)

    def reply_comment_with_choose_problem(self, driver, reply_comment, choose_problem, total_shipping_fee):
        self.reso_center.fill_message_and_choose_problem(driver, reply_comment, choose_problem, total_shipping_fee)

    def choose_solution(self, driver, choose_solution, fill_refund_money):
        self.reso_center.choose_solution(driver, choose_solution, fill_refund_money)



