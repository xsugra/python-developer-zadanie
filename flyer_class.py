from dataclasses import dataclass


# DATA CLASS
@dataclass
class Flyer:
    """
    Data class represents one flyer.
    """
    title: str
    thumbnail: str
    shop_name: str
    valid_from: str  # YYYY-MM-DD
    valid_to: str  # YYYY-MM-DD
    parsed_time: str  # YYYY-MM-DD
