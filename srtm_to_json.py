# Based on srtm-python by Aatish Neupane
# https://github.com/aatishnn/srtm-python

import os
import numpy as np

SAMPLES = 1201 # Change this to 3601 for SRTM1
BLOCKS = SAMPLES - 1
HGTDIR = 'hgt' # All 'hgt' files will be kept here uncompressed
JSONDIR = 'json'

hgtfile = os.path.join(HGTDIR, "N27E086.hgt")
jsonfile = os.path.join(JSONDIR, "data.js") # store as js file for ease of use

def convert():
    step = 4 # Increase this to skip values for less file size.
    r = []

    print("converting...")

    with open(hgtfile) as hgt_data:
        elevations = np.fromfile(hgt_data, np.dtype('>i2'), SAMPLES * SAMPLES).reshape((SAMPLES, SAMPLES))
        for i in range(BLOCKS / step):
            for j in range(BLOCKS / step):
                r.append(elevations[BLOCKS - (i * step), j * step].astype(int))

    print("creating js file...")

    with open(jsonfile, 'w') as outfile:
        outfile.write("var data = %s;" %r)

    print("saved to " + jsonfile)

if __name__ == '__main__':
    convert()
