import allure
from selenium.webdriver.common.by import By

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from test_url import MAIN_PAGE_URL


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открываем главную страницу')
    def open(self):
        self.open_url(MAIN_PAGE_URL)
        return self

    @allure.step('Нажимаем кнопку Заказать в хедере')
    def click_order_button_top(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_TOP)

    @allure.step('Нажимаем кнопку Заказать внизу страницы')
    def click_order_button_bottom(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_BOTTOM)

    @allure.step('Нажимаем на вопрос FAQ №{question_number}')
    def click_faq_question(self, question_number):
        self.click_element((By.ID, f"{MainPageLocators.ACCORDION_HEADING}{question_number - 1}"))

    @allure.step('Получаем текст ответа FAQ №{answer_number}')
    def get_faq_answer_text(self, answer_number):
        return self.get_text((By.ID, f"{MainPageLocators.ACCORDION_PANEL}{answer_number - 1}"))

    @allure.step('Проверяем видимость ответа FAQ №{answer_number}')
    def is_faq_answer_visible(self, answer_number):
        return self.is_element_visible((By.ID, f"{MainPageLocators.ACCORDION_PANEL}{answer_number - 1}"))

    @allure.step('Принимаем cookies')
    def accept_cookies_if_present(self):
        self.click_if_clickable(MainPageLocators.CONFIRM_COOKIES_BUTTON, timeout=5)
