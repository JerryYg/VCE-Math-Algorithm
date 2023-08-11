def dec_to_bin(x):
    """Converting from Decimal to Binary"""
    quotient = x
    result  = []
    
    while quotient > 0:
        remainder = quotient % 2
        result.append(remainder)
        quotient = int(quotient / 2)
    return reversed(result)
    

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
            print("{} is converted from decimal to binary as:".format(x), end=" ")
            for b in dec_to_bin(x):
                print(b, end="")
            # print()
            count = 0
            break
    finally:
        count += 1
        if count == MAX_TRIES:
            print('Retry limit ({} times) reached! Bye'.format(MAX_TRIES))
            break      