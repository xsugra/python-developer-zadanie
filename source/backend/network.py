import requests
from bs4 import BeautifulSoup
from typing import Optional
import logging

logger = logging.getLogger(__name__)


def fetch_page(session: requests.Session, url: str) -> Optional[BeautifulSoup]:
    """
    Downloads the page content using the provided session and returns a BeautifulSoup object.
    """
    try:
        response = session.get(url, timeout=10)
        response.raise_for_status()
        return BeautifulSoup(response.content, 'html.parser')
    except requests.RequestException as e:
        logger.error(f"Error while downloading the URL {url}: {e}")
        return None
