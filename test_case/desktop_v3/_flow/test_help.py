__author__ = 'QC1'

from utils.function.setup import *
import time, unittest
from main.activity.desktop_v3.activity_help import *

class TestHelpSite(unittest.TestCase):
    dict = {
        "site" : "live",
        "domain" : "bantuan/"
    }

    def setUp(self):
        self.driver = tsetup("firefox")
        print("Test Case for Tokopedia Help microsite")
        print("======================================")
        self.activity = HelpActivity(self.driver)
        self.activity.set_parameter(self.dict)

    def test_1_help_site_element_inspection(self):
        print("Test #1 : Inspecting the elements of help site")
        print("==============================================")
        self.activity.HelpPageInspection(self.driver)

    def test_2_help_search_no_article_found(self):
        print("Test #2 : Help search no article found page")
        print("===========================================")
        self.activity.HelpPageInputNoArticleFound(self.driver)

    def test_3_help_search_result_page(self):
        print("Test #3: Help site search result page")
        print("=====================================")
        self.activity.HelpPageInputSearchResult(self.driver)


    def tearDown(self):
        print("Test environment will be closed in a few moment. . .")
        self.driver.close()
        time.sleep(5)

if(__name__ == "__main__"):
    unittest.main()