import requests

URL = "http://localhost/"

HEADERS = {"User-Agent": "python-bot/1.0"}

for _ in range(200):
    requests.get(URL, headers=HEADERS)
