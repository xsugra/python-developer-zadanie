import requests
import time
import logging
from typing import List
from . import config
from .flyers import Flyer
from .network import fetch_page
from .parser import get_shop_name_from_url, parse_flyers_from_shop, parse_shop_urls
from .storage import save_flyers_to_json

logger = logging.getLogger(__name__)


class ProspektScraper:
    """
    Orchestrates the process of scraping flyers from the Prospektmaschine website.
    """

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(config.HEADERS)
        self.flyers: List[Flyer] = []

    def run(self):
        """
        Executes the entire scraping process.
        """
        logger.info("Starting scraper...")

        # 1. Fetch the main category page
        logger.info(f"Analyzing category: {config.START_URL}")
        category_soup = fetch_page(self.session, config.START_URL)
        if not category_soup:
            logger.error("Could not fetch the category page. Aborting.")
            return

        # 2. Parse shop URLs from the category page
        shop_url_paths = parse_shop_urls(category_soup)

        # 3. Process each shop
        for shop_url_path in shop_url_paths:
            full_shop_url = f"{config.BASE_URL}{shop_url_path}" if shop_url_path.startswith("/") else shop_url_path
            shop_name = get_shop_name_from_url(full_shop_url)
            logger.info(f"Processing hypermarket: {shop_name}")

            shop_soup = fetch_page(self.session, full_shop_url)
            if shop_soup:
                flyers = parse_flyers_from_shop(shop_soup, shop_name)
                if flyers:
                    self.flyers.extend(flyers)

            # Be polite to the server
            time.sleep(1)

        # 4. Save all collected flyers
        save_flyers_to_json(self.flyers)

        logger.info("Scraping finished.")
