from selenium.webdriver.common.by import By


class OrdersFeedLocators:
    ORDER_FEED_HEADER = By.XPATH, './/h1[text()="Лента заказов"]'

    # Первый заказ в ленте заказов
    FIRST_ORDER = By.XPATH, '(.//a[contains(@class, "OrderHistory_link__1iNby")])[1]'

    ORDER_WINDOW = By.XPATH, './/div[contains(@class, "Modal_orderBox__1xWdi")]/parent::div/parent::section'
    CLOSE_WINDOW_ORDER_BUTTON = By.XPATH, '(.//button[contains(@class, "Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK")])[last()]'
    ORDER_NUMBER_IN_WINDOW = By.XPATH, './/p[contains(@class, "text text_type_digits-default mb-10 mt-5")]'

    # Счетчик "Выполнено за все время"
    ALL_ORDERS_COUNTER = By.XPATH, '(.//p[contains(@class, "OrderFeed_number__2MbrQ")])[1]'

    # Счетчик "Выполнено за сегодня"
    TODAY_ORDERS_COUNTER = By.XPATH, '(.//p[contains(@class, "OrderFeed_number__2MbrQ")])[last()]'

    # Надпись, о том, что нет заказов в работе
    EMPTY_ORDERS_IN_WORK = By.XPATH, './/li[text()="Все текущие заказы готовы!"]'

    # Заказы находящиеся в работе
    ORDERS_IN_WORK = By.XPATH, '(.//ul[contains(@class, "OrderFeed_orderListReady")]/li)[1]'

    # Локатор подтверждающий, что окно заказа, загрузилось
    ORDER_WINDOW_OPENED = By.XPATH, './/div[contains(@class, "Modal_modal_opened__3ISw4")]'

    # Локатор подтверждающий, что окно заказа закрыто
    ORDER_WINDOW_CLOSE = By.XPATH, './/section[contains(@class, "Modal_modal__P3_V5")]'

    PROFILE_LINK = By.LINK_TEXT, 'Личный Кабинет'
    HISTORY_LINK = By.LINK_TEXT, 'История заказов'

    # Номер последнего заказа в истории заказов
    LAST_ORDER = By.XPATH, '(.//div[contains(@class, "OrderHistory_textBox__3lgbs")]/p[contains(@class, "text text_type_digits-default")])[last()]'

    # Номер заказа, во всплывающем окне, при оформлении
    ORDER_NUMBER = By.XPATH, './/h2[contains(@class, "title_shadow__3ikwq")]'

    ORDER_FEED_LINK = By.XPATH, './/p[text()="Лента Заказов"]'

    BUILDER_HEADER = By.XPATH, './/h1[text()="Соберите бургер"]'

    BUILDER_LINK = By.LINK_TEXT, 'Конструктор'

    # Зона, куда перетаскиваются ингредиенты
    DROP_BASKET_AREA = By.XPATH, './/section[contains(@class, "BurgerConstructor_basket")]'

    # Первая булка в конструкторе
    FIRST_BUN = By.XPATH, '(.//a[contains(@href, "/ingredient/")])[1]'

    # Кнопка 'Оформить заказ' / 'Войти в аккаунт'
    ORDER_BUTTON = By.XPATH, './/button[contains(@class, "button_button_size_large")]'
