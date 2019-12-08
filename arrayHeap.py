class ArrayHeap():
    def __init__(self):
        self._maxSize = 10
        self._currentSize = 0
        self._data = [-1] * self._maxSize

    def maxh(self):
        if self._currentSize == 0:
            print('Heap Array is empty')
        return self._data[1]

    def insert(self, e):
        if self._maxSize == self._currentSize:
            return 'Empty Array'
        self._currentSize += 1
        i = self._currentSize
        while i != 1 and e > self._data[i // 2]:
            self._data[i] = self._data[i//2]
            i = i//2
        self._data[i] = e

    def deletemax(self):
        if self._currentSize == 0:
            return "Empty Heap"

        x = self._data[1]
        y = self._data[self._currentSize]
        self._currentSize -= 1
        i = 1
        ci = 2

        while ci <= self._currentSize:
            if ci < self._currentSize and self._data[ci] < self._data[ci+1]:
                ci += 1
            if y >= self._data[ci]:
                break

            self._data[i] = self._data[ci]
            i = ci
            ci = ci * 2

        self._data[i] = y


h = ArrayHeap()
h.insert(29)
h.insert(14)
h.insert(22)
h.insert(13)
h.insert(2)
print(h._data)
h.deletemax()
print(h._data)
h.deletemax()
print(h._data)
            

        




        

        

    
