import requests

url = "https://www.nytimes.com/#publisher"
html_output_name = './ny.html'

req = requests.get(url, 'html.parser')

with open(html_output_name, 'w') as f:
    f.write(req.text)
    f.close()