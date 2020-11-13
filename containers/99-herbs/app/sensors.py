


class Reader():

    __data = ''

    async def read(self):
        pass

    async def moisture(self):
        pass

    async def sun(self):
        pass

    async def humidity(self):
        pass

    async def temperature(self):
        pass


class Writer():
    def __init__(self, host):
        self._url = f'https://{host}'

    def write(self):
        data = {
            'moisture': self.moisture(),
            'temperature': self.temperature(),
            'sun': self.sun(),
            'humidity': self.humidity()
        }
        result = requests.post(
            
