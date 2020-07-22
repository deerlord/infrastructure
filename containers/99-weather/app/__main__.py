import interface
from os import environ as settings


client = interface.OpenWeatherAPI(
    api_key=settings.API_KEY,
    lat=settings.LAT,
    lon=settings.LON,
    units=settings.UNITS
)


