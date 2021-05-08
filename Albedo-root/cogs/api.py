import requests
import json

url = 'https://api.jikan.moe/v3/search/anime?q=naruto&limit=2'

response = requests.request("GET", url).json()
print(response)