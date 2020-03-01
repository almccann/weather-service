from flask import Flask, jsonify, make_response
from flask_restful import Api
from weather_api import WeatherAPI
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_url_path="")
api = Api(app)

api.add_resource(WeatherAPI, '/v1/weather', endpoint='weather')

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

if __name__ == '__main__':
    app.run(debug=True)
