from flask import jsonify, make_response
from flask_restful import Resource, reqparse, fields, marshal
import time
from auth import auth
from weather_source import source_data
from util import key_exists

weather_fields = {
    'wind_speed': fields.Integer,
    'temperature_degrees': fields.Integer,
}

cache = dict()

class WeatherAPI(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('city', type=str, required=True,
                                   help='City required',
                                   location='args')
        super(WeatherAPI, self).__init__()

    def get(self):
        args = self.reqparse.parse_args()
        city = args['city']
        cache_exists = key_exists(city, cache)

        # Use fresh cache
        if cache_exists and less_than_3_seconds(cache[city]['timestamp']):
            return marshal(cache[city], weather_fields), 200

        data = source_data(city)
        # Update cache and return
        if data != False:
            cache[city] = data
            return marshal(data, weather_fields), 200
        # Use stale cache if external sources fail
        elif cache_exists:
            return marshal(cache[city], weather_fields), 200
        # Give up if no external sources nor stale cache
        else:
            return make_response(jsonify( { 'error': 'Bad request' } ), 400)

def less_than_3_seconds(t):
   return time.time() - t <= 3

# Generic memoise function, not used
def memoise(func):
    def memoised_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return memoised_func
