## What is it?
These are a few simple demos that I put together to learn how to use python GDAL to modify a GeoTIFF.
The python code is a modified version of https://gis.stackexchange.com/a/243369/49134.
There are a few demos:

**`filter_pixels.py`**: reads the input GeoTIFF file and filters out any pixels whose value is below the mean for
the whole image.

**`update_pixels.py`**: reads the input GeoTIFF and updates a region of pixels to a new value.


## How to run
You can run this demo like this:
```bash
git clone <this repo>
# [start] create a virtualenv
mkdir gupd_venv
cd gupd_venv
virtualenv .
. bin/activate
cd ..
# [end] create a virtualenv
cd <this repo>
# make sure you've already installed GDAL on your system
./pip-install.sh
python gupd/filter_pixels.sh
python gupd/update_pixels.sh
# open the *_output.tif files to view the results
```

## QGIS colours
A singleband pseudocolor map file is included to make seeing changes between the source and the outputs easier. To use it:

 1. open QGIS
 1. load an output GeoTIFF
 1. double click it in the layer list
 1. go to the `Style` tab
 1. set `Render type:` to `Singleband pseudocolor`
 1. use the `open color map` button and select `assets/qgis-colour-map.txt`
 1. press `OK`
