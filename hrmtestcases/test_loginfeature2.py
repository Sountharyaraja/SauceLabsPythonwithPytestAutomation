import pytest

from conftest import *
from hrmpages.loginPage import LoginPage


@pytest.mark.usefixtures("browser_setup")
class Test_Login:
    def setup_class(self):
        self.driver.get(BaseUrl)
        self.loginPage=LoginPage(self.driver)

    def test_valid_login(self):
        self.loginPage.login(Username,Password)

    def teardown_class(self):
        self.driver.quit()
