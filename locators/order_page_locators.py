from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder*='Имя']")
    SURNAME_INPUT = (By.CSS_SELECTOR, "input[placeholder*='Фамилия']")
    ADDRESS_INPUT = (By.CSS_SELECTOR, "input[placeholder*='Адрес']")
    METRO_STATION_DROPDOWN = (By.CSS_SELECTOR, "input[placeholder*='Станция']")
    METRO_STATION_OPTION = (
        By.XPATH,
        "//div[contains(@class,'select-search__select')]//button[normalize-space()='{station}']",
    )
    PHONE_INPUT = (By.CSS_SELECTOR, "input[placeholder*='Телефон']")
    NEXT_BUTTON = (
        By.XPATH,
        "//button[contains(@class,'Button_Button') and normalize-space()='Далее']",
    )

    DATE_INPUT = (By.CSS_SELECTOR, "input[placeholder*='Когда привезти']")
    RENT_PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")
    RENT_PERIOD_OPTION = (
        By.XPATH,
        "//div[contains(@class,'Dropdown-option') and normalize-space()='{period}']",
    )
    COLOR_CHECKBOX_BLACK = (By.ID, "black")
    COLOR_CHECKBOX_GREY = (By.ID, "grey")
    COMMENT_INPUT = (By.CSS_SELECTOR, "input[placeholder*='Комментарий']")
    ORDER_BUTTON_FINAL = (
        By.XPATH,
        "//div[contains(@class,'Order_Buttons')]//button[normalize-space()='Заказать']",
    )

    CONFIRM_HEADER = (
        By.XPATH,
        "//div[contains(@class,'Order_ModalHeader') and contains(.,'Хотите оформить заказ')]",
    )
    CONFIRM_BUTTON_YES = (
        By.XPATH,
        "//div[contains(@class,'Order_Modal')]//div[contains(@class,'Order_Buttons')]//button[contains(@class,'Button_Middle') and not(contains(@class,'Button_Inverted'))]",
    )
    SUCCESS_HEADER = (
        By.XPATH,
        "//div[contains(@class,'Order_ModalHeader') and contains(.,'Заказ оформлен')]",
    )
