from selenium.webdriver.common.by import By

from base.base_action import BaseAction
class DisplayPage(BaseAction):
    view_button = By.XPATH,"//*[contains(@text,'显示')]"
    search_button = By.ID,'com.android.settings:id/search'
    search_textbox = By.ID,"android:id/search_src_text"
    back_button = By.CLASS_NAME,"android.widget.ImageButton"


    def click_view(self):
        self.click(self.view_button)

    def click_search(self):
        self.click(self.search_button)

    def input_search(self,text):
        self.input_text(self.search_textbox,text)

    def click_back(self):
        self.click(self.back_button)



