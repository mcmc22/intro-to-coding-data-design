#I define the dictionary cities, where I am going to collect information about a particular city, which is defined by the user
cities = {}
while True:
    city = input("Please enter the name of the city: ")
    #if the user type exit, the program breaks and give the summary
    if city == "exit":
        break
    #I define this variable where I am going to store the temperature system, celsius or fahrenheit, which is chosen by the user
    asking_units = input("are you entering the temperature in Fahrenheit or Celsius?: ")
    if asking_units == "Celsius":
        temperature_celsius = float(input(f"Please enter the current temperature in Celsius in {city} "))
        #conversion from celsius to fahrenheit
        temperature_fahrenheit = temperature_celsius * 9 / 5 + 32
    elif asking_units == "Fahrenheit":
        temperature_fahrenheit = float(input(f"Please enter the current temperature in Fahrenheit in {city} "))
        #conversion from fahrenheit to celsius
        temperature_celsius = (temperature_fahrenheit - 32) * 5 / 9
    #now I need to know if in this particular city it´s raining. the user can choose between yes and no.
    raining = input(f"Is it raining in {city}? (yes/no) ")
    #now I need to know if in this particular city the sun is shining. the user can choose between yes and no.
    shining = input(f"is the sun shining in {city}? (yes/no) ")
    if raining == "yes":
        print("Is it raining?: yes ")
    else:
        print("Is it raining?: no ")
    if shining == "yes":
        print("Is the sun shining?: yes " )
    else:
        print("Is the sun shining?: no ")
    #this saves the city´s temperature in celsius and fahrenheit, and weather conditions rain or/and sun shining in the cities dictionary
    cities[city] = {"Celsius": temperature_celsius, "Fahrenheit": temperature_fahrenheit, "raining": raining, "shining": shining }
print("\nSummary:")
#the program goes through each city and its weahter information in the cities dictionary
for city, weather in cities.items():
    #there is 2 possibilities, rain or sun, the program can store one, two or none of these weather situations
    if weather["shining"] == "yes":
        sun_text = "sun"
    else:
        sun_text = "no sun"
    if weather["raining"] == "yes":
        rain_text = "rain"
    else:
        rain_text = "no rain"
    #print the city´s weather: name of the city, temperature in Celsius, temperature in Fahrenheit, and conditions of rain and/or sun shining. 
    print(f"{city}: {weather['Celsius']:.0f}°C, " f"{weather['Fahrenheit']:.0f}°F, " f"{sun_text} and {rain_text}")
    if weather["Celsius"] < 0:
        print(f"Warning: The temperature in {city} is below the freezing point.")
    if weather["raining"] == "yes" and weather["shining"] == "yes":
        print(f"There is a rainbow in {city}.")