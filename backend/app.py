from flask import Flask, request, jsonify, make_response
# from flask import Flask, request, jsonify

from flask_cors import CORS
import datetime
import Mongodb_Hardware
import Mongodb_Users
import Mongodb_Projects
import jwt

# const jwt = require('jsonwebtoken')
# require('dotenv').config


x = datetime.datetime.now()
app = Flask(__name__)
CORS(app)

def verifyJWT(request):
    #if i pass username here i can verify 
    token = request.headers.get("x-access-token")
    if not token:
        print("in verifyJWT Token: ", token)
        return make_response("No token found", 401)
    
    else:
        try:
            decoded = jwt.decode(token, "jwtSecret", algorithms=["HS256"])
            print("Decoded JWT:", decoded)  
            user = decoded['user']
            password = decoded['pass']

            print("decoded user", user)
            print("decoded pass", password)
        except jwt.ExpiredSignatureError:
            return make_response(jsonify(auth=False, message="Token has expired"), 401)
        except jwt.InvalidTokenError:
            return make_response(jsonify(auth=False, message="Invalid token"), 401)
    return None

@app.route('/isUserAuth', methods=['GET'])
def is_user_auth():
    error = verifyJWT(request)
    if error:
        return error
    return jsonify(auth=True, message="User is authenticated, congrats!")

@app.route('/login', methods=['POST', 'GET'])
def login():
    try:
        if request.method == 'POST':    # For Testing Purposes  
            data = request.get_json()
            print(data)
            print("Hello")

            response = Mongodb_Users.existingAccount(data["Username"], data["Password"])
            print("Response: ", response)
            existingUser = response['Access']
            print("existingUser: " , existingUser)
            if(existingUser):
                user = response["Username"]
                password = response["Password"]

                # var token = jwt.sign(user, process.env.ACCESS_TOKEN_SECRET, {
                print("request.data: " , request.data)
                # token = jwt.sign( user, "jwtSecret", expiresIn=1800)  # 5 mins
                # token = jwt.encode( user, "jwtSecret", expiresIn=1800)  # 5 mins
                # encoded_jwt = jwt.encode({'user': user}, "jwtSecret", algorithm='HS256')
                # not that this is encoded with the encrypted user and encrypted password
                encoded_jwt = jwt.encode({'user': user, 'pass': password}, "jwtSecret", algorithm='HS256')



                print(encoded_jwt)
                return jsonify(auth=True, token=encoded_jwt, response=response)
        
            print("this is response" , response)
            print("this is responsejsonify " , jsonify(response = response))

            return jsonify(response=response)
        else:
            print("in else")
            user =[{"Status": "work in progress"}]   # For Testing Purposes
            return jsonify(user)
            # return jsonify(auth=True, token=encoded_jwt, response=)
    except Exception as e:
        print("error")
        return jsonify({"error": str(e)}), 400

# x = datetime.datetime.now()
# app = Flask(__name__)
# CORS(app)

# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     try:
#         if request.method == 'POST':    # For Testing Purposes  
#             data = request.get_json()
#             print(data)
#             response = Mongodb_Users.existingAccount(data["Username"], data["Password"])
#             return response
#         else:
#             user =[{"Status": "work in progress"}]   # For Testing Purposes
#             return jsonify(user)
#     except Exception as e:
#         return jsonify({"error": str(e)}), 400
    
@app.route('/Create-User', methods=["POST"])
def create():
    try:
        data = request.get_json()
        response = Mongodb_Users.create_user(data["Username"], data["Password"])
        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 400
   
    
@app.route('/projectPage', methods=["POST"])
def projectPage():
    try:
        data = request.get_json()
        response = Mongodb_Projects.projectList(data["Username"], data["Password"])
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@app.route('/createProject', methods=["POST"])
def createProject():
    try:
        data = request.get_json()
        response = Mongodb_Projects.create_project(data["ProjectName"], data["Description"])
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@app.route('/leaveProject', methods=["POST"])
def leaveProject():
    try:
        data = request.get_json()
        response = Mongodb_Projects.leave_project(data["Username"], data["Password"], data["projectName"])
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/joinProject', methods=["POST"])
def joinProject():
    try:
        data = request.get_json()
        response = Mongodb_Projects.join_project(data["Username"], data["Password"], data["projectName"])
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@app.route('/availabilityCapacity', methods=["POST"])
def availabilityCapacity():
    try:
        data = request.get_json()
        response = Mongodb_Hardware.availability_capacity(data["HardwareSet"])
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@app.route('/checkIn', methods=["POST"])
def checkIn():
    try:
        data = request.get_json()
        response = Mongodb_Hardware.checkIn({data["HardwareSet"], data["qty"]})
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/checkOut', methods=["POST"])
def checkOut():
    try:
        data = request.get_json()
        response = Mongodb_Hardware.checkOut({data["HardwareSet"], data["qty"]})
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run()
    # app.run(debug=True, port=2871)