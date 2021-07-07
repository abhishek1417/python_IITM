# create a function that will output MULTIPLE values ?

def circle(radius, pi = 3.141):
    area = pi * radius * radius
    perimeter = 2* pi *radius
    return [area, perimeter]

print("Area of circle : ", circle(10)[0])
print("Perimeter of circle : ", circle(10)[1])