#Write a program which prompts the user for a Celsius temperature,
#convert the temperature to Fahrenheit
#and print out the converted temperature.

temp_c = input("Write the temperature in Celcius:")
temp_f = (float(temp_c) * (9/5) + 32)
print("The temperature in Fahrenheit is",temp_f)
