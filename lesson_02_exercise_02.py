#ask the user about the name of the first city
city1 = input("Enter the name of the first city:")
#ask the user about the name of the second city
city2 = input("Enter the name of the second city:")
#ask the user about the temperature in the first city and convert it to float
temperature1 = float(input(f"Enter the temperature in Fahrenheit in {city1}:"))
temperature_conversion_celsius1 = (temperature1-32)*(5/9)
#ask the user about the temperature in the second city and convert it to float
temperature2 = float(input(f"Enter the temperature in Fahrenheit in {city2}:"))
temperature_conversion_celsius2 = (temperature2-32)*(5/9)
if(temperature1<32 and temperature2<32):
    print("Alert: The temperatures in both cities are below freezing point.")
elif(temperature1<32 or temperature2<32):
    print("Alert: The temperature in one of the cities is below freezing point.")
else:
    print("The temperatures in both cities are above the freezing point.")
print(f"The temperature in {city1} is {temperature_conversion_celsius1:.1f} degrees Celsius.")
print(f"The temperature in {city2} is {temperature_conversion_celsius2:.1f} degrees Celsius.")