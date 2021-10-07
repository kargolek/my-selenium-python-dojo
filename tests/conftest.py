import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType


@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
    driver.get("https://github.com/login")
    request.cls.driver = driver
    yield
    driver.quit()
