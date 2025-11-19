# Ask for temp in Fahrenheit
fahrenheit = input("Enter a temperature in Fahrenheit: ")

# Convert input to float for maths
fahrenheit = float(fahrenheit)

# Convert Fahrenheit to Celsius
celsius = (fahrenheit - 32) * 5/9

# Display result
print(f"{fahrenheit}°F is equal to {celsius:.2f}°C.")