#! python3
# downloadXkcd.py - Downloads every single XKCD comic.
"""
This is what your program does:
    1. Loads the XKCD home page
    2. Saves the comic image on that page 
    3. Follows the Previous Comic link
    4. Repeats until it reaches the first comic

This means your code will need to do the following:
    1. Download pages with the requests module.
    2. Find the URL of the comic image for a page using Beautiful Soup.
    3. Download and save the comic image to the hard drive with iter_content(). 
    4. Find the URL of the Previous Comic link, and repeat.

"""

import requests, os, bs4

url = 'https://xkcd.com' # starting url 
downloadFolder = 'c12_WebScraping/xkcd'
os.makedirs(downloadFolder, exist_ok=True) # store comics in ./xkcd 
numOpen = 3
count = 1

while not url.endswith('#'):

    if count > numOpen:
        break
    count += 1

    # TODO: Download the page.
    print(f"Downloading page {url}...")
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # TODO: Find the URL of the comic image. 
    comicElem = soup.select('#comic img')   # '#comic img': < div id='comic'><img src="//imgs.xkcd.com/comics/lab_equipment.png"

    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = 'https:' + comicElem[0].get('src')

        # TODO: Download the image.
        print(f"Downloading image {comicUrl}")
        res = requests.get(comicUrl)
        res.raise_for_status

        # Save the image to ./xkcd.
        imageFile = open(os.path.join(downloadFolder, os.path.basename(comicUrl)), 'wb')

        for chunk in res.iter_content(10000): 
            imageFile.write(chunk)
        imageFile.close()
    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
        
    url = 'https://xkcd.com' + prevLink.get('href')

print('\n' + f' Done. {numOpen} files have been downloaded! '.center(100, '=') + '\n')
