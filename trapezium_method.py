from math import *
def f(x):
    return pow(2, x)
    
a = float(input("Low bound: "))
b = float(input("Upper Bound: "))
n = int(input("Number of strips: "))

h = (b - a) / n

left = a
right = a + h
sum = 0

for i in range(n):
    area = 0.5 * (f(left) + f(right)) * h
    sum += area
    left += h
    right += h
    
print (sum)