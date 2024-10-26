from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import requests
import io
from PIL import Image
from urllib.parse import urlparse
from selenium.common.exceptions import NoSuchWindowException


class GoogleImageScraper:
    def __init__(self, webdriver_path, image_path, search_key="cat", number_of_images=1, headless=True,
                 min_resolution=(0, 0), max_resolution=(1920, 1080), max_missed=10):
        image_path = os.path.join(image_path, search_key)
        if not os.path.exists(image_path):
            print("[INFO] Image path not found. Creating a new folder.")
            os.makedirs(image_path)

        options = Options()
        if headless:
            options.add_argument('--headless')
        options.add_argument("--enable-logging")
        options.add_argument("--v=1")
        service = Service(webdriver_path)
        print(f"[INFO] Starting Chrome with executable at: {webdriver_path}")

        self.driver = webdriver.Chrome(service=service)

        self.driver.set_window_size(1400, 1050)
        self.search_key = search_key
        self.number_of_images = number_of_images
        self.image_path = image_path
        self.url = f"https://www.google.com/search?q={search_key}&source=lnms&tbm=isch"
        self.min_resolution = min_resolution
        self.max_resolution = max_resolution
        self.max_missed = max_missed

    def find_image_urls(self):
        if not self.driver:
            print("[ERROR] Driver not initialized.")
            return []

        self.driver.get(self.url)
        image_urls = []
        visited_urls = set()
        count, missed_count = 0, 0

        print("[INFO] Gathering image links")
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "img.YQ4gaf"))
        )

        while count < self.number_of_images and missed_count < self.max_missed:
            thumbnails = self.driver.find_elements(By.CSS_SELECTOR, "img.YQ4gaf")

            for thumbnail in thumbnails[len(image_urls):]:
                try:
                    thumbnail.click()

                    WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "n3VNCb"))
                    )

                    for class_name in ["n3VNCb", "iPVvYb", "r48jcc"]:
                        try:
                            images = self.driver.find_elements(By.CLASS_NAME, class_name)
                            if images:
                                for image in images:
                                    src_link = image.get_attribute("src")
                                    if "http" in src_link and "encrypted" not in src_link and src_link not in visited_urls:
                                        print(f"[INFO] {self.search_key} \t #{count} \t {src_link}")
                                        image_urls.append(src_link)
                                        visited_urls.add(src_link)
                                        count += 1
                                        break
                                break
                        except Exception as e:
                            print(f"[INFO] Unable to get link using class: {class_name}. Error: {e}")
                except Exception as e:
                    print(f"[INFO] Error clicking thumbnail: {e}")
                    missed_count += 1

                if count >= self.number_of_images:
                    break

            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)

        self.driver.quit()
        print("[INFO] Google search ended")
        return image_urls


    def find_image_urls(self):
        if not self.driver:
            print("[ERROR] Driver not initialized.")
            return []

        self.driver.get(self.url)
        image_urls = []
        visited_urls = set()
        count, missed_count = 0, 0

        print("[INFO] Gathering image links")
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "img.YQ4gaf"))
        )

        while count < self.number_of_images and missed_count < self.max_missed:
            thumbnails = self.driver.find_elements(By.CSS_SELECTOR, "img.YQ4gaf")

            for thumbnail in thumbnails[len(image_urls):]:
                try:
                    thumbnail.click()
                    time.sleep(5)

                    for class_name in ["n3VNCb", "iPVvYb", "r48jcc"]:
                        try:
                            images = self.driver.find_elements(By.CLASS_NAME, class_name)
                            if images:
                                for image in images:
                                    src_link = image.get_attribute("src")
                                    if "http" in src_link and "encrypted" not in src_link and src_link not in visited_urls:
                                        print(f"[INFO] {self.search_key} \t #{count} \t {src_link}")
                                        image_urls.append(src_link)
                                        visited_urls.add(src_link)
                                        count += 1
                                        break
                                break
                        except Exception as e:
                            print(f"[INFO] Unable to get link using class: {class_name}. Error: {e}")
                except Exception as e:
                    print(f"[INFO] Error clicking thumbnail: {e}")
                    missed_count += 1

                if count >= self.number_of_images:
                    break

            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)

        self.driver.quit()
        print("[INFO] Google search ended")
        return image_urls

    def save_images(self, image_urls, keep_filenames):
        print("[INFO] Saving images, please wait...")
        for indx, image_url in enumerate(image_urls):
            try:
                print("[INFO] Image URL:", image_url)
                search_string = ''.join(e for e in self.search_key if e.isalnum())
                image = requests.get(image_url, timeout=5)
                if image.status_code == 200:
                    with Image.open(io.BytesIO(image.content)) as image_from_web:
                        if keep_filenames:
                            o = urlparse(image_url)
                            image_url = o.scheme + "://" + o.netloc + o.path
                            name = os.path.splitext(os.path.basename(image_url))[0]
                            filename = f"{name}.{image_from_web.format.lower()}"
                        else:
                            filename = f"{search_string}{indx}.{image_from_web.format.lower()}"

                        image_path = os.path.join(self.image_path, filename)
                        print(f"[INFO] {self.search_key} \t {indx} \t Image saved at: {image_path}")
                        image_from_web.save(image_path)

            except Exception as e:
                print("[ERROR] Download failed:", e)
        print(
            "[INFO] Downloads completed. Please note that some photos were not downloaded as they were not in the correct format (e.g., jpg, jpeg, png)")

