import json
import logging
from dataclasses import asdict
from typing import List
from pathlib import Path
from .flyers import Flyer

logger = logging.getLogger(__name__)


def save_flyers_to_json(flyers: List[Flyer], filename: str = "hyperia_letaky.json"):
    """Saves the list of flyers to a JSON file."""
    if not flyers:
        logger.info("No flyers to save.")
        return

    data = [asdict(f) for f in flyers]

    current_script_path = Path(__file__).resolve()

    project_root = current_script_path.parent.parent

    output_dir = project_root / "flyers"
    output_file_path = output_dir / filename

    try:
        output_dir.mkdir(parents=True, exist_ok=True)

        with open(output_file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        logger.info(f"Data successfully saved to {output_file_path} ({len(data)} records).")
    except IOError as e:
        logger.error(f"Error writing to file: {e}")
