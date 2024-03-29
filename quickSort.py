def QuickSort(A, low, high):
    if low < high:
        p = partition(A, low, high)
        QuickSort(A, low, p -1)
        QuickSort(A, p+1, high)

def partition(A, low, high):
    i = low -1
    pivot = A[high]

    for j in range(low, high):
        if A[j] <= pivot:
            i += 1
            A[i] , A[j] = A[j], A[i]
    A[i+1], A[high] = A[high], A[i+1]

    return i + 1


A = [84, 21, 96, 15, 47]
print('Original Array', A)
QuickSort(A,0, len(A)-1)
print('Sorted Array', A)
