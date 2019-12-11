def bubbleSort(A):
    length = len(A)
    for i in range(1, len(A)):
        pos = 1
        while pos < length:
            if A[pos] < A[pos - 1]:
                A[pos], A[pos-1] = A[pos - 1], A[pos]
            pos += 1
        length -= 1



A = [84, 21, 96, 15, 47]
print('Original Array', A)
bubbleSort(A)
print('Sorted Array', A)