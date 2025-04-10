print("whats your name?")
name = input()  
print("Hello " + name + ", welcome to the temperature converter!")
print("Please enter the temperature you want to convert:")
temp = float(input())
print("Is this temperature in Celsius or Fahrenheit? (C/F)")    
unit = input().upper()
if unit == "C":
    converted_temp = (temp * 9/5) + 32
    print(f"{temp}°C is equal to {converted_temp}°F")
    converted_temp = round(converted_temp, 2)
elif unit == "F":
    converted_temp = (temp - 32) * 5/9
    converted_temp = round(converted_temp, 2)
    print(f"{temp}°F is equal to {converted_temp}°C")
else:
    print("Invalid unit.")