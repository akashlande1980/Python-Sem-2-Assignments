import math
def area_circle(radius):
    if radius < 0:
        raise ValueError("radius cannot be negative.")
    return math.pi*radius**2
def area_rectangle(length,width):
    if length < 0 or width < 0:
        raise ValueError("length and width cannot be negative.")
    return length*width
def area_triangle(base,height):
    if base < 0 or height < 0:
        raise ValueError("base and height cannot be negative.")
    return 0.5 * base * height