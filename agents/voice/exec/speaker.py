


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

