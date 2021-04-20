from flask import Flask
import json

app = Flask(__name__)


@app.route('/hello', methods=['POST', 'GET'])
def hello_world():
    return json.dumps({
        "code": 1,
        "message": "Hello world!"
    })


# Run in HTTP
app.run(host='127.0.0.1', debug=True, port='5000')
