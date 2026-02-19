import requests

url = "https://api-manager.upbit.com/api/v1/announcements"
params = {
    "os": "web",
    "page": 1,
    "per_page": 20,
    "category": "trade"
}

response = requests.get(url, params=params)
data = response.json()
print(data)