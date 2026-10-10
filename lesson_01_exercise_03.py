#ask the user for their name
name = input("Enter your name:")
#ask the user about the name of the first city
city1 = input("Enter the name of the first city:")
#ask the user about the name of the second city
city2 = input("Enter the name of the second city:")
#ask the user about the temperature in the first city and convert it to float
temperature1 = float(input(f"Enter the temperature in Celsius in {city1}:"))
#ask the user about the temperature in the second city and convert it to float
temperature2 = float(input(f"Enter the temperature in Celsius in {city2}:"))
#calculate the average temperature
average_two_temperatures = (temperature1 + temperature2)/2
temperature_conversion_fahrenheit = (1.8*average_two_temperatures)+32
#type the average temperature of these two cities in Celsius and Fahrenheit
print(f"The average temperature between {city1} and {city2} is {average_two_temperatures} degrees Celsius. That´s {temperature_conversion_fahrenheit} degrees Fahrenheit.")
