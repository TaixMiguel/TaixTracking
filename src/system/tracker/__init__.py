import logging
from src.system.persistence.bbdd import get_instance as get_instance_bbdd
from src.system.tracker.abstractTracker import AbstractTracker
from src.system.tracker.trackerGlobalCainiao import TrackerGlobalCainiao
from src.system.tracker.tracking import Tracking, to_tracking


def get_tracking(track_type: str, track_code: str) -> Tracking:
    database_manager = get_instance_bbdd()
    rows: list = database_manager.select('strack005', [track_type, track_code])
    database_manager.close()
    if rows:
        return to_tracking(rows)[0]
    return None


def create_tracking(track_type: str, track_code: str, user_id: int) -> Tracking:
    logging.debug(f'Se crea el track "{track_code}" del tipo {track_type}')
    database_manager = get_instance_bbdd()
    id_tracking: int = database_manager.insert('itrack001', [track_type, track_code])
    rows: list = database_manager.select('strack001', [id_tracking])
    database_manager.close()
    add_user_tracking(id_tracking, user_id)
    return to_tracking(rows)[0]


def add_user_tracking(id_tracking: int, id_user: int) -> None:
    database_manager = get_instance_bbdd()
    database_manager.insert('itrack003', [id_user, id_tracking])
    database_manager.close()


def get_instance_tracker(track_code: str, order: str) -> AbstractTracker:
    # TODO: hacer un switch con el track_code
    return TrackerGlobalCainiao(order)
