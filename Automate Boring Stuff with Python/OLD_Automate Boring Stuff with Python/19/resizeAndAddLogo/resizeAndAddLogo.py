#! python3
# resizeAndAddLogo.py - Resizes all images in current working directory to fit 
# in a 300x300 square, and adds catlogo.png to the lower-right corner.

import os
from PIL import Image
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

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

logging.debug(f'logoWidth = {logoWidth}\tlogoHeight = {logoHeight}')

os.makedirs('withLogo', exist_ok=True)
# TODO: Loop over all files in the working directory.
n =1
for filename in os.listdir('.'):
    fileExt = filename.split('.')[-1].lower()
    # if not(filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.gif') or filename.endswith('.bmp')) or filename == LOGO_FILENAME:
    if not(fileExt == 'png' or fileExt == 'jpg' or fileExt == 'gif' or fileExt == 'bmp') or filename == LOGO_FILENAME:
        continue     # skip non-image files and the logo file itself
    im = Image.open(filename)
    width, height = im.size
    logging.debug(f'<{filename}> ========= width = {width} , height = {height }=========')

    if width <= 2*logoWidth or height <=2*logoHeight:
        continue

    # TODO: Add the logo.
    print('Adding logo to image # %s : %s... size: %s X %s'%(n, filename, width, height))
    n += 1
    im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)

    # TODO: Save changes.
    im.save(os.path.join('withLogo', filename))