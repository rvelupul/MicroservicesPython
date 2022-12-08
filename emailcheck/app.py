from flask import request, Flask
import json
import socket
import re

import sys
sys.path.append('..')

#from my_imports import top

app = Flask(__name__)

#
# curl http://localhost:9000
#


@app.route('/')
def echo():
    returnDictionary = {}
    returnDictionary["echo"] = str(socket.gethostname())
    return json.dumps(returnDictionary)

#
# curl -d "{ \"email\" : \"foo@bar\" }" -X POST http://localhost:9000/check -H "Content-type: application/json"
#


@app.route("/check", methods=["POST"])
def compute():
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    hostName = socket.gethostname()

    email = request.json['email']
    number_of_at_signs = email.count("@")

    returnDictionary = {}
    returnDictionary["email"] = email
    returnDictionary["at_signs"] = number_of_at_signs

    if (re.fullmatch(regex, email)):
        returnDictionary["valid email"] = True
    else:
        returnDictionary["invalid email"] = False

    return json.dumps(returnDictionary)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9000)
