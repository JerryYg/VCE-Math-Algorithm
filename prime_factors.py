def prime_factor(x):
    """List prime factors of input interger"""
    quotient = x
    count = 0
    result = []
    
    for i in range(2, quotient + 1):
    
        while (quotient % i == 0):
            count += 1
            quotient = quotient // i
            
        if quotient == 1:
            result.append([i, count])
            break
        if count != 0: 
            result.append([i, count])
            count = 0            
            
    return result
    
count = 0
MAX_TRIES = 4

while True:
    try:
        temp = input("Key in an integer greater than 1 (e.g. 2, 3, 123, etc.): ")
        x = int(temp)
    except ValueError as e:
        print("'{temp}' is not an interger.".format(temp=temp))
    else:
        if x <= 1:
            if count < MAX_TRIES - 1:
                print('{} is an integer NOT greater than 1.'' Please try again!'.format(x))
            else:
                print('{} is an integer NOT greater than 1.'.format(x))
        else:
            print(prime_factor(x))
            count = 0
            break
    finally:
        count += 1
        if count == MAX_TRIES:
            print('Retry limit ({} times) reached! Bye'.format(MAX_TRIES))
            break        