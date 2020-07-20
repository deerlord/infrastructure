import dataclasses
import requests
import pytz
from src import settings


class OpenWeatherAPI():

    url = 'https://api.openweathermap.org/data/2.5/onecall'
    __api_key = ''

    def __init__(
        self,
        api_key: str,
        lat: str,
        lon: str,
        units: str = 'imperial'
    ):
        self.__units = units
        self.__api_key = api_key
        self.__lat = lat
        self.__lon = lon

    @property
    def current(self):
        return self.__data(current=True).get('current', {})

    @property
    def minutely(self):
        return self.__data(minutely).get('minutely', {})

    @property
    def hourly(self):
        return self.__data(hourly=True).get('hourly', {})

    @property
    def daily(self):
        return self.__data(daily=True).get('daily', {})

    @property
    def data(self):
        return self.__data(True, True, True, True)
    
    def __data(
        self,
        current: bool = False,
        minutely: bool = False,
        hourly: bool = False,
        daily: bool = False
    ):
        exclude = ','.join([
            name
            for name, value in zip(
                ['current', 'minutely', 'hourly', 'daily'],
                [current, minutely, hourly, daily]
            )
            if not value
        ])
        exclude_str = f'&exclude={exclude}' if exclude else ''
        query_url = (
            self.url +
            f'?lat={self.__lat}&lon={self.__lon}' +
            f'&units={self.__units}' +
            exclude_str +
            f'&appid={self.__api_key}'
        )
        result = requests.get(query_url) 
        return result.json()
    
    def _convert_utc_to_local(timestamp):
        dtime = datetime.datetime.fromtimestamp(timestamp)
        return dtime.replace(
            tzinfo=datetime.timezone.utc
        ).astimezone(tz=pytz.timezone(settings.timezone))
