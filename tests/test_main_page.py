import pytest
import allure

from pages.main_page import MainPage
from test_data import (
    FAQ_ANSWER_1,
    FAQ_ANSWER_2,
    FAQ_ANSWER_3,
    FAQ_ANSWER_4,
    FAQ_ANSWER_5,
    FAQ_ANSWER_6,
    FAQ_ANSWER_7,
    FAQ_ANSWER_8,
)


class TestMainPage:
    @pytest.mark.parametrize(
        "question_number,expected_answer",
        [
            (1, FAQ_ANSWER_1),
            (2, FAQ_ANSWER_2),
            (3, FAQ_ANSWER_3),
            (4, FAQ_ANSWER_4),
            (5, FAQ_ANSWER_5),
            (6, FAQ_ANSWER_6),
            (7, FAQ_ANSWER_7),
            (8, FAQ_ANSWER_8),
        ],
        ids=[f"faq_{index}" for index in range(1, 9)],
    )
    @allure.title("FAQ: открывается ответ для вопроса №{question_number}")
    @allure.description("Проверяем, что при клике по стрелке вопроса в блоке FAQ отображается корректный текст ответа.")
    def test_faq_arrow_click_opens_answer(self, driver, question_number, expected_answer):
        main_page = MainPage(driver).open()
        main_page.accept_cookies_if_present()
        main_page.click_faq_question(question_number)
        answer_text = main_page.get_faq_answer_text(question_number)
        assert expected_answer == answer_text
        assert main_page.is_faq_answer_visible(question_number)
