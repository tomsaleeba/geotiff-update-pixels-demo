import os
import gdal
import numpy

def strip_low_values(in_file_path, out_file_path):
    ds = gdal.Open(in_file_path)
    band = ds.GetRasterBand(1)
    arr = band.ReadAsArray()
    [cols, rows] = arr.shape
    arr_mean = int(arr.mean())
    arr_out = numpy.where((arr < arr_mean), 255, arr)
    driver = gdal.GetDriverByName("GTiff")
    outdata = driver.Create(out_file_path, rows, cols, 1, gdal.GDT_Byte)
    outdata.SetGeoTransform(ds.GetGeoTransform())
    outdata.SetProjection(ds.GetProjection())
    outdata.GetRasterBand(1).WriteArray(arr_out)
    outdata.GetRasterBand(1).SetNoDataValue(255)
    outdata.FlushCache()


curr_dir = os.path.dirname(os.path.realpath(__file__))
infile = os.path.join(curr_dir, 'south_australia_landcover_30x36_lambert_cropped.tif')
outfile = os.path.join(curr_dir, 'output.tif')
strip_low_values(infile, outfile)
print('Wrote output to %s' % outfile)
