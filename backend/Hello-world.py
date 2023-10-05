from flask import Flask, request, jsonify
import datetime

x = datetime.datetime.now()
app = Flask(__name__)

@app.route('/login', methods=['POST', 'GET'])
def login():
    flag = "False"
    try:
        if request.method == 'POST':
            data = request.get_json()
            # username = request.form['Username']
            # password = request.form['Password']
            response = request.get_json("http://-------------:<Port>/", json=data)
            user = [{"Access": response}]
            return jsonify(user, status=200,mimetype='application/json')
        else:
            user =[{"Status": "work in progress"}]
            return jsonify(user)

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=2871)