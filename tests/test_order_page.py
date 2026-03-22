from datetime import date

import allure

from pages.main_page import MainPage
from pages.order_page import OrderPage
from test_data import ORDER_DATA_1, ORDER_DATA_2
from test_url import DZEN_URL, MAIN_PAGE_URL, ORDER_PAGE_URL


class TestOrderPage:
    @allure.title('Переход на главную по логотипу "Самокат"')
    @allure.description("Проверяем, что после перехода на страницу заказа клик по логотипу Самокат возвращает на главную страницу.")
    def test_scooter_logo_navigates_to_main_page(self, driver):
        main_page = MainPage(driver).open()
        main_page.accept_cookies_if_present()

        main_page.click_order_button_top()
        main_page.wait_for_url_to_be(ORDER_PAGE_URL)
        main_page.click_scooter_logo()

        assert main_page.wait_for_url_to_be(MAIN_PAGE_URL)

    @allure.title('Переход в Дзен по логотипу "Яндекс"')
    @allure.description("Проверяем, что клик по логотипу Яндекса открывает новую вкладку и ведет на dzen.ru.")
    def test_yandex_logo_navigates_to_dzen(self, driver):
        main_page = MainPage(driver).open()
        main_page.accept_cookies_if_present()

        main_page.click_order_button_top()
        main_page.click_yandex_logo()
        main_page.switch_to_new_window()

        assert main_page.wait_for_url_contains(DZEN_URL)

    @allure.title('Позитивный сценарий заказа самоката по верхней кнопке')
    @allure.description("Проверяем полный сценарий заказа: старт по кнопке Заказать, заполнение формы и отображение окна успешного создания заказа.")
    def test_order_flow_top_button(self, driver):
        main_page = MainPage(driver).open()
        main_page.accept_cookies_if_present()

        main_page.click_order_button_top()

        order_page = OrderPage(driver)
        order_page.create_order(
            ORDER_DATA_1["name"],
            ORDER_DATA_1["surname"],
            ORDER_DATA_1["address"],
            ORDER_DATA_1["metro"],
            ORDER_DATA_1["phone"],
            date.today().strftime("%d.%m.%Y"),
            ORDER_DATA_1["period"],
            ORDER_DATA_1["color"],
            ORDER_DATA_1["comment"],
        )
        assert order_page.is_order_successful()

    @allure.title('Позитивный сценарий заказа самоката по нижней кнопке')
    @allure.description("Проверяем полный сценарий заказа: старт по кнопке Заказать, заполнение формы и отображение окна успешного создания заказа.")
    def test_order_flow_bottom_button(self, driver):
        main_page = MainPage(driver).open()
        main_page.accept_cookies_if_present()

        main_page.click_order_button_bottom()

        order_page = OrderPage(driver)
        order_page.create_order(
            ORDER_DATA_2["name"],
            ORDER_DATA_2["surname"],
            ORDER_DATA_2["address"],
            ORDER_DATA_2["metro"],
            ORDER_DATA_2["phone"],
            date.today().strftime("%d.%m.%Y"),
            ORDER_DATA_2["period"],
            ORDER_DATA_2["color"],
            ORDER_DATA_2["comment"],
        )
        assert order_page.is_order_successful()
