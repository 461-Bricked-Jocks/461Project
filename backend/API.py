from flask import Flask, request, jsonify
import datetime
import Mongodb_Hardware
import Mongodb_Users


x = datetime.datetime.now()
app = Flask(__name__)

@app.route('/login', methods=['POST', 'GET'])
def login():
    try:
        if request.method == 'POST':    # For debugging purposes  
            data = request.get_json()
            response = Mongodb_Users.existingAccount(data["Username"], data["Password"]) 
            return response
        else:
            user =[{"Status": "work in progress"}]   # For debugging purposes
            return jsonify(user)
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    

@app.route('/create', methods=["POST"])
def create():
    try:
        data = request.get_json()
        response = Mongodb_Users.create_user(data["Username"], data["Password"])
        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=2871)