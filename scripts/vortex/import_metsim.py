from mil.army.usace.hec.vortex.io import BatchImporter
from mil.army.usace.hec.vortex import Options
from mil.army.usace.hec.vortex.geo import WktFactory
import os
from glob import glob

#Temperature
infiles = [r'C:\workspace\Chinle\output\chinle_20050101-20051231.nc',r'C:\workspace\Chinle\output\chinle_20060101-20061231.nc']
variables = ['prec']

# targ_crs = u'PROJCS["NAD83 / UTM zone 13N",GEOGCS["NAD83",DATUM["North_American_Datum_1983",SPHEROID["GRS 1980",6378137,298.257222101,AUTHORITY["EPSG","7019"]],OWGS84[0,0,0,0,0,0,0],AUTHORITY["EPSG","6269"]],PRIMEM["Greenwich",0,AUTHORITY["EPSG","8901"]],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]],AUTHORITY["EPSG","4269"]],PROJECTION["Transverse_Mercator"],PARAMETER["latitude_of_origin",0],PARAMETER["central_meridian",-105],PARAMETER["scale_factor",0.9996],PARAMETER["false_easting",500000],PARAMETER["false_northing",0],UNIT["metre",1,AUTHORITY["EPSG","9001"]],AXIS["Easting",EAST],AXIS["Northing",NORTH],AUTHORITY["EPSG","26913"]]'
geo_options = Options.create()
geo_options.add('targetWkt', WktFactory.shg())
geo_options.add('targetCellSize', '2000')

destination = r"C:\workspace\Chinle\output\Chinle_MetSim_GridMET.dss"

write_options = Options.create()
write_options.add('partF', 'GRIDMET_METSIM')
write_options.add('partA', 'SHG')
write_options.add('partB', 'CHINLE')
write_options.add('partC', 'PRECIPITATION')
write_options.add('dataType', 'PER-CUM')
write_options.add('units','mm')

myImport = BatchImporter.builder() \
    .inFiles(infiles) \
    .variables(variables) \
    .geoOptions(geo_options) \
    .destination(destination) \
    .writeOptions(write_options) \
    .build()

myImport.process()

del myImport, write_options, geo_options, infiles, variables

