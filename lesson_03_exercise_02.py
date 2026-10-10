#create a variable to save the highest temperature
highest_temperature = 0
#create a variable to save the lowest temperature
lowest_temperature = 0
#create a variable to save the city with the highest temperture
city_with_the_highest_temperature = ""
#create a variable to save the city with the lowest temperature
city_with_the_lowest_temperature = ""
#at the beginning i have not entered any city, for that reason true means that i am starting to enter a first city
first_city = True
#ask the user for the name of a city or the world "exit"
city = input("Enter the name of the city or type exit to stop the program: ")
#with the command while repeat the program as a loop, when the name of the city is different to "exit"
while city!="exit":
    #ask the user to enter the temperature for the city the user previously chose
    temperature = float(input(f"Enter the temperature in Fahrenheit in {city}: "))
    #conversion from fahrenheit to celsius
    temperature_conversion_celsius = (temperature-32)*(5/9)
    #here I save the values of temp in celsius or fahrenheit of a city
    citytemp = (f"The temperature in {city} is {temperature:.1f} degrees Fahrenheit or {temperature_conversion_celsius:.1f} degrees Celsius.")
    print(citytemp)
    #with this command I can  say that at first the temperatures of the first city are at the same time the lowest and the highest, but the situation will change when i enter the second round of information
    if first_city:
        highest_temperature = temperature_conversion_celsius
        lowest_temperature = temperature_conversion_celsius
        city_with_the_highest_temperature = city
        city_with_the_lowest_temperature = city
        #the first city has already been processed, the next city isn´t the first city anymore, that means from now on the variable won´t be always the first one
        first_city = False
    #from the second city on, i can compare and define which is the lowest and highest temperature and its matching city
    else:
        if temperature_conversion_celsius>highest_temperature:
            highest_temperature=temperature_conversion_celsius
            city_with_the_highest_temperature=city
        if temperature_conversion_celsius<lowest_temperature:
            lowest_temperature=temperature_conversion_celsius
            city_with_the_lowest_temperature=city
    #check is the temperature in fahrenheit is below the freezing point
    if(temperature<32):
        #add the alert for this city´s temperature
        print(f"Warning: The temperature in {city} is below freezing point.")
    #check the other case, if the temperature is above the freezing point.
    else:
        #now you checked that the temperature is above the freezing point
        print(f"The temperature in {city} is above the freezing point.")
    #ask the name of the next city to start to repeat the loop
    city = input("Enter the name of the city or type exit to stop the program: ")
#I want to print the summary of all the calculations of the highest and lowest temperature and its matching city
print("Summary")
print(f"The highest temperature is {highest_temperature:.1f} degrees Celsius in {city_with_the_highest_temperature}.")
print(f"The lowest temperature is {lowest_temperature:.1f} degrees Celsius in {city_with_the_lowest_temperature}")