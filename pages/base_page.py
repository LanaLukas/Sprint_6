import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @allure.step('Находим видимый элемент')
    def find_visible_element(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator))

    @allure.step('Открываем страницу {url}')
    def open_url(self, url):
        self.driver.get(url)

    @allure.step('Ожидаем URL {url}')
    def wait_for_url_to_be(self, url, timeout=10):
        return WebDriverWait(self.driver, timeout).until(ec.url_to_be(url))

    @allure.step('Ожидаем URL содержит {text}')
    def wait_for_url_contains(self, text, timeout=10):
        return WebDriverWait(self.driver, timeout).until(ec.url_contains(text))

    @allure.step('Кликаем по элементу при доступности')
    def click_if_clickable(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable(locator)).click()
            return True
        except TimeoutException:
            return False

    @allure.step('Кликаем по логотипу Самокат')
    def click_scooter_logo(self):
        self.click_element(BasePageLocators.SCOOTER_LOGO)

    @allure.step('Кликаем по логотипу Яндекс')
    def click_yandex_logo(self):
        self.click_element(BasePageLocators.YANDEX_LOGO)

    @allure.step('Кликаем по элементу')
    def click_element(self, locator):
        self.wait.until(ec.element_to_be_clickable(locator)).click()

    @allure.step('Вводим текст в поле')
    def enter_text(self, locator, text):
        element = self.find_visible_element(locator)
        element.clear()
        element.send_keys(text)
        return element

    @allure.step('Проверяем видимость элемента')
    def is_element_visible(self, locator):
        try:
            self.wait.until(ec.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    @allure.step('Получаем текст элемента')
    def get_text(self, locator):
        return self.find_visible_element(locator).text

    @allure.step('Ожидаем появление нового окна')
    def wait_for_new_window(self, windows_count=2):
        self.wait.until(ec.number_of_windows_to_be(windows_count))

    @allure.step('Переключаемся на новое окно')
    def switch_to_new_window(self):
        self.wait_for_new_window()
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Получаем текущий URL')
    def get_current_url(self):
        return self.driver.current_url
