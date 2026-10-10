#ask the user for the name of a city or the world "exit"
city = input("Enter the name of the city or type exit to stop the program: ")
#with the command while repeat the program as a loop, when the name of the city is different to "exit"
while city!="exit":
    #ask the user to enter the temperature for the city the user previously chose
    temperature = float(input(f"Enter the temperature in Fahrenheit in {city}: "))
    #conversion from fahrenheit to celsius
    temperature_conversion_celsius = (temperature-32)*(5/9)
    #in this variable I save my output about a city and its temperatures in Fahrenheit and celsius
    citytemp = (f"The temperature in {city} is {temperature:.1f} degrees Fahrenheit or {temperature_conversion_celsius:.1f} degrees Celsius.")
    print(citytemp)
    #check if the temperature in fahrenheit is below the freezing point
    if(temperature<32):
        #add the alert for this city´s temperature
        print(f"Warning: The temperature in {city} is below freezing point.")
    #check the other case, if the temperature is above the freezing point.
    else:
        print(f"The temperatures in {city} is above the freezing point.")
    #ask the name of the next city to start to repeat the loop
    city = input("Enter the name of the city or type exit to stop the program: ")