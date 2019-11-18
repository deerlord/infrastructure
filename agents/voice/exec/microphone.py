import sounddevice
import requests
from io import StringIO

CHUNK = 1024

class AudioListener():

    __wait_interval = 10

    def __init__(self):
        # find microphone
        self.__stream = sounddevice.RawInputStream(
            samplerate=44100,
            blocksize=1024,
            device=None,
            channels=1,
        )
        self.__buffer = []
        self.__quiet_count = 0

    def __trigger(self, chunk):
        retval = False
        # if chunk has "sound" return True, else False
        if True:
            retval = True
        else:
            self.__quiet_count += 1
        return retval
    
    def __listen(self):
        QUIET = self.__wait_interval
        for frame in self.__stream.read(self.__stream.read_available):
            if self.__trigger(frame):
                self.__buffer.append(data)
            elif (
                len(self.__buffer) and
                self.__quiet_count > QUIET
            ):
                url = 'https://openhab.HOST_DOMAIN/api/voice/'
                data = StringIO()
                for chunk in self.__buffer:
                    data.write(chunk)
                files = {'files': data}
                resp = requests.post(url, files=files)
                self.__buffer = []
                self.__quiet_count = 0
    
    def run(self):
        while True:
            self.__listen()


listener = AudioListener()
listener.run()
