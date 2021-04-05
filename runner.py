
from PIL import Image
import numpy as np
from numpy import save
from FileLoader import save_array_as_csv
from ImageFilter import filter_pts
from WhitespaceModifier import bleach, bleachmanual, removeptrange
from Lines import drawhor, drawvert, drawgrid

img_filter_save_path = 'SaveFile.png'
contrast_pt = 110

# load file
img_load_path = 'LoadFile.png'
Image.MAX_IMAGE_PIXELS = None   #disable DecompressionBombWarning for large files
image = Image.open(img_load_path)
image = image.convert('L')

# setup array
im = np.array(image)

# bleach at 120
bleach(im, 125)

drawgrid(im, 20)

# remove single pixels
#removeptrange(im, 1)


# save file
img_save_path = 'SaveFile2.png'
gr_im = Image.fromarray(im).save(img_save_path)
