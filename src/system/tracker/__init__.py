import logging
from src.system.persistence.bbdd import get_instance as get_instance_bbdd
from src.system.tracker.abstractTracker import AbstractTracker
from src.system.tracker.trackerGlobalCainiao import TrackerGlobalCainiao
from src.system.tracker.tracking import Tracking, to_tracking


def create_tracking(track_type: str, track_code: str, telegram_user_id: int) -> Tracking:
    logging.debug(f'Se crea el track "{track_code}" del tipo {track_type}')
    database_manager = get_instance_bbdd()
    id_tracking: int = database_manager.insert('itrack001', [track_type, track_code, telegram_user_id])
    rows: list = database_manager.select('strack001', [id_tracking])
    database_manager.close()
    return to_tracking(rows)[0]


def get_instance_tracker(track_code: str, order: str) -> AbstractTracker:
    # TODO: hacer un switch con el track_code
    return TrackerGlobalCainiao(order)
