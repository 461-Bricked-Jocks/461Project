from flask import Flask, request, jsonify
import datetime
import Mongodb_Hardware
import Mongodb_Users


x = datetime.datetime.now()
app = Flask(__name__)

@app.route('/login', methods=['POST', 'GET'])
def login():
    flag = "False"
    try:
        if request.method == 'POST':                    # For debugging purposes  
            data = request.get_json()
            # username = request.form['Username']
            # password = request.form['Password']
            response = request.get_json("", json=data)
            user = [{"Access": response}]
            return jsonify(user, status=200,mimetype='application/json')        # Access database
        else:
            user =[{"Status": "work in progress"}]
            return jsonify(user)

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=2871)