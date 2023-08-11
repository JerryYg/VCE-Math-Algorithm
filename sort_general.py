def sort_general(A):
    length = len(A)
    for i in range(length):
        mini = A[i]
        for j in range(i, length - 1):            
            if mini > A[j+1]:
                mini = A[j+1]
        m = A.index(mini)
        A[m] = A[i]        
        A[i] = mini
    return A