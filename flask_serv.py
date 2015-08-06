from flask import Flask

app = Flask(__name__)
from requests import get


@app.route('/<key>')
def count_view(key):
    url = "http://localhost:5555/count/{}".format(key)
    response = get(url)
    return response.content


def fibo():
    old = 0
    n = 1
    while True:
        yield n
        old, n = n, old+n


f = fibo()


@app.route('/fibo')
def fibonacci():
    return str(next(f))
