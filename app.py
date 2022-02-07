from flask import Flask, request, make_response, render_template
from flask_cors import CORS
from crawler import crawl
import json

# create API
app = Flask(__name__)
CORS(app)

@app.route('/')
def main():
    with open('db.json', 'r') as f:
        return json.load(f)

@app.route('/update')
def update():
    data = crawl()
    return data

if __name__ == '__main__':
    app.run(debug=True)

