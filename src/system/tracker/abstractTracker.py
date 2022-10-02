from abc import ABC, abstractmethod
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.webdriver import WebDriver
from webdriver_manager.firefox import GeckoDriverManager


class AbstractTracker(ABC):

    _track_order: str

    _headDetail: str
    _textDetail: str
    _timeDetail: int

    def __init__(self, track_order: str):
        self._track_order = track_order

    def search_track_order(self) -> None:
        options = webdriver.FirefoxOptions()
        options.headless = True
        options.add_argument("window-size=1920x1080")
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        driver: WebDriver = webdriver.Firefox(options=options, service=Service(GeckoDriverManager().install()))
        self._search_data(driver=driver)
        driver.quit()

    @abstractmethod
    def _search_data(self, driver: WebDriver) -> None:
        pass

    def get_head_detail(self) -> str:
        return self._headDetail

    def get_text_detail(self) -> str:
        return self._textDetail

    def get_time_detail(self) -> int:
        return self._timeDetail
