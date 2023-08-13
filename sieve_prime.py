from math import pow
def sieve_prime(n):
    p_list = [] # container list for primes no larger than square root of n
    n_list = [] 
    for n in range(2, n + 1):
        n_list.append(n) # all integers from 2 to n
        
    while pow(n_list[0], 2) <= n: # check the square of first item (a prime) in n_list
        for item in n_list:
            if (item > n_list[0]) and (item % n_list[0] == 0): 
                n_list.remove(item) # remove all items which are multiple of the first item 
        p_list.append(n_list.pop(0)) # remove first item (a prime) and add it to p_list
        
    return p_list + n_list # p_list are all primes no larger than square root of n; n_list are those larger than
        