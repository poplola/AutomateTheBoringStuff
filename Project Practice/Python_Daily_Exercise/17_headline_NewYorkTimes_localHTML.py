from bs4 import BeautifulSoup
import requests

# headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
# url = "https://www.nytimes.com"
url = "./Python_Daily_Exercise/ny1.html"
# response = requests.get(url)
# response = requests.get(url, "html.parser")
# response.raise_for_status()
# print(response.text)


# print(res.status_code)

with open(url, 'r') as fp:
    contents = fp.read()
    soup = BeautifulSoup(contents, 'html.parser')

# soup = BeautifulSoup(response.content, "html.parser")
# # soup = bs4.BeautifulSoup(res.text, 'html.parser')
# print(soup.prettify())
# # print(res.text)

headlines = soup.find_all("a", {"class": "css-sv6851"})
# headlines = soup.find_all("span", {"class": "balancedHeadline"})
# headlines = soup.find_all('span', attrs={"class":"balancedHeadline"})
# headlines = soup.find_all(class_="balancedHeadline")
# headlines = soup.find_all("span")

print(len(headlines))
num = 1
article_list = []
for headline in headlines:
    print("+"*20)
    print(f"#{num} : {headline.text}")
    print(headline['href'])
    num += 1
#     for dictionary in headline:
#         article_list.append(dictionary)
# print('\n'*2, article_list)




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