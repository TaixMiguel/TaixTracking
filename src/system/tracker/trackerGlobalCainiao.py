from datetime import datetime
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from src.system.tracker.abstractTracker import AbstractTracker

TYPE = 'global.cainiao'


class TrackerGlobalCainiao(AbstractTracker):

    def __init__(self, track_order: str):
        super().__init__(track_order)

    def _search_data(self, driver: WebDriver) -> None:
        driver.get("https://global.cainiao.com/detail.htm?mailNoList=" + self._track_order)
        time.sleep(5)

        last_detail = driver.find_element(By.CLASS_NAME, "TrackingDetail--firstStep--dSIAnAW")
        self._headDetail = last_detail.find_element(By.CLASS_NAME, "TrackingDetail--head--20GpNSP").text
        self._textDetail = last_detail.find_element(By.CLASS_NAME, "TrackingDetail--text--3Odqdxz").text

        time_gmt: str = last_detail.find_element(By.CLASS_NAME, "TrackingDetail--timeInfoWrap--Ad4suAI").text
        time_gmt = time_gmt + ':00' if len(time_gmt) > 25 else time_gmt[0:24] + '0' + time_gmt[24:25] + ':00'
        date_gmt: datetime = datetime.datetime.strptime(time_gmt, '%Y-%m-%d %H:%M:%S %Z%z')
        self._timeDetail = int(date_gmt.timestamp())
