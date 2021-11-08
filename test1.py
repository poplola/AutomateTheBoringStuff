import requests
from bs4 import BeautifulSoup

url = "https://www.cnn.com"

response = requests.get(url)
response.raise_for_status()

print(type(response.content))

with open("d.html", 'bw') as f:
    f.write(response.content)