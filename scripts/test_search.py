from base.base_driver import init_driver
from page.search_page import SearchPage
import  os ,sys
sys.path.append(os.getcwd())


class TestSearch():

    def setup(self):
        self.driver = init_driver()
        self.search_page = SearchPage(self.driver)

    def search_input(self):
        self.search_page.click()










