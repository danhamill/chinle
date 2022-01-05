from numpy.core.numeric import full
import rioxarray
import xarray as xr
from glob import glob
import pandas as pd
import numpy as np
import rasterio
from affine import Affine
import os


#Search for the downloaded files from earth data
files = glob('../*.nc4')

#Define Start of cumulative sum
start = pd.to_datetime('2006-10-01')

#Defin end of cumulate 
end = pd.to_datetime('2007-10-01')
output = np.zeros((18,14))
for file in files:

    #PArse grid date from file name
    date, hour = file.split('.')[3:5]

    #Convert time to pandas time stamp
    ts = pd.to_datetime(date+hour, format = '%Y%m%d%H')

    #open the netcdf file
    ds = xr.open_rasterio(file)

    #extract geotransform from array
    gt = ds.transform
    if ts> start and ts< end:

        arr = ds[0,:,:].to_numpy()
        output+= arr
    ds.close()

oName = f"cumulative_precip_{start.strftime('%Y-%m-%d')}_to_{end.strftime('%Y-%m-%d')}.tif"
oroot = '../output'

fullOut = oroot + os.sep + oName

with rasterio.open(fullOut, 'w', 
                    driver='GTiff', 
                    height = output.shape[0], 
                    width = output.shape[1], 
                    dtype=rasterio.dtypes.float64, 
                    crs={'init': 'epsg:4326'}, 
                    count = 1, 
                    transform=Affine.from_gdal(*gt)) as dst:
    dst.write(output)
    dst.nodata = -9999


ds = rasterio.open(fullOut,1)
ds.close()