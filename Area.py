#Vivek

import math
def calc_area(length,shape):
    if shape == 'C':
        return math.pi*pow(length,2)
    else:
        return pow(length, 2)
shape = input("Enter a shape(C for circle, S for square) for finding the area ")
length = int(input("Please enter the neccessary length or radius "))
print(f"The ascii code of {shape} is",ord(shape))
print(f"The area of the {shape} with the length {length} is",calc_area(length,shape))