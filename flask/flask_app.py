from flask import Flask, request, jsonify
from flask_restx import Api,Resource, Namespace, fields
from learning import get_restaurant,kmeans
from chat_api import chat_to_keyword
from crawl import crawling

app = Flask(__name__)
api = Api(app)
modelNS = Namespace('Model')
api.add_namespace(modelNS,'/model')

# @app.route('/')
# def root():
#     return 'hello'

modelInput = modelNS.model('키워드로 식당추천', strict=True, model={
    'keyword': fields.List(fields.Integer,title='키워드',default=[1,1,0,0,0,0,0,0,0],required=True)
})

@modelNS.route('/cosine')
class ModelCosine(Resource):
    @staticmethod
    @modelNS.expect(modelInput,validate=True)
    def post():
        if request.method == 'POST':
            params = request.get_json()
            list =['나의식당']
            for i in params['keyword']:
                list.append(i)
            result = get_restaurant(list)
            # result = result.to_dict()

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
    result = get_restaurant(list)
    # result = result.to_dict()
    return jsonify(result)

@modelNS.route('/k_means')
class modelKmeans(Resource):
    @staticmethod
    @modelNS.expect(modelInput,validate=True)
    def post():
        if request.method == 'POST':
            params = request.get_json()
            list = []
            for i in params['keyword']:
                list.append(i)
            result = kmeans(list)
            # result = result.to_dict()

        return jsonify(result)

crawlInput = modelNS.model('url로 정보 크롤링', strict=True, model={
    'urls': fields.List(fields.String,title='모바일 네이버 식당주소',required=True, default=["https://m.place.naver.com/restaurant/1759441377/home","https://m.place.naver.com/restaurant/1412069565/home"])
})

@modelNS.route('/crawl')
class modelCrawl(Resource):
    @staticmethod
    @modelNS.expect(crawlInput,validate=True)
    def post():
        if request.method == 'POST':
            params = request.get_json()
            urls = params['urls']
            result = crawling(urls)

        return jsonify(result)

app.run(host='0.0.0.0',debug=True)
