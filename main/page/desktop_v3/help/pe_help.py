__author__ = 'QC1'

from main.page.base import BasePage
from selenium.webdriver.common.by import By
import time

class HelpSitePage(BasePage):

    loading = time.sleep(2)



    #header locator
    _tokopedia_help_center_logo_loc = (By.XPATH, "/html/body/div[1]/div/div[1]")
    _tokopedia_com_loc = (By.XPATH, "/html/body/div[1]/div/div[2]/ul/li/a/span")

    #FAQ locator
    _FAQ_1_loc = (By.XPATH, "/html/body/section/div[1]/div[2]/div[1]/div/div[1]")
    _FAQ_2_loc = (By.XPATH, "/html/body/section/div[1]/div[2]/div[1]/div/div[2]")
    _FAQ_3_loc = (By.XPATH, "/html/body/section/div[1]/div[2]/div[1]/div/div[3]")

    _FAQ_1_Xbutton_loc = (By.XPATH, "//*[@id='div1']/div/div[2]/span")
    _FAQ_2_Xbutton_loc = (By.XPATH, "//*[@id='div2']/div/div[2]/span")
    _FAQ_3_Xbutton_loc = (By.XPATH, "//*[@id='div3']/div/div[2]/span")

    #search bar locator
    _search_input_loc = (By.XPATH, "/html/body/div[2]/div/div/div[2]/div/form/input")
    _search_submit_loc = (By.XPATH, "/html/body/div[2]/div/div/div[2]/div/form/button")

    #help header locator
    _header_my_acc_loc = (By.XPATH, "/html/body/section/div[1]/div[4]/div/div[1]/div[1]/div/h2")
    _header_buyer_loc = (By.XPATH, "/html/body/section/div[1]/div[4]/div/div[1]/div[2]/div/h2")
    _header_seller_loc = (By.XPATH, "/html/body/section/div[1]/div[4]/div/div[1]/div[3]/div/h2")
    _header_payment_loc =(By.XPATH, "/html/body/section/div[1]/div[4]/div/div[2]/div[1]/div/h2")
    _header_cash_withdrawal_loc = (By.XPATH, "/html/body/section/div[1]/div[4]/div/div[2]/div[2]/div/h2")
    _header_feature_loc = (By.XPATH, "/html/body/section/div[1]/div[4]/div/div[2]/div[3]/div/h2")
    _header_contact_us_loc = (By.XPATH, "/html/body/section/div[1]/div[4]/div/div[3]/div[1]/div/h2")
    _header_product_guide_loc = (By.XPATH, "/html/body/section/div[1]/div[4]/div/div[3]/div[2]/div/h2")
    _header_brand_violation_loc = (By.XPATH, "/html/body/section/div[1]/div[4]/div/div[3]/div[3]/div/h2")

    #help top 3 content locator
    _content_my_acc_loc = (By.XPATH, "/html/body/section/div[1]/div[4]/div/div[1]/div[1]/div/ul")
    _content_buyer_loc =  (By.XPATH, "/html/body/section/div[1]/div[4]/div/div[1]/div[2]/div/ul")
    _content_seller_loc = (By.XPATH, "/html/body/section/div[1]/div[4]/div/div[1]/div[1]/div/ul")
    _content_payment_loc = (By.XPATH, "/html/body/section/div[1]/div[4]/div/div[2]/div[1]/div/ul")
    _content_withdraw_loc = (By.XPATH, "/html/body/section/div[1]/div[4]/div/div[2]/div[2]/div/ul")
    _content_feature_loc = (By.XPATH, "/html/body/section/div[1]/div[4]/div/div[2]/div[3]/div/ul")
    _content_contact_us_loc = (By.XPATH, "/html/body/section/div[1]/div[4]/div/div[3]/div[1]/div/ul")
    _content_product_guide_loc = (By.XPATH, "/html/body/section/div[1]/div[4]/div/div[3]/div[2]/div/ul")
    _content_brand_violation_loc = (By.XPATH, "/html/body/section/div[1]/div[4]/div/div[3]/div[3]/div/ul")



    #video tutorial locator
    _video_tutorial_1_loc = (By.XPATH, "/html/body/section/div[2]/div/div/div/ul/li[1]")
    _video_tutorial_2_loc = (By.XPATH, "/html/body/section/div[2]/div/div/div/ul/li[2]")
    _video_tutorial_3_loc = (By.XPATH, "/html/body/section/div[2]/div/div/div/ul/li[3]")

    #footer locator
    _footer_copyright_loc = (By.XPATH, "/html/body/div[4]/div[1]")
    _footer_socialmed_loc = (By.XPATH, "/html/body/div[4]/div[2]")

    #help error locator
    _no_article_text_loc = (By.XPATH, "//*[@id='main-content']/div/div/div[1]/div/div/div[2]/p[2]")
    _contact_us_paragraph_loc = (By.XPATH, "//*[@id='main-content']/div/div/div[1]/div/div/div[2]/div/p")

    #search result page locator
    _search_result_text_loc = (By.XPATH, "//*[@id='main-content']/div/div/div[1]/div/div/div[2]/p")

    #help right sidebar locator
    _sidebar_my_account_loc = (By.XPATH, "//*[@id='main-content']/div/div/div[2]/ul/li[1]")
    _sidebar_buyer_loc = (By.XPATH, "//*[@id='main-content']/div/div/div[2]/ul/li[2]")
    _sidebar_seller_loc = (By.XPATH, "//*[@id='main-content']/div/div/div[2]/ul/li[3]")
    _sidebar_payment_loc = (By.XPATH, "//*[@id='main-content']/div/div/div[2]/ul/li[4]")
    _sidebar_withdraw_loc = (By.XPATH, "//*[@id='main-content']/div/div/div[2]/ul/li[5]")
    _sidebar_feature_loc = (By.XPATH, "//*[@id='main-content']/div/div/div[2]/ul/li[6]")
    _sidebar_contact_us_loc = (By.XPATH, "//*[@id='main-content']/div/div/div[2]/ul/li[7]")
    _sidebar_help_loc = (By.XPATH, "//*[@id='main-content']/div/div/div[2]/ul/li[8]")
    _sidebar_brand_loc = (By.XPATH, "//*[@id='main-content']/div/div/div[2]/ul/li[9]")


    def domain(self, site, x=""):
        self._open(site, x)
        self.target_domain = x

    def inspect_element(self):
        print("Inspecting the elements of Tokopedia Help Page...")
        time.sleep(1)

        print("Help FAQ 1 element is found")
        self.mouse_hover_to(*self._FAQ_1_loc)
        time.sleep(2)
        self.find_element(*self._FAQ_1_loc).click()
        print("Help FAQ 1 element can be clicked")
        time.sleep(2)
        self.find_element(*self._FAQ_1_Xbutton_loc).click()
        print("[X] button closed the FAQ - OK")
        time.sleep(2)

        # try:
        #     self.check_visible_element(*self._FAQ_1_Xbutton_loc).click()
        #
        # except Exception ('ElementNotVisibleException'):
        #     print("[X] button closed the FAQ - OK")
        #     time.sleep(2)



        print("Help FAQ 2 element is found")
        self.mouse_hover_to(*self._FAQ_2_loc)
        time.sleep(2)
        self.find_element(*self._FAQ_2_loc).click()
        print("Help FAQ 2 element can be clicked")
        time.sleep(2)
        self.find_element(*self._FAQ_2_Xbutton_loc).click()
        print("[X] button closed the FAQ - OK")
        time.sleep(2)

        print("Help FAQ 3 element is found")
        self.mouse_hover_to(*self._FAQ_3_loc)
        time.sleep(2)
        self.find_element(*self._FAQ_3_loc).click()
        print("Help FAQ 3 element can be clicked")
        time.sleep(2)
        self.find_element(*self._FAQ_3_Xbutton_loc).click()
        print("[X] button closed the FAQ - OK")
        time.sleep(2)

        print("Checking Help article Categories...")
        self.mouse_hover_to(*self._header_my_acc_loc)
        print("My Account header found.")
        self.find_element(*self._content_my_acc_loc)
        print("My Account content found.")
        time.sleep(2)
        self.mouse_hover_to(*self._header_buyer_loc)
        print("Buyer header found.")
        self.find_element(*self._content_buyer_loc)
        print("Buyer content found.")
        time.sleep(2)
        self.mouse_hover_to(*self._header_seller_loc)
        print("Seller header found.")
        self.find_element(*self._content_seller_loc)
        print("Seller content found.")
        time.sleep(2)
        self.mouse_hover_to(*self._header_payment_loc)
        print("Payment header found.")
        self.find_element(*self._content_payment_loc)
        print("Payment content found.")
        time.sleep(2)
        self.mouse_hover_to(*self._header_cash_withdrawal_loc)
        print("Cash withdrawal header found.")
        self.find_element(*self._content_withdraw_loc)
        print("Withdraw content found.")
        time.sleep(2)
        self.mouse_hover_to(*self._header_feature_loc)
        print("Feature header found.")
        self.find_element(*self._content_feature_loc)
        print("Feature content found.")
        time.sleep(2)
        self.mouse_hover_to(*self._header_contact_us_loc)
        print("Contact Us header found.")
        self.find_element(*self._content_contact_us_loc)
        print("Contact Us content found.")
        time.sleep(2)
        self.mouse_hover_to(*self._header_product_guide_loc)
        print("Product Guide header found.")
        self.find_element(*self._content_product_guide_loc)
        print("Product guide content found.")
        time.sleep(2)
        self.mouse_hover_to(*self._header_brand_violation_loc)
        print("Brand violation header found.")
        self.find_element(*self._content_brand_violation_loc)
        print("Brand violation content found.")
        print("All help category headers and contents are found.")
        time.sleep(2)


    def help_search_error(self):
        self.find_element(*self._search_input_loc).send_keys('asdasd')
        self.find_element(*self._search_submit_loc).click()
        time.sleep(2)
        print("Checking the elements of no article page of help microsite: ")
        time.sleep(2)
        assert self.find_element(*self._no_article_text_loc).text == 'Tidak ada artikel'
        print("No article text found.")
        assert self.find_element(*self._contact_us_paragraph_loc)
        print("Div box paragraph for contact us found.")
        time.sleep(2)

    def help_search_input_found_result_page(self):
        self.find_element(*self._search_input_loc).send_keys('Pembayaran')
        self.find_element(*self._search_submit_loc).click()
        time.sleep(2)
        print("Checking the elements of search result page: ")
        time.sleep(2)
        assert self.find_element(*self._search_result_text_loc).text == 'Hasil Pencarian Artikel "Pembayaran"'
        print("Search result success : ", self.find_element(*self._search_result_text_loc).text)


    def help_sidebar_inspection(self):
        print("Checking help sidebar on the right side of the page...")
        self.mouse_hover_to(*self._sidebar_my_account_loc)
        print("My Account sidebar found!")
        time.sleep(2)
        self.mouse_hover_to(*self._sidebar_buyer_loc)
        print("Buyer sidebar found!")
        time.sleep(2)
        self.mouse_hover_to(*self._sidebar_seller_loc)
        print("Seller sidebar found!")
        time.sleep(2)
        self.mouse_hover_to(*self._sidebar_payment_loc)
        print("Payment sidebar found!")
        time.sleep(2)
        self.mouse_hover_to(*self._sidebar_withdraw_loc)
        print("Withdrawal sidebar found!")
        time.sleep(2)
        self.mouse_hover_to(*self._sidebar_feature_loc)
        print("Feature sidebar found!")
        time.sleep(2)
        self.mouse_hover_to(*self._sidebar_contact_us_loc)
        print("Contact Us sidebar found!")
        time.sleep(2)
        self.mouse_hover_to(*self._sidebar_help_loc)
        print("Guide/ help sidebar found!")
        time.sleep(2)
        self.mouse_hover_to(*self._sidebar_brand_loc)
        print("Brand sidebar found!")
        time.sleep(2)

    def help_header_inspection(self):
        self.check_visible_element(*self._tokopedia_help_center_logo_loc)
        print("Tokopedia help center logo found")

        self.check_visible_element(*self._tokopedia_com_loc)
        print("tokopedia.com link at the top found")

    def help_footer_inspection(self):
        print("Checking Help site footer...")
        self.mouse_hover_to(*self._footer_copyright_loc)
        print("Footer Tokopedia copyright found.")
        self.mouse_hover_to(*self._footer_socialmed_loc)
        print("Footer Tokopedia social media found.")
        print("Help site footer check passed.")
