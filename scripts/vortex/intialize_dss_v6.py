import sys
sys.path.append(r"C:\Local_Software\HEC-DSSVue 3.2.3\jar\sys\jythonUtils.jar")
sys.path.append(r"C:\Local_Software\HEC-DSSVue 3.2.3\jar\hec.jar")
sys.path.append(r"C:\Local_Software\HEC-DSSVue 3.2.3\jar\jython-standalone-2.7.0.jar")
sys.path.append(r"C:\Local_Software\HEC-DSSVue 3.2.3\jar\hec-dssvue-3.2.3.jar")
sys.path.append(r"C:\Local_Software\HEC-DSSVue 3.2.3\jar\rma.jar")

try:
    from hec.heclib.dss import HecDss
    from hec.io import TimeSeriesContainer
    print 'Sucessfully found DSS API'
except:
    print 'import from DSS failed'

import os
from glob import glob


files = ['Chinle_MetSim_GridMET.dss']

for file in files:

    root = r'C:\workspace\Chinle\output'

    dss_file = root + os.sep + file
    fid = HecDss.open(dss_file,6)
    fid.close()
    del fid