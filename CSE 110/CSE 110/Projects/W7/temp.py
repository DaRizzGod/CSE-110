# T is the temperature in degrees Fahrenheit

# V is the wind speed in miles per hour

# V^0.16 means V to the power of 0.16, which can be found in Python using the ** operator.
# Wind Chill (ºF) = 35.74 + 0.6215T - 35.75(V0.16) + 0.4275T(V0.16)
import math

def conversion(Celsius):
    Fahrenheit = float(Celsius) * (9/5) + 32
    return Fahrenheit

def snow(Temperature,Velocity):
    return 35.74 + 0.6215 * Temperature - 35.75 * (Velocity ** 0.16) + 0.4275 * Temperature * (Velocity ** 0.16)

user = input('What is the temperature?')
word = input('Do you want it to be Fahreheit or Celsius (F/C)? ')  
freezing = 0
if word == 'C':
    freezing = conversion(user)
else:
    freezing = float(user)
    
for velocity in range(5, 61, 5):
    windchill = snow(freezing,velocity)
    print(f'At temperature {freezing}F, and wind speed {velocity}mph, the windchill is: {windchill}F')
    
