from main.page.header import *

#Check header status
class headerActivity():
    def check_header_status(self, driver, flag):
        header_page = HeaderPage(driver)

        header_page.check_header_status(flag)


    #Mouse hover to header
    def check_header_of_page(self, driver):
        header_page = HeaderPage(driver)

        header_page.mouse_hover_to_notification_bar()
        header_page.mouse_hover_and_go_to_inbox_message_notification()
