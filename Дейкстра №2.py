#версия с хирьяновской лекции. В ней поддерживаются графы с несколькими компонентами связности 
from collections import deque
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
Q=deque()
s={i:float("inf")for i in range(n)}
s[start]=0
Q.append(start)
while Q:
    v=Q.pop()
    for u in G[v]:
        if u not in s or s[v]+G[v][u]<s[u]:
            s[u]=s[v]+G[v][u]
            Q.append(u)
print(s)


