
echo "Creating blank DSS files..."
C:\jython2.7.2\bin\jython.exe -Djava.library.path="C:\Local_Software\HEC-DSSVue 3.2.3\lib" C:\workspace\Chinle\scripts\vortex\intialize_dss_v6.py

echo "Writing Grids to file..."
set "VORTEX_HOME=C:\Local_Software\vortex-0.10.26"
set "PATH=%VORTEX_HOME%\bin;%VORTEX_HOME%\bin\gdal;%PATH%"
set "GDAL_DRIVER_PATH=%VORTEX_HOME%\bin\gdal\gdalplugins"
set "GDAL_DATA=%VORTEX_HOME%\bin\gdal\gdal-data"
set "PROJ_LIB=%VORTEX_HOME%\bin\gdal\projlib"
set "CLASSPATH=%VORTEX_HOME%\lib\*"
C:\jython2.7.2\bin\jython.exe -Djava.library.path=%VORTEX_HOME%\bin;%VORTEX_HOME%\bin\gdal C:\workspace\Chinle\scripts\vortex\import_metsim.py
cmd /k