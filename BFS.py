from collections import deque
N,M=map(int,input().split())
G={i:set() for i in range(N)}#коприхеншэн
for i in range(M):
    v1,v2=map(int,input().split())# koordinati
    G[v1].add(v2)
    G[v2].add(v1)
print(G)
distances=[None]*N
start_vertex=0
distances[start_vertex]=0
queue=deque([start_vertex])
parents=[None]*N

while queue:
    cur_v= queue.popleft()
    for neigh_v in G[cur_v]:
        if distances[neigh_v] is None:
            distances[neigh_v]=distances[cur_v]+1
            parents[neigh_v]=cur_v
            queue.append(neigh_v)

end_vertex=9

path=[end_vertex]
parent=parents[end_vertex]
while not parent is None:
    
    path.append(parent)
    parent=parents[parent]
print(path[::-1])
print(parents)

print(distances)
