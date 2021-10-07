import time
from flask import Flask, render_template
import datetime
import uuid
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello, World!"


@app.route('/get_data/', methods=['GET', 'POST'])
@app.route('/get_data/<int:num>', methods=['GET', 'POST'])
def get_data(num=None):
    start = time.monotonic()
    data = []
    if num is None:
        return f"{uuid.uuid4()}:{int((time.monotonic() - start))}ms:{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    else:
        for i in range(num):
            data.append(f"{uuid.uuid4()}:{int((time.monotonic() - start))}ms:{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        return render_template('index.html', data_id=data)


if __name__ == "__main__":
    app.run(debug=True)
