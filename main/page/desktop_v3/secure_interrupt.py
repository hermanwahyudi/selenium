from main.page.desktop_v3.myshop.pe_myshop_base import *
from utils.lib.user import *

class SecurityInterruptPage(MyshopSettingsBasePage):

    _page = "interrupt.pl?type=security_check"

    #Locators
    _interrupt_type_loc = (By.CSS_SELECTOR, 'div.text-left p')
    _input_text_loc = (By.CSS_SELECTOR, 'form#register-form div.text-left input.span12')
    _submit_loc = (By.CSS_SELECTOR, 'div.row-fluid div.span12 button#confirm')

    def input_answer(self,type, input):
        if type == "phone":
            print ("coba phone" + input)
            self.find_element(*self._input_text_loc).send_keys(input)
            print ("phone")
            time.sleep(5)
        elif type == "bank_account":
            print ("coba bank : " + input)
            self.find_element(*self._input_text_loc).send_keys(input)
            print ("bank acc")
            time.sleep(5)

    def click_submit(self):
        self.check_clickable_element(*self._submit_loc)
        click_submit = self.find_element(*self._submit_loc)
        self._click(click_submit)

    def check_security_question(self, phone_numb, bank_acc):
        if self.find_element(*self._interrupt_type_loc).text == "Masukkan nomor HP Anda yang sudah terverifikasi di Tokopedia:":
            self.input_answer("phone", phone_numb)
            self.click_submit()
        elif self.find_element(*self._interrupt_type_loc).text == "Masukkan nomor Rekening Anda yang sudah terverifikasi di Tokopedia:":
            self.input_answer("bank_account", bank_acc)
            self.click_submit()
        else:
            raise Exception("Interrupt Security faced an issue! needs to be checked!")



