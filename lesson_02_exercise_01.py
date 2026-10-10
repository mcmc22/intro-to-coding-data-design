#ask the user about the name of the first city
city = input("Enter the name of the city: ")
#ask the user about the temperature in the city and convert it to float
temperature = float(input(f"Enter the temperature in Fahrenheit in {city}: "))
temperature_conversion_celsius = (temperature-32)*(5/9)
if(temperature_conversion_celsius<0):
    print("Alert: The temperature is below freezing point.")
else:
    print("The temperature is above the freezing point.")
print(f"The temperature in {city} is {temperature_conversion_celsius:.1f} degrees Celsius.")