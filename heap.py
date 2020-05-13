import heapq
h=[]
heapq.heappush(h,167)
heapq.heappush(h,33)
heapq.heappush(h,67)
print("Elements of heap:")
for a in h:
    print(a)
print("The smallest element in the heap:")
print(h[0])
print("Elements in heap after popping:")
heapq.heappop(h)
for a in h:
    print(a)


