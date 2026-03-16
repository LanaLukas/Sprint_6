from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    URL = "https://qa-scooter.praktikum-services.ru/"

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get(self.URL)
        return self

    def click_order_button_top(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_TOP)

    def click_order_button_bottom(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_BOTTOM)

    def click_faq_question(self, question_number):
        self.click_element((By.ID, f"{MainPageLocators.ACCORDION_HEADING}{question_number - 1}"))

    def get_faq_answer_text(self, answer_number):
        return self.get_text((By.ID, f"{MainPageLocators.ACCORDION_PANEL}{answer_number - 1}"))

    def is_faq_answer_visible(self, answer_number):
        return self.is_element_visible((By.ID, f"{MainPageLocators.ACCORDION_PANEL}{answer_number - 1}"))

    def accept_cookies_if_present(self):
        try:
            cookie_button = WebDriverWait(self.driver, 5).until(
                ec.element_to_be_clickable(MainPageLocators.CONFIRM_COOKIES_BUTTON)
            )
            cookie_button.click()
        except TimeoutException:
            return
