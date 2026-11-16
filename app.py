from flask import Flask, render_template
from datetime import datetime
from zoneinfo import ZoneInfo

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.now(ZoneInfo("Europe/Prague"))
    return render_template(
        'index.html',
        hour=now.hour,
        minute=now.minute,
        second=now.second,
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
