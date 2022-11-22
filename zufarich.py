import heapq
n=int(input())
arr=list(map(int,input().split()))
heapq.heapify(arr)
print(*arr)
