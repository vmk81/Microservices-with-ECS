from flask import Flask, jsonify,request
import random


app = Flask(__name__)

@app.route('/post',methods=['POST'])
def rand():
    data = request.get_json()
    first = int(data['min'])
    second = int(data['max'])
    number = random.randint(first,second)
    return jsonify(number)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)
    #app.run(debug=True)
