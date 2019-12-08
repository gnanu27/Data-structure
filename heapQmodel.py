import heapq as heap

L = []
heap.heappush(L,20)
heap.heappush(L,23)
heap.heappush(L,10)
heap.heappush(L,30)
heap.heappush(L,12)
heap.heappush(L,2)

print(L)
print(heap.heappop(L))
print(L)
print(heap.heappushpop(L, 18))
print(L)

L1 = heap.nlargest(3, L)
print(L1)
L2 = heap.nsmallest(3, L)
print(L2)

L3 = [20, 14, 22, 30, 18, 11]
print(L3)
heap.heapify(L3)
print(L3)





