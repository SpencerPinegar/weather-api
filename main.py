import os
import json

from flask import Flask, request, jsonify
import requests

# ENV VARS
WEATHER_API_KEY = os.environ.get('WEATHER_API_KEY')

# ENV CONSTANTS
OPEN_WEATHER_API_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"

# Flask App
app = Flask(__name__)


################################ API ROUTES #######################################
@app.route('/', methods=['GET'])
def index():
    return jsonify({"MSG": 'Please navigate to /weather to use the API'}), 200


@app.route('/weather', methods=['GET'])
def get_weather():
    # Ensure lat & long API get Params valid
    lat = request.args.get('lat')
    long = request.args.get('long')
    bad_request_string = get_lat_or_long_bad_request_string(lat, long)
    if bad_request_string:
        return app.response_class(
            response=json.dumps({"error": bad_request_string}),
            status=400,
            mimetype='application/json'
        )
    else:
        lat = float(lat)
        long = float(long)

    # Get weather response
    weather_resp = get_weather_data(lat, long)
    return handle_weather_resp(weather_resp)


################################ TESTABLE HELPER FUNCTIONS #######################################
def handle_weather_resp(weather_resp):
    def _kelvin_to_how_temp_feels(kel):
        fahrenheit = ((kel - 273.15) * 9 / 5) + 32
        if fahrenheit < 33:
            return "Cold"
        elif fahrenheit < 90:
            return "Moderate"
        else:
            return "Hot"

    if weather_resp.status_code == 500:
        return app.response_class(
            response=json.dumps({"error": "Weather API Error"}),
            status=500,
            mimetype='application/json'
        )
    if weather_resp.status_code == 401:
        return app.response_class(
            response=json.dumps({"error": "Weather API Key Invalid"}),
            status=401,
            mimetype='application/json'
        )
    if weather_resp.status_code != 200:
        return app.response_class(
            response=json.dumps({"error": "Failed Unknown Weather Status Code"}),
            status=weather_resp.status_code,
            mimetype='application/json'
        )

    # Handle expected response
    weather_json = weather_resp.json()
    expected_conditions = weather_json['weather'][0]['description'].title()
    temp_feeling = _kelvin_to_how_temp_feels(weather_json['main']['feels_like'])
    data = {
        'Conditions': expected_conditions,
        'Temp': temp_feeling,
        # Add more data as needed
    }

    # return JSON
    return jsonify(data)


def get_weather_data(lat, long):
    url = f'{OPEN_WEATHER_API_ENDPOINT}?lat={lat}&lon={long}&appid={WEATHER_API_KEY}&units=standard'
    return requests.get(url)


def get_lat_or_long_bad_request_string(lat, long):
    try:
        # Perform validation logic here
        if not (-90 <= float(lat) <= 90):
            raise Exception()
    except:
        return f"lat parameter must be a number between -90 & 90; lat: {lat}"
    try:
        if not (-180 <= float(long) <= 180):
            raise Exception()
    except:
        return f"long parameter must be a number between -90  &  90; long: {long}"
    return None


#################################### Run Flask Application ###############################
if __name__ == "__main__":
    if not WEATHER_API_KEY:
        raise Exception(
            f"Please set the WEATHER_API_KEY env var with the appropriate API Key for {OPEN_WEATHER_API_ENDPOINT}")
    app.run(debug=True)
