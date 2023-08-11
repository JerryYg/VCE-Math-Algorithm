def bubble_sort(L):
    l = len(L)
    for i in range(l):
        for j in range(l-1-i ):
            if L[j] > L[j+1]:
                temp = L[j+1]
                L[j+1] = L[j]
                L[j] = temp
    return L