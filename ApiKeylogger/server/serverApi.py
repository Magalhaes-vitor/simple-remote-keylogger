import flask
from flask import request, render_template

import dataRepository

SERVER_HOST = "localhost"
SERVER_PORT = 8080

app = flask.Flask(__name__)
print(__name__)
app.config["DEBUG"] = True


@app.route('/upload', methods=['POST'])
def upload():

    user = request.json['user']
    data = request.json['data']

    dataRepository.insert(user, data)


@app.route('/fetch', methods=['GET'])
def fetch():
    args = request.args
    user = args.to_dict().get("user")

    response = dataRepository.get(user)

    return render_template('template.html', response=response)


if __name__ == '__main__':
    app.run(host=SERVER_HOST, port=SERVER_PORT, debug=True)
