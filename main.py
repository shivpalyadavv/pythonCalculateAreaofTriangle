# If a, b and c are three sides of a triangle. Then,

# s = (a+b+c)/2
# area = √(s(s-a)*(s-b)*(s-c))

# Python Program to find the area of triangle

a = 87
b = 49
c = 63

# Uncomment below to take inputs from the user
# a = float(input('Enter first side: '))
# b = float(input('Enter second side: '))
# c = float(input('Enter third side: '))

# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)