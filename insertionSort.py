def insertSort(A):
    for i in range(1, len(A)):
        value = A[i]
        pos = i

        while pos > 0 and A[pos -1] > value:
            A[pos] = A[pos - 1]
            pos -= 1
        
        A[pos] = value

        
A = [84, 21, 96, 15, 47]
print('original Array',A)
insertSort(A)
print('Sorted Array', A)