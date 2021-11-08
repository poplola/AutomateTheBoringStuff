from bs4 import BeautifulSoup
import requests

url = "https://www.cnn.com"
# response = requests.get(url, headers=headers)
response = requests.get(url)
response.raise_for_status()
# print(response)


# print(res.status_code)

# with open("doc.html") as fp:
#     soup = bs4.BeautifulSoup(fp, 'html.parser')

# soup = bs4.BeautifulSoup(res.text, "html.parser")
soup = BeautifulSoup(response.content, 'html.parser')
print(soup.prettify())

# file_path = f"../Python_Daily_Exercise/html.txt"
# textFile = open(file_path, 'w')
# textFile.write(soup.prettify())
# textFile.close()
# print(response.text)
# headlines = soup.find_all("span", {"class": "balancedHeadline"})
# headlines = soup.find_all('span', attrs={"class":"balancedHeadline"})
# headlines = soup.find_all('span', class_="cd__headline-text vid-left-enabled")
# headlines = soup.select(".cd__headline-text vid-left-enabled")
headlines = soup.find_all("script", {"type": "application/ld+json"})

print(len(headlines))

for i in range(len(headlines)):
    print("+++++++++++++++++++")
    print(headlines[i].text)




# import requests, sys, webbrowser, bs4
# print('Searching...')   # display text while downloading the search result page 
# res = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
# print(res.raise_for_status())


# # TODO: Retrieve top search result links.
# soup = bs4.BeautifulSoup(res.text, 'html.parser')

# # TODO: Open a browser tab for each result.
# linkElems = soup.select('.package-snippet')
# numOpen = min(5, len(linkElems))
# for i in range(numOpen):
#     urlToOpen = 'https://pypi.org' + linkElems[i].get('href') 
#     print('Opening', urlToOpen) 
#     webbrowser.open(urlToOpen)