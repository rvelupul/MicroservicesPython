#
#
#
from flask import request, Flask
import json
import socket


app = Flask(__name__)

#
# curl http://localhost:9003
#
emailRoles = []

@app.route('/')
def echo():
    returnDictionary = {}
    returnDictionary["echo"] = str(socket.gethostname())
    return json.dumps(returnDictionary)

#
# curl -d "{ "user_id" : "id", "email" : "user_email", "newRole" : "role_to_add" }" -X POST http://localhost:9003/addrole  -H "Content-type: application/json"
#


@app.route("/addrole", methods=["POST"])
def compute():
    hostName = socket.gethostname()
    user_id = request.json['user_id']
    user_email = request.json['email']
    new_role = request.json['newRole']

    if user_id == "":
        return json.dumps("Please input the ID")
    elif user_email == "":
        return json.dumps("Please input the username")
    elif new_role == "":
        return json.dumps("Please input the password")
    elif new_role not in emailRoles:
#       print(emailRoles)
        emailRoles.append(new_role)
        return json.dumps("role assigned " + new_role)
    else:
        user_role_already = emailRoles[user_id]
        if new_role not in usr_roles_already:
            usr_roles_already += [new_role]
            return json.dumps("role modified " + new_role)
    return json.dumps(emailRoles)

# curl -d "{ "user_id" : "id", "email" : "user_email", "delRole" : "role_to_delete" }" -X POST
# http://localhost:9003/removerole -H "Content-type: application/json"


@app.route("/removerole", methods=["POST"])
def removerole():
    user_id = request.json['user_id']
    user_email = request.json['email']
    remove_role = request.json['delRole']

    if remove_role in emailRoles:
       emailRoles.remove(remove_role)
       return json.dumps("role removed " + remove_role)
    
    return json.dumps("Please provide correct details")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9003)
