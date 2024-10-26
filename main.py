import time
from GoogleURLsScraper import GoogleURLsScraper
from GoogleImageScraper import GoogleImageScraper


class GoogleScraper:
    def run(self, query, inf, pages_or_images, scrape_type):
        if scrape_type == "URLs":
            url_scraper = GoogleURLsScraper(query, pages_or_images, inf, scrape_type)

            for page in range(0, pages_or_images):
                response = url_scraper.fetch(query, page, scrape_type)
                url_scraper.parse(response, scrape_type, query, pages_or_images)
                time.sleep(5)
        elif scrape_type == "Images":
            images_scraper = GoogleImageScraper(
                webdriver_path="C:/Users/Planete Gaming/Desktop/Projects/urlScrapper/chromedriver.exe",
                image_path="C:/Users/Planete Gaming/Desktop/Projects/urlScrapper/Images",
                search_key=query,
                number_of_images=pages_or_images
            )
            image_urls = images_scraper.find_image_urls()
            images_scraper.save_images(image_urls, keep_filenames=False)

