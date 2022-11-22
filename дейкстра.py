def add_edge(G,a,b,weight):
    if a not in G:
        G[a]={b:weight}
    else:
        G[a][b]=weight
# G - словарь словарей с весами
n,m,start,f=map(int,input().split())#start- страт f-финиш
G={}
for i in range(m):
    a,b,weight=map(int,input().split())
    add_edge(G,a,b,weight)
    add_edge(G,b,a,weight)
    
#print(G)
d = {v: float("+inf") for v in G}
par={v: None for v in G}
d[start] = 0
used = set()
while len(used) != len(G):
    min_d = float("+inf")
    for v in d:
        if d[v] < min_d and v not in used:

            current = v
            min_d = d[v]
    for neighbour in G[current]:
        l = d[current] + G[current][neighbour]
        if l < d[neighbour]:
            d[neighbour] = l
            
            par[neighbour]=current
    used.add(current)
print(d)#словарь расстояний до вершин 



path=[]#путь от старта к финишу
path.append(f)#следующий цикл крафтит вывод
while True:
    kond=par[f]
    if kond==None:
        break
    path.append(kond)
    f=kond
    
    
print(*path[::-1])
