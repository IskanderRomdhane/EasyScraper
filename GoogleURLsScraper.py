from requests_html import HTMLSession
import re
import time
import requests


class GoogleURLsScraper:
    def __init__(self, query, number_of_urls, inf, scrape_type):
        self.query = query
        self.number_of_urls = number_of_urls
        self.inf = inf
        self.scrape_type = scrape_type
        self.pagination_params = {
            'q': '',
            'sxsrf': 'ACYBGNRmhZ3C1fo8pX_gW_d8i4gVeu41Bw:1575654668368',
            'ei': 'DJXqXcmDFumxrgSbnYeQBA',
            'start': '',
            'sa': 'N',
            'ved': '2ahUKEwjJua-Gy6HmAhXpmIsKHZvOAUI4FBDy0wN6BAgMEDI',
            'biw': '811',
            'bih': '628'
        }
        self.initial_params = {
            'sxsrf': 'ACYBGNQ16aJKOqQVdyEW9OtCv8zRsBcRig:1575650951873',
            'source': 'hp',
            'ei': 'h4bqXcT0MuPzqwG87524BQ',
            'q': '',
            'oq': '',
            'gs_l': 'psy-ab.1.1.35i362i39l10.0.0..139811...4.0..0.0.0.......0......gws-wiz.....10.KwbM7vkMEDs'
        }
        self.headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'referer': 'https://www.google.com/',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
        }
        self.results = []

    def fetch(self, query, page, scrape_type):
        self.initial_params['q'] = query

        if not page:
            params = self.initial_params
        else:
            params = self.pagination_params
            params['start'] = str(page * 10)
            params['q'] = query

        base_url = 'https://www.google.com/search'
        if scrape_type == "Images":
            base_url = "https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={query}&oq={query}&gs_l=img"
        response = requests.get(base_url, params=params, headers=self.headers)
        print('HTTP GET request to URL: %s | Status code: %s' % (response.url, response.status_code))

        return response

    def get_source(self, url):
        try:
            session = HTMLSession()
            response = session.get(url)
            return response

        except requests.exceptions.RequestException as e:
            print(e)

    def extract_site_urls(self, urls):
        site_urls = []
        for url in urls:
            match = re.search(r'url=(https?://[^&]+)', url)
            if match:
                site_urls.append(match.group(1))
        return site_urls

    def parse(self, response, scrape_type, query, pages_or_images):
        resp = self.get_source(response.url)
        links = list(resp.html.absolute_links)
        google_domains = (
            'https://www.google.', 'https://google.', 'https://webcache.googleusercontent.',
            'https://policies.google.', 'https://support.google.', 'https://maps.google.', 'https://wikipedia.org',
            'https://youtube.com', 'https://translate.google.com'
        )

        clean_urls = self.extract_site_urls(links)
        filtered_links = [url for url in clean_urls if not url.startswith(google_domains)]

        if scrape_type == "URLs":
            with open("Your Urls Saving Path", "a") as f:
                for link in filtered_links:
                    f.write(link + "\n")

    def fetch(self, query, page, scrape_type):
        self.initial_params['q'] = query

        if not page:
            params = self.initial_params
        else:
            params = self.pagination_params
            params['start'] = str(page * 10)
            params['q'] = query

        base_url = 'https://www.google.com/search'
        response = requests.get(base_url, params=params, headers=self.headers)
        print('HTTP GET request to URL: %s | Status code: %s' % (response.url, response.status_code))

        return response

