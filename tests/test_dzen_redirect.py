import allure
import pytest

from pages.main_page import MainPage
from utils.constants import Urls


class TestDzenRedirect:

    @allure.feature('Функциональность открытия новой вкладки dzen.')
    @allure.description('Проверка открытия новой вкладки dzen с разных страниц.')
    @pytest.mark.parametrize("initial_url", [Urls.ORDER_URL, Urls.TRACK_URL])
    def test_yandex_logo_redirect(self, driver, initial_url):
        main_page = MainPage(driver)
        main_page.open_page(initial_url)
        main_page.click_cookies_accept_button()
        main_page.click_yandex_logo()
        assert main_page.check_new_window(Urls.DZEN_REDIRECT)