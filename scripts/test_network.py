import os,sys
sys.path.append(os.getcwd())
from base.base_driver import init_driver

from page.network_page import NetworkPage


class TestNetwork:
    def setup(self):
        self.driver = init_driver()
        self.network_page = NetworkPage(self.driver)


    def test_2g_network(self):
        self.network_page.click_more()
        self.network_page.click_network()
        self.network_page.click_first_network()
        self.network_page.click_network_2g()
        self.network_page
    def test_3g_network(self):
        self.network_page.click_more()
        self.network_page.click_network()
        self.network_page.click_first_network()
        self.network_page.click_network_3g()





