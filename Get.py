from flask import Flask, jsonify,request
import random


app = Flask(__name__)

@app.route('/get', methods=['GET'])
def index():
    number = random.randint(1,100)
    return jsonify(number)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)