#! python3
# searchpypi.py - Opens several search results.
"""
This is what your program does:
    1. Gets search keywords from the command line arguments 
    2. Retrieves the search results page
    3. Opens a browser tab for each result

This means your code will need to do the following:
    1. Read the command line arguments from sys.argv.
    2. Fetch the search result page with the requests module.
    3. Find the links to each search result.
    4. Call the webbrowser.open() function to open the web browser.

Using Command line to run program:
python3 searchpypi.py python
"""

import requests, sys, webbrowser, bs4
print('Searching...')   # display text while downloading the search result page 
res = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
print(res.raise_for_status())


# TODO: Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# TODO: Open a browser tab for each result.
linkElems = soup.select('.package-snippet')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href') 
    print('Opening', urlToOpen) 
    webbrowser.open(urlToOpen)