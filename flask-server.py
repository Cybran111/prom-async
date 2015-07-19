from collections import defaultdict
from flask import Flask
app = Flask(__name__)

counts = defaultdict(lambda: 0)


@app.route('/count/<key>')
def count_view(key):
    counts[key] += 1
    return str(counts[key])

app.run(port=8000, debug=True)
