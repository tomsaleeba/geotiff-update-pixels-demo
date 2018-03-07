import os
import unittest

import osgeo.gdal as gdal
import numpy

LAND_USE_CODE = 18

def convert_to_pixels(absolute_value, extent_min, block_size):
    relative_value = absolute_value - extent_min
    pixel_offset = relative_value / block_size
    return int(pixel_offset) # TODO round up/down appropriately, not always .floor()


def check_polarity(lower, higher):
    if higher < lower:
        raise ValueError('Values round the wrong way, expected "%d" to be GREATER THAN "%d"' % (higher, lower))
    return


def update_values(in_file_path, out_file_path, x1, y1, x2, y2):
    ds = gdal.Open(in_file_path, gdal.gdalconst.GA_ReadOnly)
    band = ds.GetRasterBand(1)
    print('Source GeoTIFF attributes:')
    print('  datatype = %s' % gdal.GetDataTypeName(band.DataType))
    arr = band.ReadAsArray()
    [rows, cols] = arr.shape
    print('  %d cols, %d rows' % (cols, rows))
    geoTransform = ds.GetGeoTransform()
    minx = geoTransform[0]
    maxy = geoTransform[3]
    maxx = minx + geoTransform[1] * ds.RasterXSize
    miny = maxy + geoTransform[5] * ds.RasterYSize
    print('  x extent = %s to %s' % (minx, maxx))
    print('  y extent = %s to %s' % (miny, maxy))
    x_block_size = (maxx - minx) / cols
    y_block_size = (maxy - miny) / rows
    adjusted = {
        'x1': convert_to_pixels(x1, minx, x_block_size),
        'y1': rows - convert_to_pixels(y2, miny, y_block_size),
        'x2': convert_to_pixels(x2, minx, x_block_size) + 1,
        'y2': rows - convert_to_pixels(y1, miny, y_block_size) + 1
    }
    print('Updating range: %d,%d to %d,%d' % (adjusted['x1'], adjusted['y1'], adjusted['x2'], adjusted['y2']))
    arr[adjusted['y1']:adjusted['y2'], adjusted['x1']:adjusted['x2']] = LAND_USE_CODE
    driver = gdal.GetDriverByName("GTiff")
    outdata = driver.Create(out_file_path, cols, rows, 1, band.DataType)
    outdata.SetGeoTransform(ds.GetGeoTransform())
    outdata.SetProjection(ds.GetProjection())
    outdata.GetRasterBand(1).WriteArray(arr)
    outdata.GetRasterBand(1).SetNoDataValue(band.GetNoDataValue())
    outdata.FlushCache()


if __name__ == '__main__':
    minx = 1355057
    maxx = 1355427
    miny = 1673162
    maxy = 1673800
    check_polarity(minx, maxx)
    check_polarity(miny, maxy)
    curr_dir = os.path.dirname(os.path.realpath(__file__))
    infile = os.path.join(curr_dir, '..', 'assets', 'south_australia_landcover_33m_lambert_cropped.tif')
    outfile = os.path.join(curr_dir, '..', 'assets', 'updated_output.tif')
    update_values(infile, outfile, minx, miny, maxx, maxy)
    print('Wrote output to %s' % outfile)


class TestUpdatePixels(unittest.TestCase):

    def test_convert_to_pixels01(self):
        result = convert_to_pixels(1350800, 1344779.2661046935245395, 33.92)
        self.assertEqual(result, 177)
