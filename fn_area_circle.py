# function with default arguments

def Area_of_circle(radius, pi=3.141):
    area =pi * radius * radius
    return area

print(Area_of_circle(10))

print(Area_of_circle(10,20))