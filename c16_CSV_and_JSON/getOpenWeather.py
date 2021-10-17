#! python3
# getOpenWeather.py - Prints the weather for a location from the command line.
"""
Overall, the program does the following:
1. Reads the requested location from the command line
2. Downloads JSON weather data from OpenWeatherMap.org 
3. Converts the string of JSON data to a Python data structure 
4. Prints the weather for today and the next two days

So the code will need to do the following:
1. Join strings in sys.argv to get the location.
2. Call requests.get() to download the weather data.
3. Call json.loads() to convert the JSON data to a Python data structure. 
4. Print the weather forecast.

For this project, open a new file editor window and save it as getOpenWeather.py. 
Then visit https://openweathermap.org/api/ in your browser and sign up for a 
free account to obtain an API key, also called an app ID, which for the OpenWeatherMap 
service is a string code that looks something like '30144aba38018987d84710d0e319281e'. 
You don’t need to pay for this service unless you plan on making more than 60 API calls 
per minute. Keep the API key secret; anyone who knows it can write scripts that use your 
account’s usage quota.

JSON data ===> Temperature. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.

Formula	from Kelvin to Fahrenheit:
    (288.09K − 273.15) × 9/5 + 32 = 58.892°F
"""

# Current day API - get API key from website by register
API_key = 'bdd263d10146660f44e5bc260000672a'

import json, requests, sys, pprint

# Compute location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
    sys.exit()
city = ','.join(sys.argv[1:])
print(f"city : {city}")

# TODO: Download the JSON data from OpenWeatherMap.org's API.
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"

print(url)

response = requests.get(url)
response.raise_for_status()

# Uncomment to see the raw JSON text: 
# print(response.text)

# TODO: Load JSON data into a Python variable.
weatherData = json.loads(response.text)
# pprint.pprint(weatherData)

print('Current weather in %s:' % (city)) 
# print(len(weatherData))
w = weatherData['main']
current_temp_k = w['temp']
current_temp_F = (current_temp_k - 273.15) * 9/5 +32
# print(w)
print(f"Current Temperature is {int(current_temp_F)}F.")

