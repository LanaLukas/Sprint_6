import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from test_data import BLACK_COLOR, GRAY_COLOR


class OrderPage(BasePage):
    @allure.step('Выбираем станцию метро {metro_station}')
    def select_metro_station(self, metro_station):
        self.enter_text(
            OrderPageLocators.METRO_STATION_DROPDOWN,
            metro_station
        )
        station_option = (
            OrderPageLocators.METRO_STATION_OPTION[0],
            OrderPageLocators.METRO_STATION_OPTION[1].format(station=metro_station),
        )
        self.click_element(station_option)

    @allure.step('Заполняем первую форму заказа')
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

    @allure.step('Заполняем вторую форму заказа')
    def fill_second_form(self, date, period, color, comment):
        date_input = self.enter_text(OrderPageLocators.DATE_INPUT, date)
        date_input.send_keys(Keys.ESCAPE)

        self.click_element(OrderPageLocators.RENT_PERIOD_DROPDOWN)
        period_option = (
            OrderPageLocators.RENT_PERIOD_OPTION[0],
            OrderPageLocators.RENT_PERIOD_OPTION[1].format(period=period),
        )
        self.click_element(period_option)

        color_locators = {
            BLACK_COLOR: OrderPageLocators.COLOR_CHECKBOX_BLACK,
            GRAY_COLOR: OrderPageLocators.COLOR_CHECKBOX_GREY,
        }
        color_locator = color_locators[color]
        self.click_element(color_locator)

        self.enter_text(OrderPageLocators.COMMENT_INPUT, comment)

    @allure.step('Подтверждаем заказ')
    def submit_order(self):
        self.click_element(OrderPageLocators.ORDER_BUTTON_FINAL)
        self.wait.until(
            ec.visibility_of_element_located(OrderPageLocators.CONFIRM_HEADER)
        )
        self.click_element(OrderPageLocators.CONFIRM_BUTTON_YES)

    @allure.step('Проверяем успешное оформление заказа')
    def is_order_successful(self):
        return bool(self.is_element_visible(OrderPageLocators.SUCCESS_HEADER))

    @allure.step('Создаем заказ')
    def create_order(self, name, surname, address, metro, phone, date, period, color, comment):
        self.fill_first_form(name, surname, address, metro, phone)
        self.fill_second_form(date, period, color, comment)
        self.submit_order()
