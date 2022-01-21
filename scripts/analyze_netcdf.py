from numpy.core.numeric import full
import rioxarray
import xarray as xr
from glob import glob
import pandas as pd
import numpy as np
import rasterio
from affine import Affine
import os
from pyproj import CRS


#Search for the downloaded files from earth data
files = glob('*.nc4')

#Define Start of cumulative sum
start = pd.to_datetime('2006-10-01')

#Defin end of cumulate 
end = pd.to_datetime('2006-10-08')
output = np.zeros((14,18)) #<- had to flip to transpose the input data

cc = CRS("EPSG:4326")
for file in files[:50]:

    #PArse grid date from file name
    date, hour = file.split('.')[1:3]

    #Convert time to pandas time stamp
    ts = pd.to_datetime(date+hour, format = '%Y%m%d%H')

    #open the netcdf file
    ds = xr.open_rasterio(file)

    #Rebuild the netcdf with the correct demsions
    xds = xr.DataArray( np.transpose(ds.data, axes = [0,2,1]),#<- had to trnspose the first and second axis
                        coords = { 'time': ('time'   , [ts]),#<- Note were are adding the time variable to the data structure
                                    'y'   : ('y'      , ds.x.values.tolist()), #<- Note we are assigning the input x values to a new variable y
                                    'x'   : ('x'      , ds.y.values.tolist()), #<- Note we are assigning the input y values to a new variable x
                                },
                        dims = ['time','y','x']
                        )
    xds.rio.write_crs(cc.to_string(), inplace=True)#<- Now we are getting rio xarray to recalculate the affine transformation
    xds = xds.transpose('y','x')



    #extract geotransform from array
    gt = xds.rio.transform()


    if ts> start and ts< end:

        arr = xds[0,:,:].to_numpy()
        output+= arr
    ds.close()

oName = f"cumulative_precip_{start.strftime('%Y-%m-%d')}_to_{end.strftime('%Y-%m-%d')}.tif"
oroot = 'output'

fullOut = oroot + os.sep + oName

with rasterio.open(fullOut, 'w', 
                    driver='GTiff', 
                    height = output.shape[0], 
                    width = output.shape[1], 
                    dtype=rasterio.dtypes.float32, 
                    crs={'init': 'epsg:4326'}, 
                    count = 1, 
                    transform=gt) as dst:
    dst.write(output.astype('float32'),1)
    dst.nodata = -9999


ds = rasterio.open(fullOut,1)
ds.close()