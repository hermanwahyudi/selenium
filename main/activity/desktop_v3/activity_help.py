__author__ = 'QC1'


from main.page.desktop_v3.help.pe_help import *
from utils.lib.user import *
import time

class HelpActivity():

    def __init__(self, driver):
        self.help_page = HelpSitePage(driver)

    def set_parameter(self, param):
        self.dict = param

    def HelpPageInspection(self, driver):
        self.help_page.domain(self.dict['site'], self.dict['domain'])
        self.help_page.help_header_inspection()
        self.help_page.inspect_element()
        self.help_page.help_footer_inspection()
        print("Help page element inspection completed.")
        time.sleep(2)

    def HelpPageInputNoArticleFound (self, driver):
        self.help_page.domain(self.dict['site'], self.dict['domain'])
        print("Testing help microsite by inspecting article not found page...")
        self.help_page.help_header_inspection()
        self.help_page.help_search_error()
        self.help_page.help_sidebar_inspection()
        self.help_page.help_footer_inspection()
        print("No article page of Tokopedia help microsite passed the test!")
        time.sleep(2)

    def HelpPageInputSearchResult (self, driver):
        self.help_page.domain(self.dict['site'], self.dict['domain'])
        print("Testing help microsite by inspecting search result page...")
        self.help_page.help_header_inspection()
        self.help_page.help_search_input_found_result_page()
        self.help_page.help_sidebar_inspection()
        self.help_page.help_footer_inspection()
        print("Search result page of Tokopedia help microsite passed the test!")
        time.sleep(2)