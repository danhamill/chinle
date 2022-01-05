from pydap.client import open_url
from pydap.cas.urs import setup_session
from datetime import datetime, timedelta

url = 'https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L3/GPM_3IMERGHH.06'
session = setup_session(username='anita.y.sie@usace.army.mil', password='Misty8484!', check_url = url)
dataset = open_url(url, session=session)

var_name = 'precipitationCal'

min_time = datetime(year=2000, month=6, day=1, hour=0, minute=0)
event_start_time = datetime(year=2020, month=8, day=25, hour=0, minute=0)
start_time_index = int((event_start_time - min_time).total_seconds()/(60*30))

requested_data = dataset[var_name][0:1, 1240:1263, 686:719]


wget --load-cookies .urs_cookies --save-cookies .urs_cookies --auth-no-challenge=on --keep-session-cookies --user=anita.y.sie@usace.army.mil --ask-password --content-disposition -i subset_TRMM_3B42_7_20220104_210333.txt