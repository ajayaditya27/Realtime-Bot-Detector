import requests, time, random

URLS = [
    "http://localhost/",
    "http://localhost/index.html",
    "http://localhost/about.html",
    "http://localhost/contact.html"
]

HEADERS = [
    {"User-Agent": "Mozilla/5.0"},
    {"User-Agent": "Chrome/120.0"},
    {"User-Agent": "Safari/537.36"}
]

for _ in range(300):
    url = random.choice(URLS)
    headers = random.choice(HEADERS)
    requests.get(url, headers=headers)
    time.sleep(random.uniform(2, 6))  # human delay
