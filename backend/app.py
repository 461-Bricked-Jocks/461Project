from flask import Flask, request, jsonify
from flask_cors import CORS
import datetime
import Mongodb_Hardware
import Mongodb_Users
import Mongodb_Projects


x = datetime.datetime.now()
app = Flask(__name__)
CORS(app)

@app.route('/login', methods=['POST', 'GET'])
def login():
    try:
        if request.method == 'POST':    # For Testing Purposes  
            data = request.get_json()
            print(data)
            response = Mongodb_Users.existingAccount(data["Username"], data["Password"])
            return response
        else:
            user =[{"Status": "work in progress"}]   # For Testing Purposes
            return jsonify(user)
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@app.route('/Create-User', methods=["POST"])
def create():
    try:
        data = request.get_json()
        response = Mongodb_Users.create_user(data["Username"], data["Password"])
        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 400
   
    
@app.route('/Projects', methods=["POST"]) # TODO Put Last three in one page
def projectPage():
    data = request.get_json()
    method = data["Method"]
    if method is "createProject":
        response = createProject(data)
    elif method is "checkin":
        response = checkin(data)
    elif method is "checkout":
        response = checkout(data)
    else:
        # TODO Return Project Data and Related Hardware Sets (I have questions)
        response = []
    return response
def createProject(data):
    try:
        
        
        # TODO
        
        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 400
def checkin(data):
    try:
        data = request.get_json()

        # TODO
        
        
    except Exception as e:
        return jsonify({"error": str(e)}), 400  
def checkout(data):
    try:
        data = request.get_json()
        
        # TODO
        

    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run()
    # app.run(debug=True, port=2871)