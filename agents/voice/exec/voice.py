from http.server import BaseHTTPRequestHandler, HTTPServer
from io import BytesIO
import sounddevice
import requests

CHUNK = 1024

class AudioListener():
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
        for frame in self.__stream.read(self.__stream.read_available):
            if self.__trigger(frame):
                self.__buffer.append(data)
            elif (
                len(self.__buffer) and
                self.__quiet_count > QUIET
            ):
                url = 'https://openhab.HOST_DOMAIN/api/voice/'
                files = {'files': self.__buffer}
                resp = requests.post(url, files=files)
                self.__buffer = []
                self.__quiet_count = 0
    
    def run(self):
        while True:
            self.__listen()


class AudioPlayer():
    def __init__(self):
        self.__stream = sounddevice.RawOutputStream(
            samplerate=44100,
            blocksize=1024,
            device=2,
            channels=2,
        )
    
    def play(self, data):
        # make sure data is prepared for writing
        self.__stream.write(data)


listener = AudioListener()
# start thread
player = AudioPlayer()


class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        audio = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        listener.stop()
        player.play(audio)
        listener.start()


httpd = HTTPServer(('', 8080), RequestHandler)
httpd.serve_forever()
