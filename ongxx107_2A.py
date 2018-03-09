#HW2 Problem A

import math

def poiseuille(viscosity, length, radius):
    resistance = ((8*viscosity*length)/(math.pi*(radius**4)))
    return resistance

viscosity = float(input("Input the viscosity: "))
length = int(input("Input the length: "))
radius = int(input("Input the radius: "))
print("The resistance is",poiseuille(viscosity, length, radius))
