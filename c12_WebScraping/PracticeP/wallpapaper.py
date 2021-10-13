#! python3
# Image Site Downloader
# wallpapaper.py
"""
Write a program that goes to a photo-sharing site like Flickr or Imgur, searches for 
a category of photos, and then downloads all the resulting images. You could write a 
program that works with any photo site that has a search feature.
"""

import requests, os, bs4
from pathlib import Path
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

url = 'https://wallpaperscraft.com/catalog/art/1600x1200'               # starting url

folderPath = 'c12_WebScraping/PracticeP/wallpaper'
os.makedirs( folderPath, exist_ok=True)    # store image in ./wallpaper

res = requests.get(url)
# res = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

## Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# Open a browser tab for each result.
wallPaper = soup.select('.wallpapers__image')

logging.debug(f'wallPaper : {wallPaper}')

imageSize = '1600x1200'

for i in range(len(wallPaper)):
    wallpaperUrl = wallPaper[i].get('src')
    wallpaperNewUrl = str(wallpaperUrl).replace('300x255', f'{imageSize}')
    # logging.debug(f'wallpaperNewUrl : ')
    print(f"Downloading image {i+1} from {wallpaperNewUrl}...")
    res = requests.get(wallpaperNewUrl)
    res.raise_for_status
    imageFile = open(os.path.join(folderPath, os.path.basename(wallpaperUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()



# while not url.endswith('#'):
#     # TODO: Download the page.
#     print('Downloading page %s...' % url)
#     res = requests.get(url)
#     res.raise_for_status()
    
#     soup = bs4.BeautifulSoup(res.text, 'html.parser')

#     # TODO: Find the URL of the comic image.
#     comicElem = soup.select('#comic img')
#     if comicElem == []:
#         print('Could not find comic image.')
#     else:
#         comicUrl = 'https:' + comicElem[0].get('src')
#         # TODO: Download the image.
#         res = requests.get(comicUrl)
#         res.raise_for_status()

#         # TODO: Save the image to ./xkcd.
#         imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
#         for chunk in res.iter_content(100000):
#             imageFile.write(chunk)
#         imageFile.close()

#     # TODO: Get the Prev button's url.
#     prevLink = soup.select('a[rel="prev"]')[0]
#     url = 'http://xkcd.com' + prevLink.get('href')

print(f"Done. Totally {len(wallPaper)} images have been downloaded to folder {Path.cwd()/folderPath} ")