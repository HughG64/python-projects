# Write a function called celsius_to_fahrenheit that:

# Takes a temperature in Celsius
# Returns it converted to Fahrenheit
# Formula: (celsius * 9/5) + 32
# Then use a list comprehension to convert this entire list:

def celsius_to_fahrenheit(celsius):
    fahrenheit = (float(celsius) * 9/5) + 32
    return f"{float(celsius):.1f}°C = {float(fahrenheit):.1f}°F"

print(celsius_to_fahrenheit(input("Temp: ")))


# pythontemps = [0, 10, 20, 30, 40, 100]
# temp_conversion = [celsius_to_fahrenheit(n) for n in pythontemps]
# for temp in temp_conversion:
#     print(temp)
