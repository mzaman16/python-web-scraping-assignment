# Task 1: Python Web Scraping
# Scrapes paragraph text from a Medium article and saves it to a text file.

import os
import requests
from bs4 import BeautifulSoup

url = "https://aditideodhar.medium.com/your-guide-to-web-scraping-in-python-5e54ff08bcb2"
headers = {"User-Agent": "Mozilla/5.0"}

try:
    response = requests.get(url, headers=headers, timeout=15)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    paragraphs = soup.find_all("p")

    article_text = "\n".join(
        p.get_text(" ", strip=True)
        for p in paragraphs
        if p.get_text(strip=True)
    )

    os.makedirs("scraped_articles", exist_ok=True)
    output_file = os.path.join("scraped_articles", "medium_article.txt")

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(article_text)

    print("Article scraped successfully.")
    print("Saved to:", output_file)

except requests.RequestException as error:
    print("Error downloading article:", error)
