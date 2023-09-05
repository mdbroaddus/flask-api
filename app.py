from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

# brief_text = {}
TOA_html = {}

# argument parsing
parser = reqparse.RequestParser()
parser.add_argument('q',help='Pass a sentence to analyse')


class Brief(Resource):
    def post(self):

        # use parser and find the user's query
        args = parser.parse_args()
        brief_text = args['q']
        TOA_html["TOA_entry"] = brief_text
        return jsonify(brief_text)
        # return jsonify(TOA_html)
    
api.add_resource(Brief, "/")    

if __name__ == "__main__":
    app.run(debug=True)
            