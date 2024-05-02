#Flask Weather API 
This README provides instructions for setting up and running the Flask API application on macOS using Homebrew and virtual environments.

## Prerequisites
- macOS operating system
- Homebrew installed (Installation guide)

## Prepare to Run API
#### 1. Download Python with Homebrew
Open Terminal and run the following command to install Python 3 using Homebrew:

``brew install python``
#### 2. Set up Python Virtual Environment
Navigate to the Flask project base directory <weather-api> in Terminal and create a virtual environment using the following command:

``python3 -m venv venv``
### 3. Activate Python Virtual Environment
Activate the virtual environment by running:

``source venv/bin/activate```
### 4. Install Requirements Recursively
While in the activated virtual environment, install the project dependencies recursively using the following command:

``pip install -r requirements.txt``
### 5. Run Python Main Application
Run the main Python application using:

## Run API
### 1. Activate Python  Virtual Environment if not Activated
Activate the virtual environment by running:
``python3 -m venv venv``

### 2. Set API Key Variable
Set your Personal Weather API Key variable from [OpenWeatherMap](https://home.openweathermap.org/api_keys)
In your terminal use the command  

`WEATHER_API_KEY=<actual_api_key>`

### 3. Run the API application 
Start the API using
``python main.py``

### 4. Test Python Main Application in Browser
Open your web browser and navigate to the following URL:
``http://127.0.0.1:5000/weather?lat=40.468530&long=-111.923490``

You will receive a response like:
```json
{
"Conditions": "Few Clouds",
"Temp": "Cold"
}
```

# Unit Tests
To run unit tests, execute the following command in Terminal:

`python test_main.py``

This will run all the unit tests and provide the test results.

##  Additional Notes
Customize the port number in your main.py file if it's different from the default Flask port (5000).