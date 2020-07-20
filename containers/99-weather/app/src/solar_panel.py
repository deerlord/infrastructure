import datetime

import getters
import interface


API_KEY='e2b24e60e909cbf5ea344b6201b90e12'
LAT='30.412494'
LON='-97.744411'

client = interface.OpenWeatherAPI(api_key=API_KEY, lat=LAT, lon=LON)
data = client.current

"""
get total sun for the day
run in the morning
"""
sunrise = getters._convert_utc_to_cst(data['sunrise'])
sunset = getters._convert_utc_to_cst(data['sunset'])
total_sun = sunset - sunrise
