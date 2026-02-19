import requests

url = "https://api-manager.upbit.com/api/v1/announcements"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept": "application/json",
    "Accept-Language": "en-US,en;q=0.9",
    "Origin": "https://upbit.com",
    "Referer": "https://upbit.com/"
}

params = {
    "os": "web",
    "page": 1,
    "per_page": 10,
    "category": "all"
}

res = requests.get(url, headers=headers, params=params, timeout=30)
print(res)




