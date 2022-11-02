from base_page import BasePage


class MainPage(BasePage):

    def go_to_catalogue(self):
        self.browser.find_element(By.XPATH, '//*[@id="browse"]/li/ul/li[1]/a').click()
