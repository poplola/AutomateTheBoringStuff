#! python3
# searchpypi.py  - Opens several search results.

import requests, sys, webbrowser, bs4
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


print('Searching...')    # display text while downloading the search result page
res = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))

# res = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))

# res = requests.get('https://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

logging.debug(f'sys.argv[1:] : {sys.argv[1:]}')

# logging.debug(f'res.raise_for_status() : {res.raise_for_status()}')

# TODO: Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# logging.debug(f'res.text : {soup}')

# TODO: Open a browser tab for each result.
# linkElems = soup.select('a')
linkElems = soup.select('.package-snippet')
# linkElems = soup.select('.yuRUbf')
# linkElems = soup.select('Search projects')


# logging.debug(f'LinkElems =  {linkElems}')
# webbrowser.open('https://pypi.org/search/?q=')

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')

    logging.debug(f'href =  {urlToOpen}')
    print('Opening', urlToOpen)
    # webbrowser.open('https://pypi.org/search/?q=')
    webbrowser.open(urlToOpen)
    