import json
import logging
from dataclasses import asdict
from typing import List
from flyer_class import Flyer

logger = logging.getLogger(__name__)


def save_flyers_to_json(flyers: List[Flyer], filename: str = "hyperia_letaky.json"):
    """Saves the list of flyers to a JSON file."""
    if not flyers:
        logger.info("No flyers to save.")
        return

    data = [asdict(f) for f in flyers]
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        logger.info(f"Data successfully saved to {filename} ({len(data)} records).")
    except IOError as e:
        logger.error(f"Error writing to file: {e}")
