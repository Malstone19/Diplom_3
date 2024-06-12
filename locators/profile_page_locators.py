from selenium.webdriver.common.by import By


class ProfilePageLocators:
    PROFILE_LINK = By.LINK_TEXT, 'Личный Кабинет'
    HISTORY_LINK = By.LINK_TEXT, 'История заказов'
    LOGOUT_BUTTON = By.XPATH, './/button[contains(@class, "Account_button")]'  # Кнопка выхода из аккаунта

    NAME_FIELD = By.XPATH, './/label[text()="Имя"]/parent::div/input'  # Поле с именем пользователя

    # Номер первого заказа в истории заказов
    ORDER_NUMBER = By.XPATH, '(.//p[contains(@class, "text text_type_digits-default")])[1]'

    # Надпись со статусом первого заказа в истории заказов
    ORDER_DONE = By.XPATH, '(.//p[contains(@class, "OrderHistory_visible__19YMB")])[1]'

    # Номер последнего заказа в истории заказов
    LAST_ORDER = By.XPATH, '(.//div[contains(@class, "OrderHistory_textBox__3lgbs")]/p[contains(@class, "text text_type_digits-default")])[last()]'

    # Кнопка 'Оформить заказ' / 'Войти в аккаунт'
    ORDER_BUTTON = By.XPATH, './/button[contains(@class, "button_button_size_large")]'

    LOGIN_HEADER = By.XPATH, './/h2[text()="Вход"]'

    EMAIL_INPUT = By.XPATH, './/label[text()="Email"]/parent::div/input'
    PASS_INPUT = By.XPATH, './/label[text()="Пароль"]/parent::div/input'

    RESET_BUTTON = By.XPATH, './/button[contains(@class, "button_button_size_medium")]'
