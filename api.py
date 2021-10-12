from flask import Flask, request
from routes import *

app = Flask(__name__)


@app.route('/')
def index_route():
    return index()

@app.route('/byma/snapshot')
def snapshot_route():
    return snapshot()

@app.route('/byma/instrument/intraday')
def intraday_route():
    return intraday(request.json)

@app.route('/byma/instrument/quarter')
def quarter_route():
    return quarter(request.json)

@app.route('/byma/instrument/history')
def history_route():
    return history(request.json)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')