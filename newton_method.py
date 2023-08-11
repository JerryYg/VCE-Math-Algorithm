def f(x):
	return -pow(x,3) + 5 * pow(x, 2) - 3 * x + 4
    
def df(x):
    return -3 * pow(x, 2) + 10 * x - 3
    
x = float(input("Please type the initial value: "))

while abs(f(x)) > pow(10, -6):
    x = x - (f(x) / df(x))
    print(x, f(x), sep="\t")
    