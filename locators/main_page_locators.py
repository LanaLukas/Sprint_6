from selenium.webdriver.common.by import By


class MainPageLocators:
    ORDER_BUTTON_TOP = (
        By.XPATH,
        "//div[contains(@class,'Header_Nav')]//button['Заказать']",
    )
    ORDER_BUTTON_BOTTOM = (
        By.XPATH,
        "//div[contains(@class,'Home_FinishButton')]//button['Заказать']",
    )

    ACCORDION_HEADING = "accordion__heading-"
    ACCORDION_PANEL = "accordion__panel-"

    CONFIRM_COOKIES_BUTTON = (By.ID, "rcc-confirm-button")

