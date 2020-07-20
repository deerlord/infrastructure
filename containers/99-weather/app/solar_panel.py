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


def maximum_power(power_per_panel: int, total_panels: int = 1):
    client = interface.OpenWeatherAPI(api_key=API_KEY, lat=LAT, lon=LON)
    current = client.current
    sunrise = getters._convert_utc_to_cst(current['sunrise'])
    sunset = getters._convert_utc_to_cst(current['sunset'])
    total_sun = sunset - sunrise
    hours = (total_sun.seconds / 3600)
    return int(hours * power_per_panel * total_panels)


def calculate_power(cloudiness: int, power_per_panel: int, total_panels: int = 1):
    cloud_percent = (cloudiness / 100)
    return int(power_per_panel * cloud_percent * total_panels)


print(maximum_power(250))
print(calculate_power(cloudiness=90, power_per_panel=250))
