## What is it?
This is a simple demo that I put together to learn how to use python GDAL to modify a GeoTIFF.
The python code is a modified version of https://gis.stackexchange.com/a/243369/49134.
It reads the input GeoTIFF file and filters out any pixels whose value is below the mean for
the whole image. It's a pointless task but it demonstrates GDAL.

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
python filter_pixels.sh
# open the output.tif file to view the result
```
