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

def reformat_netcdf(file):

    cc = CRS("EPSG:4326")
    date,hour = file.split('.')[1:3]

    #Convert time to pandas time stamp
    ts = pd.to_datetime(date+hour, format = '%Y%m%d%H')

    #open the netcdf file
    ds = xr.open_rasterio(file)

    #Rebuild the netcdf with the correct demsions
    xds = xr.DataArray( np.transpose(ds.data, axes = [0,2,1]),#<- had to trnspose the first and second axis
                        coords = { 'time' : ('time'   , [ts]),#<- Note were are adding the time variable to the data structure
                                    'y'   : ('y'      , ds.x.values.tolist()), #<- Note we are assigning the input x values to a new variable y
                                    'x'   : ('x'      , ds.y.values.tolist()), #<- Note we are assigning the input y values to a new variable x
                                },
                        dims = ['time','y','x']
                        )
    xds.rio.write_crs(cc.to_string(), inplace=True)#<- Now we are getting rio xarray to recalculate the affine transformation

    return xds

#Search for the downloaded files from earth data
files = glob('*.nc4')

output = xr.DataArray()

for file in files:

    ds = reformat_netcdf(file)

    if output.shape == ():
        output = ds
    else:
        output = xr.concat([output, ds], dim='time')

output.to_netcdf('TRMM_Data_Combined.nc')

print('here')
