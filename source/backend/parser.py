import logging
from typing import List, Optional
from bs4 import BeautifulSoup
from .flyers import Flyer
from .date_helper import DateHelper

logger = logging.getLogger(__name__)


def get_shop_name_from_url(url: str) -> str:
    """Extracts a clean shop name from its URL."""
    return url.strip("/").split("/")[-1].replace("-", " ").title()


def parse_shop_urls(soup: BeautifulSoup) -> List[str]:
    """Parses the main category page to find shop URLs."""
    shop_links = soup.select("ul#left-category-shops li a")
    if not shop_links:
        logger.warning("Could not find any links to stores. Check if the element ID has changed.")
        return []

    logger.info(f"Found {len(shop_links)} store links.")

    urls = [link.get('href') for link in shop_links if link.get('href')]
    return urls


def _parse_flyer_element(el: BeautifulSoup, shop_name: str) -> Optional[Flyer]:
    """Parses a single flyer element from the shop page."""
    img_el = el.select_one("img")
    if not img_el:
        logger.warning("Skipping element because no image was found.")
        return None

    thumbnail = img_el.get("src") or img_el.get("data-src") or ""

    raw_title_text = img_el.get("alt", "").strip()
    title = raw_title_text.split("(from")[0].split("gültig")[0].strip()
    if not title:
        title_el = el.select_one(".letak-description strong")
        title = title_el.text.strip() if title_el else "Prospekt"

    date_el = el.select_one(".letak-description small")
    date_text = date_el.text.strip() if date_el else ""

    valid_from, valid_to = DateHelper.parse_german_date(date_text)
    if not valid_from or not valid_to:
        logger.debug(f"Could not parse date from '{date_text}', falling back to title parsing.")
        valid_from, valid_to = DateHelper.parse_german_date(raw_title_text)

    if not valid_from or not valid_to:
        logger.warning(f"Skipping flyer, could not determine date from text: '{date_text}' or '{raw_title_text}'")
        return None

    return Flyer(
        title=title,
        thumbnail=thumbnail,
        shop_name=shop_name,
        valid_from=valid_from,
        valid_to=valid_to,
        parsed_time=DateHelper.get_current_timestamp()
    )


def parse_flyers_from_shop(soup: BeautifulSoup, shop_name: str) -> List[Flyer]:
    """Parses a shop page to find all its flyers."""
    flyers = []
    flyer_elements = soup.select("div.brochure-thumb[data-brochure-id]")

    if not flyer_elements:
        logger.warning(f"No flyers found for {shop_name} (selector: div.brochure-thumb[data-brochure-id]).")
        return []

    logger.info(f"Found {len(flyer_elements)} flyers for {shop_name}.")

    for element in flyer_elements:
        try:
            flyer = _parse_flyer_element(element, shop_name)
            if flyer:
                flyers.append(flyer)
                logger.debug(f"Parsed flyer: {flyer.title}")
        except Exception as e:
            logger.error(f"Error parsing a flyer element for {shop_name}: {e}", exc_info=True)

    return flyers
