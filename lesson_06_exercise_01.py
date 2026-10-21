import requests

# dictionary with the weather codes from https://open-meteo.com
WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    56: "Light freezing drizzle",
    57: "Dense freezing drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    66: "Light freezing rain",
    67: "Heavy freezing rain",
    71: "Slight snow fall",
    73: "Moderate snow fall",
    75: "Heavy snow fall",
    77: "Snow grains",
    80: "Slight rain shower",
    81: "Moderate rain shower",
    82: "Violent rain shower",
    85: "Slight snow shower",
    86: "Heavy snow shower",
    95: "Thunderstorm",
    96: "Thunderstorm with slight hail",
    99: "Thunderstorm with heavy hail",
}


def get_coordinates(city_name):
    """Returns the latitude, longitude and elevation of a city."""
    # Create the API call URL
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=en&format=json"
    # Send the request to the website and get the response
    response = requests.get(url)
    # Convert the response from JSON to a Python dictionary
    data = response.json()
    # Check if the city was found
    if "results" not in data:
        raise Exception("City not found.")
    # Get the latitude, longitude and elevation from the response
    latitude = data["results"][0]["latitude"]
    longitude = data["results"][0]["longitude"]
    elevation = data["results"][0]["elevation"]
    return latitude, longitude, elevation


def get_weather(city_name):
    # Error handling when the city is not found
    try:
        latitude, longitude, elevation = get_coordinates(city_name)
    except Exception as e:
        print(e)
        return "Error", float("nan")
    # Create the API call URL
    url = "https://api.open-meteo.com/v1/forecast?"
    url += "current_weather=true"  # Add current_weather to request URL
    url += f"&latitude={latitude:.2f}"  # Add latitude to request URL
    # TODO: finish the function

    # 1. Add longitude and elevation to the request URL
    url += f"&longitude={longitude:.2f}"
    url += f"&elevation={elevation:.1f}"
    
    # 2. Send the request to the website and get the response
    response = requests.get(url)
    
    # 3. Convert the response from JSON to a Python dictionary
    data = response.json()
    
    # 4. Get the temperature and weather code from the response
    #the current_weather data is stored in a dictionary under the key 'current_weather'
    current = data["current_weather"]
    #I am extracting the specific value temperature inside the variable current and then saves this value inside the variable temperature
    temperature = current["temperature"]
    #I am extracting the specific value which it is a code that represents how it´s the weather going
    code = current["weathercode"]
    
    # 5. Get the weather description from the WEATHER_CODES dictionary
    # I use .get() to avoid mistakes if a code is not in the dictionary. If it exits, I use the matching weather description if not, I use the message "Unknown weather condition"
    weather = WEATHER_CODES.get(code, "Unknown weather condition")
    
    return weather, temperature


if __name__ == "__main__":
    #I start the loop, executing the program until the user writes exit
    while True:
        city = input("Please enter the name of a city: ")
        if city.lower() == "exit":
            break
        #following this way I can get two results weather and temperature from the function get_weather and assign them to separate variables all in one line.
        weather, temp = get_weather(city)
        #if the info about this city exits, the program print the name of the city, how the weather is going and its temperature in °C, if not it is an error and that´s it.
        if weather != "Error":
            print(f"The current weather in {city} is {weather} and the temperature is {temp}°C.")
        
        
