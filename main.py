import logging
from scraper import ProspektScraper

# Configure logging for the entire application
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)

if __name__ == "__main__":
    """
    Main entry point for the scraper application.
    """
    scraper = ProspektScraper()
    scraper.run()
