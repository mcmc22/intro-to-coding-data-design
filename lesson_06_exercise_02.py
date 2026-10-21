import requests

def get_coordinates(city_name):
    """Returns the latitude, longitude and elevation of a city."""
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=en&format=json"
    response = requests.get(url)
    response.raise_for_status()
    
    data = response.json()
    # Check if the city was found
    if "results" not in data or not data["results"]:
        raise Exception("City not found.") 
    # Get the latitude, longitude and elevation from the response
    latitude = data["results"][0]["latitude"]
    longitude = data["results"][0]["longitude"]
    elevation = data["results"][0]["elevation"]
    return latitude, longitude, elevation

def get_weather_forecast(city_name):
    days = []
    temp_max = []
    temp_min = []

    # Error handling when the city is not found
    try:
        latitude, longitude, elevation = get_coordinates(city_name)
    except Exception as e:
        print(e)
        return days, temp_max, temp_min
    
    # Create the API call URL
    url = "https://api.open-meteo.com/v1/forecast?"
    url += "current_weather=true"  # Add current_weather to request URL
    url += f"&latitude={latitude:.2f}"  # Add latitude to request URL
    url += f"&longitude={longitude:.2f}"  # Add longitude to request URL
    url += f"&elevation={elevation:.2f}"  # Add elevation to request URL
    # TODO: Get the weather forecast for the next 7 days

    #I add the daily and timezone parameters to the request URL
    url += "&daily=temperature_2m_max,temperature_2m_min"
    url += "&timezone=Europe%2FBerlin"

    #I send the request and convert the response to a Python dictionary
    response = requests.get(url)
    #the dictionary is called data
    data = response.json()

    #it stores the forecast dates and saves them in days
    days = data["daily"]["time"]
    #it stores each day’s maximum temperatures and saves it in temp_max
    temp_max = data["daily"]["temperature_2m_max"]
    #it stores each day’s minimum temperatures and saves it in temp_min
    temp_min = data["daily"]["temperature_2m_min"]

    return days, temp_max, temp_min

if __name__ == "__main__":
    city_name = input("Please enter the name of a city: ")

    while city_name != "exit":
        days, temp_max, temp_min = get_weather_forecast(city_name)
        # TODO: Print the weather data for the next 7 days    
        #it goes through each forecast day, element is the position of the day in the list
        for element in range(len(days)):
            #the program prints the max temp, the min temp in °C for the city,for each of the 7 days.
            print(f"{days[element]}: Maximum temperature: {temp_max[element]}°C, Minimum temperature: {temp_min[element]}°C")
        #at the end of the city´s forecast, the program is again asking for a new city to show the results for the next city
        city_name = input("Please enter the name of a city: ")    
    