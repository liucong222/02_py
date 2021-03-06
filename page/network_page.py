import sys, os

from selenium.webdriver.common.by import By
from base.base_action import BaseAction
sys.path.append(os.getcwd())


class NetworkPage(BaseAction):
    more_button = By.XPATH,"//*[contains(@text,'更多')]"
    network_button = By.XPATH, "//*[contains(@text,'移动网络')]"
    first_network_button = By.XPATH, "//*[contains(@text,'首选网络类型')]"
    network_2g_button = By.XPATH,"//*[contains(@text,'2G')]"
    network_3g_button = By.XPATH,"//*[contains(@text,'3G')]"


    def click_more(self):
        self.click(self.more_button)

    def click_network(self):
        self.click(self.network_button)

    def click_first_network(self):
        self.click(self.first_network_button)

    def click_network_2g(self):
        self.click(self.network_2g_button)

    def click_network_3g(self):
        self.click(self.network_3g_button)