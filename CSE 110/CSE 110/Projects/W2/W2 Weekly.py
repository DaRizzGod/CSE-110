# If you release an object (ball, rock, whatever) from rest (or you could throw it) and let it fall through a fluid,
# the change in speed of the object is affected by several things: the mass of the object, the acceleration due to gravity, 
# the shape of the projectile, the size of the projectile, and the density of the fluid.

import math

print("Welcome to the velocity calculator. Please enter the following: \n")

mass = float(input("Mass (in kg): "))
gravity = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
time = float(input("Time (in seconds): "))
fluid_density = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
object_area = float(input("Cross sectional area of the object (in m^2): "))
object_drag = float(input("Drag constant (0.5 for a sphere, 1.1 for a cylinder on its side): "))
c_coefficient = 0.5 * fluid_density * object_area * object_drag

#First calculate c = 1/2 p A C

velocity = math.sqrt(mass*gravity / c_coefficient) * (1-math.exp((- math.sqrt(mass*gravity*c_coefficient)/mass)*time))

print(f"The inner value of c is: {c_coefficient:.3f}")
print(f"The velocity of the object after {time} seconds is: {velocity:.3f} m/s")
