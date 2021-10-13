#! python3
# resizeAndAddLogo.py - Resizes all images in current working directory to fit 
# in a 300x300 square, and adds catlogo.png to the lower-right corner.

import os
from PIL import Image
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'train_mountains_art_130351_300x255.jpg'

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

# Check if image needs to be resized.
if logoWidth > SQUARE_FIT_SIZE and logoHeight > SQUARE_FIT_SIZE:
    # Calculate the new width and height to resize to.
    if logoWidth > logoHeight:
        logoHeight = int((SQUARE_FIT_SIZE / logoWidth) * logoHeight)
        logoWidth = SQUARE_FIT_SIZE
    else:
        logoWidth = int((SQUARE_FIT_SIZE / logoHeight) * logoWidth)
        logoHeight = SQUARE_FIT_SIZE

    # Resize the image.
    print('Resizing %s... to size by %s X %s pixles' % (LOGO_FILENAME, logoWidth, logoHeight))
logoIm = logoIm.resize((logoWidth, logoHeight))
logoIm.save('test.jpg')

