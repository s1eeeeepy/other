import requests
import lxml
from bs4 import BeautifulSoup


URL = ""


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "uk-UA,uk;q=0.8,en-US;q=0.5,en;q=0.3",
    # 'Accept-Encoding': 'gzip, deflate, br',
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "If-None-Match": "25e58e8093bfaead65cb3f1926e15739-ssl",
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

s = requests.Session()
response = s.get(URL, headers=headers)

with open("data.html", "w") as file:
    file.write(response.text)
