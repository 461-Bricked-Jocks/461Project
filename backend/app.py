from flask import Flask, request, jsonify
import datetime
import Mongodb_Hardware
import Mongodb_Users


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
   
    
@app.route('/New-Project', methods=["POST"]) # TODO
def createProject():
    try:
        data = request.get_json()
        
        # TODO
        
        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/Checkout', methods=["POST"]) # TODO
def checkout():
    try:
        data = request.get_json()

        # TODO

        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/Checkin', methods=["POST"]) # TODO
def checkin():
    try:
        data = request.get_json()

        # TODO

        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=2871)