import requests

api_key = '5b46d50c9aa44816b1eda337ec1b3871'
url = 'https://newsapi.org/v2/top-headlines'
params = {
    'apiKey': api_key,
    'language': 'hi',
    'pageSize': 5
}
response = requests.get(url, params=params)
data = response.json()
print(data)
