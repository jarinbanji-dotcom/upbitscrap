import requests

session = requests.Session()

session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept": "application/json",
    "Referer": "https://upbit.com/"
})

response = session.get(
    "https://api-manager.upbit.com/api/v1/announcements",
    params={"os":"web","page":1,"per_page":20,"category":"trade"}
)

print(response.json())


