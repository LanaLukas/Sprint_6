from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def find_visible_element(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator))

    def click_scooter_logo(self):
        self.click_element(BasePageLocators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click_element(BasePageLocators.YANDEX_LOGO)

    def click_element(self, locator):
        self.wait.until(ec.element_to_be_clickable(locator)).click()

    def enter_text(self, locator, text):
        element = self.find_visible_element(locator)
        element.clear()
        element.send_keys(text)
        return element

    def is_element_visible(self, locator):
        try:
            self.wait.until(ec.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def get_text(self, locator):
        return self.find_visible_element(locator).text

    def wait_for_new_window(self, windows_count=2):
        self.wait.until(ec.number_of_windows_to_be(windows_count))

    def switch_to_new_window(self):
        self.wait_for_new_window()
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def get_current_url(self):
        return self.driver.current_url
