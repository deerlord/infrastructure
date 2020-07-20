from src import interface
import datetime
from pytz import timezone


API_KEY='e2b24e60e909cbf5ea344b6201b90e12'
LAT='30.412494'
LON='-97.744411'

client = interface.OpenWeatherAPI(api_key=API_KEY, lat=LAT, lon=LON)
data = client.data
print('len minutely', len(data['minutely']))
print('len hourly', len(data['hourly']))
print('len daily', len(data['daily']))
