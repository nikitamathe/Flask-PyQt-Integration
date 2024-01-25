from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify(message='Welcome to the Flask API!')

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify(message='Hello, API!')

if __name__ == '__main__':
    app.run(debug=True)
