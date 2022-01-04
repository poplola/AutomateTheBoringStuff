from bs4 import BeautifulSoup
import requests

url = "https://www.sohu.com"
# response = requests.get(url, headers=headers)
response = requests.get(url)
response.raise_for_status()
print(type(response.content))
print(response.content)

with open("e.html", 'w') as f:
    f.write(str(response.content))



# import requests
# from bs4 import BeautifulSoup

# url = "https://www.cnn.com"

# response = requests.get(url)
# response.raise_for_status()

# print(type(response.content))

# with open("d.html", 'bw') as f:
#     f.write(response.content)



# print(res.status_code)

# with open("doc.html") as fp:
#     soup = bs4.BeautifulSoup(fp, 'html.parser')

# soup = bs4.BeautifulSoup(res.text, "html.parser")
soup = BeautifulSoup(response.content, 'html.parser')
# print(soup.prettify())
# print(response.text)
# headlines = soup.find_all("span", {"class": "balancedHeadline"})
# headlines = soup.find_all('span', attrs={"class":"balancedHeadline"})
# headlines = soup.find_all('span', class_="cd__headline-text vid-left-enabled")
headlines = soup.select('div p a', class_='news')


print(len(headlines))
# print(headlines)
num = 1
for headline in headlines:
    print("+++++++++++++++++++\n")
    # print(headline.get_text())
    # print(headline['href'])
    print(f"#{num} : {headline.get_text()}")
    print(headline['href'])
    num += 1




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