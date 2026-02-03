import pytest
from pages.market_main_page import MarketPage

import allure
import pytest


@pytest.mark.regression
@pytest.mark.usefixtures('user_login')
class TestBuyProduct:
    @allure.title("Покупка продукта - основной тест")
    @allure.description("Тест процесса покупки товара: добавление в корзину и оформление заказа")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("purchase", "cart", "checkout")
    def test_buy_product(self, browser):
        with allure.step("Переход на страницу магазина"):
            p = MarketPage(browser)

        with allure.step("Добавление товара в корзину"):
            p.add_to_cart()

        with allure.step("Оформление заказа"):
            p.checkout()


@pytest.mark.regression
@pytest.mark.usefixtures('user_login')
class TestBuyProduct2:
    @allure.title("Покупка продукта - альтернативный тест")
    @allure.description("Второй тест процесса покупки товара")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("purchase", "cart", "checkout")
    def test_buy_product_2(self, browser):
        with allure.step("Инициализация страницы магазина"):
            p = MarketPage(browser)

        with allure.step("Добавление товара в корзину"):
            p.add_to_cart()

        with allure.step("Завершение процесса покупки"):
            p.checkout()