from flask import Flask, request, jsonify
import datetime
import Mongodb_Hardware
import Mongodb_Users
import Mongodb_Projects


x = datetime.datetime.now()
app = Flask(__name__)

@app.route('/login', methods=['POST', 'GET'])
def login():
    try:
        if request.method == 'POST':    # For Testing Purposes  
            data = request.get_json()
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
   
    
@app.route('/Projects', methods=["POST"]) 
def projectPage():
    data = request.get_json()
    method = data["Method"]
    if method is "checkin":
        response = checkin(data)
    elif method is "checkout":
        response = checkout(data)
    else:
        # TODO Return Project Data and Related Hardware Sets (I have questions)
        response = data["projectId"]
    return response
def checkin(data):
    try:
        
        
        # TODO
        
        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 400  
def checkout(data):
    try:
        
        
        # TODO
        
        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route('/joinProject', methods=['POST'])
def get_data():
    try:
        data = request.get_json()
        # TODO join function
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/leaveProject', methods=['POST'])
def get_data():
    try:
        data = request.get_json()
        # TODO Leave function
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@app.route('/createProject', methods=['POST'])
def get_data():
    try:
        data = request.get_json()
        return jsonify(Mongodb_Projects.create_project(data["name"], data["description"], data["projectid"]))
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=2871)