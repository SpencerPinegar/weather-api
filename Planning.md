# Weather-API  

## Goal/Prompt

```
Weather Service
Coding Exercise

Write an http server that uses the Open Weather API that exposes an endpoint that takes in lat/long
coordinates. This endpoint should return what the weather condition is outside in that area (snow, rain,
etc), whether it’s hot, cold, or moderate outside (use your own discretion on what temperature equates to
each type).
The API can be found here:https://openweathermap.org/api. Even though most of the API calls found on
OpenWeather aren’t free, you should be able to use the free “current weather data” API call for this
project. First, sign-up for an account, which shouldn’t require credit card or payment information. Once
you’ve created an account, use https://openweathermap.org/faq to get your API Key setup to start using
the API.
Once you’ve coded your project, add it to a publicly accessible Github repository and share it
with the team. Additionally, please don’t add your API Key to the project. Each member of the
team reviewing your code has their own key to use for testing your project.
```

## Expected Input
1. Latitude
2. Longitude

## Expected Output
1. Conditions: (ENUM)
    1. Raining
    2. Sunny
    3. Snowing
    4. Cloudy
2. Temperature
    1. Cold (T <= 32 degrees F)
    2. Moderate (32< T <90 degrees F)
    3. Hot (>=90 Degrees F)
    
# Customer Scenarios
1. Latitude Invalid - return 400 
2. Longitude Invalid - return 400
3. Lat/Long Valid, Weather Service API up, API key valid - return 200
4. Lat/Long Valid, Weather Service API down - return 503
5. Lat/Long Valid, Weather Service APIup, API key invalid - return 403

# Design
1. Set up a Python Flask Server
2. Add a GET API route with `lat` & `long GET parameters
3. Validate lat & long GET parameters`- return 400 if invalid
4. Make Weather API Request
5. Handle Weather Response 500 - return 500
6. Handle Weather Response 401 - return 401
7. Handle 200 - parse data from response return formatted JSON

# Example Resp From Weather API
```json
{
  'coord': {'lon': 90, 'lat': 90}, 
  'weather': [
    {
      'id': 803,
      'main': 'Clouds', 
      'description': 'broken clouds',
      'icon': '04n'
    }
   ], 
  'base': 'stations', 
  'main': 
    {
      'temp': 258.67,
      'feels_like': 253.25, 
      'temp_min': 258.67, 
      'temp_max': 258.67, 
      'pressure': 1036,
      'humidity': 97, 
      'sea_level': 1036,
      'grnd_level': 1036
    }, 
  'visibility': 10000, 
  'wind': 
    {
      'speed': 2.33,
      'deg': 300,
      'gust': 2.23
    },
  'clouds': {'all': 52}, 
  'dt': 1714604721, 
  'sys': {'sunrise': 0, 'sunset': 0}, 
  'timezone': 21600, 
  'id': 0, 
  'name': '', 
  'cod': 200}
```
NOTE: We will be using the get param units=standard to ensure temperature units are in kelvin

Data relevant to the project:

Conditions - ['weather'][0]['description'] - Using this for conditions

Temperature - ['main']['feels_like']  - Use this for feeling of temperature, convert to Fahrenheit and map to feeling based on range; (Cold, Moderate, Hot)



 

