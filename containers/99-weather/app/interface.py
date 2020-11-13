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

    def map(self):
        prefix = 'https://tile.openweathermap.org/map'
        url = f'{prefix}/{layer}/{z}/{x}/{y}.png?appid={self.__api_key}'
        requests.get(url)

    def current(self):
        return self.__data(current=True).get('current', {})

    def minutely(self):
        return self.__data(minutely=True).get('minutely', {})

    def hourly(self):
        return self.__data(hourly=True).get('hourly', {})

    def daily(self):
        return self.__data(daily=True).get('daily', {})

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
        print('API result', result)
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
        self.__client.create_retention_policy(
            'current',
            '24h',
            '1',
            'weather'
        )

    def _local_time(self, dt):
        dt = datetime.datetime.utcfromtimestamp(dt)
        dt_str = dt.strftime('%Y-%m-%dT%H:%M:%SZ')
        return dt_str

    def _write(self, measurement, fields, time, tags={}):
        data_wrapper = [{
            "measurement": measurement,
            "tags": tags,
            "time": time,
            "fields": fields
        }]
        self.__client.write_points(data_wrapper)

    def hourly(self, data: list):
        """
        Drop series from "hourly"
        """
        points = []
        for d in data:
            weather = d.get('weather')[0]
            point = {
                'measurement': 'hourly',
                "tags": {},
                'time': d.get('dt'),
                'fields': {
                    'temp': int(d.get('temp')),
                    'feels_like': int(d.get('feels_like')),
                    'pressure': float(d.get('pressure')),
                    'humidity': float(d.get('humidity')),
                    'clouds': float(d.get('clouds')),
                    'visibility': float(d.get('visibility')),
                    'wind_speed': float(d.get('wind_speed')),
                    'weather_id': int(weather.get('id')),
                    'weather_main': str(weather.get('main')),
                    'weather_desc': str(weather.get('description')),
                    'weather_icon': str(weather.get('icon')),
                    'rain': float(d.get(
                        'rain',
                        {'1h': 0}
                    )['1h']),
                    'snow': float(d.get(
                        'snow',
                        {'1h': 0}
                    )['1h']),
                    'pop': float(d.get('pop'))
                }
            }
            points.append(point)
        self.__client.delete_series(measurement='hourly')
        self.__client.write_points(points)

    def get_current(self):
        query = 'SELECT * FROM current' 
        return self.__client.query(query)

    def current(self, data):
        weather = data.get('weather')[0]
        self._write(
            'current',
            tags={},
            fields={
                'sunrise': data.get('sunrise'),
                'sunset': data.get('sunset'),
                'temp': int(data.get('temp')),
                'feels_like': int(data.get('feels_like')),
                'pressure': float(data.get('pressure')),
                'humidity': float(data.get('humidity')),
                'dew_point': float(data.get('dew_point')),
                'uvi': float(data.get('uvi')),
                'clouds': float(data.get('clouds')),
                'visibility': float(data.get('visibility')),
                'wind_speed': float(data.get('wind_speed')),
                'wind_deg': float(data.get('wind_deg')),
                'weather_id': int(weather.get('id')),
                'weather_main': str(weather.get('main')),
                'weather_desc': str(weather.get('description')),
                'weather_icon': str(weather.get('icon')),
                'rain': float(data.get(
                    'rain',
                    {'1h': 0}
                )['1h']),
                'snow': float(data.get(
                    'snow',
                    {'1h': 0}
                )['1h'])
            },
            time=self._local_time(data.get('dt'))
        )


def main():
    from os import environ as settings
    from time import sleep
    from datetime import datetime, timedelta
    import pprint

    pp = pprint.PrettyPrinter(indent=4)
    weather = OpenWeatherAPI(
        api_key=settings['API_KEY'],
        lat=settings['LAT'],
        lon=settings['LON'],
        units=settings['UNITS']
    )
    database = InfluxDB()
    now = datetime.now
    interval = timedelta(seconds=600)
    while True:
        _next = now() + interval
        data = weather.data()
        current = data['current']
        pp.pprint(current)
        database.current(data=current)
        database.hourly(data=data['hourly'])
        sleep((_next - now()).seconds)


if __name__ == '__main__':
    main()


"""
InfluxDB schema
point: (in time) of weather data
- a SQL row
measurement:
- a SQL table
"""
