import time
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from src.system.tracker.abstractTracker import AbstractTracker


class TrackerGlobalCainiao(AbstractTracker):

    def __init__(self, order: str):
        super().__init__(order)

    def _search_data(self, driver: WebDriver) -> None:
        driver.get("https://global.cainiao.com/detail.htm?mailNoList=" + self._order)
        time.sleep(5)

        last_detail = driver.find_element(By.CLASS_NAME, "TrackingDetail--firstStep--dSIAnAW")
        self._headDetail = last_detail.find_element(By.CLASS_NAME, "TrackingDetail--head--20GpNSP").text
        self._textDetail = last_detail.find_element(By.CLASS_NAME, "TrackingDetail--text--3Odqdxz").text
        self._timeDetail = last_detail.find_element(By.CLASS_NAME, "TrackingDetail--timeInfoWrap--Ad4suAI").text
