from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    URL = "https://qa-scooter.praktikum-services.ru/order"

    def select_metro_station(self, metro_station):
        metro_input = self.enter_text(
            OrderPageLocators.METRO_STATION_DROPDOWN,
            metro_station
        )

        options = self.wait.until(
            ec.visibility_of_all_elements_located(OrderPageLocators.METRO_STATION_OPTIONS)
        )

        station_name = metro_station.lower()
        for option in options:
            if station_name in option.text.lower():
                option.click()
                return

        metro_input.send_keys(Keys.ARROW_DOWN)
        metro_input.send_keys(Keys.ENTER)

    def fill_first_form(self, name, surname, address, metro, phone):
        self.enter_text(OrderPageLocators.NAME_INPUT, name)
        self.enter_text(OrderPageLocators.SURNAME_INPUT, surname)
        self.enter_text(OrderPageLocators.ADDRESS_INPUT, address)
        self.select_metro_station(metro)
        self.enter_text(OrderPageLocators.PHONE_INPUT, phone)
        self.click_element(OrderPageLocators.NEXT_BUTTON)

        self.wait.until(
            ec.visibility_of_element_located(OrderPageLocators.DATE_INPUT)
        )

    def fill_second_form(self, date, period, color, comment):
        date_input = self.enter_text(OrderPageLocators.DATE_INPUT, date)
        date_input.send_keys(Keys.ESCAPE)

        self.click_element(OrderPageLocators.RENT_PERIOD_DROPDOWN)
        period_option = (
            OrderPageLocators.RENT_PERIOD_OPTION[0],
            OrderPageLocators.RENT_PERIOD_OPTION[1].format(period=period),
        )
        self.click_element(period_option)

        if color == "чёрный":
            self.click_element(OrderPageLocators.COLOR_CHECKBOX_BLACK)
        elif color == "серый":
            self.click_element(OrderPageLocators.COLOR_CHECKBOX_GREY)

        if comment:
            self.enter_text(OrderPageLocators.COMMENT_INPUT, comment)

    def submit_order(self):
        self.click_element(OrderPageLocators.ORDER_BUTTON_FINAL)
        self.wait.until(
            ec.visibility_of_element_located(OrderPageLocators.CONFIRM_HEADER)
        )
        self.click_element(OrderPageLocators.CONFIRM_BUTTON_YES)

    def is_order_successful(self):
        return bool(self.is_element_visible(OrderPageLocators.SUCCESS_HEADER))

    def create_order(self, name, surname, address, metro, phone, date, period, color, comment):
        self.fill_first_form(name, surname, address, metro, phone)
        self.fill_second_form(date, period, color, comment)
        self.submit_order()
