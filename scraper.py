
import requests
from bs4 import BeautifulSoup
import json

BASE_URL = "https://www.mudah.my/malaysia/property-for-sale"
HEADERS = {"User-Agent": "Mozilla/5.0"}

results = []

# Simulate 2 pages for demo (you can increase this number)
for page in range(1, 3):
    url = f"{BASE_URL}?o={page}&q=klang+valley"
    resp = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(resp.text, "html.parser")
    listings = soup.select(".listing_params")

    for listing in listings:
        title_tag = listing.select_one("a.list_title")
        title = title_tag.text.strip() if title_tag else ""
        link = title_tag["href"] if title_tag else ""
        price_tag = listing.select_one(".ads_price")
        price = price_tag.text.strip() if price_tag else ""
        details = listing.select(".list_detail li")

        location = details[0].text.strip() if len(details) > 0 else ""
        property_type = details[1].text.strip() if len(details) > 1 else ""
        size = details[2].text.strip() if len(details) > 2 else ""

        results.append({
            "title": title,
            "price": price,
            "type": property_type,
            "location": location,
            "built_up": size,
            "bedrooms": "",
            "bathrooms": "",
            "land_size": "",
            "image": "https://via.placeholder.com/150",
            "url": link
        })

# Save to data.json
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=4)

print(f"Saved {len(results)} properties to data.json")
