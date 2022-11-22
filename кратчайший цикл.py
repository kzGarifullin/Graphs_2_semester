from collections import deque
N,M=map(int,input().split())
G={i:set() for i in range(N)}#коприхеншэн
for i in range(M):
    v1,v2=map(int,input().split())# koordinati
    G[v1].add(v2)
    

shortest = -1 # length of shortest cycle
short_path = [] # shortest cycle
length=47
path=[]
for i in range(N):
    flag=False
    distances=[None]*N
    start_vertex=i
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
            elif neigh_v==start_vertex:
                length=distances[cur_v]-distances[neigh_v]+1
                
                path=[]
                parent=cur_v
                while not parent is None:
                    path.append(parent)
                    parent=parents[parent]
                flag=True
                break
        if flag==True:
            break
   
    if length != -1 and (shortest == -1 or length < shortest):
        shortest = length
        short_path = path
if short_path:
    print(*short_path[::-1])
else:
    print("NO CYCLES")
