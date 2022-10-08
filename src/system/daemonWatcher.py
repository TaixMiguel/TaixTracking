from src.io import get_instance_communication
from src.system.configApp import ConfigApp
from src.system.tracker import get_instance_tracker
from src.system.tracker.abstractTracker import AbstractTracker
from src.system.tracker.tracking import get_actives_tracking
from src.system.tracker.trackingDetail import TrackingDetail
import logging
import threading
import time


def _update_active_tracking() -> None:
    list_tracking: list = get_actives_tracking()
    for tracking in list_tracking:
        try:
            tracker: AbstractTracker = get_instance_tracker(tracking.get_track_type(), tracking.get_track_code())
            tracker.search_track_order()

            tracking_detail: TrackingDetail = tracking.get_last_detail()
            if not tracking_detail or not tracking_detail.is_equals(tracker.get_head_detail(), tracker.get_text_detail(),
                                                                    tracker.get_time_detail()):
                detail: TrackingDetail = tracking.create_new_tracking_detail(tracker.get_head_detail(),
                                                                             tracker.get_text_detail(),
                                                                             tracker.get_time_detail())
                date_format: str = ConfigApp().get_date_format()
                get_instance_communication().send_message(tracking.get_user_id(), detail.msg_to_user(date_format))
        except Exception as error:
            logging.info(f'Se ha producido un error al trackear el tracking {tracking.to_string()}')
            logging.error(error)


class DaemonWatcher:

    turnOff: bool
    timeSleep: int

    def __init__(self) -> None:
        self.timeSleep = ConfigApp().get_interval_time_search_tracking() * 60

    def run(self) -> None:
        thread = threading.Thread(target=self.__turn_on, name='DaemonWatcher')
        thread.start()

    def __turn_on(self) -> None:
        self.turnOff = False
        ConfigApp().set_daemon_launch(True)

        while not self.turnOff:
            _update_active_tracking()

            # TODO: avisar de pedidos apunto de vencer
            # TODO: eliminar pedidos antiguos
            time.sleep(self.timeSleep)

    def turn_off(self) -> None:
        ConfigApp().set_daemon_launch(False)
        self.turnOff = True
