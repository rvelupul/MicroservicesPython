from flask import request, Flask
import json
import socket
import random
import string

import sys
sys.path.append('..')

# from my_imports import top

app = Flask(__name__)

#
# curl http://localhost:9002
#

glob_ran = ""

@app.route('/')
def echo():
    returnDictionary = {}
    returnDictionary["echo"] = str(socket.gethostname())
    return json.dumps(returnDictionary)

#
# curl -d "{ \"email\" : \"admin@test.com\", \"password\" : \"xxxxx\" }" -X POST http://localhost:9002/check -H "Content-type: application/json"
#


@app.route("/check", methods=["POST"])
def compute():
    hostName = socket.gethostname()
    global glob_ran
    email = request.json['email']
    password = request.json['password']

    returnDictionary = {}
    returnDictionary["email"] = email
    returnDictionary["password"] = password

    if (email == "admin@test.com"):
        if (password == "xxxxx"):
            ran = random.randint(0,100000000)
            returnDictionary["please verify the OTP"] = True
            glob_ran = ran
            returnDictionary["OTP KEY"] = ran
        else:
            returnDictionary["access denied"] = False
    else:
        returnDictionary["incorrect username"] = False

    return json.dumps(returnDictionary)

@app.route("/otp", methods=["POST"])
def otpcheck():

    global global_ran
    hostName = socket.gethostname()

    otp = request.json['OTP KEY']

    returnDictionary = {}
    returnDictionary["OTP KEY"] = otp

    if (glob_ran == otp):
        returnDictionary["User Authorized"] = True
    else:
        returnDictionary["Unathorized"] = False

    return json.dumps(returnDictionary)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9002)
