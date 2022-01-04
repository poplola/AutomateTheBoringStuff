#! python3
# threadedDownloadXkcd.py - Downloads XKCD comics using multiple threads.

import requests, os, bs4, threading
import logging
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)

url = 'https://wallpaperscraft.com/catalog/art/1600x1200'               # starting url

os.makedirs('wallpaper', exist_ok=True)    # store comics in ./xkcd

totalImage = 0

def wallpaperDownload(numPage):     # webpage link page number from page2 to page10
    global totalImage
    res = requests.get(url+f'/page{numPage}')
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    wallPaper = soup.select('.wallpapers__image')

    imageSize = '1600x1200'

    for i in range(len(wallPaper)):
        wallpaperUrl = wallPaper[i].get('src')
        wallpaperNewUrl = str(wallpaperUrl).replace('300x255', f'{imageSize}')
        # logging.debug(f'wallpaperNewUrl : ')
        res = requests.get(wallpaperNewUrl)
        res.raise_for_status
        # imageNum += 1
        totalImage += 1
        print(f'Downloading IMAGE #{str(totalImage)} on PAGE {numPage} from link : {wallpaperNewUrl}')
        imageFile = open(os.path.join('wallpaper', os.path.basename(wallpaperUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
        

# TODO: Create and start the Thread objects.
downloadThreads = []             # a list of all the Thread objects
for i in range(2, 5):    # loops 9 times, creates 9 threads
    downloadThread = threading.Thread(target=wallpaperDownload, args=(str(i)))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# TODO: Wait for all threads to end.
for downloadThread in downloadThreads:
    downloadThread.join()
print(f'Done. There are totally {totalImage} image(s) downloaded.')

