from flask import Flask
from datetime import datetime
import pytz
app = Flask(__name__)
local_tz = pytz.timezone('America/New_York')
@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def get_time():
    local_time = datetime.now(local_tz)
    return 'Current time: {}'.format(local_time)

if __name__ == '__main__':
    app.run(host='0.0.0.0',
        port=8080,
        debug=True)
