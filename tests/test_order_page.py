from datetime import date, timedelta

import pytest
import allure
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from pages.main_page import MainPage
from pages.order_page import OrderPage
from test_data import DZEN_URL, ORDER_DATA_1, ORDER_DATA_2


class TestOrderPage:
    @allure.title('Переход на главную по логотипу "Самокат"')
    @allure.description("Проверяем, что после перехода на страницу заказа клик по логотипу Самокат возвращает на главную страницу.")
    def test_scooter_logo_navigates_to_main_page(self, driver):
        main_page = MainPage(driver).open()
        main_page.accept_cookies_if_present()

        main_page.click_order_button_top()
        WebDriverWait(driver, 10).until(ec.url_to_be(OrderPage.URL))
        main_page.click_scooter_logo()

        WebDriverWait(driver, 10).until(ec.url_to_be(MainPage.URL))
        assert main_page.get_current_url() == MainPage.URL

    @allure.title('Переход в Дзен по логотипу "Яндекс"')
    @allure.description("Проверяем, что клик по логотипу Яндекса открывает новую вкладку и ведет на dzen.ru.")
    def test_yandex_logo_navigates_to_dzen(self, driver):
        main_page = MainPage(driver).open()
        main_page.accept_cookies_if_present()

        main_page.click_order_button_top()
        main_page.click_yandex_logo()
        main_page.switch_to_new_window()

        WebDriverWait(driver, 10).until(
            lambda d: DZEN_URL in d.current_url
        )
        assert DZEN_URL in main_page.get_current_url()

    @pytest.mark.parametrize(
        "start_order,data",
        [
            (MainPage.click_order_button_top, ORDER_DATA_1),
            (MainPage.click_order_button_bottom, ORDER_DATA_2),
        ],
        ids=["top_button", "bottom_button"],
    )
    @allure.title("Позитивный сценарий заказа самоката: {start_order.__name__}")
    @allure.description("Проверяем полный сценарий заказа: старт по кнопке Заказать, заполнение формы и отображение окна успешного создания заказа.")
    def test_order_flow(self, driver, start_order, data):
        main_page = MainPage(driver).open()
        main_page.accept_cookies_if_present()

        start_order(main_page)

        order_page = OrderPage(driver)
        order_page.create_order(
            data["name"],
            data["surname"],
            data["address"],
            data["metro"],
            data["phone"],
            date.today().strftime("%d.%m.%Y"),
            data["period"],
            data["color"],
            data["comment"],
        )
        assert order_page.is_order_successful()
