import sounddevice
from http.server import BaseHTTPRequestHandler, HTTPServer

class AudioPlayer():
    def __check_devices(self):
        retval = False
        devices = sd.query_devices()
        try:
            soundcard = [
                d
                for d in devices
                if 'name' in d and d['name'] == 'dmix'
            ][0]
            if soundcard['max_output_channels'] < 0:
                raise Exception
        except IndexError:
            # cannot find soundcard to use
            return retval
        except:
            return retval
        if len(devices) >= 3:
            soundcard = devices[2]
            soundcard['id'] = 2
            self.__soundcard = soundcard
            retval = True
        return retval

    def __init__(self):
        self.__check_devices()
        self.__stream = sounddevice.RawOutputStream(
            samplerate=44100,
            blocksize=1024,
            device=self.__soundcard['id'],
            channels=2,
        )

    def play(self, data):
        # make sure data is prepared for writing
        self.__stream.write(data)


player = AudioPlayer()


class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        audio = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        # stop listener
        player.play(audio)
        # start listener


httpd = HTTPServer(('', 8080), RequestHandler)
httpd.serve_forever()

