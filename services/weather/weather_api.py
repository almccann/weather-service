from flask_restful import Resource, reqparse, fields, marshal
from auth import auth
from weather_source import source_data

weather_fields = {
    'wind_speed': fields.Integer,
    'temperature_degrees': fields.Integer,
}

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
        result = source_data(args['city'])
        return marshal(result, weather_fields), 200
