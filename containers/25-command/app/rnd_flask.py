from flask import Flask
import language
import openhabapi


app = Flask('command')

@app.route('/', methods=['POST'])
def index():
    if request.method != 'POST':
        return None
    audio = request.get_data()
