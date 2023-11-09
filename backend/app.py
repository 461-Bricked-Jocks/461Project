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
   
    
@app.route('/projectPage', methods=["POST"])
def projectPage():
    try:
        data = request.get_json()
        response = Mongodb_Projects.projectList(data["Username"])
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@app.route('/createProject', methods=["POST"])
def createProject():
    try:
        data = request.get_json()
        response = Mongodb_Projects.create_project(data["ProjectName"], data["Description"], data["User"])
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@app.route('/leaveProject', methods=["POST"])
def leaveProject():
    try:
        data = request.get_json()
        print(data)
        print(data["Username"])
        response = Mongodb_Projects.leave_project(data["Username"], data["projectName"])
        print("made it to this ")
        print(response)
        return jsonify(response)
    except Exception as e:
        print("exception")
        return jsonify({"error": str(e)}), 400

@app.route('/joinProject', methods=["POST"])
def joinProject():
    try:
        data = request.get_json()
        response = Mongodb_Projects.join_project(data["Username"], data["projectName"])
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
        response = Mongodb_Hardware.checkIn(data["projectName"],data["HardwareSet"], data["qty"])
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/checkOut', methods=["POST"])
def checkOut():
    try:
        data = request.get_json()
        print(data)
        response = Mongodb_Hardware.checkOut(data["projectName"], data["HardwareSet"], data["qty"])
        print(response)
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run()
    # app.run(debug=True, port=2871)