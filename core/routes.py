from core import api
from flask import jsonify
from core.utils import get_jokes
from flask_restx import Resource, reqparse

ns = api.namespace('/', description='Jokes API')

parser = reqparse.RequestParser()
parser_copy = parser
@ns.route('/get-jokes/random-joke')
class DailyHoroscopeAPI(Resource):
    @ns.doc(parser=parser_copy)
    def get(self):
        data = get_jokes()
        return data
