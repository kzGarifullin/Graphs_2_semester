
from collections import deque
from heapq import*
def add_edge(G,a,b,weight):
    G[(a,0)][(b,1)]=weight
    G[(a,1)][(b,0)]=weight
# G - словарь словарей с весами
a=input().split()
n=int(a[0])
m=int(a[1])

G={(i,0):{} for i in range(n)}
for i in range(n):
    G[(i,1)]={}

for i in range(m):
    a,b,weight=map(int,input().split())# koordinati
    add_edge(G,a,b,weight)
    add_edge(G,b,a,weight)

k=int(input())
for i in range(k):
    start,finish=map(int,input().split())
    Q=deque()
    par={v: None for v in G}
    s={(i,0):float("inf")for i in range(n)}
    for i in range(n):
        s[(i,1)]=float("inf")
    s[(start,0)]=0
    Q.append((start,0))
    while Q:
        v=Q.pop()
        for u in G[v]:
            if u not in s or s[v]+G[v][u]<s[u]:
                s[u]=s[v]+G[v][u]
                Q.append(u)
                par[u]=v
    
    path=[]
    finish=(finish,0)
    if s[(finish)]==float("inf"):
        print(-1)
        continue
    path.append(finish[0])
    while True:
        kond=par[finish]
        if kond==None:
            break
        path.append(kond[0])
        finish=kond
    
    print(*path[::-1])

