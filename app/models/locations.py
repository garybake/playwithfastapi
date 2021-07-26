import logging
import os
from typing import Dict

logger = logging.getLogger("jokes-logger")


class LocationKey:
    @staticmethod
    def get_location_key() -> Dict[str, str]:
        env_key = os.getenv("MAPBOX_API_KEY")
        if env_key:
            ret_dict = {"key": env_key, "status": "success"}
        else:
            logger.error("Failed to find MAPBOX_API_KEY")
            ret_dict = {"status": "failure", "msg": "Missing MAPBOX_API_KEY"}

        return ret_dict
