from math import pow
def sieve_prime(n):
    p_list = []
    n_list = []
    for n in range(2, n+1):
        n_list.append(n)
        
    while pow(n_list[0], 2) <= n:
        for item in n_list:
            if (item > n_list[0]) and (item % n_list[0] == 0):
                n_list.remove(item)
        p_list.append(n_list.pop(0))
        
    return p_list + n_list
        