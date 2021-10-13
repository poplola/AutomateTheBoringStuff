#! Python3
# mapIt.py
# PROJECT: MAPIT.PY WITH THE WEBBROWSER MODULE
# Launches a map in the browser using an address from the command line or clipboard.
"""
it’s tedious to copy a street address to the clipboard and bring up a map of it on Google Maps. You could take a few steps out of this task by writing a simple script to automatically launch the map in your browser using the contents of your clipboard. This way, you only have to copy the address to a clipboard and run the script, and the map will be loaded for you.

This is what your program does:
    1. Gets a street address from the command line arguments or clipboard 
    2. Opens the web browser to the Google Maps page for the address

This means your code will need to do the following:
    1. Read the command line arguments from sys.argv.
    2. Read the clipboard contents.
    3. Call the webbrowser.open() function to open the web browser.

eg: C:\> python3 mapit.py 870 Valencia St, San Francisco, CA 94110
sys.argv ==> ['mapIt.py', '870', 'Valencia', 'St,', 'San', 'Francisco,', 'CA', '94110']
"""

import webbrowser, sys, logging, pyperclip

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable()

if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
    logging.debug(address)
    logging.debug(sys.argv)
else:
    # Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
