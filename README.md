
# FITS File Conversion to Erg Units

This repository contains a Python script to convert the data units in a FITS file from MJy/sr to erg/cm²/sr/s/Hz using in the FITS header. The script also updates the BUNIT header in the FITS file to reflect the new units.

## Requirements

- Python 3.x
- Astropy
- Numpy
- Matplotlib

You can install the necessary Python packages using:

```sh
pip install astropy numpy matplotlib
```

## Script Overview

The script `convert_to_erg.py` performs the following steps:

1. **Import Libraries**: Imports necessary libraries for file handling, data manipulation, and FITS file operations.
2. **Set Up Variables**: Defines the source name and file names for input and output FITS files.
3. **Open FITS File**: Reads the FITS file and extracts the data and header from the first extension.
4. **Update Header and Data**: Changes the BUNIT header to 'erg/cm2/sr/s/Hz' and converts the data units from MJy/sr to erg/cm²/sr/s/Hz.
5. **Write New FITS File**: Writes the updated data and header to a new FITS file.
6. **Check New File Units**: Opens the new FITS file to verify the updated units and data.
7. **Print Execution Time**: Prints the time taken to execute the script.

## Detailed Steps

### 1. Import Libraries

```python
import os
import math
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from datetime import datetime
```

### 2. Set Up Variables

Define the source name and file names for the input and output FITS files.

```python
source_name = "ngc7538_160micron"
original_fits = source_name + '.fits'
fits_image_filename = original_fits
new_fits = source_name + '_erg.fits'
```

### 3. Open FITS File

Reads the FITS file and extracts the data and header from the first extension.

```python
hdul = fits.open(fits_image_filename)
data = hdul[1].data  # assume the first extension is an image
header = hdul[1].header
```

### 4. Update Header and Data

Changes the BUNIT header to 'erg/cm2/sr/s/Hz' and converts the data units from MJy/sr to erg/cm²/sr/s/Hz.

```python
# change BUNIT
header['BUNIT'] = 'erg/cm2/sr/s/Hz'

# multiply the data with 1e-23 for erg/cm2/sr/s/Hz conversion from MJy/sr
hdul[1].data = (data[:] * 1e-23)/(((header['CDELT2'] * 3600)**2)*2.35e-11)
print('old = ', data[:])
```

### 5. Write New FITS File

Writes the updated data and header to a new FITS file.

```python
# Write our the new file
hdul.writeto(new_fits)
hdul.close()
```

### 6. Check New File Units

Opens the new FITS file to verify the updated units and data.

```python
#checking the new file units
hdu2 = fits.open(new_fits)
data_erg = hdu2[1].data  # assume the first extension is an image
header2 = hdu2[1].header
print('NEW = ', data_erg[:])
```

### 7. Print Execution Time

Prints the time taken to execute the script.

```python
print('The time you spent (h:mm:ss.s) is :', datetime.now() - startTime)
print("Good job! At least, you code has worked without any interruption.")
```

## Running the Script

Ensure that the FITS file `ngc7538_160micron.fits` is in the same directory as the script. Run the script using:

```sh
python convert_to_erg.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
