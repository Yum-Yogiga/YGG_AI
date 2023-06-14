from flask import Flask, request, jsonify
from learning import get_restaurant, get_restaurant2
from chat_api import chat_to_keyword

app = Flask(__name__)

@app.route('/')
def root():
    return 'hello'

@app.route('/model', methods=['POST'])
def model():
    if request.method  == 'POST':
        params = request.get_json()
        list =['나의식당']
        for i in params['keyword']:
            list.append(i)
        result = get_restaurant(list)
        result = result.to_dict()

    return jsonify(result)

@app.route('/chat', methods=['POST'])
def chat():
    if request.method == 'POST':
        params = request.get_json()
        chat = params['chat']
        result = chat_to_keyword(chat)
    list = ['나의식당']
    for i in result:
        list.append(i)
    result = get_restaurant2(list)
    result = result.to_dict()
    return jsonify(result)

app.run(debug=True)