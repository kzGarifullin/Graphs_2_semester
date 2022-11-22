
from collections import deque
from heapq import*
def add_edge(G,a,b,weight):
    G[a][b]=weight
# G - словарь словарей с весами
n,m,start=input().split()
n=int(n)
m=int(m)
start=int(start)
G={i:{} for i in range(n)}
for i in range(m):
    a,b,weight=map(int,input().split())# koordinati
    add_edge(G,a,b,weight)
    add_edge(G,b,a,weight)
print(G)


d = {v: float("inf") for v in G}
d[start] = 0
Q = [(0, start)]
used = set()
while len(used) != len(G):
    
    if not Q:
        break
    d_c, current = heappop(Q)
    if d_c != d[current]:
        continue
    for neighbour in G[current]:
        l = d[current] + G[current][neighbour]
        if l < d[neighbour]:
            d[neighbour] = l
            heappush(Q, (l, neighbour))
    used.add(current)
print(d)
