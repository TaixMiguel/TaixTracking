from src.system.tracker.abstractTracker import AbstractTracker
from src.system.tracker.trackerGlobalCainiao import TrackerGlobalCainiao


def get_instance(track_code: str, order: str) -> AbstractTracker:
    # TODO: hacer un switch con el track_code
    return TrackerGlobalCainiao(order)
