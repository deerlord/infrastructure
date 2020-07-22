import dataclasses
import datetime
import influxdb
import pytz
import requests


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
        return self.__data(minutely=True).get('minutely', {})

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


class InfluxDB():
    def __init__(self):
        self._connect()
        self._create_database()

    def _connect(self):
        self.__client = influxdb.InfluxDBClient(
            host='influxdb',
            port=8086
        )

    def _create_database(self):
        has_weather_db = [
            True
            for item in self.__client.get_list_database()
            if item['name'] == 'weather'
        ]
        if not has_weather_db:
            self.__client.create_database('weather')
        self.__client.switch_database('weather')

    def _prep(self, data):
        dt = datetime.datetime.fromtimestamp(data.get('dt'))
        dt_str = dt.strftime('%Y-%m-%dT%H:%M:%SZ')
        return dt_str

    def _write(self, measurement, fields, time, tags={}):
        try:
            data_wrapper = [{
                "measurement": measurement,
                "tags": tags,
                "time": time,
                "fields": fields
            }]
            self.__client.write_points(data_wrapper)
        except influxdb.exceptions.InfluxDBClientError:
            pass

    def get_current(self):
        query = 'SELECT * FROM "weather"."autogen"."current"'
        return self.__client.query(query)

    def current(self, data):
        dt = self._prep(data)
        weather = data.get('weather')[0]
        return self._write(
            'current',
            tags={},
            fields={
                'sunrise': data.get('sunrise'),
                'sunset': data.get('sunset'),
                'temp': data.get('temp'),
                'feels_like': data.get('feels_like'),
                'pressure': data.get('pressure'),
                'humidity': data.get('humidity'),
                'dew_point': data.get('dew_point'),
                'uvi': data.get('uvi'),
                'clouds': data.get('clouds'),
                'visibility': data.get('visibility'),
                'wind_speed': data.get('wind_speed'),
                'wind_deg': data.get('wind_deg'),
                'weather_id': weather.get('id'),
                'weather_main': weather.get('main'),
                'weather_desc': weather.get('description'),
                'weather_icon': weather.get('icon'),
                'rain': data.get('rain', 0),
                'snow': data.get('snow', 0)
            },
            time=dt
        )


def main():
    from os import environ as settings
    from time import sleep

    weather = OpenWeatherAPI(
        api_key=settings['API_KEY'],
        lat=settings['LAT'],
        lon=settings['LON'],
        units=settings['UNITS']
    )
    database = InfluxDB()
    while True:
        data = weather.current
        database.current(data=data)
        sleep(60)


if __name__ == '__main__':
    main()


"""
InfluxDB schema
point: (in time) of weather data
- a SQL row
measurement:
- a SQL table
"""
