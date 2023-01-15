from datetime import datetime
import time
from src.system.tracker.abstractTracker import AbstractTracker
from bs4 import BeautifulSoup
from bs4.element import PageElement

TYPE = 'global.cainiao'


class TrackerGlobalCainiao(AbstractTracker):

    def __init__(self, track_order: str):
        super().__init__(track_order)

    def _get_url_page(self, track_order: str) -> str:
        return "https://global.cainiao.com/newDetail.htm?mailNoList=" + track_order

    def _search_data(self, soup: BeautifulSoup) -> None:
        last_detail: PageElement = soup.find("div", {"class": "TrackingDetail--firstStep--dSIAnAW"})
        self._headDetail = last_detail.findNext("span", {"class": "TrackingDetail--head--20GpNSP"}).get_text()
        self._textDetail = last_detail.findNext("span", {"class": "TrackingDetail--text--3Odqdxz"}).get_text()
        time_gmt: str = last_detail.findNext("span", {"class": "TrackingDetail--timeText--3x08R3x"}).get_text()

        date_gmt: datetime = None

        if len(time_gmt) >= 25:
            if len(time_gmt) == 26:
                time_gmt = time_gmt + ':00'
            elif len(time_gmt) == 25:
                time_gmt = time_gmt[0:24] + '0' + time_gmt[24:25] + ':00'
            date_gmt = datetime.strptime(time_gmt, '%Y-%m-%d %H:%M:%S %Z%z')
        else:
            time_gmt = time_gmt[0:19]
            date_gmt = datetime.strptime(time_gmt, '%Y-%m-%d %H:%M:%S')
        self._timeDetail = int(date_gmt.timestamp())
