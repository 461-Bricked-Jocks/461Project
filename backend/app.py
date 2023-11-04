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
   
    
@app.route('/projectPage', methods=["POST"]) # TODO Put Last three in one page
def projectPage():
    try:
        data = request.get_json()
        response = Mongodb_Projects.projectList
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run()
    # app.run(debug=True, port=2871)