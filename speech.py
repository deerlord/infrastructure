from http.server import BaseHTTPRequestHandler, HTTPServer
from io import BytesIO
import speech_recognition as sr
class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        audio = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        try:
            r = sr.Recognizer()
            result = r.recognize_sphinx(audio)
        except sr.UnknownValueError:
            result = None
        except sr.RequestError:
            result = None
        response.write(result)
        self.wfile.write(response)
httpd = HTTPServer(('', 8080), RequestHandler)
httpd.serve_forever()
