import re
from datetime import datetime
from typing import Optional, Tuple


class DateHelper:
    """
    Static class for parsing and formatting dates.
    """

    @staticmethod
    def parse_german_date(date_text: str) -> Tuple[Optional[str], Optional[str]]:
        """
        Tries to extract dates from text like "Gültig von 17.02. bis 22.02.2025", "17.02. - 22.02.", or even a single date like "ab 15.01.2026".
        """
        current_year = datetime.now().year

        # Regex to find dates like "17.02." or "17.02.2025"
        pattern = r"(\d{1,2})\.(\d{1,2})\.?(\d{4})?"
        matches = re.findall(pattern, date_text)

        if len(matches) >= 2:
            # Case 1: Date range found
            d1, m1, y1 = matches[0]
            d2, m2, y2 = matches[1]

            year_from = int(y1) if y1 else current_year
            year_to = int(y2) if y2 else current_year

            # Handle year change, e.g. "28.12. - 02.01."
            if not y1 and not y2 and int(m1) > int(m2):
                year_to = current_year + 1

            try:
                date_from_obj = datetime(year_from, int(m1), int(d1))
                date_to_obj = datetime(year_to, int(m2), int(d2))
                return date_from_obj.strftime("%Y-%m-%d"), date_to_obj.strftime("%Y-%m-%d")
            except ValueError:
                return None, None

        elif len(matches) == 1:
            # Case 2: Only a single date found, e.g., "gültig ab 12.11.2025"
            d1, m1, y1 = matches[0]
            year_from = int(y1) if y1 else current_year

            try:
                date_from_obj = datetime(year_from, int(m1), int(d1))
                # When only one date is present, we can assume it's valid for at least that one day.
                # Setting both from and to dates to the same value.
                date_str = date_from_obj.strftime("%Y-%m-%d")
                return date_str, date_str
            except ValueError:
                return None, None

        return None, None

    @staticmethod
    def get_current_timestamp() -> str:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
