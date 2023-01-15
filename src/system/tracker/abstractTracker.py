from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
from bs4.element import PageElement
from playwright.sync_api import sync_playwright


class AbstractTracker(ABC):

    __track_order: str

    _headDetail: str
    _textDetail: str
    _timeDetail: int

    def __init__(self, track_order: str):
        self.__track_order = track_order

    def search_track_order(self) -> None:
        # Use sync version of Playwright
        with sync_playwright() as p:
            # Launch the browser
            browser = p.chromium.launch()

            # Open a new browser page
            page = browser.new_page()
            page_path = self._get_url_page(self.__track_order)

            # Open our test file in the opened page
            page.goto(page_path)
            page_content = page.content()

            # Process extracted content with BeautifulSoup
            soup = BeautifulSoup(page_content, "html.parser")
            self._search_data(soup)

            # Close browser
            browser.close()

    @abstractmethod
    def _get_url_page(self, track_order: str) -> str:
        pass

    @abstractmethod
    def _search_data(self, soup: BeautifulSoup) -> None:
        pass

    def get_head_detail(self) -> str:
        return self._headDetail

    def get_text_detail(self) -> str:
        return self._textDetail

    def get_time_detail(self) -> int:
        return self._timeDetail
