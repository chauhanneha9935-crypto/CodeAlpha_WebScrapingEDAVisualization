import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

BASE_URL = "http://quotes.toscrape.com/page/{}/"

def scrape_quotes():
    page = 1
    all_quotes = []

    while True:
        try:
            print(f"Scraping page {page}...")
            response = requests.get(BASE_URL.format(page), timeout=10)

            if response.status_code != 200:
                break

            soup = BeautifulSoup(response.text, "html.parser")
            quotes = soup.find_all("div", class_="quote")

            if not quotes:
                break

            for quote in quotes:
                text = quote.find("span", class_="text").get_text(strip=True)
                author = quote.find("small", class_="author").get_text(strip=True)

                all_quotes.append({
                    "text": text,
                    "author": author
                })

            page += 1
            time.sleep(1)

        except Exception as e:
            print("Error occurred:", e)
            break

    # ✅ Create correct absolute path
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_folder = os.path.join(base_dir, "data", "raw")

    os.makedirs(output_folder, exist_ok=True)

    output_path = os.path.join(output_folder, "quotes_raw.csv")

    df = pd.DataFrame(all_quotes)
    df.to_csv(output_path, index=False)

    print(f"\nScraping complete! File saved at:\n{output_path}")


if __name__ == "__main__":
    scrape_quotes()