# chinle

Working repository for Chinle FPMS hydrologic model development

The environment used is described in environment.yml

# Scripts

## [metsim2005-2006.ipynb](https://github.com/danhamill/chinle/blob/master/scripts/metsim2005-2006.ipynb)

This notebook consumes [GridMet](https://www.northwestknowledge.net/metdata/data/) and [Parameters for PITRI Precipitation Temporal Disaggregation over continental US, Mexico, and southern Canada, 1981-2013](https://zenodo.org/record/1402223#.YkHUUnrMJaS) data.  

The notebook produces temporally disggregrated recipitation grids using [MetSim](https://github.com/UW-Hydro/MetSim). 

The Gridmet Precipitaion grids are clipped to the boundary in [input/shp](https://github.com/danhamill/chinle/tree/master/input/shp). 

All gridmet files (tmmn_YYYY.nc, tmmx_YYYY.nc, pr_YYYY.nc) should be placed in `input` as netcdf files.

## Vortex

### [import_metsim.bat](https://github.com/danhamill/chinle/blob/master/scripts/vortex/import%20_metsim.bat)

Need to specify the -Djava.livrary.path on [line 3](https://github.com/danhamill/chinle/blob/master/scripts/vortex/import%20_metsim.bat#L3)
Need to specify the root vortex folder on [line 6](https://github.com/danhamill/chinle/blob/master/scripts/vortex/import%20_metsim.bat#L6)

This script does two operations:
1. Intalizes version 6 dss file using HecDSS api
2. Imports the temporally disaggregrated precip grids to DSS using vortex.

### [intialize_dss_v6.py](https://github.com/danhamill/chinle/blob/master/scripts/vortex/intialize_dss_v6.py)

- All sys.path inserts need to be mapped to the dss installation on your computer
- Speficy output dss file on [line 19](https://github.com/danhamill/chinle/blob/master/scripts/vortex/intialize_dss_v6.py#L19)
- Speficy output root directory on [line 23](https://github.com/danhamill/chinle/blob/master/scripts/vortex/intialize_dss_v6.py#L23)

### [import_metsim.py](https://github.com/danhamill/chinle/blob/master/scripts/vortex/import_metsim.py)

- Specify input precipitation necdf files on [line 8](https://github.com/danhamill/chinle/blob/master/scripts/vortex/import_metsim.py#L8)
- Specify output dss file created by intialize_dss_v6.py on [line 16](https://github.com/danhamill/chinle/blob/master/scripts/vortex/import_metsim.py#L16)
- Specify dss path name part on [lines 18-24](https://github.com/danhamill/chinle/blob/master/scripts/vortex/import_metsim.py#L18-L24)

# Process
1. Run .ipynb
2. Run import_metsim.bat


