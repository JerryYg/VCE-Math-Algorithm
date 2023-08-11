def hcf(x, y):
    r = x % y
    while r > 0:
        x = y
        y = r
        r = x % y
    return y    
        
n1 = int(input("First natural number: "))
n2 = int(input("Second natural number: "))
if n1 >= n2:
    print("HCF({}, {}) = {}".format(n1, n2, hcf(n1, n2)))
else:
    print("HCF({}, {}) = {}".format(n2, n1, hcf(n2, n1)))