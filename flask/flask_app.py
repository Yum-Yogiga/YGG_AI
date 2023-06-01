from flask import Flask, request, jsonify
from learning import get_restaurant, add_want_keyword

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

# def main():
#     app.run(host='127.0.0.1', port=80, debug=False)
#
# if __name__ == '__main__':
#     main()

app.run(debug=True)