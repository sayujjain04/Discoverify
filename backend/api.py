from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, Flask API!'})

if __name__ == '_main_':
    app.run(debug=True)