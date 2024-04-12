#!/usr/bin/python

#-------------------------------------------
# importing libraries
#-------------------------------------------
import os
import math
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits


from datetime import datetime
startTime = datetime.now()

source_name = "ngc7538_160micron"
original_fits = source_name + '.fits'
fits_image_filename = original_fits
new_fits = source_name + '_erg.fits'

hdul = fits.open(fits_image_filename)
data = hdul[1].data  # assume the first extension is an image
header = hdul[1].header

# change BUNIT
header['BUNIT'] = 'erg/cm2/sr/s/Hz'

# multiply the data with 1e-17 for erg/cm2/sr/s/Hz conversion from MJy/sr
hdul[1].data = (data[:] * 1e-23)/(((header['CDELT2'] * 3600)**2)*2.35e-11)
print('old = ', data[:])

# Write our the new file
hdul.writeto(new_fits)
hdul.close()

#checking the new file units
hdu2 = fits.open(new_fits)
data_erg = hdu2[1].data  # assume the first extension is an image
header2 = hdu2[1].header
print('NEW = ', data_erg[:])

print('The time you spent (h:mm:ss.s) is :', datetime.now() - startTime)
print("Good job! At least, you code has worked without any interruption.")
