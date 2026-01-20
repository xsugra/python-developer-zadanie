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
        Tries to extract dates from text as "Gültig von 17.02. bis 22.02.2025" or "17.02. - 22.02."
        """
        current_year = datetime.now().year

        # Use of regex to find dates
        # Finding patterns like "17.02."
        pattern = r"(\d{1,2})\.(\d{1,2})\.?"
        matches = re.findall(pattern, date_text)

        if len(matches) >= 2:
            # Assuming a start on "from" and end as "to"
            day_from, month_from = matches[0]
            day_to, month_to = matches[1]

            # Logic of the year: If the year is not stated, apply actual year.
            year_from = current_year
            year_to = current_year

            # If now is 10th of December and the flyer ends in 10th of January, we must add +1 year.
            if int(month_from) == 12 & int(month_to) == 1:
                year_to += 1

            # Trying to find year in the text (e.g. 2026)
            year_match = re.search(r"20\d{2}", date_text)
            if year_match:
                found_year = int(year_match.group(0))
                year_from = found_year
                year_to = found_year

            # Formatting date into YYYY-MM-DD form
            try:
                date_from_obj = datetime(year_from, int(month_from), int(day_from))
                date_to_obj = datetime(year_to, int(month_to), int(day_to))
                return date_from_obj.strftime("%Y-%m-%d"), date_to_obj.strftime("%Y-%m-%d")
            except ValueError:
                return None, None

        return None, None

    @staticmethod
    def get_current_timestamp() -> str:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
