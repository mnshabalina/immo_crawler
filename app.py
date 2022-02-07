from flask import Flask, request, make_response, render_template
from flask_cors import CORS

# create API
app = Flask(__name__)
CORS(app)

@app.route('/')
def main():
    response = make_response(render_template('index.html'))	
    return response


if __name__ == '__main__':
    app.run(debug=True)

