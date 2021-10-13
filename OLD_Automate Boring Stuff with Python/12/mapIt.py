#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.

import webbrowser, sys, pyperclip
import logging
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(filename='debugmapItLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug(f'sys.argv : ====== {sys.argv} ======')
if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
# TODO: Get address from clipboard.
    address = pyperclip.paste()
logging.debug(f'address got ====== {address} ======')

webbrowser.open('https://www.google.com/maps/place/' + address)